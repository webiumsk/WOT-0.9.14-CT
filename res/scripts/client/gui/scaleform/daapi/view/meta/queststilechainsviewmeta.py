# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsTileChainsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsTileChainsViewMeta(BaseDAAPIComponent):

    def getTileData(self, vehicleType, taskFilterType):
        self._printOverrideError('getTileData')

    def getChainProgress(self):
        self._printOverrideError('getChainProgress')

    def getTaskDetails(self, taskId):
        self._printOverrideError('getTaskDetails')

    def selectTask(self, taskId):
        self._printOverrideError('selectTask')

    def refuseTask(self, taskId):
        self._printOverrideError('refuseTask')

    def gotoBack(self):
        self._printOverrideError('gotoBack')

    def showAwardVehicleInfo(self, awardVehicleID):
        self._printOverrideError('showAwardVehicleInfo')

    def showAwardVehicleInHangar(self, awardVehicleID):
        self._printOverrideError('showAwardVehicleInHangar')

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_updateTileDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTileData(data)

    def as_updateChainProgressS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateChainProgress(data)

    def as_updateTaskDetailsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTaskDetails(data)

    def as_setSelectedTaskS(self, taskId):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedTask(taskId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\queststilechainsviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
