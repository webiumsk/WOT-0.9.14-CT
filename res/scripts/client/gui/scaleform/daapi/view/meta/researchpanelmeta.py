# 2016.02.14 12:40:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ResearchPanelMeta(BaseDAAPIComponent):

    def goToResearch(self):
        self._printOverrideError('goToResearch')

    def as_updateCurrentVehicleS(self, name, type, vDescription, earnedXP, isElite, isPremIGR):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCurrentVehicle(name, type, vDescription, earnedXP, isElite, isPremIGR)

    def as_setEarnedXPS(self, earnedXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarnedXP(earnedXP)

    def as_setEliteS(self, isElite):
        if self._isDAAPIInited():
            return self.flashObject.as_setElite(isElite)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\researchpanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:28 St�edn� Evropa (b�n� �as)
