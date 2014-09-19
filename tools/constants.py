FIRST_DEV = ["PitBrat"]
USER_HELP = ["Vgr", "EQ2Alyza"]
CODERS = ["Vgr", "Insight"]
GUI_CODERS = ["Insight"]
PROCESS_CODERS = ["Vgr"]
GAME_CONV = ["Kompass63"]
BETA_TESTERS = ["Iceboundphoenix", "Vgr", "EQ2Alyza", "Kompass63"]
SPECIAL_THANKS = ["DLPB", "Kranmer", "UGerstl", "Aali", "ficedula", "Covarr", "Qhimm"]
EXT_HELP = ["nasonfish"]

EMAIL = "Bootleg@DadaData.net"

PROCESS_CODE = "https://github.com/Vgr255/Bootleg"

COMMANDS = ["help", "run"]
HIDDEN_COMMANDS = ["debug", "vgr", "do", "clean", "copy", "git"] # some of these don't work

DEBUG_COMMANDS = ["remove", "copy"]
ERROR_COMMANDS = ["exit", "restart"]

DISALLOWED_COMMANDS = ["help", "run"] # commands to be disallowed during setting finding

POSSIBLE_HELP = ["programming", "support", "code", "commands"]
HIDDEN_HELP = ["bootleg"]

POSSIBLE_RUN = ["help", "silent"]
HIDDEN_RUN = []

CURRENT_RELEASE = "041"
BUILD_INFO = "Alpha"
RELEASE_INFO = "August 29th, 2014"

SETTINGS_PREFIXES = {

"USER_VAR":          "/",
"PATH_VAR":          "/", # for simplicity, keep it the same
"SYS_VAR":           "-",
"BOOT_PACK_VAR":     "@", # unusued for now
"KERNEL_VAR":        "%", # also unused, but there for completeness' sake

}

LOGGERS = {"normal": "LOG", "error": "ERROR", "debug": "DEBUG", "traceback": "TRACE", "input": "INPUT", "help": "DEBUG", "all": "MIXED"}

# parsables

USER_SETTINGS = { # uses USER_VAR

"CLOUD_FIELD":       "C",
"TRISH_SAVE":        "S",
"TRISH_PHOENIX":     "P",
"TRISH_MASAMUNE":    "U",
"AERITH_REVIVAL":    "R",
"REUNION":           "O",
"SPELL_PATCH":       "N",
"AVALANCHE":         "A",
"NEW_AERITH":        "V",
"CLOUD_BATTLE":      "H",
"LIMIT_BREAK":       "L",
"MENU_BACKGROUND":   "M",
"KERNEL_SELECT":     "K",
"MOVIES":            "E",
"FIELD_TEXTURES":    "T",
"AVATARS":           "Z",
"IND_AVATARS":       "J",
"BUNNY_GIRLS":       "B",
"SOUNDTRACK":        "W",
"ANY_CD":            "Y",
"OPENING_CREDITS":   "Q",
"CLOUD_SWORDS":      "G",
"BOOT_PACK":         "@",

}

SYS_SETTINGS = { # uses SYS_VAR

"DEBUG_CODE":        "!",
"CREATE_IMAGE":      "$",

}

PATH_SETTINGS = { # uses PATH_VAR

"FFVII_IMAGE":       "I",
"FFVII_PATH":        "D",
"BOOTLEG_TEMP":      "X",
"MOD_LOCATION":      "F",

}

BOOT_PACK_SETTINGS = { # the numbers here are start and end of index

"ROMEO_MAT":         "0:1", # starts at 0, ends at 1. length=1
"CONDOR_MINIGAME":   "1:2",
"AV_SOUND_FX":       "2:3",
"GLITCHED_FIELD":    "3:4",
"TANK_PIRATE_SHIP":  "4:5",
"BARRET_BATTLE":     "5:6",
"BATTLE_SCENES_LGP": "6:7",
"BATTLE_SCENES_PNG": "7:8",
"LAPTOP_KEYPATCH":   "8:9",
"VINCENT_BATTLE":    "9:10",
"FMV_NO_CAIT":       "10:11",
"RETRANSLATED_FMV":  "11:12",
"ASSAULT_BIGGS":     "12:13",
"ASSAULT_JESSIE":    "13:14",
"ASSAULT_WEDGE":     "14:15",
"CLOUD_HAIR":        "15:16",
"TIFA_HAIR":         "16:17",
"YUFFIE_HAIR":       "17:18",
"BASE_MODELS":       "18:19",
"STYLE_SWITCHER":    "19:20",
"FIELD_POTIONS":     "20:21",
"SEPHIROTH_BATTLE":  "21:22",
"GRIMMY_MAGIC":      "22:23",
"GRIMMY_HUGE_MAT":   "23:24",
"LANGUAGE":          "24:25",
"ALWAYS_RUN_TOGGLE": "25:26",
"BUGGY_COSTA":       "26:27",
"SUBMARINE_COSTA":   "27:28",
"HIGHWIND_COSTA":    "28:29",
"CUSTOM_MODELS":     "29:30",
"KRANMER_MASTER":    "30:31",
"TIFA_BATTLE":       "31:32",
"YUFFIE_BATTLE":     "32:33",
"RED_XIII_BATTLE":   "33:34",
"COIN_SKILL":        "34:36", # this is why we need both start and end indexes
"BLUE_COUNTER":      "36:37",
"CAIT_WEAPONS":      "37:38",
"CID_FIELD":         "38:39",
"RE_ANIMATIONS":     "39:40",
"SEPHIROTH_FIELD":   "40:41",
"YUFFIE_FIELD":      "41:42",
"TIFA_FIELD":        "42:43",
"AERITH_FIELD":      "43:44",
"VINCENT_FIELD":     "44:45",
"BARRET_FIELD":      "45:46",
"RED_XIII_FIELD":    "46:47",
"RUBY_WEAPON":       "47:48",
"NIGHTMARE_SEVEN":   "48:49",
"CAIT_BATTLE":       "49:50",
"GUARD_SCORPION":    "50:51",
"SWEEPER":           "51:52",
"MATERIAS_MODELS":   "52:53",

}

KERNEL_SETTINGS = { # I don't know yet if that will be used, but it's there

"REASONABLE_DIFF":   "RD",
"REMASTERED_AI":     "RM",
"SCENE_REDUX":       "SR",
"ITEMS_EASY":        "IE",
"ITEMS_NORMAL":      "IN",
"ITEMS_DIFFICULT":   "ID",
"LOST_WINGS":        "LW",
"MODE_SWITCHING":    "MS",
"AERITH_INSTALLED":  "AE",
"AERITH_HARDCORE":   "AH",
"HARDMOD_INSTALLED": "HC",

}

RANGE = {

"CLOUD_FIELD":       25,
"CLOUD_BATTLE":      12,
"TRISH_SAVE":        5,
"TRISH_PHOENIX":     3,
"TRISH_MASAMUNE":    1,
"AERITH_REVIVAL":    1,
"REUNION":           1,
"SPELL_PATCH":       1,
"AVALANCHE":         1,
"NEW_AERITH":        3,
"VINCENT_BATTLE":    2,
"LIMIT_BREAK":       10,
"MENU_BACKGROUND":   12,
"KERNEL_SELECT":     15,
"MOVIES":            12,
"FIELD_TEXTURES":    4,
"AVATARS":           23,
"BUNNY_GIRLS":       1,
"SOUNDTRACK":        9,
"CLOUD_SWORDS":      -6222222224222234, # a - means it needs as many params as there are digits, each digit is the maximum
"REASONABLE_DIFF":   1,
"REMASTERED_AI":     1,
"SCENE_REDUX":       1,
"ITEMS_EASY":        1,
"ITEMS_NORMAL":      1,
"ITEMS_DIFFICULT":   1,
"LOST_WINGS":        1,
"MODE_SWITCHING":    1,

}

NON_INT_SETTINGS = ["PATH"]
ALLOWED_DEFAULTS = ["USER", "SYS", "BOOT_PACK", "KERNEL"]
USE_INDEX = ["BOOT_PACK"]

# Random stuff

BOOT_ASCII = [
"          ____     ____     ____    _______   _        ______    _____",
"         |  _ \   / __ \   / __ \  |__   __| | |      |  ____|  / ____|",
"         | |_) | | |  | | | |  | |    | |    | |      | |__    | |  __",
"         |  _ <  | |  | | | |  | |    | |    | |      |  __|   | | |_ |",
"         | |_) | | |__| | | |__| |    | |    | |____  | |____  | |__| |",
"         |____/   \____/   \____/     |_|    |______| |______|  \_____|",
" ______ _             _ ______          _               __      _______ _____",
"|  ____(_)           | |  ____|        | |              \ \    / /_   _|_   _|",
"| |__   _ _ __   __ _| | |__ __ _ _ __ | |_ __ _ ___ _   \ \  / /  | |   | |",
"|  __| | | '_ \ / _` | |  __/ _` | '_ \| __/ _` / __| | | \ \/ /   | |   | |",
"| |    | | | | | (_| | | | | (_| | | | | || (_| \__ \ |_| |\  /   _| |_ _| |_",
"|_|    |_|_| |_|\__,_|_|_|  \__,_|_| |_|\__\__,_|___/\__, | \/   |_____|_____|",
"                                                      __/ |",
# the last line is hardcoded in the functions
]