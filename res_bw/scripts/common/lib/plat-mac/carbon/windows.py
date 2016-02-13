# 2016.02.13 15:12:33 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/Carbon/Windows.py


def FOUR_CHAR_CODE(x):
    return x


false = 0
true = 1
kWindowNoConstrainAttribute = 2147483648L
kAlertWindowClass = 1
kMovableAlertWindowClass = 2
kModalWindowClass = 3
kMovableModalWindowClass = 4
kFloatingWindowClass = 5
kDocumentWindowClass = 6
kUtilityWindowClass = 8
kHelpWindowClass = 10
kSheetWindowClass = 11
kToolbarWindowClass = 12
kPlainWindowClass = 13
kOverlayWindowClass = 14
kSheetAlertWindowClass = 15
kAltPlainWindowClass = 16
kDrawerWindowClass = 20
kWindowNoAttributes = 0L
kWindowCloseBoxAttribute = 1L
kWindowHorizontalZoomAttribute = 2L
kWindowVerticalZoomAttribute = 4L
kWindowFullZoomAttribute = kWindowVerticalZoomAttribute | kWindowHorizontalZoomAttribute
kWindowCollapseBoxAttribute = 8L
kWindowResizableAttribute = 16L
kWindowSideTitlebarAttribute = 32L
kWindowToolbarButtonAttribute = 64L
kWindowNoUpdatesAttribute = 65536L
kWindowNoActivatesAttribute = 131072L
kWindowOpaqueForEventsAttribute = 262144L
kWindowNoShadowAttribute = 2097152L
kWindowHideOnSuspendAttribute = 16777216L
kWindowStandardHandlerAttribute = 33554432L
kWindowHideOnFullScreenAttribute = 67108864L
kWindowInWindowMenuAttribute = 134217728L
kWindowLiveResizeAttribute = 268435456L
kWindowStandardDocumentAttributes = kWindowCloseBoxAttribute | kWindowFullZoomAttribute | kWindowCollapseBoxAttribute | kWindowResizableAttribute
kWindowStandardFloatingAttributes = kWindowCloseBoxAttribute | kWindowCollapseBoxAttribute
kWindowDefProcType = FOUR_CHAR_CODE('WDEF')
kStandardWindowDefinition = 0
kRoundWindowDefinition = 1
kFloatingWindowDefinition = 124
kDocumentWindowVariantCode = 0
kModalDialogVariantCode = 1
kPlainDialogVariantCode = 2
kShadowDialogVariantCode = 3
kMovableModalDialogVariantCode = 5
kAlertVariantCode = 7
kMovableAlertVariantCode = 9
kSideFloaterVariantCode = 8
documentProc = 0
dBoxProc = 1
plainDBox = 2
altDBoxProc = 3
noGrowDocProc = 4
movableDBoxProc = 5
zoomDocProc = 8
zoomNoGrow = 12
floatProc = 1985
floatGrowProc = 1987
floatZoomProc = 1989
floatZoomGrowProc = 1991
floatSideProc = 1993
floatSideGrowProc = 1995
floatSideZoomProc = 1997
floatSideZoomGrowProc = 1999
rDocProc = 16
kWindowDocumentDefProcResID = 64
kWindowDialogDefProcResID = 65
kWindowUtilityDefProcResID = 66
kWindowUtilitySideTitleDefProcResID = 67
kWindowSheetDefProcResID = 68
kWindowSimpleDefProcResID = 69
kWindowSheetAlertDefProcResID = 70
kWindowDocumentProc = 1024
kWindowGrowDocumentProc = 1025
kWindowVertZoomDocumentProc = 1026
kWindowVertZoomGrowDocumentProc = 1027
kWindowHorizZoomDocumentProc = 1028
kWindowHorizZoomGrowDocumentProc = 1029
kWindowFullZoomDocumentProc = 1030
kWindowFullZoomGrowDocumentProc = 1031
kWindowPlainDialogProc = 1040
kWindowShadowDialogProc = 1041
kWindowModalDialogProc = 1042
kWindowMovableModalDialogProc = 1043
kWindowAlertProc = 1044
kWindowMovableAlertProc = 1045
kWindowMovableModalGrowProc = 1046
kWindowFloatProc = 1057
kWindowFloatGrowProc = 1059
kWindowFloatVertZoomProc = 1061
kWindowFloatVertZoomGrowProc = 1063
kWindowFloatHorizZoomProc = 1065
kWindowFloatHorizZoomGrowProc = 1067
kWindowFloatFullZoomProc = 1069
kWindowFloatFullZoomGrowProc = 1071
kWindowFloatSideProc = 1073
kWindowFloatSideGrowProc = 1075
kWindowFloatSideVertZoomProc = 1077
kWindowFloatSideVertZoomGrowProc = 1079
kWindowFloatSideHorizZoomProc = 1081
kWindowFloatSideHorizZoomGrowProc = 1083
kWindowFloatSideFullZoomProc = 1085
kWindowFloatSideFullZoomGrowProc = 1087
kWindowSheetProc = 1088
kWindowSheetAlertProc = 1120
kWindowSimpleProc = 1104
kWindowSimpleFrameProc = 1105
kWindowNoPosition = 0
kWindowDefaultPosition = 0
kWindowCenterMainScreen = 10250
kWindowAlertPositionMainScreen = 12298
kWindowStaggerMainScreen = 14346
kWindowCenterParentWindow = 43018
kWindowAlertPositionParentWindow = 45066
kWindowStaggerParentWindow = 47114
kWindowCenterParentWindowScreen = 26634
kWindowAlertPositionParentWindowScreen = 28682
kWindowStaggerParentWindowScreen = 30730
kWindowCenterOnMainScreen = 1
kWindowCenterOnParentWindow = 2
kWindowCenterOnParentWindowScreen = 3
kWindowCascadeOnMainScreen = 4
kWindowCascadeOnParentWindow = 5
kWindowCascadeOnParentWindowScreen = 6
kWindowCascadeStartAtParentWindowScreen = 10
kWindowAlertPositionOnMainScreen = 7
kWindowAlertPositionOnParentWindow = 8
kWindowAlertPositionOnParentWindowScreen = 9
kWindowTitleBarRgn = 0
kWindowTitleTextRgn = 1
kWindowCloseBoxRgn = 2
kWindowZoomBoxRgn = 3
kWindowDragRgn = 5
kWindowGrowRgn = 6
kWindowCollapseBoxRgn = 7
kWindowTitleProxyIconRgn = 8
kWindowStructureRgn = 32
kWindowContentRgn = 33
kWindowUpdateRgn = 34
kWindowOpaqueRgn = 35
kWindowGlobalPortRgn = 40
dialogKind = 2
userKind = 8
kDialogWindowKind = 2
kApplicationWindowKind = 8
inDesk = 0
inNoWindow = 0
inMenuBar = 1
inSysWindow = 2
inContent = 3
inDrag = 4
inGrow = 5
inGoAway = 6
inZoomIn = 7
inZoomOut = 8
inCollapseBox = 11
inProxyIcon = 12
inToolbarButton = 13
inStructure = 15
wNoHit = 0
wInContent = 1
wInDrag = 2
wInGrow = 3
wInGoAway = 4
wInZoomIn = 5
wInZoomOut = 6
wInCollapseBox = 9
wInProxyIcon = 10
wInToolbarButton = 11
wInStructure = 13
kWindowMsgDraw = 0
kWindowMsgHitTest = 1
kWindowMsgCalculateShape = 2
kWindowMsgInitialize = 3
kWindowMsgCleanUp = 4
kWindowMsgDrawGrowOutline = 5
kWindowMsgDrawGrowBox = 6
kWindowMsgGetFeatures = 7
kWindowMsgGetRegion = 8
kWindowMsgDragHilite = 9
kWindowMsgModified = 10
kWindowMsgDrawInCurrentPort = 11
kWindowMsgSetupProxyDragImage = 12
kWindowMsgStateChanged = 13
kWindowMsgMeasureTitle = 14
kWindowMsgGetGrowImageRegion = 19
wDraw = 0
wHit = 1
wCalcRgns = 2
wNew = 3
wDispose = 4
wGrow = 5
wDrawGIcon = 6
kWindowStateTitleChanged = 1
kWindowCanGrow = 1
kWindowCanZoom = 2
kWindowCanCollapse = 4
kWindowIsModal = 8
kWindowCanGetWindowRegion = 16
kWindowIsAlert = 32
kWindowHasTitleBar = 64
kWindowSupportsDragHilite = 128
kWindowSupportsModifiedBit = 256
kWindowCanDrawInCurrentPort = 512
kWindowCanSetupProxyDragImage = 1024
kWindowCanMeasureTitle = 2048
kWindowWantsDisposeAtProcessDeath = 4096
kWindowSupportsGetGrowImageRegion = 8192
kWindowDefSupportsColorGrafPort = 1073741826
kWindowIsOpaque = 16384
kWindowSupportsSetGrowImageRegion = 8192
deskPatID = 16
wContentColor = 0
wFrameColor = 1
wTextColor = 2
wHiliteColor = 3
wTitleBarColor = 4
kWindowDefinitionVersionOne = 1
kWindowDefinitionVersionTwo = 2
kWindowIsCollapsedState = 1L
kStoredWindowSystemTag = FOUR_CHAR_CODE('appl')
kStoredBasicWindowDescriptionID = FOUR_CHAR_CODE('sbas')
kStoredWindowPascalTitleID = FOUR_CHAR_CODE('s255')
kWindowDefProcPtr = 0
kWindowDefObjectClass = 1
kWindowDefProcID = 2
kWindowModalityNone = 0
kWindowModalitySystemModal = 1
kWindowModalityAppModal = 2
kWindowModalityWindowModal = 3
kWindowGroupAttrSelectAsLayer = 1
kWindowGroupAttrMoveTogether = 2
kWindowGroupAttrLayerTogether = 4
kWindowGroupAttrSharedActivation = 8
kWindowGroupAttrHideOnCollapse = 16
kWindowActivationScopeNone = 0
kWindowActivationScopeIndependent = 1
kWindowActivationScopeAll = 2
kNextWindowGroup = true
kPreviousWindowGroup = false
kWindowGroupContentsReturnWindows = 1
kWindowGroupContentsRecurse = 2
kWindowGroupContentsVisible = 4
kWindowPaintProcOptionsNone = 0
kScrollWindowNoOptions = 0
kScrollWindowInvalidate = 1L
kScrollWindowEraseToPortBackground = 2L
kWindowMenuIncludeRotate = 1
kWindowZoomTransitionEffect = 1
kWindowSheetTransitionEffect = 2
kWindowSlideTransitionEffect = 3
kWindowShowTransitionAction = 1
kWindowHideTransitionAction = 2
kWindowMoveTransitionAction = 3
kWindowResizeTransitionAction = 4
kWindowConstrainMayResize = 1L
kWindowConstrainMoveRegardlessOfFit = 2L
kWindowConstrainAllowPartial = 4L
kWindowConstrainCalcOnly = 8L
kWindowConstrainUseTransitionWindow = 16L
kWindowConstrainStandardOptions = kWindowConstrainMoveRegardlessOfFit
kWindowLatentVisibleFloater = 1
kWindowLatentVisibleSuspend = 2
kWindowLatentVisibleFullScreen = 4
kWindowLatentVisibleAppHidden = 8
kWindowLatentVisibleCollapsedOwner = 16
kWindowLatentVisibleCollapsedGroup = 32
kWindowPropertyPersistent = 1
kWindowGroupAttrSelectable = kWindowGroupAttrSelectAsLayer
kWindowGroupAttrPositionFixed = kWindowGroupAttrMoveTogether
kWindowGroupAttrZOrderFixed = kWindowGroupAttrLayerTogether
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-mac\carbon\windows.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:12:33 St�edn� Evropa (b�n� �as)
