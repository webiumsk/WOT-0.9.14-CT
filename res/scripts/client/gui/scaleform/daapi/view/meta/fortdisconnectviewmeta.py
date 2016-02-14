# 2016.02.14 12:40:19 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortDisconnectViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortDisconnectViewMeta(BaseDAAPIComponent):

    def as_setWarningTextsS(self, warningTxt, warningDescTxt):
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningTexts(warningTxt, warningDescTxt)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortdisconnectviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:19 Støední Evropa (bìžný èas)
