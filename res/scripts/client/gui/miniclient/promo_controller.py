# 2016.02.13 15:00:41 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/promo_controller.py
from helpers import aop

class ShowPromoBrowserPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.PromoController', 'PromoController', 'onLobbyInited', aspects=(aop.DummyAspect,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\promo_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:00:41 St�edn� Evropa (b�n� �as)
