# 2016.02.14 12:49:09 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_methodattrs.py
"""Fix bound method attributes (method.im_? -> method.__?__).
"""
from .. import fixer_base
from ..fixer_util import Name
MAP = {'im_func': '__func__',
 'im_self': '__self__',
 'im_class': '__self__.__class__'}

class FixMethodattrs(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< any+ trailer< '.' attr=('im_func' | 'im_self' | 'im_class') > any* >\n    "

    def transform(self, node, results):
        attr = results['attr'][0]
        new = unicode(MAP[attr.value])
        attr.replace(Name(new, prefix=attr.prefix))
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_methodattrs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:49:09 St�edn� Evropa (b�n� �as)
