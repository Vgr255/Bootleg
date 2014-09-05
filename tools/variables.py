# system variables

INITIALIZED = False
RETRY = False
ALLOW_RUN = True
NEWFILE = False
SHOW_HIDDEN_COMMANDS = False
SHOW_HIDDEN_HELP = False
ERROR = False
ARCHITECTURE = None # '32bit' or '64bit'
REGISTRY = None # location of the registry
ON_WINDOWS = False # will set it to True if used on Windows. set it here to bypass that on Linux
REG_ENTRY = None
SHORT_REG = None

# defaults

DEV_LOG = False

DEBUG_MODE = False
VERBOSE = False

LOG_EVERYTHING = False
DISPLAY_EVERYTHING = False

SHOW_HIDDEN_COMMANDS = False
SHOW_HIDDEN_HELP = False

TEMP_REG = "bootleg"

ALLOW_INIT = True

# user settings
# currently a dict for simplicity, gets converted to each variable on runtime
# those are defaults

USER_SETTINGS = {

"CLOUD_FIELD":       "0",
"TRISH_SAVE":        "0",
"TRISH_PHOENIX":     "0",
"TRISH_MASAMUNE":    "0",
"AERITH_REVIVAL":    "0",
"REUNION":           "0",
"SPELL_PATCH":       "0",
"AVALANCHE":         "0",
"NEW_AERITH":        "0",
"CLOUD_BATTLE":      "0",
"LIMIT_BREAK":       "0",
"MENU_BACKGROUND":   "0",
"KERNEL_SELECT":     "0",
"MOVIES":            "0",
"FIELD_TEXTURES":    "0",
"AVATARS":           "0",
"IND_AVATARS":       "0",
"BUNNY_GIRLS":       "0",
"SOUNDTRACK":        "0",
"ANY_CD":            "0",
"OPENING_CREDITS":   "0",
"CLOUD_SWORDS":      "0",
"FFVII_IMAGE":       "0",
"FFVII_PATH":        "0",
"BOOTLEG_TEMP":      "0",
"MOD_LOCATION":      "0",
"BRAT_PACK":         "0",

}

SYS_VARIABLES = {

"DEBUG_CODE":        "0",
"CREATE_IMAGE":      "0",

}
