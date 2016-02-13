# 2016.02.13 15:02:53 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnsFormMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportRespawnsFormMeta(BaseRallyRoomView):

    def onReadyClick(self, userID):
        self._printOverrideError('onReadyClick')

    def as_setMapBGS(self, imgsource):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapBG(imgsource)

    def as_setProgressS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(time)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportrespawnsformmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:53 Støední Evropa (bìžný èas)
