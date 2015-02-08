# Startup initialization

import configparser
import shutil
import locale
import os

from tools import constants as con
from tools import variables as var
from tools import logger as log

# Copy or create config file if it doesn't exist

if not os.path.isfile(con.CONFIG_FILES[0]): # user did not rename their config file, let's silently copy it
    if os.path.isfile(con.CONFIG_FILES[0] + ".example"):
        shutil.copy(os.path.join(os.getcwd(), con.CONFIG_FILES[0] + ".example"),
            os.path.join(os.getcwd(), con.CONFIG_FILES[0]))
    else: # if it can't use default, create a blank config
        with open(con.CONFIG_FILES[0], "w") as new:
            new.write("# New blank config created by {0}\n".format(con.PROGRAM_NAME))

# Initialize temp folders

for folder in con.CLEAN_FOLDERS:
    if os.path.isdir(folder):
        shutil.rmtree(os.path.join(os.getcwd(), folder))
    os.mkdir(folder)

# Copy existing config file to use

with open(con.CONFIG_FILES[0]) as f, open("temp/" + con.CONFIG_FILES[0], "x") as w:
    lines = f.readlines()
    if lines[0] != "[config]\n":
        w.write("[config]\n")
    for line in lines:
        w.write(line)

# Parse config into a dict

cfgparser = configparser.ConfigParser()
cfgparser.read("temp/" + con.CONFIG_FILES[0])

config = {}

for setting, value in cfgparser["config"].items():
    setting = setting.replace(" ", "_").upper()
    if value == "":
        continue # no need to assign it
    if value.lower() in ("false", "no", "off", "0"):
        config[setting] = False
    elif value.lower() in ("true", "yes", "on", "1"):
        config[setting] = True
    else: # Fallback in case it wasn't true/false (int or string)
        config[setting] = value

# Check for overriding config file

if os.path.isfile(con.CONFIG_FILES[1]):
    with open(con.CONFIG_FILES[1]) as f, open("temp/" + con.CONFIG_FILES[1], "x") as w:
        lines = f.readlines()
        if lines[0] != "[config-override]\n":
            w.write("[config-override]\n")
        for line in lines:
            w.write(line)

    cfgparser.read("temp/" + con.CONFIG_FILES[1])
    config.update(cfgparser["config-override"])

# Convert settings into standalone variables

for x, y in config.items():
    if not x.isupper() or y == "":
        continue
    if x not in con.NON_INT_SETTINGS and (isinstance(y, int) or (isinstance(y, str) and y.isdigit())):
        setattr(var, x, int(y))
        continue
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

# Warn about the time the initialization may take
# Generating decorators takes a long time

log.help("GENERATING_DECORATORS")

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
    for comm, lst in getattr(var, decorator).items():
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

var.LADMIN = bool(ctypes.windll.shell32.IsUserAnAdmin())

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

    try: # 1998 original
        var.GAME_VERSION = 1998
        var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(arch)
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
    except OSError: # does not exist
        try: # 2012 Square Enix store
            var.GAME_VERSION = 2012
            var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1".format(arch)
            reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
        except OSError:
            try: # 2013 Steam
                var.GAME_VERSION = 2013
                var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 39140".format(arch)
                reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, var.REG_ENTRY)
            except OSError:
                var.GAME_VERSION = 1999
                var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(arch)

    if var.GAME_VERSION != 1999:
        var.REG_SOUND = var.REG_ENTRY + "\\1.00\\Sound"
        var.REG_GRAPH = var.REG_ENTRY + "\\1.00\\Graphics"
        var.REG_MIDI = var.REG_ENTRY + "\\1.00\\MIDI"

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

# FFVII installation

if not var.FFVII_PATH:
    var.FFVII_PATH = os.getcwd() + "/Final Fantasy VII"
var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
if var.FFVII_PATH[-1] != "\\":
    var.FFVII_PATH = var.FFVII_PATH + "\\"

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

# Installation image

if var.FFVII_IMAGE:
    if not var.FFVII_IMAGE.lower().endswith((".zip", ".7z", ".rar")):
        var.FFVII_IMAGE = None

# System files

if os.path.isfile(var.SYS_FOLDER + "7za.exe"):
    var.SEVENZ_LOCATION = var.SYS_FOLDER + "7za.exe"
if os.path.isfile(var.SYS_FOLDER + "UnRAR.exe"):
    var.RAR_LOCATION = var.SYS_FOLDER + "UnRAR.exe"
if os.path.isfile(var.SYS_FOLDER + "ulgp.exe"):
    var.ULGP_LOCATION = var.SYS_FOLDER + "ulgp.exe"

# Auto-update checking via git

def git_checking():
    checker = git.check(var.GIT_LOCATION, silent=True)

    if checker is None and var.FETCH_GIT: # not a git repo, make it so
        tmpfold = tempfile.gettempdir() + "\\" + get.random_string()
        log.logger("", "CREATING_REPO", "FIRST_SETUP_WAIT", "REST_AFT_UPD", form=[os.getcwd(), con.PROGRAM_NAME, con.PROGRAM_NAME])
        log.logger(tmpfold, type="temp", display=False)
        git.clone([var.GIT_LOCATION, "clone", con.PROCESS_CODE + ".git", tmpfold], silent=True)
        shutil.copytree(tmpfold + "\\.git", os.getcwd() + "\\.git") # moving everything in the current directory
        if os.path.isdir(os.getcwd() + "\\presets"):
            shutil.rmtree(os.getcwd() + "\\presets") # making sure to overwrite everything
        if os.path.isdir(os.getcwd() + "\\documentation"):
            shutil.rmtree(os.getcwd() + "\\documentation")
        shutil.copytree(tmpfold + "\\presets", os.getcwd() + "\\presets")
        shutil.copytree(tmpfold + "\\documentation", os.getcwd() + "\\documentation")
        shutil.rmtree(os.getcwd() + "\\tools")
        shutil.copytree(tmpfold + "\\tools", os.getcwd() + "\\tools")
        os.remove("config.ini")
        for file in os.listdir(tmpfold):
            if not fn.IsFile.get(tmpfold + "\\" + file): # Not a file, let's not copy it
                continue
            if fn.IsFile.cur(file):
                os.remove(file) # makes sure that the cloned versions are kept, and not the possibly-outdated ones
            shutil.copy(tmpfold + "\\" + file, os.getcwd() + "\\" + file)
        met.AttribFile(os.getcwd() + "/.git", "+H", "/S /D") # sets the git folder as hidden
        git.pull(var.GIT_LOCATION, silent=True)
        cmd.clean() # cleans the folder to start anew, and takes care of the temp folder if possible
        return

    import urllib.request

    diff = git.diff(var.GIT_LOCATION, silent=True)

    rev = git.rev(var.GIT_LOCATION, silent=True)[0].decode("utf-8")
    data = urllib.request.urlopen(con.RELEASE_POINT).read().decode("utf-8").split("\n")
    if data[0] != rev: # update ready! yay!
        if not checker:
            return # rev ID is different but there aren't any changess
        if not diff:
            new = False
            if not fn.IsFile.cur(con.CHANGELOG):
                new = True
            with open(con.CHANGELOG, "a") as f:
                if not new:
                    f.write("\n\n")
                f.write(log.get_timestamp(False, "[%Y-%m-%d] (%H:%M:%S)"))
                f.write("Update received - Version {0}\n".format(data[1]))
                f.write("Commit reference point: {0}\n\n".format(data[0]))
                f.write("Changelog:\n\n" + "\n".join(data[2:]))
            if not var.SILENT_UPDATE:
                log.logger("", "UPDATE_AVAIL", form=[con.PROGRAM_NAME, data[1]])
                var.UPDATE_READY = True
            else:
                log.logger("", "SILENT_UPD")
                if not var.LADMIN:
                    log.logger("REST_AFT_UPD", form=con.PROGRAM_NAME)
                git.pull(var.GIT_LOCATION, silent=True)
                cmd.restart(force=True)

    if checker and diff and not var.IGNORE_LOCAL_CHANGES and var.ALLOW_RUN:
        log.logger("", "UNCOMMITTED_FILES", "")
        line = git.diff_get(var.GIT_LOCATION, silent=True)
        log.logger(line, type="debug")
        get.pause()

if var.GIT_LOCATION and var.AUTO_UPDATE: git_checking()

# Warn if not ran as admin

if not var.LADMIN and not var.IGNORE_NON_ADMIN:
    log.logger("", "WARN_NOT_RUN_ADMIN", "RUN_BOOT_ELEVATED", form=[con.PROGRAM_NAME, con.PROGRAM_NAME], display=var.ALLOW_RUN)
    get.pause()

if var.GET_HELP:
    var.SILENT_RUN = False
    cmd.help("help")
