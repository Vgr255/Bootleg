﻿# Note: Any setting contained here will be overriden by the config's equivalent setting on startup
# unless DISALLOW_CONFIG is set to True in the config. Do NOT edit this file

# system variables

INITIALIZED = False
RETRY = False
ALLOW_RUN = True
ERROR = False
GET_HELP = False

FATAL_ERROR = []
SYS_ERROR = []

ARCHITECTURE = None # '32bit' or '64bit'
REG_ENTRY = None
REG_SOUND = None
REG_GRAPH = None
REG_MIDI = None

PARSING = None

LANGUAGE = None

PROGRAM_FILES = None
GAME_VERSION = None
GIT_LOCATION = None
LAUNCH_PARAMS = None

NEWFILE_ALL = True
NEWFILE_TRA = True

UPDATE_READY = False
AUTO_UPDATE = False
NEED_RESTART = False

SEVENZ_LOCATION = None
ULGP_LOCATION = None
RAR_LOCATION = None

CD_DRIVE = None

PRESET_IMPORTED = False

# defaults

DEV_LOG = False

DEBUG_MODE = False
DELETE_TEMP = True

LOG_EVERYTHING = False # puts everything in a single file as well
DISPLAY_EVERYTHING = False # displays everything to screen
WRITE_EVERYTHING = False # writes every occurence to file

DISPLAY_TRACEBACK = False # if True, will print traceback to screen

SHOW_HIDDEN_COMMANDS = False

IGNORE_FATAL_ERROR = False
IGNORE_SYSTEM_ERROR = False

ON_WINDOWS = False

FORCE_CONFIG = False # forces config to be carried over no matter what. do NOT manually set.

LOG_FILE = "bootleg"
LOG_EXT = "log"

ERROR_FILE = "errors"
ERROR_EXT = "log"

DEBUG_FILE = "debug"
DEBUG_EXT = "log"

TRACE_FILE = "traceback"
TRACE_EXT = "log"

INPUT_FILE = "input"
INPUT_EXT = "log"

MIXED_FILE = "bootleg"
MIXED_EXT = "dmp"

SETTINGS_FILE = "settings"
SETTINGS_EXT = "ini"

TEMP_FILE = "bootleg"
TEMP_EXT = "tmp"

GIT_FILE = "git"
GIT_EXT = "log"

PRESET_FILE = "bootleg"
PRESET_EXT = "bp"

PRESET = ""
PREVIOUS_PRESET = ""

IGNORE_LOCAL_CHANGES = False
SILENT_UPDATE = False
FETCH_GIT = True

IGNORE_NON_ADMIN = False # Ignores running not as admin

SILENT_RUN = True

GIT_BRANCH = "master"
USE_GIT_LINK = True # if set to False, only "git pull" will be sent
USE_GIT_ORIGIN = False # determines whether or not to use origin in the git pull. overrides above

# The following settings are default. Do not alter.

# User settings

CLOUD_FIELD        = 2
TRISH_SAVE         = 1
TRISH_PHOENIX      = 1
TRISH_MASAMUNE     = 1
AERITH_REVIVAL     = 0
REUNION            = 1
SPELL_PATCH        = 1
AVALANCHE          = 1
NEW_AERITH         = 0
CLOUD_BATTLE       = 3
LIMIT_BREAK        = 5
MENU_BACKGROUND    = 0
KERNEL_SELECT      = 0
MOVIES             = 1
FIELD_TEXTURES     = 1
CLOUD_AVATARS      = 1
BARRET_AVATARS     = 1
TIFA_AVATARS       = 1
AERITH_AVATARS     = 1
RED_XIII_AVATARS   = 1
YUFFIE_AVATARS     = 1
CAIT_AVATARS       = 1
VINCENT_AVATARS    = 1
CID_AVATARS        = 1
YOUNG_AVATARS      = 1
SEPHIROTH_AVATARS  = 1
CHOCOBO_AVATARS    = 1
SOUNDTRACK         = 2
ANY_CD             = 0
OPENING_CREDITS    = 2
AVALANCHE_GUI      = 1
NEW_THREAT_MOD     = 0
HARDCORE_GJOERULV  = 0
NEW_60_FPS         = 0
BUSTER_SWORD       = 4
MYTHRIL_SABER      = 1
HARDEDGE           = 1
BUTTERFLY_EDGE     = 1
ENHANCE_SWORD      = 1
ORGANICS           = 1
CRYSTAL_SWORD      = 1
FORCE_STEALER      = 1
RUNE_BLADE         = 1
MURASAME           = 1
NAIL_BAT           = 1
YOSHIYUKI          = 1
APOCALYPSE         = 1
HEAVENS_CLOUD      = 1
RAGNAROK           = 3
ULTIMA_WEAPON      = 3
ROMEO_MAT          = 0
CONDOR_MINGAME     = 0
AV_SOUND_FX        = 0
GLITCHED_FIELD     = 0
TANK_PIRATE_SHIP   = 0
BARRET_BATTLE      = 0
BATTLE_SCENES_LGP  = 0
BATTLE_SCENES_PNG  = 0
LAPTOP_KEYPATCH    = 0
VINCENT_BATTLE     = 1
FMV_NO_CAIT        = 0
RETRANSLATED_FMV   = 0
ASSAULT_BIGGS      = 0
ASSAULT_JESSIE     = 0
ASSAULT_WEDGE      = 0
CLOUD_HAIR         = 0
TIFA_HAIR          = 0
YUFFIE_HAIR        = 0
BASE_MODELS        = 0
STYLE_SWITCHER     = 0
FIELD_POTIONS      = 0
SEPHIROTH_BATTLE   = 0
GRIMMY_MAGIC       = 0
GRIMMY_HUGE_MAT    = 0
GAME_LANGUAGE      = 0
ALWAYS_RUN_TOGGLE  = 0
BUGGY_COSTA        = 0
SUBMARINE_COSTA    = 0
HIGHWIND_COSTA     = 0
CUSTOM_MODELS      = 0
KRANMER_MASTER     = 0
TIFA_BATTLE        = 0
YUFFIE_BATTLE      = 0
RED_XIII_BATTLE    = 0
COIN_SKILL         = 00 # this needs to be two numbers
BLUE_COUNTER       = 0
CAIT_WEAPONS       = 0
CID_FIELD          = 0
RE_ANIMATIONS      = 0
SEPHIROTH_FIELD    = 0
YUFFIE_FIELD       = 0
TIFA_FIELD         = 0
AERITH_FIELD       = 0
VINCENT_FIELD      = 0
BARRET_FIELD       = 0
RED_XIII_FIELD     = 0
RUBY_WEAPON        = 0
NIGHTMARE_SEVEN    = 0
CAIT_BATTLE        = 0
GUARD_SCORPION     = 0
SWEEPER            = 0
MATERIAS_MODELS    = 0
RUMBAH_MOVIES      = 4 # Only used if MOVIES is 4

# System settings

DEBUG_CODE         = 0
CREATE_IMAGE       = 0

# Path settings

FFVII_IMAGE        = None
FFVII_PATH         = None
BOOTLEG_TEMP       = None
MOD_LOCATION       = None
CD_DRIVE           = None
SYS_FOLDER         = None

# Kernel settings

REASONABLE_DIFF    = 0
REMASTERED_AI      = 0
SCENE_REDUX        = 0
ITEMS_EASY         = 0
ITEMS_NORMAL       = 0
ITEMS_DIFFICULT    = 0
LOST_WINGS         = 0
MODE_SWITCHING     = 0
AERITH_INSTALLED   = 0
AERITH_HARDCORE    = 0
HARDMOD_INSTALLED  = 0

COMMANDS = {}
HELPERS = {}
USERS = {}
