# 2016.02.14 12:42:42 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelWindowMeta(AbstractWindowView):

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setCloseEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseEnabled(enabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\channelwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:42:42 Støední Evropa (bìžný èas)
