# 2016.02.14 12:40:31 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TrainingWindowMeta(AbstractWindowView):

    def updateTrainingRoom(self, key, time, isPrivate, description):
        self._printOverrideError('updateTrainingRoom')

    def as_setDataS(self, info, mapsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(info, mapsData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\trainingwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:31 Støední Evropa (bìžný èas)
