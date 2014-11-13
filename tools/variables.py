# Note: Any setting contained here will be overriden by the config's equivalent setting on startup
# unless DISALLOW_CONFIG is set to True in the config. Do NOT edit this file

# system variables

INITIALIZED = False
RETRY = False
ALLOW_RUN = True
ERROR = False

FATAL_ERROR = []
SYS_ERROR = []

ARCHITECTURE = None # '32bit' or '64bit'
REGISTRY = None # location of the registry
REG_ENTRY = None
REG_SOUND = None
REG_GRAPH = None
REG_MIDI = None

FINDING = None
PARSING = None

USERS = None
COMMANDS = None
LANGUAGE = None

PROGRAM_FILES = None
GAME_VERSION = None
GIT_LOCATION = None

NEWFILE_ALL = True
NEWFILE_TRA = True

UPDATE_READY = False
AUTO_UPDATE = False
NEED_RESTART = False

SEVENZ_LOCATION = None
ULGP_LOCATION = None
RAR_LOCATION = None

CD_DRIVE = None

# launcher arguments. only here for consistency

LADMIN = False # checks if it was launched as admin
SILENT = False # checks if it needs to run in silent mode
RUNNING = False # checks if it should run without prompting the user
ARGUMENTS = None # holds what arguments it was used to be launched

# defaults

DEV_LOG = False

DEBUG_MODE = False
DELETE_TEMP = True

LOG_EVERYTHING = False # puts everything in a single file as well
DISPLAY_EVERYTHING = False # displays everything to screen
WRITE_EVERYTHING = False # writes every occurence to file

SHOW_HIDDEN_COMMANDS = False
SHOW_HIDDEN_HELP = False

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

SETTINGS_FILE = "bootleg"
SETTINGS_EXT = "ini"

TEMP_FILE = "bootleg"
TEMP_EXT = "tmp"

PRESET_FILE = ""
PREVIOUS_PRESET = ""
PRESET_EXT = "bp"
TEMP_PRESET = False

SYS_FOLDER = None

IGNORE_LOCAL_CHANGES = False
SILENT_UPDATE = False
FETCH_GIT = True

IGNORE_NON_ADMIN = False # Ignores running not as admin

SILENT_RUN = True

GIT_BRANCH = "master"
USE_GIT_LINK = True # if set to False, only "git pull" will be sent
USE_GIT_ORIGIN = False # determines whether or not to use origin in the git pull. overrides above

# user settings
# those are dicts for simplicity, gets converted to each variable on runtime
# those are defaults, do not change

USER_SETTINGS = {

"CLOUD_FIELD":       2,
"TRISH_SAVE":        1,
"TRISH_PHOENIX":     1,
"TRISH_MASAMUNE":    1,
"AERITH_REVIVAL":    0,
"REUNION":           1,
"SPELL_PATCH":       1,
"AVALANCHE":         1,
"NEW_AERITH":        0,
"CLOUD_BATTLE":      3,
"LIMIT_BREAK":       5,
"MENU_BACKGROUND":   0,
"KERNEL_SELECT":     0,
"MOVIES":            1,
"FIELD_TEXTURES":    1,
"AVATARS":           1,
"IND_AVATARS":       0, # no default for this
"BUNNY_GIRLS":       0,
"SOUNDTRACK":        2,
"ANY_CD":            0,
"OPENING_CREDITS":   2,
"CLOUD_SWORDS":      4111111111111133,
"BOOT_PACK":         0, # this one doesn't actually get checked

}

SYS_SETTINGS = {

"DEBUG_CODE":        0,
"CREATE_IMAGE":      0,

}

PATH_SETTINGS = {

"FFVII_IMAGE":       None,
"FFVII_PATH":        None,
"BOOTLEG_TEMP":      None,
"MOD_LOCATION":      None,

}

BOOT_PACK_SETTINGS = {

"ROMEO_MAT":         0,
"CONDOR_MINGAME":    0,
"AV_SOUND_FX":       0,
"GLITCHED_FIELD":    0,
"TANK_PIRATE_SHIP":  0,
"BARRET_BATTLE":     0,
"BATTLE_SCENES_LGP": 0,
"BATTLE_SCENES_PNG": 0,
"LAPTOP_KEYPATCH":   0,
"VINCENT_BATTLE":    1,
"FMV_NO_CAIT":       0,
"RETRANSLATED_FMV":  0,
"ASSAULT_BIGGS":     0,
"ASSAULT_JESSIE":    0,
"ASSAULT_WEDGE":     0,
"CLOUD_HAIR":        0,
"TIFA_HAIR":         0,
"YUFFIE_HAIR":       0,
"BASE_MODELS":       0,
"STYLE_SWITCHER":    0,
"FIELD_POTIONS":     0,
"SEPHIROTH_BATTLE":  0,
"GRIMMY_MAGIC":      0,
"GRIMMY_HUGE_MAT":   0,
"GAME_LANGUAGE":     0,
"ALWAYS_RUN_TOGGLE": 0,
"BUGGY_COSTA":       0,
"SUBMARINE_COSTA":   0,
"HIGHWIND_COSTA":    0,
"CUSTOM_MODELS":     0,
"KRANMER_MASTER":    0,
"TIFA_BATTLE":       0,
"YUFFIE_BATTLE":     0,
"RED_XIII_BATTLE":   0,
"COIN_SKILL":        00, # this needs to be two numbers
"BLUE_COUNTER":      0,
"CAIT_WEAPONS":      0,
"CID_FIELD":         0,
"RE_ANIMATIONS":     0,
"SEPHIROTH_FIELD":   0,
"YUFFIE_FIELD":      0,
"TIFA_FIELD":        0,
"AERITH_FIELD":      0,
"VINCENT_FIELD":     0,
"BARRET_FIELD":      0,
"RED_XIII_FIELD":    0,
"RUBY_WEAPON":       0,
"NIGHTMARE_SEVEN":   0,
"CAIT_BATTLE":       0,
"GUARD_SCORPION":    0,
"SWEEPER":           0,
"MATERIAS_MODELS":   0,

}

KERNEL_SETTINGS = {

"REASONABLE_DIFF":   0,
"REMASTERED_AI":     0,
"SCENE_REDUX":       0,
"ITEMS_EASY":        0,
"ITEMS_NORMAL":      0,
"ITEMS_DIFFICULT":   0,
"LOST_WINGS":        0,
"MODE_SWITCHING":    0,
"AERITH_INSTALLED":  0,
"AERITH_HARDCORE":   0,
"HARDMOD_INSTALLED": 0,

}