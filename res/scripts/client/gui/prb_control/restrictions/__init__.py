# 2016.02.14 12:38:26 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/restrictions/__init__.py
from UnitBase import ROSTER_TYPE
from constants import PREBATTLE_TYPE
from prebattle_shared import decodeRoster

def createPermissions(functional, pID = None):
    clazz = functional._permClass
    rosterKey = functional.getRosterKey(pID=pID)
    if rosterKey is not None:
        team, _ = decodeRoster(rosterKey)
        pInfo = functional.getPlayerInfo(pID=pID, rosterKey=rosterKey)
        if pInfo is not None:
            return clazz(roles=functional.getRoles(pDatabaseID=pInfo.dbID, clanDBID=pInfo.clanDBID, team=team), pState=pInfo.state, teamState=functional.getTeamState(team=team), hasLockedState=functional.hasLockedState())
    return clazz()


def createUnitActionValidator(prbType, rosterSettings, proxy):
    from gui.prb_control.restrictions import limits
    if prbType == PREBATTLE_TYPE.SORTIE:
        validator = limits.SortieActionValidator(rosterSettings)
    elif prbType == PREBATTLE_TYPE.FORT_BATTLE:
        validator = limits.FortBattleActionValidator(rosterSettings)
    elif prbType == PREBATTLE_TYPE.CLUBS:
        validator = limits.ClubsActionValidator(rosterSettings, proxy)
    elif prbType == PREBATTLE_TYPE.SQUAD:
        validator = limits.SquadActionValidator(rosterSettings)
    elif prbType == PREBATTLE_TYPE.FALLOUT:
        validator = limits.FalloutSquadActionValidator(rosterSettings)
    else:
        validator = limits.UnitActionValidator(rosterSettings)
    return validator
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\restrictions\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:38:26 St�edn� Evropa (b�n� �as)
