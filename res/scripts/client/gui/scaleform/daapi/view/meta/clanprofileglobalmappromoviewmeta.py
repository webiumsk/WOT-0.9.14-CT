# 2016.02.14 12:40:14 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileGlobalMapPromoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileGlobalMapPromoViewMeta(BaseDAAPIComponent):

    def showInfo(self):
        self._printOverrideError('showInfo')

    def showMap(self):
        self._printOverrideError('showMap')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\clanprofileglobalmappromoviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:14 St�edn� Evropa (b�n� �as)
