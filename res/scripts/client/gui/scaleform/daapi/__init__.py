# 2016.02.14 12:38:35 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py
from gui.Scaleform.framework.entities.View import View

class LobbySubView(View):
    __background_alpha__ = 0.6

    def seEnvironment(self, app):
        app.setBackgroundAlpha(self.__background_alpha__)
        super(LobbySubView, self).seEnvironment(app)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:38:35 St�edn� Evropa (b�n� �as)
