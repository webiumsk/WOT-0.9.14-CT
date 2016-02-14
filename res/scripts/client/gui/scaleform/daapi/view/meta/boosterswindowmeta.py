# 2016.02.14 12:40:12 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BoostersWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BoostersWindowMeta(AbstractWindowView):

    def requestBoostersArray(self, isAvailable):
        self._printOverrideError('requestBoostersArray')

    def onBoosterActionBtnClick(self, boosterID, questID):
        self._printOverrideError('onBoosterActionBtnClick')

    def onFiltersChange(self, filters):
        self._printOverrideError('onFiltersChange')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setListDataS(self, boosters, scrollToTop):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(boosters, scrollToTop)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\boosterswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:12 Støední Evropa (bìžný èas)
