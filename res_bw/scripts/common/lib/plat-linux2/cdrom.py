# 2016.02.13 15:12:12 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-linux2/CDROM.py
CDROMPAUSE = 21249
CDROMRESUME = 21250
CDROMPLAYMSF = 21251
CDROMPLAYTRKIND = 21252
CDROMREADTOCHDR = 21253
CDROMREADTOCENTRY = 21254
CDROMSTOP = 21255
CDROMSTART = 21256
CDROMEJECT = 21257
CDROMVOLCTRL = 21258
CDROMSUBCHNL = 21259
CDROMREADMODE2 = 21260
CDROMREADMODE1 = 21261
CDROMREADAUDIO = 21262
CDROMEJECT_SW = 21263
CDROMMULTISESSION = 21264
CDROM_GET_MCN = 21265
CDROM_GET_UPC = CDROM_GET_MCN
CDROMRESET = 21266
CDROMVOLREAD = 21267
CDROMREADRAW = 21268
CDROMREADCOOKED = 21269
CDROMSEEK = 21270
CDROMPLAYBLK = 21271
CDROMREADALL = 21272
CDROMGETSPINDOWN = 21277
CDROMSETSPINDOWN = 21278
CDROMCLOSETRAY = 21273
CDROM_SET_OPTIONS = 21280
CDROM_CLEAR_OPTIONS = 21281
CDROM_SELECT_SPEED = 21282
CDROM_SELECT_DISC = 21283
CDROM_MEDIA_CHANGED = 21285
CDROM_DRIVE_STATUS = 21286
CDROM_DISC_STATUS = 21287
CDROM_CHANGER_NSLOTS = 21288
CDROM_LOCKDOOR = 21289
CDROM_DEBUG = 21296
CDROM_GET_CAPABILITY = 21297
CDROMAUDIOBUFSIZ = 21378
DVD_READ_STRUCT = 21392
DVD_WRITE_STRUCT = 21393
DVD_AUTH = 21394
CDROM_SEND_PACKET = 21395
CDROM_NEXT_WRITABLE = 21396
CDROM_LAST_WRITTEN = 21397
CDROM_PACKET_SIZE = 12
CGC_DATA_UNKNOWN = 0
CGC_DATA_WRITE = 1
CGC_DATA_READ = 2
CGC_DATA_NONE = 3
CD_MINS = 74
CD_SECS = 60
CD_FRAMES = 75
CD_SYNC_SIZE = 12
CD_MSF_OFFSET = 150
CD_CHUNK_SIZE = 24
CD_NUM_OF_CHUNKS = 98
CD_FRAMESIZE_SUB = 96
CD_HEAD_SIZE = 4
CD_SUBHEAD_SIZE = 8
CD_EDC_SIZE = 4
CD_ZERO_SIZE = 8
CD_ECC_SIZE = 276
CD_FRAMESIZE = 2048
CD_FRAMESIZE_RAW = 2352
CD_FRAMESIZE_RAWER = 2646
CD_FRAMESIZE_RAW1 = CD_FRAMESIZE_RAW - CD_SYNC_SIZE
CD_FRAMESIZE_RAW0 = CD_FRAMESIZE_RAW - CD_SYNC_SIZE - CD_HEAD_SIZE
CD_XA_HEAD = CD_HEAD_SIZE + CD_SUBHEAD_SIZE
CD_XA_TAIL = CD_EDC_SIZE + CD_ECC_SIZE
CD_XA_SYNC_HEAD = CD_SYNC_SIZE + CD_XA_HEAD
CDROM_LBA = 1
CDROM_MSF = 2
CDROM_DATA_TRACK = 4
CDROM_LEADOUT = 170
CDROM_AUDIO_INVALID = 0
CDROM_AUDIO_PLAY = 17
CDROM_AUDIO_PAUSED = 18
CDROM_AUDIO_COMPLETED = 19
CDROM_AUDIO_ERROR = 20
CDROM_AUDIO_NO_STATUS = 21
CDC_CLOSE_TRAY = 1
CDC_OPEN_TRAY = 2
CDC_LOCK = 4
CDC_SELECT_SPEED = 8
CDC_SELECT_DISC = 16
CDC_MULTI_SESSION = 32
CDC_MCN = 64
CDC_MEDIA_CHANGED = 128
CDC_PLAY_AUDIO = 256
CDC_RESET = 512
CDC_IOCTLS = 1024
CDC_DRIVE_STATUS = 2048
CDC_GENERIC_PACKET = 4096
CDC_CD_R = 8192
CDC_CD_RW = 16384
CDC_DVD = 32768
CDC_DVD_R = 65536
CDC_DVD_RAM = 131072
CDS_NO_INFO = 0
CDS_NO_DISC = 1
CDS_TRAY_OPEN = 2
CDS_DRIVE_NOT_READY = 3
CDS_DISC_OK = 4
CDS_AUDIO = 100
CDS_DATA_1 = 101
CDS_DATA_2 = 102
CDS_XA_2_1 = 103
CDS_XA_2_2 = 104
CDS_MIXED = 105
CDO_AUTO_CLOSE = 1
CDO_AUTO_EJECT = 2
CDO_USE_FFLAGS = 4
CDO_LOCK = 8
CDO_CHECK_TYPE = 16
CD_PART_MAX = 64
CD_PART_MASK = CD_PART_MAX - 1
GPCMD_BLANK = 161
GPCMD_CLOSE_TRACK = 91
GPCMD_FLUSH_CACHE = 53
GPCMD_FORMAT_UNIT = 4
GPCMD_GET_CONFIGURATION = 70
GPCMD_GET_EVENT_STATUS_NOTIFICATION = 74
GPCMD_GET_PERFORMANCE = 172
GPCMD_INQUIRY = 18
GPCMD_LOAD_UNLOAD = 166
GPCMD_MECHANISM_STATUS = 189
GPCMD_MODE_SELECT_10 = 85
GPCMD_MODE_SENSE_10 = 90
GPCMD_PAUSE_RESUME = 75
GPCMD_PLAY_AUDIO_10 = 69
GPCMD_PLAY_AUDIO_MSF = 71
GPCMD_PLAY_AUDIO_TI = 72
GPCMD_PLAY_CD = 188
GPCMD_PREVENT_ALLOW_MEDIUM_REMOVAL = 30
GPCMD_READ_10 = 40
GPCMD_READ_12 = 168
GPCMD_READ_CDVD_CAPACITY = 37
GPCMD_READ_CD = 190
GPCMD_READ_CD_MSF = 185
GPCMD_READ_DISC_INFO = 81
GPCMD_READ_DVD_STRUCTURE = 173
GPCMD_READ_FORMAT_CAPACITIES = 35
GPCMD_READ_HEADER = 68
GPCMD_READ_TRACK_RZONE_INFO = 82
GPCMD_READ_SUBCHANNEL = 66
GPCMD_READ_TOC_PMA_ATIP = 67
GPCMD_REPAIR_RZONE_TRACK = 88
GPCMD_REPORT_KEY = 164
GPCMD_REQUEST_SENSE = 3
GPCMD_RESERVE_RZONE_TRACK = 83
GPCMD_SCAN = 186
GPCMD_SEEK = 43
GPCMD_SEND_DVD_STRUCTURE = 173
GPCMD_SEND_EVENT = 162
GPCMD_SEND_KEY = 163
GPCMD_SEND_OPC = 84
GPCMD_SET_READ_AHEAD = 167
GPCMD_SET_STREAMING = 182
GPCMD_START_STOP_UNIT = 27
GPCMD_STOP_PLAY_SCAN = 78
GPCMD_TEST_UNIT_READY = 0
GPCMD_VERIFY_10 = 47
GPCMD_WRITE_10 = 42
GPCMD_WRITE_AND_VERIFY_10 = 46
GPCMD_SET_SPEED = 187
GPCMD_PLAYAUDIO_TI = 72
GPCMD_GET_MEDIA_STATUS = 218
GPMODE_R_W_ERROR_PAGE = 1
GPMODE_WRITE_PARMS_PAGE = 5
GPMODE_AUDIO_CTL_PAGE = 14
GPMODE_POWER_PAGE = 26
GPMODE_FAULT_FAIL_PAGE = 28
GPMODE_TO_PROTECT_PAGE = 29
GPMODE_CAPABILITIES_PAGE = 42
GPMODE_ALL_PAGES = 63
GPMODE_CDROM_PAGE = 13
DVD_STRUCT_PHYSICAL = 0
DVD_STRUCT_COPYRIGHT = 1
DVD_STRUCT_DISCKEY = 2
DVD_STRUCT_BCA = 3
DVD_STRUCT_MANUFACT = 4
DVD_LAYERS = 4
DVD_LU_SEND_AGID = 0
DVD_HOST_SEND_CHALLENGE = 1
DVD_LU_SEND_KEY1 = 2
DVD_LU_SEND_CHALLENGE = 3
DVD_HOST_SEND_KEY2 = 4
DVD_AUTH_ESTABLISHED = 5
DVD_AUTH_FAILURE = 6
DVD_LU_SEND_TITLE_KEY = 7
DVD_LU_SEND_ASF = 8
DVD_INVALIDATE_AGID = 9
DVD_LU_SEND_RPC_STATE = 10
DVD_HOST_SEND_RPC_STATE = 11
DVD_CPM_NO_COPYRIGHT = 0
DVD_CPM_COPYRIGHTED = 1
DVD_CP_SEC_NONE = 0
DVD_CP_SEC_EXIST = 1
DVD_CGMS_UNRESTRICTED = 0
DVD_CGMS_SINGLE = 2
DVD_CGMS_RESTRICTED = 3
CDROM_MAX_SLOTS = 256
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\plat-linux2\cdrom.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.13 15:12:12 St�edn� Evropa (b�n� �as)
