# 2016.02.13 15:02:27 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTest.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.WindowsManager import g_windowsManager
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.utils.functions import getViewName

class _ProfileTest(object):

    def __init__(self):
        pass

    def showProfileWindow(self, userName = 'Happy_3rd_friend'):
        g_windowsManager.window.fireEvent(events.LoadViewEvent(VIEW_ALIAS.PROFILE_WINDOW, getViewName(VIEW_ALIAS.PROFILE_WINDOW, 'test'), {'userName': userName}), EVENT_BUS_SCOPE.LOBBY)


g_instance = _ProfileTest()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\profile\profiletest.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:27 Støední Evropa (bìžný èas)
