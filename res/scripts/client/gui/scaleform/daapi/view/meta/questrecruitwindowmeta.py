# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestRecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class QuestRecruitWindowMeta(AbstractWindowView):

    def onApply(self, data):
        self._printOverrideError('onApply')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\questrecruitwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
