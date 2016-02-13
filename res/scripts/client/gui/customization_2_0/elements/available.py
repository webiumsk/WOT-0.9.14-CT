# 2016.02.13 15:00:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/customization_2_0/elements/available.py
import Math
from constants import IGR_TYPE
from gui.game_control import getIGRCtrl
from gui.shared import g_itemsCache
from helpers.i18n import makeString as _ms
from CurrentVehicle import g_currentVehicle

class Item(object):
    __slots__ = ('_qualifier', '_rawData', '_price', '__isInDossier', '__isInQuests', '__isInShop', '__itemID', '__nationID', '__allowedVehicles', '__notAllowedVehicles', '__allowedNations', '__notAllowedNations', '__igrReplaced', '__numberOfItems', '__numberOfDays', '__groupName')

    def __init__(self, itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName):
        self.__isInDossier = isInDossier
        self.__isInQuests = isInQuests
        self.__isInShop = isInShop
        self.__itemID = itemID
        self.__allowedVehicles = allowedVehicles
        self.__notAllowedVehicles = notAllowedVehicles
        self.__allowedNations = allowedNations
        self.__igrReplaced = igrReplaced
        self.__notAllowedNations = notAllowedNations
        self.__nationID = nationID
        self.__groupName = groupName
        self.__numberOfItems = numberOfItems
        self.__numberOfDays = numberOfDays
        self._qualifier = qualifier
        self._rawData = rawData

    def getID(self):
        return self.__itemID

    def getNationID(self):
        return self.__nationID

    def getGroupName(self):
        return self.__groupName

    def getTexturePath(self):
        raise NotImplementedError

    def getGroup(self):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    def getIgrType(self):
        raise NotImplementedError

    @property
    def numberOfDays(self):
        return self.__numberOfDays

    @property
    def numberOfItems(self):
        return self.__numberOfItems

    @property
    def isReplacedByIGRItem(self):
        return self.__igrReplaced

    @property
    def isAllowedForCurrentVehicle(self):
        intCD = g_currentVehicle.item.intCD
        cNationID = g_currentVehicle.item.descriptor.type.customizationNationID
        if self.__allowedNations and cNationID not in self.__allowedNations:
            return False
        if not self.__allowedVehicles and not self.__notAllowedVehicles:
            return True
        if self.__allowedVehicles and intCD in self.__allowedVehicles:
            return True
        if self.__notAllowedVehicles and intCD not in self.__notAllowedVehicles:
            return True
        return False

    @property
    def isInDossier(self):
        return self.__isInDossier or self.getIgrType() == getIGRCtrl().getRoomType() and getIGRCtrl().getRoomType() != IGR_TYPE.NONE

    @property
    def isInQuests(self):
        return self.__isInQuests

    @property
    def isInShop(self):
        return self.__isInShop

    @property
    def isFeatured(self):
        return False

    @property
    def qualifier(self):
        return self._qualifier

    @property
    def allowedVehicles(self):
        return self.__allowedVehicles

    @property
    def notAllowedVehicles(self):
        return self.__notAllowedVehicles

    @property
    def allowedNations(self):
        return self.__allowedNations

    @property
    def notAllowedNations(self):
        return self.__notAllowedNations

    def priceIsGold(self, duration):
        return not duration

    def markIsInDossier(self):
        self.__isInDossier = True

    def markIsInShop(self):
        self.__isInShop = True

    def setAllowedVehicles(self, allowedVehicles):
        self.__allowedVehicles = allowedVehicles


class Emblem(Item):

    def __init__(self, itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName):
        super(Emblem, self).__init__(itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName)
        self._price = g_itemsCache.items.shop.playerEmblemCost

    def getTexturePath(self):
        return self._rawData[2].replace('gui/maps', '../maps')

    def getGroup(self):
        return self._rawData[0]

    def getName(self):
        return self._rawData[4]

    def getDescription(self):
        return None

    def getIgrType(self):
        return self._rawData[1]

    def getPrice(self, duration):
        return int(round(self._price[duration][0] * g_currentVehicle.item.level * g_itemsCache.items.shop.getEmblemsGroupPriceFactors()[self.getGroup()]))


class Inscription(Item):

    def __init__(self, itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName):
        super(Inscription, self).__init__(itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName)
        self._price = g_itemsCache.items.shop.playerInscriptionCost

    def getTexturePath(self):
        return self._rawData[2].replace('gui/maps', '../maps')

    def getGroup(self):
        return self._rawData[0]

    def getName(self):
        return self._rawData[4]

    def getDescription(self):
        return None

    def getIgrType(self):
        return self._rawData[1]

    @property
    def isFeatured(self):
        return self._rawData[5]

    def getPrice(self, duration):
        return int(round(self._price[duration][0] * g_currentVehicle.item.level * g_itemsCache.items.shop.getInscriptionsGroupPriceFactors(g_currentVehicle.item.descriptor.type.customizationNationID)[self.getGroup()]))


class Camouflage(Item):

    def __init__(self, itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName):
        super(Camouflage, self).__init__(itemID, nationID, rawData, qualifier, isInDossier, isInQuests, isInShop, allowedVehicles, notAllowedVehicles, allowedNations, notAllowedNations, igrReplaced, numberOfItems, numberOfDays, groupName)
        self._price = g_itemsCache.items.shop.camouflageCost

    def getTexturePath(self):
        colors = self._rawData.get('colors', (0, 0, 0, 0))
        weights = Math.Vector4((colors[0] >> 24) / 255.0, (colors[1] >> 24) / 255.0, (colors[2] >> 24) / 255.0, (colors[3] >> 24) / 255.0)
        return 'img://camouflage,{0:d},{1:d},"{2:>s}",{3[0]:d},{3[1]:d},{3[2]:d},{3[3]:d},{4[0]:n},{4[1]:n},{4[2]:n},{4[3]:n},{5:d}'.format(128, 128, self._rawData['texture'], colors, weights, self._rawData.get('armorColor', 0))

    def getGroup(self):
        groupName = self._rawData['groupName']
        if getIGRCtrl().getRoomType() == IGR_TYPE.PREMIUM:
            groupName = groupName[3:] if groupName.startswith('IGR') else groupName
        return groupName

    def getName(self):
        return _ms('{}/label'.format(self._rawData['description']))

    def getDescription(self):
        return _ms('{}/description'.format(self._rawData['description']))

    def getIgrType(self):
        return self._rawData['igrType']

    def getPrice(self, duration):
        return int(round(self._price[duration][0] * g_itemsCache.items.shop.getVehCamouflagePriceFactor(g_currentVehicle.item.descriptor.type.compactDescr) * g_itemsCache.items.shop.getCamouflagesPriceFactors(g_currentVehicle.item.descriptor.type.customizationNationID)[self.getID()]))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\customization_2_0\elements\available.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:00:31 St�edn� Evropa (b�n� �as)
