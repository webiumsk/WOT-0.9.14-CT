# 2016.02.13 15:03:04 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReportBugMeta.py
from gui.Scaleform.framework.entities.DAAPIModule import DAAPIModule

class ReportBugMeta(DAAPIModule):

    def reportBug(self):
        self._printOverrideError('reportBug')

    def as_setHyperLinkS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHyperLink(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\reportbugmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:03:04 Støední Evropa (bìžný èas)
