# 2016.02.14 12:40:12 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ChannelCarouselMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelCarouselMeta(BaseDAAPIComponent):

    def channelOpenClick(self, itemID):
        self._printOverrideError('channelOpenClick')

    def closeAll(self):
        self._printOverrideError('closeAll')

    def channelCloseClick(self, itemID):
        self._printOverrideError('channelCloseClick')

    def updateItemDataFocus(self, itemID, wndType, isFocusIn):
        self._printOverrideError('updateItemDataFocus')

    def updateItemDataOpened(self, itemID, wndType, isWindowOpened):
        self._printOverrideError('updateItemDataOpened')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_getBattlesDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getBattlesDataProvider()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\channelcarouselmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:13 Støední Evropa (bìžný èas)
