# 2016.02.14 12:40:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TmenXpPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TmenXpPanelMeta(BaseDAAPIComponent):

    def accelerateTmenXp(self, selected):
        self._printOverrideError('accelerateTmenXp')

    def as_setTankmenXpPanelS(self, visible, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmenXpPanel(visible, selected)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\tmenxppanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:31 St�edn� Evropa (b�n� �as)
