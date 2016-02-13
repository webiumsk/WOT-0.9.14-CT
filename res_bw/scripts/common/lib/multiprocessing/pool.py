# 2016.02.13 15:11:58 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/multiprocessing/pool.py
__all__ = ['Pool']
import threading
import Queue
import itertools
import collections
import time
from multiprocessing import Process, cpu_count, TimeoutError
from multiprocessing.util import Finalize, debug
RUN = 0
CLOSE = 1
TERMINATE = 2
job_counter = itertools.count()

def mapstar(args):
    return map(*args)


class MaybeEncodingError(Exception):
    """Wraps possible unpickleable errors, so they can be
    safely sent through the socket."""

    def __init__(self, exc, value):
        self.exc = repr(exc)
        self.value = repr(value)
        super(MaybeEncodingError, self).__init__(self.exc, self.value)

    def __str__(self):
        return "Error sending result: '%s'. Reason: '%s'" % (self.value, self.exc)

    def __repr__(self):
        return '<MaybeEncodingError: %s>' % str(self)


def worker(inqueue, outqueue, initializer = None, initargs = (), maxtasks = None):
    if not (maxtasks is None or type(maxtasks) == int and maxtasks > 0):
        raise AssertionError
        put = outqueue.put
        get = inqueue.get
        if hasattr(inqueue, '_writer'):
            inqueue._writer.close()
            outqueue._reader.close()
        initializer is not None and initializer(*initargs)
    completed = 0
    while maxtasks is None or maxtasks and completed < maxtasks:
        try:
            task = get()
        except (EOFError, IOError):
            debug('worker got EOFError or IOError -- exiting')
            break

        if task is None:
            debug('worker got sentinel -- exiting')
            break
        job, i, func, args, kwds = task
        try:
            result = (True, func(*args, **kwds))
        except Exception as e:
            result = (False, e)

        try:
            put((job, i, result))
        except Exception as e:
            wrapped = MaybeEncodingError(e, result[1])
            debug('Possible encoding error while sending result: %s' % wrapped)
            put((job, i, (False, wrapped)))

        completed += 1

    debug('worker exiting after %d tasks' % completed)
    return


class Pool(object):
    """
    Class which supports an async version of the `apply()` builtin
    """
    Process = Process

    def __init__(self, processes = None, initializer = None, initargs = (), maxtasksperchild = None):
        self._setup_queues()
        self._taskqueue = Queue.Queue()
        self._cache = {}
        self._state = RUN
        self._maxtasksperchild = maxtasksperchild
        self._initializer = initializer
        self._initargs = initargs
        if processes is None:
            try:
                processes = cpu_count()
            except NotImplementedError:
                processes = 1

        if processes < 1:
            raise ValueError('Number of processes must be at least 1')
        if initializer is not None and not hasattr(initializer, '__call__'):
            raise TypeError('initializer must be a callable')
        self._processes = processes
        self._pool = []
        self._repopulate_pool()
        self._worker_handler = threading.Thread(target=Pool._handle_workers, args=(self,))
        self._worker_handler.daemon = True
        self._worker_handler._state = RUN
        self._worker_handler.start()
        self._task_handler = threading.Thread(target=Pool._handle_tasks, args=(self._taskqueue,
         self._quick_put,
         self._outqueue,
         self._pool,
         self._cache))
        self._task_handler.daemon = True
        self._task_handler._state = RUN
        self._task_handler.start()
        self._result_handler = threading.Thread(target=Pool._handle_results, args=(self._outqueue, self._quick_get, self._cache))
        self._result_handler.daemon = True
        self._result_handler._state = RUN
        self._result_handler.start()
        self._terminate = Finalize(self, self._terminate_pool, args=(self._taskqueue,
         self._inqueue,
         self._outqueue,
         self._pool,
         self._worker_handler,
         self._task_handler,
         self._result_handler,
         self._cache), exitpriority=15)
        return

    def _join_exited_workers(self):
        """Cleanup after any worker processes which have exited due to reaching
        their specified lifetime.  Returns True if any workers were cleaned up.
        """
        cleaned = False
        for i in reversed(range(len(self._pool))):
            worker = self._pool[i]
            if worker.exitcode is not None:
                debug('cleaning up worker %d' % i)
                worker.join()
                cleaned = True
                del self._pool[i]

        return cleaned

    def _repopulate_pool(self):
        """Bring the number of pool processes up to the specified number,
        for use after reaping workers which have exited.
        """
        for i in range(self._processes - len(self._pool)):
            w = self.Process(target=worker, args=(self._inqueue,
             self._outqueue,
             self._initializer,
             self._initargs,
             self._maxtasksperchild))
            self._pool.append(w)
            w.name = w.name.replace('Process', 'PoolWorker')
            w.daemon = True
            w.start()
            debug('added worker')

    def _maintain_pool(self):
        """Clean up any exited workers and start replacements for them.
        """
        if self._join_exited_workers():
            self._repopulate_pool()

    def _setup_queues(self):
        from .queues import SimpleQueue
        self._inqueue = SimpleQueue()
        self._outqueue = SimpleQueue()
        self._quick_put = self._inqueue._writer.send
        self._quick_get = self._outqueue._reader.recv

    def apply(self, func, args = (), kwds = {}):
        """
        Equivalent of `apply()` builtin
        """
        raise self._state == RUN or AssertionError
        return self.apply_async(func, args, kwds).get()

    def map(self, func, iterable, chunksize = None):
        """
        Equivalent of `map()` builtin
        """
        raise self._state == RUN or AssertionError
        return self.map_async(func, iterable, chunksize).get()

    def imap(self, func, iterable, chunksize = 1):
        """
        Equivalent of `itertools.imap()` -- can be MUCH slower than `Pool.map()`
        """
        if not self._state == RUN:
            raise AssertionError
            result = chunksize == 1 and IMapIterator(self._cache)
            self._taskqueue.put((((result._job,
              i,
              func,
              (x,),
              {}) for i, x in enumerate(iterable)), result._set_length))
            return result
        else:
            raise chunksize > 1 or AssertionError
            task_batches = Pool._get_tasks(func, iterable, chunksize)
            result = IMapIterator(self._cache)
            self._taskqueue.put((((result._job,
              i,
              mapstar,
              (x,),
              {}) for i, x in enumerate(task_batches)), result._set_length))
            return (item for chunk in result for item in chunk)

    def imap_unordered(self, func, iterable, chunksize = 1):
        """
        Like `imap()` method but ordering of results is arbitrary
        """
        if not self._state == RUN:
            raise AssertionError
            result = chunksize == 1 and IMapUnorderedIterator(self._cache)
            self._taskqueue.put((((result._job,
              i,
              func,
              (x,),
              {}) for i, x in enumerate(iterable)), result._set_length))
            return result
        else:
            raise chunksize > 1 or AssertionError
            task_batches = Pool._get_tasks(func, iterable, chunksize)
            result = IMapUnorderedIterator(self._cache)
            self._taskqueue.put((((result._job,
              i,
              mapstar,
              (x,),
              {}) for i, x in enumerate(task_batches)), result._set_length))
            return (item for chunk in result for item in chunk)

    def apply_async(self, func, args = (), kwds = {}, callback = None):
        """
        Asynchronous equivalent of `apply()` builtin
        """
        raise self._state == RUN or AssertionError
        result = ApplyResult(self._cache, callback)
        self._taskqueue.put(([(result._job,
           None,
           func,
           args,
           kwds)], None))
        return result

    def map_async(self, func, iterable, chunksize = None, callback = None):
        """
        Asynchronous equivalent of `map()` builtin
        """
        if not self._state == RUN:
            raise AssertionError
            if not hasattr(iterable, '__len__'):
                iterable = list(iterable)
            if chunksize is None:
                chunksize, extra = divmod(len(iterable), len(self._pool) * 4)
                if extra:
                    chunksize += 1
            chunksize = len(iterable) == 0 and 0
        task_batches = Pool._get_tasks(func, iterable, chunksize)
        result = MapResult(self._cache, chunksize, len(iterable), callback)
        self._taskqueue.put((((result._job,
          i,
          mapstar,
          (x,),
          {}) for i, x in enumerate(task_batches)), None))
        return result

    @staticmethod
    def _handle_workers(pool):
        thread = threading.current_thread()
        while thread._state == RUN or pool._cache and thread._state != TERMINATE:
            pool._maintain_pool()
            time.sleep(0.1)

        pool._taskqueue.put(None)
        debug('worker handler exiting')
        return

    @staticmethod
    def _handle_tasks(taskqueue, put, outqueue, pool, cache):
        thread = threading.current_thread()
        for taskseq, set_length in iter(taskqueue.get, None):
            i = -1
            for i, task in enumerate(taskseq):
                if thread._state:
                    debug('task handler found thread._state != RUN')
                    break
                try:
                    put(task)
                except Exception as e:
                    job, ind = task[:2]
                    try:
                        cache[job]._set(ind, (False, e))
                    except KeyError:
                        pass

            else:
                if set_length:
                    debug('doing set_length()')
                    set_length(i + 1)
                continue

            break
        else:
            debug('task handler got sentinel')

        try:
            debug('task handler sending sentinel to result handler')
            outqueue.put(None)
            debug('task handler sending sentinel to workers')
            for p in pool:
                put(None)

        except IOError:
            debug('task handler got IOError when sending sentinels')

        debug('task handler exiting')
        return

    @staticmethod
    def _handle_results(outqueue, get, cache):
        thread = threading.current_thread()
        while 1:
            try:
                task = get()
            except (IOError, EOFError):
                debug('result handler got EOFError/IOError -- exiting')
                return

            if thread._state:
                if not thread._state == TERMINATE:
                    raise AssertionError
                    debug('result handler found thread._state=TERMINATE')
                    break
                task is None and debug('result handler got sentinel')
                break
            job, i, obj = task
            try:
                cache[job]._set(i, obj)
            except KeyError:
                pass

        while cache and thread._state != TERMINATE:
            try:
                task = get()
            except (IOError, EOFError):
                debug('result handler got EOFError/IOError -- exiting')
                return

            if task is None:
                debug('result handler ignoring extra sentinel')
                continue
            job, i, obj = task
            try:
                cache[job]._set(i, obj)
            except KeyError:
                pass

        if hasattr(outqueue, '_reader'):
            debug('ensuring that outqueue is not full')
            try:
                for i in range(10):
                    if not outqueue._reader.poll():
                        break
                    get()

            except (IOError, EOFError):
                pass

        debug('result handler exiting: len(cache)=%s, thread._state=%s', len(cache), thread._state)
        return

    @staticmethod
    def _get_tasks(func, it, size):
        it = iter(it)
        while 1:
            x = tuple(itertools.islice(it, size))
            if not x:
                return
            yield (func, x)

    def __reduce__(self):
        raise NotImplementedError('pool objects cannot be passed between processes or pickled')

    def close(self):
        debug('closing pool')
        if self._state == RUN:
            self._state = CLOSE
            self._worker_handler._state = CLOSE

    def terminate(self):
        debug('terminating pool')
        self._state = TERMINATE
        self._worker_handler._state = TERMINATE
        self._terminate()

    def join(self):
        debug('joining pool')
        raise self._state in (CLOSE, TERMINATE) or AssertionError
        self._worker_handler.join()
        self._task_handler.join()
        self._result_handler.join()
        for p in self._pool:
            p.join()

    @staticmethod
    def _help_stuff_finish(inqueue, task_handler, size):
        debug('removing tasks from inqueue until task handler finished')
        inqueue._rlock.acquire()
        while task_handler.is_alive() and inqueue._reader.poll():
            inqueue._reader.recv()
            time.sleep(0)

    @classmethod
    def _terminate_pool(cls, taskqueue, inqueue, outqueue, pool, worker_handler, task_handler, result_handler, cache):
        debug('finalizing pool')
        worker_handler._state = TERMINATE
        task_handler._state = TERMINATE
        debug('helping task handler/workers to finish')
        cls._help_stuff_finish(inqueue, task_handler, len(pool))
        if not (result_handler.is_alive() or len(cache) == 0):
            raise AssertionError
            result_handler._state = TERMINATE
            outqueue.put(None)
            debug('joining worker handler')
            if threading.current_thread() is not worker_handler:
                worker_handler.join(1e+100)
            if pool and hasattr(pool[0], 'terminate'):
                debug('terminating workers')
                for p in pool:
                    if p.exitcode is None:
                        p.terminate()

            debug('joining task handler')
            if threading.current_thread() is not task_handler:
                task_handler.join(1e+100)
            debug('joining result handler')
            if threading.current_thread() is not result_handler:
                result_handler.join(1e+100)
            pool and hasattr(pool[0], 'terminate') and debug('joining pool workers')
            for p in pool:
                if p.is_alive():
                    debug('cleaning up worker %d' % p.pid)
                    p.join()

        return


class ApplyResult(object):

    def __init__(self, cache, callback):
        self._cond = threading.Condition(threading.Lock())
        self._job = job_counter.next()
        self._cache = cache
        self._ready = False
        self._callback = callback
        cache[self._job] = self

    def ready(self):
        return self._ready

    def successful(self):
        raise self._ready or AssertionError
        return self._success

    def wait(self, timeout = None):
        self._cond.acquire()
        try:
            if not self._ready:
                self._cond.wait(timeout)
        finally:
            self._cond.release()

    def get(self, timeout = None):
        self.wait(timeout)
        if not self._ready:
            raise TimeoutError
        if self._success:
            return self._value
        raise self._value

    def _set(self, i, obj):
        self._success, self._value = obj
        if self._callback and self._success:
            self._callback(self._value)
        self._cond.acquire()
        try:
            self._ready = True
            self._cond.notify()
        finally:
            self._cond.release()

        del self._cache[self._job]


AsyncResult = ApplyResult

class MapResult(ApplyResult):

    def __init__(self, cache, chunksize, length, callback):
        ApplyResult.__init__(self, cache, callback)
        self._success = True
        self._value = [None] * length
        self._chunksize = chunksize
        if chunksize <= 0:
            self._number_left = 0
            self._ready = True
            del cache[self._job]
        else:
            self._number_left = length // chunksize + bool(length % chunksize)
        return

    def _set(self, i, success_result):
        success, result = success_result
        if success:
            self._value[i * self._chunksize:(i + 1) * self._chunksize] = result
            self._number_left -= 1
            if self._number_left == 0:
                if self._callback:
                    self._callback(self._value)
                del self._cache[self._job]
                self._cond.acquire()
                try:
                    self._ready = True
                    self._cond.notify()
                finally:
                    self._cond.release()

        else:
            self._success = False
            self._value = result
            del self._cache[self._job]
            self._cond.acquire()
            try:
                self._ready = True
                self._cond.notify()
            finally:
                self._cond.release()


class IMapIterator(object):

    def __init__(self, cache):
        self._cond = threading.Condition(threading.Lock())
        self._job = job_counter.next()
        self._cache = cache
        self._items = collections.deque()
        self._index = 0
        self._length = None
        self._unsorted = {}
        cache[self._job] = self
        return

    def __iter__(self):
        return self

    def next(self, timeout = None):
        self._cond.acquire()
        try:
            item = self._items.popleft()
        except IndexError:
            if self._index == self._length:
                raise StopIteration
            self._cond.wait(timeout)
            try:
                item = self._items.popleft()
            except IndexError:
                if self._index == self._length:
                    raise StopIteration
                raise TimeoutError

        finally:
            self._cond.release()

        success, value = item
        if success:
            return value
        raise value

    __next__ = next

    def _set(self, i, obj):
        self._cond.acquire()
        try:
            if self._index == i:
                self._items.append(obj)
                self._index += 1
                while self._index in self._unsorted:
                    obj = self._unsorted.pop(self._index)
                    self._items.append(obj)
                    self._index += 1

                self._cond.notify()
            else:
                self._unsorted[i] = obj
            if self._index == self._length:
                del self._cache[self._job]
        finally:
            self._cond.release()

    def _set_length(self, length):
        self._cond.acquire()
        try:
            self._length = length
            if self._index == self._length:
                self._cond.notify()
                del self._cache[self._job]
        finally:
            self._cond.release()


class IMapUnorderedIterator(IMapIterator):

    def _set(self, i, obj):
        self._cond.acquire()
        try:
            self._items.append(obj)
            self._index += 1
            self._cond.notify()
            if self._index == self._length:
                del self._cache[self._job]
        finally:
            self._cond.release()


class ThreadPool(Pool):
    from .dummy import Process

    def __init__(self, processes = None, initializer = None, initargs = ()):
        Pool.__init__(self, processes, initializer, initargs)

    def _setup_queues(self):
        self._inqueue = Queue.Queue()
        self._outqueue = Queue.Queue()
        self._quick_put = self._inqueue.put
        self._quick_get = self._outqueue.get

    @staticmethod
    def _help_stuff_finish(inqueue, task_handler, size):
        inqueue.not_empty.acquire()
        try:
            inqueue.queue.clear()
            inqueue.queue.extend([None] * size)
            inqueue.not_empty.notify_all()
        finally:
            inqueue.not_empty.release()

        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\multiprocessing\pool.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:11:59 St�edn� Evropa (b�n� �as)
