# 2016.02.14 12:44:41 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/WWISE.py
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print 'WARNING: WWISE support is not enabled.'
    enabled = False

if enabled:
    print 'WARNING: WWISE support IS enabled.'
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\wwise.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:44:41 St�edn� Evropa (b�n� �as)
