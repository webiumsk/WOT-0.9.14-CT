# 2016.02.13 15:00:29 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/customization_2_0/controller.py
from carousel import Carousel
from data_aggregator import DataAggregator
from gui.shared.utils.HangarSpace import g_hangarSpace

class Controller(object):

    def __init__(self):
        self.__aData = DataAggregator()
        self.__carousel = None
        self.__header = None
        self.__cart = None
        self.__hangarCameraLocation = None
        return

    def init(self):
        self.__aData.init()
        self.__carousel = Carousel(self.__aData)
        self.__hangarCameraLocation = g_hangarSpace.space.getCameraLocation()
        g_hangarSpace.space.locateCameraToPreview()
        g_hangarSpace.onSpaceCreate += self.__onHangarSpaceCreate

    def fini(self):
        self.__carousel.fini()
        self.__aData.fini()
        self.__carousel = None
        self.__header = None
        g_hangarSpace.onSpaceCreate -= self.__onHangarSpaceCreate
        return

    def updateTank3DModel(self, isReset = False):
        viewModel = self.__aData.initialViewModel if isReset else self.__aData.viewModel
        camouflageIDToSet, newViewData = viewModel[0], viewModel[1:3]
        if g_hangarSpace.space is not None:
            hangarSpace = g_hangarSpace.space
            hangarSpace.updateVehicleCamouflage(camouflageID=camouflageIDToSet)
            hangarSpace.updateVehicleSticker(newViewData)
            if self.__hangarCameraLocation is not None and isReset:
                hangarSpace.setCameraLocation(**self.__hangarCameraLocation)
            else:
                hangarSpace.locateCameraToPreview()
            hangarSpace.clearSelectedEmblemInfo()
        return

    @property
    def carousel(self):
        return self.__carousel

    @property
    def dataAggregator(self):
        return self.__aData

    def __onHangarSpaceCreate(self):
        if g_hangarSpace.space is not None:
            self.__hangarCameraLocation = g_hangarSpace.space.getCameraLocation()
        return


g_customizationController = Controller()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\customization_2_0\controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:00:29 St�edn� Evropa (b�n� �as)
