# 2016.02.14 12:42:43 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/FAQWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FAQWindowMeta(AbstractWindowView):

    def onLinkClicked(self, name):
        self._printOverrideError('onLinkClicked')

    def as_appendTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_appendText(text)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\faqwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:42:43 Støední Evropa (bìžný èas)
