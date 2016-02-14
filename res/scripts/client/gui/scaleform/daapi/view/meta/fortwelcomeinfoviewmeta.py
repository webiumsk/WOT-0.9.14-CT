# 2016.02.14 12:40:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortWelcomeInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortWelcomeInfoViewMeta(BaseDAAPIComponent):

    def onCreateBtnClick(self):
        self._printOverrideError('onCreateBtnClick')

    def onNavigate(self, code):
        self._printOverrideError('onNavigate')

    def openClanResearch(self):
        self._printOverrideError('openClanResearch')

    def as_setWarningTextS(self, text, disabledBtnTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setWarningText(text, disabledBtnTooltip)

    def as_setCommonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_setRequirementTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setRequirementText(text)

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortwelcomeinfoviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:21 Støední Evropa (bìžný èas)
