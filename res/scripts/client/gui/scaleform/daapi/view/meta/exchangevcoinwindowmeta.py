# 2016.02.13 15:02:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeVcoinWindowMeta.py
from gui.Scaleform.framework.entities.DAAPIModule import DAAPIModule

class ExchangeVcoinWindowMeta(DAAPIModule):

    def buyVcoin(self):
        self._printOverrideError('buyVcoin')

    def as_setTargetCurrencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTargetCurrencyData(data)

    def as_setSecondaryCurrencyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryCurrency(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\exchangevcoinwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:54 Støední Evropa (bìžný èas)
