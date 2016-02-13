# 2016.02.13 15:03:07 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        self._printOverrideError('onTabChange')

    def as_showStorePageS(self, viewAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(viewAlias)

    def as_initS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\storeviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:03:07 Støední Evropa (bìžný èas)
