FIRST_DEV = ["PitBrat"]
USER_HELP = ["Vgr", "EQ2Alyza"]
CODERS = ["Vgr", "Insight"]
GUI_CODERS = ["Insight"]
PROCESS_CODERS = ["Vgr"]
GAME_CONV = ["Kompass63"]
BETA_TESTERS = ["Iceboundphoenix", "Vgr", "EQ2Alyza", "Kompass63"]
SPECIAL_THANKS = ["DLPB", "Kranmer", "UGerstl", "Aali", "ficedula", "Covarr", "Qhimm"]

EMAIL = "Bootleg@DadaData.net"

PROCESS_CODE = "https://github.com/Vgr255/Bootleg"

COMMANDS = ["help", "run"]
HIDDEN_COMMANDS = ["debug", "vgr", "do", "clean"] # some of these don't work

DEBUG_COMMANDS = ["remove", "copy"]
ERROR_COMMANDS = ["exit", "restart"]

POSSIBLE_HELP = ["programming", "support", "code", "commands"]
HIDDEN_HELP = ["vgr", "bootleg", "help"]

POSSIBLE_RUN = ["help", "silent"]
HIDDEN_RUN = []

CURRENT_RELEASE = "041"
BUILD_INFO = "Alpha"
RELEASE_INFO = "August 29th, 2014"

USER_VAR = "/"
SYS_VAR = "-"

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
"FFVII_IMAGE":       "I",
"FFVII_PATH":        "D",
"BOOTLEG_TEMP":      "X",
"MOD_LOCATION":      "F",
"BRAT_PACK":         "@",

}

SYS_VARIABLES = { # uses SYS_VAR

"DEBUG_CODE":        "!",
"CREATE_IMAGE":      "$",

}
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
"                                                     |___/",
]