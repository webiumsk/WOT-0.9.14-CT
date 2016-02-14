# 2016.02.14 12:41:37 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/Achieved.py
from abstract import RegularAchievement
from gui.shared.gui_items.dossier.achievements import validators

class Achieved(RegularAchievement):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\achieved.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:41:37 Støední Evropa (bìžný èas)
