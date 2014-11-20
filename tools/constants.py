FIRST_DEV = ["PitBrat"]
USER_HELP = ["Vgr", "EQ2Alyza"]
CODERS = ["Vgr", "Insight"]
GUI_CODERS = ["Insight"]
PROCESS_CODERS = ["Vgr"]
OTHER_SUPPORT = ["UGerstl", "Kompass63"]
BETA_TESTERS = ["Iceboundphoenix", "Vgr", "EQ2Alyza"]
SPECIAL_THANKS = ["Kranmer", "Aali", "ficedula", "Covarr", "Qhimm"]
EXT_HELP = ["nasonfish"]

DEVELOPERS = ["Vgr"]

TRANSLATORS = ["Vgr"]
FRENCH_TRANSLATORS = ["Vgr"]

EMAIL = "Bootleg@DadaData.net"

PROCESS_CODE = "https://github.com/Vgr255/Bootleg" # This is used in many places, including auto-update. Do not edit lightly.

PROGRAM_NAME = "Bootleg" # this is what appears everywhere (e.g. "Welcome to the Bootleg configurator")

COMMANDS = ["help", "run"]
HIDDEN_COMMANDS = ["debug", "vgr", "do", "clean", "copy", "git"] # some of these don't work. that's why they're hidden

DEBUG_COMMANDS = ["remove", "copy"]
ERROR_COMMANDS = ["exit", "restart"]

INPUT_PREFIX = "" # what will appear in front of the text to input. ">>> " will mimic normal Python behaviour

DISALLOWED_COMMANDS = ["help", "run"] # commands to be disallowed during setting finding

CURRENT_RELEASE = "041"
BUILD_INFO = "Alpha"
RELEASE_INFO = "August 26th, 2014"
VERSION_INFO = "build" # Build, Release, Version, etc

LOGGERS = {"normal": "LOG", "error": "ERROR", "debug": "DEBUG", "traceback": "TRACE", "input": "INPUT", "help": "LOG", "all": "MIXED", "settings": "SETTINGS", "temp": "TEMP", "git": "GIT", "preset": "PRESET"}

IGNORE_ALL = ["all", "settings", "temp", "git", "preset"] # will not write to these files when calling log-to-all
IGNORE_TRANSLATE = ["settings", "temp", "git", "preset"] # will not attempt to translate
IGNORE_CHECK = ["settings", "temp", "git", "preset"] # will print as-is without attempting to check in translate.py
IGNORE_SPLITTER = ["temp", "git"]
IGNORE_TIMESTAMP = ["settings", "temp", "preset"] # will not write timestamps when logging
IGNORE_MIXED = ["settings", "temp", "preset"] # will not write this one to the mixed file
IGNORE_NEWLINE = ["temp", "git", "preset"] # will not print two lines on new run

DISALLOW_CARRYING = ["FORCE_CONFIG"]

LANGUAGES = {"English": ["en", 0], "French": ["fr", 1]}

GAME_LANGUAGES = {"English": ["en", "us", "us", "", 0], "French": ["fr", "fr", "fr", "f", 1], "German": ["de", "gm", "ge", "g", 2], "Spanish": ["es", "sp", "sp", "s", 3], "Italian": ["it", "it", "it", "i", 4]}

# filenames to set variables

FFVII_PATH = ["MODS_AVALANCHE", "MODS_OVERHAUL", "MODS_FINAL"]
LGP_TEMP = ["CHAR", "MINI", "FLEVEL", "FLEVEL_HC", "BATTLE", "MAGIC", "WORLD", "CHOCOBO", "FINAL"]
ADD_PROG_NAME = ["MODS_FINAL"]

TEMP_FOLDERS = ["KERNEL_VANILLA", "KERNEL_REMIX", "KERNEL_HREMIX", "BATTLE", "WORLD_VANILLA", "WORLD", "SCENE_VANILLA", "SCENE_REMIX", "SCENE_HREMIX", "SUB",
                "MAGIC", "FLEVEL", "HFLEVEL", "CHAR", "MINI", "KERNEL_HARDCORE", "KERNEL_REVIVAL", "SCENE_HARDCORE", "SCENE_REVIVAL", "CONDOR", "SNOWBOARD"]

FINAL_PATCH = ["BATTLE", "FIELD", "MINIGAME", "WM", "KERNEL", "SOUND"]

MODS_FINAL = ["BATTLE", "WORLD", "FIELD"]
MODS_AVALANCHE = ["FIELD"]

DATA_WORKING = ["BATTLE", "FIELD", "MINIGAME", "WM"]
FILES_UNDO = ["BATTLE", "MAGIC", "CHAR", "HIGH", "CHOCOBO", "WORLD"]

TRANSLATE_CHANGER = ["cd\\cr_{0}", "cd\\disc_{0}", "menu\\menu_{0}", "wm\\world_{0}", "field\\{1}flevel", "minigame\\{1}chocobo", "minigame\\{1}condor", "minigame\\{1}sub", "minigame\\high-{2}", "minigame\\snowboard-{2}"]

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

NON_INT_SETTINGS = ["FFVII_PATH", "FFVII_IMAGE", "BOOTLEG_TEMP", "MOD_LOCATION", "CD_DRIVE", "SYS_FOLDER"]

# Random stuff

BOOT_ASCII1 = [
"          ____     ____     ____    _______   _        ______    _____",
"         |  _ \   / __ \   / __ \  |__   __| | |      |  ____|  / ____|",
"         | |_) | | |  | | | |  | |    | |    | |      | |__    | |  __",
"         |  _ <  | |  | | | |  | |    | |    | |      |  __|   | | |_ |",
"         | |_) | | |__| | | |__| |    | |    | |____  | |____  | |__| |",
"         |____/   \____/   \____/     |_|    |______| |______|  \_____|",
"  ______ _             _ ______          _               __      _______ _____",
" |  ____(_)           | |  ____|        | |              \ \    / /_   _|_   _|",
" | |__   _ _ __   __ _| | |__ __ _ _ __ | |_ __ _ ___ _   \ \  / /  | |   | |",
" |  __| | | '_ \ / _` | |  __/ _` | '_ \| __/ _` / __| | | \ \/ /   | |   | |",
" | |    | | | | | (_| | | | | (_| | | | | || (_| \__ \ |_| |\  /   _| |_ _| |_",
" |_|    |_|_| |_|\__,_|_|_|  \__,_|_| |_|\__\__,_|___/\__, | \/   |_____|_____|",
"          __      _______ _____                        __/ |",
]


BOOT_ASCII2 = "           \ \  / / |  __| |__) |"

BOOT_ASCII3 = [
"             \  / | |__| | | \ \\",
"              \/   \_____|_|  \_\\  {0} {2}{3}{1}".format(BUILD_INFO, RELEASE_INFO, VERSION_INFO, " - " if RELEASE_INFO else ""),
]