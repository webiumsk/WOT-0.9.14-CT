# 2016.02.13 15:02:56 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCreateDirectionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCreateDirectionWindowMeta(AbstractWindowView):

    def openNewDirection(self):
        self._printOverrideError('openNewDirection')

    def closeDirection(self, id):
        self._printOverrideError('closeDirection')

    def as_setDescriptionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescription(value)

    def as_setupButtonS(self, enabled, visible, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setupButton(enabled, visible, tooltip)

    def as_setDirectionsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDirections(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortcreatedirectionwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:56 St�edn� Evropa (b�n� �as)
