# 2016.02.13 15:02:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FreeXPInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FreeXPInfoWindowMeta(AbstractWindowView):

    def onSubmitButton(self):
        self._printOverrideError('onSubmitButton')

    def onCancelButton(self):
        self._printOverrideError('onCancelButton')

    def as_setSubmitLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSubmitLabel(value)

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\freexpinfowindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:59 St�edn� Evropa (b�n� �as)
