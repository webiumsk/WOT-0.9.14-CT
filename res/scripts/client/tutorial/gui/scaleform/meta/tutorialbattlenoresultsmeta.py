# 2016.02.14 12:43:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialBattleNoResultsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialBattleNoResultsMeta(AbstractWindowView):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\gui\scaleform\meta\tutorialbattlenoresultsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:43:33 St�edn� Evropa (b�n� �as)
