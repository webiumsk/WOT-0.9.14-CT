# 2016.02.13 15:02:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/BasePrebattleView.py
from gui.Scaleform.daapi.view.meta.BasePrebattleViewMeta import BasePrebattleViewMeta
__author__ = 'a_ushyutsau'

class BasePrebattleView(BasePrebattleViewMeta):

    def __init__(self):
        super(BasePrebattleView, self).__init__()

    def canBeClosed(self, callback):
        callback(True)

    def _populate(self):
        super(BasePrebattleView, self)._populate()

    def _dispose(self):
        super(BasePrebattleView, self)._dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\prb_windows\baseprebattleview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:02:21 Støední Evropa (bìžný èas)
