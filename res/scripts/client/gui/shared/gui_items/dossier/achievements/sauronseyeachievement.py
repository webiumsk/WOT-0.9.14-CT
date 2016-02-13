# 2016.02.13 15:04:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/SauronsEyeAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularAchievement

class SauronsEyeAchievement(RegularAchievement):

    def __init__(self, dossier, value = None):
        super(SauronsEyeAchievement, self).__init__('sauronEye', _AB.FALLOUT, dossier, value)

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        from gui.server_events.EventsCache import g_eventsCache
        return g_eventsCache.isGasAttackEnabled()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\sauronseyeachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:04:17 Støední Evropa (bìžný èas)
