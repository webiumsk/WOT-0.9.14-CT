# 2016.02.14 12:41:44 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/SimpleProgressAchievement.py
from RegularAchievement import RegularAchievement
from dossiers2.custom.config import RECORD_CONFIGS

class SimpleProgressAchievement(RegularAchievement):

    def __init__(self, name, block, dossier, value = None):
        if dossier is not None:
            self._progressValue = self._readProgressValue(dossier)
        else:
            self._progressValue = 0
        super(SimpleProgressAchievement, self).__init__(name, block, dossier, value)
        return

    def getProgressValue(self):
        if not self._lvlUpTotalValue:
            return 1.0
        return 1 - float(self._lvlUpValue) / float(self._lvlUpTotalValue)

    def isInNear(self):
        return self.getProgressValue() > 0

    def hasProgress(self):
        return not self._isDone

    def _readLevelUpValue(self, dossier):
        minValue = RECORD_CONFIGS[self._name]
        medals, series = divmod(self._progressValue, minValue)
        return minValue - series

    def _readLevelUpTotalValue(self, dossier):
        return RECORD_CONFIGS[self._name]

    def _readProgressValue(self, dossier):
        return 0
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\simpleprogressachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:41:44 St�edn� Evropa (b�n� �as)
