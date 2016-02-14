# 2016.02.14 12:40:13 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesViewWithTableMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanInvitesViewWithTableMeta(BaseDAAPIComponent):

    def showMore(self):
        self._printOverrideError('showMore')

    def refreshTable(self):
        self._printOverrideError('refreshTable')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_getTableDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()

    def as_updateDefaultSortFieldS(self, defaultSortField, defaultSortDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDefaultSortField(defaultSortField, defaultSortDirection)

    def as_showDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)

    def as_hideDummyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()

    def as_updateButtonRefreshStateS(self, enabled, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_updateButtonRefreshState(enabled, tooltip)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\claninvitesviewwithtablemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:13 Støední Evropa (bìžný èas)
