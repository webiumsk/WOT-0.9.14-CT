# 2016.02.14 12:43:37 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/Vibroeffects/Controllers/DeathController.py
from OnceController import OnceController

class DeathController:
    __wasVehicleAlive = None

    def update(self, isVehicleAlive):
        if self.__wasVehicleAlive and not isVehicleAlive:
            OnceController('crit_death_veff')
        self.__wasVehicleAlive = isVehicleAlive
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vibroeffects\controllers\deathcontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:43:37 St�edn� Evropa (b�n� �as)
