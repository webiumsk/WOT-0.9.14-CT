# 2016.02.13 15:10:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/distutils/tests/test_sdist.py
"""Tests for distutils.command.sdist."""
import os
import tarfile
import unittest
import warnings
import zipfile
from os.path import join
from textwrap import dedent
from test.test_support import captured_stdout, check_warnings, run_unittest
try:
    import zlib
except ImportError:
    zlib = None

try:
    import grp
    import pwd
    UID_GID_SUPPORT = True
except ImportError:
    UID_GID_SUPPORT = False

from distutils.command.sdist import sdist, show_formats
from distutils.core import Distribution
from distutils.tests.test_config import PyPIRCCommandTestCase
from distutils.errors import DistutilsOptionError
from distutils.spawn import find_executable
from distutils.log import WARN
from distutils.filelist import FileList
from distutils.archive_util import ARCHIVE_FORMATS
SETUP_PY = "\nfrom distutils.core import setup\nimport somecode\n\nsetup(name='fake')\n"
MANIFEST = '# file GENERATED by distutils, do NOT edit\nREADME\nbuildout.cfg\ninroot.txt\nsetup.py\ndata%(sep)sdata.dt\nscripts%(sep)sscript.py\nsome%(sep)sfile.txt\nsome%(sep)sother_file.txt\nsomecode%(sep)s__init__.py\nsomecode%(sep)sdoc.dat\nsomecode%(sep)sdoc.txt\n'

class SDistTestCase(PyPIRCCommandTestCase):

    def setUp(self):
        super(SDistTestCase, self).setUp()
        self.old_path = os.getcwd()
        os.mkdir(join(self.tmp_dir, 'somecode'))
        os.mkdir(join(self.tmp_dir, 'dist'))
        self.write_file((self.tmp_dir, 'README'), 'xxx')
        self.write_file((self.tmp_dir, 'somecode', '__init__.py'), '#')
        self.write_file((self.tmp_dir, 'setup.py'), SETUP_PY)
        os.chdir(self.tmp_dir)

    def tearDown(self):
        os.chdir(self.old_path)
        super(SDistTestCase, self).tearDown()

    def get_cmd(self, metadata = None):
        """Returns a cmd"""
        if metadata is None:
            metadata = {'name': 'fake',
             'version': '1.0',
             'url': 'xxx',
             'author': 'xxx',
             'author_email': 'xxx'}
        dist = Distribution(metadata)
        dist.script_name = 'setup.py'
        dist.packages = ['somecode']
        dist.include_package_data = True
        cmd = sdist(dist)
        cmd.dist_dir = 'dist'
        return (dist, cmd)

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_prune_file_list(self):
        os.mkdir(join(self.tmp_dir, 'somecode', '.svn'))
        self.write_file((self.tmp_dir,
         'somecode',
         '.svn',
         'ok.py'), 'xxx')
        os.mkdir(join(self.tmp_dir, 'somecode', '.hg'))
        self.write_file((self.tmp_dir,
         'somecode',
         '.hg',
         'ok'), 'xxx')
        os.mkdir(join(self.tmp_dir, 'somecode', '.git'))
        self.write_file((self.tmp_dir,
         'somecode',
         '.git',
         'ok'), 'xxx')
        self.write_file((self.tmp_dir, 'somecode', '.nfs0001'), 'xxx')
        dist, cmd = self.get_cmd()
        cmd.formats = ['zip']
        cmd.ensure_finalized()
        cmd.run()
        dist_folder = join(self.tmp_dir, 'dist')
        files = os.listdir(dist_folder)
        self.assertEqual(files, ['fake-1.0.zip'])
        zip_file = zipfile.ZipFile(join(dist_folder, 'fake-1.0.zip'))
        try:
            content = zip_file.namelist()
        finally:
            zip_file.close()

        self.assertEqual(len(content), 4)

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_make_distribution(self):
        dist, cmd = self.get_cmd()
        cmd.formats = ['gztar', 'tar']
        cmd.ensure_finalized()
        cmd.run()
        dist_folder = join(self.tmp_dir, 'dist')
        result = os.listdir(dist_folder)
        result.sort()
        self.assertEqual(result, ['fake-1.0.tar', 'fake-1.0.tar.gz'])
        os.remove(join(dist_folder, 'fake-1.0.tar'))
        os.remove(join(dist_folder, 'fake-1.0.tar.gz'))
        cmd.formats = ['tar', 'gztar']
        cmd.ensure_finalized()
        cmd.run()
        result = os.listdir(dist_folder)
        result.sort()
        self.assertEqual(result, ['fake-1.0.tar', 'fake-1.0.tar.gz'])

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_unicode_metadata_tgz(self):
        """
        Unicode name or version should not break building to tar.gz format.
        Reference issue #11638.
        """
        dist, cmd = self.get_cmd({'name': u'fake',
         'version': u'1.0'})
        cmd.formats = ['gztar']
        cmd.ensure_finalized()
        cmd.run()
        dist_folder = join(self.tmp_dir, 'dist')
        result = os.listdir(dist_folder)
        self.assertEqual(result, ['fake-1.0.tar.gz'])
        os.remove(join(dist_folder, 'fake-1.0.tar.gz'))

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_add_defaults(self):
        dist, cmd = self.get_cmd()
        dist.package_data = {'': ['*.cfg', '*.dat'],
         'somecode': ['*.txt']}
        self.write_file((self.tmp_dir, 'somecode', 'doc.txt'), '#')
        self.write_file((self.tmp_dir, 'somecode', 'doc.dat'), '#')
        data_dir = join(self.tmp_dir, 'data')
        os.mkdir(data_dir)
        self.write_file((data_dir, 'data.dt'), '#')
        some_dir = join(self.tmp_dir, 'some')
        os.mkdir(some_dir)
        hg_dir = join(self.tmp_dir, '.hg')
        os.mkdir(hg_dir)
        self.write_file((hg_dir, 'last-message.txt'), '#')
        self.write_file((self.tmp_dir, 'buildout.cfg'), '#')
        self.write_file((self.tmp_dir, 'inroot.txt'), '#')
        self.write_file((some_dir, 'file.txt'), '#')
        self.write_file((some_dir, 'other_file.txt'), '#')
        dist.data_files = [('data', ['data/data.dt',
           'buildout.cfg',
           'inroot.txt',
           'notexisting']), 'some/file.txt', 'some/other_file.txt']
        script_dir = join(self.tmp_dir, 'scripts')
        os.mkdir(script_dir)
        self.write_file((script_dir, 'script.py'), '#')
        dist.scripts = [join('scripts', 'script.py')]
        cmd.formats = ['zip']
        cmd.use_defaults = True
        cmd.ensure_finalized()
        cmd.run()
        dist_folder = join(self.tmp_dir, 'dist')
        files = os.listdir(dist_folder)
        self.assertEqual(files, ['fake-1.0.zip'])
        zip_file = zipfile.ZipFile(join(dist_folder, 'fake-1.0.zip'))
        try:
            content = zip_file.namelist()
        finally:
            zip_file.close()

        self.assertEqual(len(content), 12)
        f = open(join(self.tmp_dir, 'MANIFEST'))
        try:
            manifest = f.read()
        finally:
            f.close()

        self.assertEqual(manifest, MANIFEST % {'sep': os.sep})

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_metadata_check_option(self):
        dist, cmd = self.get_cmd(metadata={})
        cmd.ensure_finalized()
        cmd.run()
        warnings = [ msg for msg in self.get_logs(WARN) if msg.startswith('warning: check:') ]
        self.assertEqual(len(warnings), 2)
        self.clear_logs()
        dist, cmd = self.get_cmd()
        cmd.ensure_finalized()
        cmd.metadata_check = 0
        cmd.run()
        warnings = [ msg for msg in self.get_logs(WARN) if msg.startswith('warning: check:') ]
        self.assertEqual(len(warnings), 0)

    def test_check_metadata_deprecated(self):
        dist, cmd = self.get_cmd()
        with check_warnings() as w:
            warnings.simplefilter('always')
            cmd.check_metadata()
            self.assertEqual(len(w.warnings), 1)

    def test_show_formats(self):
        with captured_stdout() as stdout:
            show_formats()
        num_formats = len(ARCHIVE_FORMATS.keys())
        output = [ line for line in stdout.getvalue().split('\n') if line.strip().startswith('--formats=') ]
        self.assertEqual(len(output), num_formats)

    def test_finalize_options(self):
        dist, cmd = self.get_cmd()
        cmd.finalize_options()
        self.assertEqual(cmd.manifest, 'MANIFEST')
        self.assertEqual(cmd.template, 'MANIFEST.in')
        self.assertEqual(cmd.dist_dir, 'dist')
        cmd.formats = 1
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)
        cmd.formats = ['zip']
        cmd.finalize_options()
        cmd.formats = 'supazipa'
        self.assertRaises(DistutilsOptionError, cmd.finalize_options)

    @unittest.skipUnless(zlib, 'requires zlib')
    @unittest.skipUnless(UID_GID_SUPPORT, 'Requires grp and pwd support')
    @unittest.skipIf(find_executable('tar') is None, 'The tar command is not found')
    @unittest.skipIf(find_executable('gzip') is None, 'The gzip command is not found')
    def test_make_distribution_owner_group(self):
        dist, cmd = self.get_cmd()
        cmd.formats = ['gztar']
        cmd.owner = pwd.getpwuid(0)[0]
        cmd.group = grp.getgrgid(0)[0]
        cmd.ensure_finalized()
        cmd.run()
        archive_name = join(self.tmp_dir, 'dist', 'fake-1.0.tar.gz')
        archive = tarfile.open(archive_name)
        try:
            for member in archive.getmembers():
                self.assertEqual(member.uid, 0)
                self.assertEqual(member.gid, 0)

        finally:
            archive.close()

        dist, cmd = self.get_cmd()
        cmd.formats = ['gztar']
        cmd.ensure_finalized()
        cmd.run()
        archive_name = join(self.tmp_dir, 'dist', 'fake-1.0.tar.gz')
        archive = tarfile.open(archive_name)
        try:
            for member in archive.getmembers():
                self.assertEqual(member.uid, os.getuid())

        finally:
            archive.close()

    def _check_template(self, content):
        dist, cmd = self.get_cmd()
        os.chdir(self.tmp_dir)
        self.write_file('MANIFEST.in', content)
        cmd.ensure_finalized()
        cmd.filelist = FileList()
        cmd.read_template()
        warnings = self.get_logs(WARN)
        self.assertEqual(len(warnings), 1)

    def test_invalid_template_unknown_command(self):
        self._check_template('taunt knights *')

    def test_invalid_template_wrong_arguments(self):
        self._check_template('prune')

    @unittest.skipIf(os.name != 'nt', 'test relevant for Windows only')
    def test_invalid_template_wrong_path(self):
        self._check_template('include examples/')

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_get_file_list(self):
        dist, cmd = self.get_cmd()
        dist.package_data = {'somecode': ['*.txt']}
        self.write_file((self.tmp_dir, 'somecode', 'doc.txt'), '#')
        cmd.formats = ['gztar']
        cmd.ensure_finalized()
        cmd.run()
        f = open(cmd.manifest)
        try:
            manifest = [ line.strip() for line in f.read().split('\n') if line.strip() != '' ]
        finally:
            f.close()

        self.assertEqual(len(manifest), 5)
        self.write_file((self.tmp_dir, 'somecode', 'doc2.txt'), '#')
        build_py = dist.get_command_obj('build_py')
        build_py.finalized = False
        build_py.ensure_finalized()
        cmd.run()
        f = open(cmd.manifest)
        try:
            manifest2 = [ line.strip() for line in f.read().split('\n') if line.strip() != '' ]
        finally:
            f.close()

        self.assertEqual(len(manifest2), 6)
        self.assertIn('doc2.txt', manifest2[-1])

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_manifest_marker(self):
        dist, cmd = self.get_cmd()
        cmd.ensure_finalized()
        cmd.run()
        f = open(cmd.manifest)
        try:
            manifest = [ line.strip() for line in f.read().split('\n') if line.strip() != '' ]
        finally:
            f.close()

        self.assertEqual(manifest[0], '# file GENERATED by distutils, do NOT edit')

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_manifest_comments(self):
        contents = dedent('            # bad.py\n            #bad.py\n            good.py\n            ')
        dist, cmd = self.get_cmd()
        cmd.ensure_finalized()
        self.write_file((self.tmp_dir, cmd.manifest), contents)
        self.write_file((self.tmp_dir, 'good.py'), '# pick me!')
        self.write_file((self.tmp_dir, 'bad.py'), "# don't pick me!")
        self.write_file((self.tmp_dir, '#bad.py'), "# don't pick me!")
        cmd.run()
        self.assertEqual(cmd.filelist.files, ['good.py'])

    @unittest.skipUnless(zlib, 'requires zlib')
    def test_manual_manifest(self):
        dist, cmd = self.get_cmd()
        cmd.formats = ['gztar']
        cmd.ensure_finalized()
        self.write_file((self.tmp_dir, cmd.manifest), 'README.manual')
        self.write_file((self.tmp_dir, 'README.manual'), 'This project maintains its MANIFEST file itself.')
        cmd.run()
        self.assertEqual(cmd.filelist.files, ['README.manual'])
        f = open(cmd.manifest)
        try:
            manifest = [ line.strip() for line in f.read().split('\n') if line.strip() != '' ]
        finally:
            f.close()

        self.assertEqual(manifest, ['README.manual'])
        archive_name = join(self.tmp_dir, 'dist', 'fake-1.0.tar.gz')
        archive = tarfile.open(archive_name)
        try:
            filenames = [ tarinfo.name for tarinfo in archive ]
        finally:
            archive.close()

        self.assertEqual(sorted(filenames), ['fake-1.0', 'fake-1.0/PKG-INFO', 'fake-1.0/README.manual'])


def test_suite():
    return unittest.makeSuite(SDistTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\distutils\tests\test_sdist.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:10:13 St�edn� Evropa (b�n� �as)