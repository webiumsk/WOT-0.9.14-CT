# 2016.02.14 12:40:28 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RetrainCrewWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RetrainCrewWindowMeta(AbstractWindowView):

    def submit(self, operationId):
        self._printOverrideError('submit')

    def changeRetrainType(self, retrainTypeIndex):
        self._printOverrideError('changeRetrainType')

    def as_setCrewDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewData(data)

    def as_setVehicleDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleData(data)

    def as_setCrewOperationDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewOperationData(data)

    def as_setAllCrewDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllCrewData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\retraincrewwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:28 Støední Evropa (bìžný èas)
