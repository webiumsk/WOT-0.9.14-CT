# 2016.02.14 12:40:24 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileAchievementSectionMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileAchievementSectionMeta(ProfileSection):

    def as_setRareAchievementDataS(self, rareID, rareIconId):
        if self._isDAAPIInited():
            return self.flashObject.as_setRareAchievementData(rareID, rareIconId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\profileachievementsectionmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:25 Støední Evropa (bìžný èas)
