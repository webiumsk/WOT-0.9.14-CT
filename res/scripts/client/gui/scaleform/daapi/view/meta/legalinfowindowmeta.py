# 2016.02.13 15:02:59 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LegalInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LegalInfoWindowMeta(AbstractWindowView):

    def getLegalInfo(self):
        self._printOverrideError('getLegalInfo')

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def as_setLegalInfoS(self, legalInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setLegalInfo(legalInfo)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\legalinfowindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:03:00 St�edn� Evropa (b�n� �as)
