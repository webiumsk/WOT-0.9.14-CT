# 2016.02.14 12:38:24 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/functional/__init__.py
from constants import IS_DEVELOPMENT

def initDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import init
        except ImportError:

            def init():
                pass

        init()


def finiDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import fini
        except ImportError:

            def fini():
                pass

        fini()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\functional\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:38:24 St�edn� Evropa (b�n� �as)
