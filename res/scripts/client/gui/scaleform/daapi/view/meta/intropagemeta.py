# 2016.02.13 15:02:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IntroPageMeta.py
from gui.Scaleform.framework.entities.View import View

class IntroPageMeta(View):

    def stopVideo(self):
        self._printOverrideError('stopVideo')

    def handleError(self, data):
        self._printOverrideError('handleError')

    def as_playVideoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\intropagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:59 St�edn� Evropa (b�n� �as)
