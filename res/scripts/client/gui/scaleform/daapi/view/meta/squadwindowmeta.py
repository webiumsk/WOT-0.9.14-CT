# 2016.02.14 12:40:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class SquadWindowMeta(BaseRallyMainWindow):

    def as_setComponentIdS(self, componentId):
        if self._isDAAPIInited():
            return self.flashObject.as_setComponentId(componentId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\squadwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:29 Støední Evropa (bìžný èas)
