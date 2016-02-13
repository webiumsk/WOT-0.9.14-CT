# 2016.02.13 15:04:48 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/sounds/sound_systems/wwise_system.py
import WWISE
import SoundGroups
from debug_utils import LOG_DEBUG
from gui.sounds.abstract import SoundSystemAbstract
from gui.sounds.sound_constants import SoundSystems, HQRenderState

class WWISESoundSystem(SoundSystemAbstract):

    def getID(self):
        return SoundSystems.WWISE

    def isMSR(self):
        return WWISE.WG_isMSR()

    def setHQEnabled(self, isEnabled):
        if isEnabled:
            state = HQRenderState.HQ_FOR_ALL
        else:
            state = HQRenderState.LQ_FOR_ALL
        SoundGroups.g_instance.setLQRenderState(state)

    def enableDynamicPreset(self):
        LOG_DEBUG('ue_set_preset_high_dynamic_range has been set')
        WWISE.WW_setVolumeThreshold(-50)
        WWISE.WW_eventGlobalSync('ue_set_preset_high_dynamic_range')

    def disableDynamicPreset(self):
        LOG_DEBUG('ue_set_preset_low_dynamic_range has been set')
        WWISE.WW_setVolumeThreshold(-40)
        WWISE.WW_eventGlobalSync('ue_set_preset_low_dynamic_range')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\sounds\sound_systems\wwise_system.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:04:48 St�edn� Evropa (b�n� �as)
