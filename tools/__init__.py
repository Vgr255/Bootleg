# Startup initialization

import configparser
import shutil
import locale
import os

from tools import constants as con
from tools import variables as var
from tools import translate

from lib import logger

# Copy or create config file if it doesn't exist

if not os.path.isfile(con.CONFIG_FILE): # user did not rename their config file, let's silently copy it
    if os.path.isfile(con.CONFIG_FILE + ".example"):
        shutil.copy(os.path.join(os.getcwd(), con.CONFIG_FILE + ".example"),
            os.path.join(os.getcwd(), con.CONFIG_FILE))
    else: # if it can't use default, create a blank config
        with open(con.CONFIG_FILE, "w") as new:
            new.write("# New blank config created by {0}\n".format(con.PROGRAM_NAME))

# Initialize temp folders

for folder in con.CLEAN_FOLDERS:
    if os.path.isdir(folder):
        shutil.rmtree(os.path.join(os.getcwd(), folder))
    os.mkdir(folder)

# Copy existing config file to use

with open(con.CONFIG_FILE) as f, open("temp/" + con.CONFIG_FILE, "x") as w:
    lines = f.readlines()
    if lines[0] != "[config]\n":
        w.write("[config]\n")
    w.write("\n".join(lines))

# Parse config into a dict

cfgparser = configparser.ConfigParser()
cfgparser.read("temp/" + con.CONFIG_FILE)

config = {}

for setting, value in cfgparser["config"].items():
    setting = setting.replace(" ", "_").upper()
    if value == "":
        continue # no need to assign it
    if value.lower() in ("false", "no", "off"):
        config[setting] = False
    elif value.lower() in ("true", "yes", "on"):
        config[setting] = True
    elif value.isdigit() and setting not in con.NON_INT_SETTINGS:
        config[setting] = int(value)
    else: # fallback
        config[setting] = value

backup_settings = {}

for x, y in config.items():
    if not hasattr(var, x) or y == "" or not x.isupper():
        continue
    backup_settings[x] = getattr(var, x)
    setattr(var, x, y)

# Set language

if var.LANGUAGE is not None:
    var.LANGUAGE = var.LANGUAGE.capitalize()
    if var.LANGUAGE in ("Default", "Current", "System"):
        syslng = locale.getdefaultlocale()[0]
        if locale.getlocale()[0]:
            syslng = locale.getlocale()[0]
        var.LANGUAGE = syslng[:2]
    for lang, lng in con.LANGUAGES.items():
        if var.LANGUAGE.lower() == lng[0]:
            var.LANGUAGE = lang
            break
    if var.LANGUAGE not in con.LANGUAGES.keys():
        var.LANGUAGE = None

if var.LANGUAGE is None:
    var.LANGUAGE = "English"

# Prepare the logger

class BootlegLogger(logger.Translater):
    def parser(self, setting):
        output = [setting]
        trout = [setting]
        self.translate(trout, var.LANGUAGE, [], {}, [])
        self.translate(output, "English", [], {}, [])
        getter = con.RANGE.get(setting, 1)
        var.FINDING = setting
        self.show("ENT_VALUE_BETWEEN", "\n", format=[getter])
        msg = trout.splitlines()
        out = output.splitlines()
        if getter > 1:
            self.show(msg.pop(0), "NO_CHG", *msg)
            self.logger(out.pop(0), "NO_CHG", *out, display=False)
        if getter == 1:
            self.show(msg[0], "CHC_NO", "CHC_YES", format=[setting])
            self.logger(out[0], "CHC_NO", "CHC_YES", format=[setting], display=False)
        self.show("", "DEF_TO_USE", format=[getattr(var, setting)])
        self.logger("DEF_TO_USE", format=[getattr(var, setting)], display=False)

LOGGERS = {type: getattr(var, file + "_FILE") + "." + getattr(var, file + "_EXT") for type, file in con.LOGGERS.items()}

log = BootlegLogger("\n", False, None, True, True, LOGGERS,
    (("timestamp", set(con.IGNORE_TIMESTAMP), set(), None, ""),
     ("splitter", set(con.IGNORE_SPLITTER), set(), None, False),
     ("display", set(), {(var, "DEBUG_MODE"), (var, "DISPLAY_EVERYTHING")}, None, True),
     ("write", set(), {(var, "DEBUG_MODE"), (var, "DEV_LOG"), (var, "WRITE_EVERYTHING")}, None, True),
     ("logall", set(), {(var, "LOG_EVERYTHING"), (var, "DEV_LOG")}, LOGGERS, "all"),
     ("files", set(con.IGNORE_ALL), set(), None, None),
     ("all", set(con.IGNORE_MIXED), set(), None, None),
     ("translate", set(con.IGNORE_TRANSLATE), set(), None, None)),
    {lang: short[0] for lang, short in con.LANGUAGES.items()}, "English", var.LANGUAGE,
    translate, None, True, "line", "[A-Z0-9_]*")

# Warn about the time the initialization may take
# Generating decorators takes a long time

log.show("GENERATING_DECORATORS")

# Define the errors

from tools import filenames as fl

errors = {
"Sprinkles"  : {"Message": "MIS_FILE_FROM_SYS", "Format" : ((fl, "SPRINKLES"), (var, "SYS_FOLDER"))},
"Sevenz"     : {"Message": "MIS_FILE_FROM_SYS", "Format" : ((fl, "SEVENZ"), (var, "SYS_FOLDER"))},
"Ff7config"  : {"Message": "MIS_FILE_FROM_SYS", "Format" : ("FF7Config.exe", (var, "FFVII_PATH"))},
"Old_opengl" : {"Message": "OLD_OPENGL_INST"},  "No_opengl": {"Message": "NO_OPENGL_ABORTING"},
}

# Create the decorators dictionaries

for decorator in con.DECORATORS:
    setattr(var, decorator, {})

import tempfile
import platform
import argparse
import ctypes

from tools import parsables as par
from tools import functions as fn
from tools import commands as cmd
from tools import methods as met
from tools import decorators
from tools import help
from tools import get
from tools import git

# Remove useless decorators

for lang in con.LANGUAGES:
    if lang != var.LANGUAGE:
        for decorator in con.DECORATORS:
            decorators.delete(getattr(var, decorator), lang)

# Remove lists from decorators

for decorator in con.DECORATORS:
    for comm, lst in list(getattr(var, decorator).items()):
        if len(lst) == 1:
            getattr(var, decorator)[comm] = lst[0]
        else:
            raise ValueError("unhandled multi-item decorator")

# Make various phantom logging decorators

for module in (log, met, cmd):
    for name in module.__dict__.keys():
        if not name.startswith("__"):
            if not name in var.LOGGER:
                var.LOGGER[name] = []
            var.LOGGER[name].append(getattr(module, name))

# Check for admin privileges

var.LADMIN = ctypes.windll.shell32.IsUserAnAdmin()

# Get processor architecture

var.ARCHITECTURE = platform.architecture()[0]

# Perform various registry initialization operations

var.ON_WINDOWS = platform.system() == "Windows"

if var.ON_WINDOWS:
    import winreg

    arch = "Wow6432Node\\" if var.ARCHITECTURE == "64bit" else ""

    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\" + arch +
            "Microsoft\\Windows\\CurrentVersion\\Uninstall\\Git_is1")
        var.GIT_LOCATION = winreg.QueryValueEx(reg, "InstallLocation")[0] + "bin\\git.exe"
    except OSError:
        if "git" in os.getenv("PATH").lower(): # It's in the path variable
            paths = os.getenv("PATH").lower().split(";")
            for path in paths:
                if "git" in path:
                    var.GIT_LOCATION = path
                    break

    if not var.FFVII_PATH:
        try: # 1998 original
            var.GAME_VERSION = 1998
            var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(arch)
            winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
        except OSError: # does not exist
            try: # 2012 Square Enix store
                var.GAME_VERSION = 2012
                var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1".format(arch)
                winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
            except OSError:
                try: # 2013 Steam
                    var.GAME_VERSION = 2013
                    var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 39140".format(arch)
                    winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
                except OSError:
                    var.GAME_VERSION = 1999
                    var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(arch)

        if var.GAME_VERSION != 1999:
            var.REG_SOUND = var.REG_ENTRY + "\\1.00\\Sound"
            var.REG_GRAPH = var.REG_ENTRY + "\\1.00\\Graphics"
            var.REG_MIDI = var.REG_ENTRY + "\\1.00\\MIDI"
        else:
            var.REG_SOUND = var.REG_GRAPH = var.REG_MIDI = None

    else:
        for name in ("GAME_VERSION", "REG_ENTRY", "REG_SOUND", "REG_GRAPH", "REG_MIDI"):
            setattr(var, name, None)

# Check launch parameters

launcher = argparse.ArgumentParser(description="{0} Final Fantasy VII Mod Configurator {1}".format(con.PROGRAM_NAME, con.CURRENT_RELEASE))
launcher.add_argument("--silent", action="store_true")
launcher.add_argument("--dump", action="store_true")
launcher.add_argument("--verbose", action="store_true")
launcher.add_argument("--debug", action="store_true")
launcher.add_argument("--logall", action="store_true")
launcher.add_argument("--writeall", action="store_true")
launcher.add_argument("--gethelp", action="store_true")
launcher.add_argument("--retry", action="store_true")
launcher.add_argument("--preset")

if launcher.parse_args().silent:
    var.SILENT_RUN = True
if launcher.parse_args().dump:
    var.DEV_LOG = True
if launcher.parse_args().verbose:
    var.DISPLAY_EVERYTHING = True
if launcher.parse_args().debug:
    var.DEBUG_MODE = True
if launcher.parse_args().logall:
    var.LOG_EVERYTHING = True
if launcher.parse_args().writeall:
    var.WRITE_EVERYTHING = True
if launcher.parse_args().gethelp:
    var.GET_HELP = True
if launcher.parse_args().retry:
    var.RETRY = True
if launcher.parse_args().preset:
    var.PREVIOUS_PRESET = var.PRESET
    var.PRESET = launcher.parse_args().preset
    if not var.PRESET.endswith("." + var.PRESET_EXT):
        var.PRESET += "." + var.PRESET_EXT

parms = str(launcher.parse_args())[10:-1]
parms = parms.split(", ")

var.LAUNCH_PARAMS = [x.split("=") for x in parms]

# Bring translators and coders in a single place

for lang in con.LANGUAGES.keys():
    lng = getattr(con, lang.upper() + "_TRANSLATORS", None)
    if lng:
        for trnl in lng:
            if trnl not in con.TRANSLATORS:
                con.TRANSLATORS.append(trnl)

for coder in con.GUI_CODERS + con.PROCESS_CODERS:
    if coder not in con.CODERS:
        con.CODERS.append(coder)

# Variables formatting

# Mods location

if var.MOD_LOCATION:
    if isinstance(var.MOD_LOCATION, (list, tuple, set)):
        var.MOD_LOCATION = ";".join(var.MOD_LOCATION)
    mod_loc = var.MOD_LOCATION.split(";")
    moloc = []
    for semicolon in mod_loc:
        if semicolon == "":
            continue
        semicolon = semicolon.replace("/", "\\")
        if semicolon[-1] != "\\":
            semicolon = semicolon + "\\"
        moloc.append(semicolon)
    if moloc:
        var.MOD_LOCATION = moloc
else:
    var.MOD_LOCATION = [os.getcwd()]

# System folder

if not var.SYS_FOLDER:
    var.SYS_FOLDER = os.getcwd() + "/utils"
var.SYS_FOLDER = var.SYS_FOLDER.replace("/", "\\")
if var.SYS_FOLDER[-1] != "\\":
    var.SYS_FOLDER += "\\"

# System files

if os.path.isfile(var.SYS_FOLDER + "7za.exe"):
    var.SEVENZ_LOCATION = var.SYS_FOLDER + "7za.exe"
else:
    var.SEVENZ_LOCATION = getattr(var, "7ZIP")
if os.path.isfile(var.SYS_FOLDER + "UnRAR.exe"):
    var.RAR_LOCATION = var.SYS_FOLDER + "UnRAR.exe"
else:
    var.RAR_LOCATION = var.UNRAR
if os.path.isfile(var.SYS_FOLDER + "ulgp.exe"):
    var.ULGP_LOCATION = var.SYS_FOLDER + "ulgp.exe"
else:
    var.ULGP_LOCATION = var.ULGP

# Installation image

if var.FFVII_IMAGE:
    if not var.FFVII_IMAGE.lower().endswith((".zip", ".7z", ".rar")):
        var.FFVII_IMAGE = None

# FFVII installation

if var.FFVII_PATH:
    var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
    if not var.FFVII_PATH.endswith("\\"):
        var.FFVII_PATH = var.FFVII_PATH + "\\"
    os.makedirs(var.FFVII_PATH, exist_ok=True)
    if not os.listdir(var.FFVII_PATH) and var.FFVII_IMAGE:
        met.CopyFolder(met.ExtractFile(var.FFVII_IMAGE), var.FFVII_PATH)

# Temporary files

if not var.BOOTLEG_TEMP:
    var.BOOTLEG_TEMP = tempfile.gettempdir() + "\\"
var.BOOTLEG_TEMP = var.BOOTLEG_TEMP.replace("/", "\\")
if var.BOOTLEG_TEMP[-1] != "\\":
    var.BOOTLEG_TEMP += "\\"
if not os.path.isdir(var.BOOTLEG_TEMP):
    os.mkdir(var.BOOTLEG_TEMP)
var.BOOTLEG_TEMP += get.random_string() + "\\"
log.logger(var.BOOTLEG_TEMP, display=False, type="temp")
os.mkdir(var.BOOTLEG_TEMP)

# Auto-update checking via git

def git_checking():
    checker = git.check(var.GIT_LOCATION, silent=True)

    if checker is None and var.FETCH_GIT: # not a git repo, make it so
        tmpfold = tempfile.gettempdir() + "\\" + get.random_string()
        log.logger("", "CREATING_REPO", "FIRST_SETUP_WAIT", form=[os.getcwd(), con.PROGRAM_NAME])
        if not var.LADMIN:
            log.logger("REST_AFT_UPD", format=[con.PROGRAM_NAME])
        log.logger(tmpfold, type="temp", display=False)
        git.clone([var.GIT_LOCATION, "clone", con.PROCESS_CODE + ".git", tmpfold], silent=True)
        for folder in os.listdir(os.getcwd()):
            if os.path.isdir(os.path.join(os.getcwd(), folder)):
                shutil.rmtree(os.path.join(os.getcwd(), folder)) # making sure to overwrite everything
        for file in os.listdir(tmpfold):
            if os.path.isdir(os.path.join(tmpfold, file)): # moving everything in the current directory
                shutil.copytree(os.path.join(tmpfold, file), os.path.join(os.getcwd(), file))
            if os.path.isfile(file):
                os.remove(file)
            if os.path.isfile(os.path.join(tmpfold, file)):
                shutil.copy(os.path.join(tmpfold, file), os.path.join(os.getcwd(), file))
        os.remove("config.ini") # this will have been created earlier
        met.AttribFile(os.getcwd() + "/.git", "+H", "/S /D") # sets the git folder as hidden
        git.pull(var.GIT_LOCATION, silent=True)
        cmd.clean() # cleans the folder to start anew, and takes care of the temp folder if possible
        cmd.restart()
        return

    diff = git.diff(var.GIT_LOCATION, silent=True)

    rev = git.rev(var.GIT_LOCATION, silent=True)
    oldhis = git.log(var.GIT_LOCATION, "HEAD^", silent=True)[0].decode("utf-8")

    if checker and (not diff if not var.IGNORE_LOCAL_CHANGES else True):
        if not var.SILENT_UPDATE:
            log.logger("", "UPDATE_AVAIL", format=[con.PROGRAM_NAME])
            var.UPDATE_READY = True
        else:
            log.logger("", "SILENT_UPD")
            if not var.LADMIN:
                log.logger("REST_AFT_UPD", format=[con.PROGRAM_NAME])
            git.pull(var.GIT_LOCATION, silent=True)
            newrev = git.rev(var.GIT_LOCATION, silent=True)
            history = git.log(var.GIT_LOCATION, rev, silent=True)
            history.append(b"\n") # to have logs end by a newline
            new = os.path.isfile(con.CHANGELOG)
            with open(con.CHANGELOG, "a") as f:
                if new:
                    f.write("\n\n")
                f.write(log._get_timestamp(False, "[%Y-%m-%d] (%H:%M:%S)"))
                f.write("Update received\n\nOld version:\n")
                f.write("\n".join((rev, oldhis, "Changelog:\n")))
                f.write("\n".join([x.decode("utf-8") for x in history]))
            cmd.restart()

    elif checker and diff and not var.IGNORE_LOCAL_CHANGES and var.ALLOW_RUN:
        log.logger("", "UNCOMMITTED_FILES", "")
        log.logger("\n".join(diff), type="debug")
        get.pause()

if var.GIT_LOCATION and var.AUTO_UPDATE: git_checking()

# Warn if not ran as admin

if not var.LADMIN and not var.IGNORE_NON_ADMIN:
    log.logger("", "WARN_NOT_RUN_ADMIN", "RUN_BOOT_ELEVATED", format=[con.PROGRAM_NAME, con.PROGRAM_NAME], display=var.ALLOW_RUN)
    get.pause()

if var.GET_HELP:
    var.SILENT_RUN = False
    cmd.help("help")
