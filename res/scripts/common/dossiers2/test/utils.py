# 2016.02.13 15:07:02 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/dossiers2/test/utils.py


def getVehicleNationID(vehTypeCompDescr):
    return vehTypeCompDescr >> 4 & 15


def isVehicleSPG(vehTypeCompDescr):
    return False


def getInBattleSeriesIndex(seriesName):
    return {'sniper': 0,
     'killing': 1,
     'piercing': 2}[seriesName]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\test\utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:07:02 Støední Evropa (bìžný èas)
