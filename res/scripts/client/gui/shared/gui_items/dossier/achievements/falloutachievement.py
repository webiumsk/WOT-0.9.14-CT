# 2016.02.13 15:04:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/FalloutAchievement.py
from abstract import RegularAchievement
from gui.shared.gui_items.dossier.achievements import validators

class FalloutAchievement(RegularAchievement):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\falloutachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:04:13 St�edn� Evropa (b�n� �as)
