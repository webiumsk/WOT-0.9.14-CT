# 2016.02.14 12:40:32 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleSellDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleSellDialogMeta(AbstractWindowView):

    def setDialogSettings(self, isOpen):
        self._printOverrideError('setDialogSettings')

    def sell(self, vehicleData, shells, eqs, optDevices, inventory, isDismissCrew):
        self._printOverrideError('sell')

    def setUserInput(self, value):
        self._printOverrideError('setUserInput')

    def setResultCredit(self, isGold, value):
        self._printOverrideError('setResultCredit')

    def checkControlQuestion(self, dismiss):
        self._printOverrideError('checkControlQuestion')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_checkGoldS(self, gold):
        if self._isDAAPIInited():
            return self.flashObject.as_checkGold(gold)

    def as_visibleControlBlockS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_visibleControlBlock(value)

    def as_enableButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableButton(value)

    def as_setControlQuestionDataS(self, isGold, value, question):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlQuestionData(isGold, value, question)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehicleselldialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:32 St�edn� Evropa (b�n� �as)
