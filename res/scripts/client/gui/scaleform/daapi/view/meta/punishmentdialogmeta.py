# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PunishmentDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class PunishmentDialogMeta(SimpleDialog):

    def as_setMsgTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMsgTitle(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\punishmentdialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:26 St�edn� Evropa (b�n� �as)
