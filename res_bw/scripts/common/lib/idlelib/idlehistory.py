# 2016.02.14 12:48:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/IdleHistory.py
"""Implement Idle Shell history mechanism with History class"""
from idlelib.configHandler import idleConf

class History:
    """ Implement Idle Shell history mechanism.
    
    store - Store source statement (called from PyShell.resetoutput).
    fetch - Fetch stored statement matching prefix already entered.
    history_next - Bound to <<history-next>> event (default Alt-N).
    history_prev - Bound to <<history-prev>> event (default Alt-P).
    """

    def __init__(self, text):
        """Initialize data attributes and bind event methods.
        
        .text - Idle wrapper of tk Text widget, with .bell().
        .history - source statements, possibly with multiple lines.
        .prefix - source already entered at prompt; filters history list.
        .pointer - index into history.
        .cyclic - wrap around history list (or not).
        """
        self.text = text
        self.history = []
        self.prefix = None
        self.pointer = None
        self.cyclic = idleConf.GetOption('main', 'History', 'cyclic', 1, 'bool')
        text.bind('<<history-previous>>', self.history_prev)
        text.bind('<<history-next>>', self.history_next)
        return

    def history_next(self, event):
        """Fetch later statement; start with ealiest if cyclic."""
        self.fetch(reverse=False)
        return 'break'

    def history_prev(self, event):
        """Fetch earlier statement; start with most recent."""
        self.fetch(reverse=True)
        return 'break'

    def fetch(self, reverse):
        """Fetch statememt and replace current line in text widget.
        
        Set prefix and pointer as needed for successive fetches.
        Reset them to None, None when returning to the start line.
        Sound bell when return to start line or cannot leave a line
        because cyclic is False.
        """
        nhist = len(self.history)
        pointer = self.pointer
        prefix = self.prefix
        if pointer is not None and prefix is not None:
            if self.text.compare('insert', '!=', 'end-1c') or self.text.get('iomark', 'end-1c') != self.history[pointer]:
                pointer = prefix = None
                self.text.mark_set('insert', 'end-1c')
        if pointer is None or prefix is None:
            prefix = self.text.get('iomark', 'end-1c')
            if reverse:
                pointer = nhist
            elif self.cyclic:
                pointer = -1
            else:
                self.text.bell()
                return
        nprefix = len(prefix)
        while 1:
            pointer += -1 if reverse else 1
            if pointer < 0 or pointer >= nhist:
                self.text.bell()
                if not self.cyclic and pointer < 0:
                    return
                if self.text.get('iomark', 'end-1c') != prefix:
                    self.text.delete('iomark', 'end-1c')
                    self.text.insert('iomark', prefix)
                pointer = prefix = None
                break
            item = self.history[pointer]
            if item[:nprefix] == prefix and len(item) > nprefix:
                self.text.delete('iomark', 'end-1c')
                self.text.insert('iomark', item)
                break

        self.text.see('insert')
        self.text.tag_remove('sel', '1.0', 'end')
        self.pointer = pointer
        self.prefix = prefix
        return

    def store(self, source):
        """Store Shell input statement into history list."""
        source = source.strip()
        if len(source) > 2:
            try:
                self.history.remove(source)
            except ValueError:
                pass

            self.history.append(source)
        self.pointer = None
        self.prefix = None
        return


if __name__ == '__main__':
    from test import test_support as support
    support.use_resources = ['gui']
    from unittest import main
    main('idlelib.idle_test.test_idlehistory', verbosity=2, exit=False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\idlehistory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:48:27 St�edn� Evropa (b�n� �as)
