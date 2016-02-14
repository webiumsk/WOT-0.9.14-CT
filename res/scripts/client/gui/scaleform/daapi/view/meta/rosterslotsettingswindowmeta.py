# 2016.02.14 12:40:28 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RosterSlotSettingsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RosterSlotSettingsWindowMeta(AbstractWindowView):

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._printOverrideError('onFiltersUpdate')

    def requestVehicleFilters(self):
        self._printOverrideError('requestVehicleFilters')

    def submitButtonHandler(self, value):
        self._printOverrideError('submitButtonHandler')

    def cancelButtonHandler(self):
        self._printOverrideError('cancelButtonHandler')

    def as_setVehicleSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleSelection(data)

    def as_setRangeSelectionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRangeSelection(data)

    def as_resetSelectionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetSelection()

    def as_selectTabS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setListDataS(self, listData):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData)

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setRosterLimitsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterLimits(data)

    def as_updateVehicleFiltersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleFilters(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\rosterslotsettingswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:28 Støední Evropa (bìžný èas)
