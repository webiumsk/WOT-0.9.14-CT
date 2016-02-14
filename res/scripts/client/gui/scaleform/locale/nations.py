# 2016.02.14 12:40:55 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/locale/NATIONS.py


class NATIONS(object):
    USSR = '#nations:ussr'
    GERMANY = '#nations:germany'
    USA = '#nations:usa'
    FRANCE = '#nations:france'
    UK = '#nations:uk'
    JAPAN = '#nations:japan'
    CZECH = '#nations:czech'
    CHINA = '#nations:china'
    all_ENUM = (USSR,
     GERMANY,
     USA,
     FRANCE,
     UK,
     JAPAN,
     CZECH,
     CHINA)

    @staticmethod
    def all(key):
        outcome = '#nations:%s' % key
        if outcome not in NATIONS.all_ENUM:
            raise Exception, 'locale key "' + outcome + '" was not found'
        return outcome
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\locale\nations.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:40:55 Støední Evropa (bìžný èas)
