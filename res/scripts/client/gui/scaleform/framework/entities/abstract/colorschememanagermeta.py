# 2016.02.13 15:03:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ColorSchemeManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ColorSchemeManagerMeta(BaseDAAPIModule):

    def getColorScheme(self, schemeName):
        self._printOverrideError('getColorScheme')

    def as_updateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_update()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\colorschememanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:03:13 St�edn� Evropa (b�n� �as)
