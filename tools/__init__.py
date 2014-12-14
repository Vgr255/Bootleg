﻿# Startup initialization

import shutil
import locale
import os

from tools import constants as con
from tools import variables as var
from tools import logger as log

# Copy or create config file if it doesn't exist

if not os.path.isfile("config.py"): # user did not rename their config file, let's silently copy it
    if os.path.isfile("config.py.example"):
        shutil.copy(os.getcwd() + "/config.py.example", os.getcwd() + "/config.py")
    else: # if it can't use default, create a blank config
        with open("config.py", "w") as new:
            new.write("# New blank config created by {0}".format(con.PROGRAM_NAME))

import config

# Check for overriding config file

if os.path.isfile("cfg.py"):
    import cfg
    for x in cfg.__dict__.keys():
        y = getattr(cfg, x)
        setattr(config, x, y)
    var.FORCE_CONFIG = True # we want config to carry over, overrides DISALLOW_CONFIG

# Convert settings into standalone variables

for x, y in config.__dict__.items():
    if config.DISALLOW_CONFIG and not var.FORCE_CONFIG:
        break # don't carry config over if disallowed
    if not x.isupper() or y == "":
        continue
    if x in con.DISALLOW_CARRYING:
        continue # forcing config cannot be manually set
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

import tempfile
import platform
import argparse
import ctypes

from tools import parsables as par
from tools import functions as fn
from tools import commands as cmd
from tools import methods as met
from tools import help
from tools import get
from tools import git

# Check for admin privileges

var.LADMIN = bool(ctypes.windll.shell32.IsUserAnAdmin())

# Get processor architecture

var.ARCHITECTURE = platform.architecture()[0]

# Perform various registry initialization operations

var.ON_WINDOWS = False

if platform.system() == "Windows":
    import winreg
    var.ON_WINDOWS = True

    try: # Checks for 64-bit version if exists
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Git_is1")
        var.GIT_LOCATION = winreg.QueryValueEx(reg, "InstallLocation")[0] + "bin\\git.exe"
    except OSError:
        try: # Checks for 32-bit version if exists
            reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Git_is1")
            var.GIT_LOCATION = winreg.QueryValueEx(reg, "InstallLocation")[0] + "bin\\git.exe"
        except OSError:
            if "git" in os.getenv("PATH").lower(): # It's in the path variable
                paths = os.getenv("PATH").lower().split(";")
                for path in paths:
                    if "git" in path:
                        var.GIT_LOCATION = path
                        break

    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
    liner = ""
    if var.ARCHITECTURE == "64bit":
        reg = winreg.OpenKey(reg, "Wow6432Node")
        liner = "Wow6432Node\\"
    try: # 1998 original
        reg = winreg.OpenKey(reg, "Square Soft, Inc.\\Final Fantasy VII")
        var.GAME_VERSION = 1998
        var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(liner)
    except OSError: # does not exist
        try: # 2012 Square Enix store
            reg = winreg.OpenKey(reg, "Microsoft")
            reg = winreg.OpenKey(reg, "Windows")
            reg = winreg.OpenKey(reg, "CurrentVersion")
            reg = winreg.OpenKey(reg, "Uninstall")
            reg = winreg.OpenKey(reg, "{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1")
            var.GAME_VERSION = 2012
            var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1".format(liner)
        except OSError:
            try: # 2013 Steam
                reg = winreg.OpenKey(reg, "Steam App 39140")
                var.GAME_VERSION = 2013
                var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 39140".format(liner)
            except OSError:
                var.GAME_VERSION = 1999
                var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(liner)

    if not var.GAME_VERSION == 1999:
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

var.LAUNCH_PARAMS = str(launcher.parse_args())[10:-1]

# Bring translators and coders in a single place

for lang in con.LANGUAGES.keys():
    if hasattr(con, lang.upper() + "_TRANSLATORS"):
        lng = getattr(con, lang.upper() + "_TRANSLATORS")
        for trnl in lng:
            if trnl not in con.TRANSLATORS:
                con.TRANSLATORS.append(trnl)

for coder in con.GUI_CODERS + con.PROCESS_CODERS:
    if coder not in con.CODERS:
        con.CODERS.append(coder)

# Variables formatting

# Mods location

if var.MOD_LOCATION:
    if var.MOD_LOCATION == list(var.MOD_LOCATION):
        var.MOD_LOCATION = ";".join(var.MOD_LOCATION)
    mod_loc = var.MOD_LOCATION.split(";")
    moloc = []
    for semicolon in mod_loc:
        if semicolon == "":
            continue
        semicolon = semicolon.replace("/", "\\")
        if not semicolon[-1:] == "\\":
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
if not var.SYS_FOLDER[-1:] == "\\":
    var.SYS_FOLDER += "\\"

# FFVII installation

if not var.FFVII_PATH:
    var.FFVII_PATH = os.getcwd() + "/Final Fantasy VII"
var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
if not var.FFVII_PATH[-1:] == "\\":
    var.FFVII_PATH = var.FFVII_PATH + "\\"

# Temporary files

if not var.BOOTLEG_TEMP:
    var.BOOTLEG_TEMP = tempfile.gettempdir() + "\\"
var.BOOTLEG_TEMP = var.BOOTLEG_TEMP.replace("/", "\\")
if not var.BOOTLEG_TEMP[-1:] == "\\":
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

# Warn if not on Windows

if not var.ON_WINDOWS:
    log.logger("NOT_ON_WINDOWS", form=[con.PROGRAM_NAME], type="error")

# Auto-update checking via git

if var.GIT_LOCATION and var.AUTO_UPDATE:
    checker = git.check(var.GIT_LOCATION, silent=True)
    diff = git.diff(var.GIT_LOCATION, silent=True)
    if checker:
        if not diff:
            if not var.SILENT_UPDATE:
                log.logger("", "UPDATE_AVAIL", form=con.PROGRAM_NAME)
                var.UPDATE_READY = True
            else:
                log.logger("", "SILENT_UPD", "REST_AFT_UPD", form=con.PROGRAM_NAME)
                git.pull(var.GIT_LOCATION, silent=True)
                var.ALLOW_RUN = False
    if checker is None and var.FETCH_GIT: # not a git repo, make it so
        tmpfold = tempfile.gettempdir() + "\\" + get.random_string()
        log.logger("", "CREATING_REPO", "FIRST_SETUP_WAIT", "REST_AFT_UPD", form=[os.getcwd(), con.PROGRAM_NAME, con.PROGRAM_NAME])
        log.logger(tmpfold, type="temp", display=False)
        git.clone([var.GIT_LOCATION, "clone", con.PROCESS_CODE + ".git", tmpfold], silent=True)
        shutil.copytree(tmpfold + "\\.git", os.getcwd() + "\\.git") # moving everything in the current directory
        if os.path.isdir(os.getcwd() + "\\presets"):
            shutil.rmtree(os.getcwd() + "\\presets") # making sure to overwrite everything
        shutil.copytree(tmpfold + "\\presets", os.getcwd() + "\\presets")
        shutil.rmtree(os.getcwd() + "\\tools")
        shutil.copytree(tmpfold + "\\tools", os.getcwd() + "\\tools")
        os.remove("config.py")
        for file in os.listdir(tmpfold):
            if not fn.IsFile.get(tmpfold + "\\" + file): # Not a file, let's not copy it
                continue
            if fn.IsFile.cur(file):
                os.remove(file) # makes sure that the cloned versions are kept, and not the possibly-outdated ones
            shutil.copy(tmpfold + "\\" + file, os.getcwd() + "\\" + file)
        met.AttribFile(os.getcwd() + "/.git", "+H", "/S /D") # sets the git folder as hidden
        git.pull(var.GIT_LOCATION, silent=True)
        cmd.clean() # cleans the folder to start anew, and takes care of the temp folder if possible
    if checker and diff and not var.IGNORE_LOCAL_CHANGES and var.ALLOW_RUN:
        log.logger("", "UNCOMMITTED_FILES", "")
        line = git.diff_get(var.GIT_LOCATION, silent=True)
        log.logger(line, type="debug")

# Warn if not ran as admin

if not var.LADMIN and not var.IGNORE_NON_ADMIN:
    log.logger("", "WARN_NOT_RUN_ADMIN", "RUN_BOOT_ELEVATED", form=[con.PROGRAM_NAME, con.PROGRAM_NAME], display=var.ALLOW_RUN)

# Check for forced config

if var.DISALLOW_CONFIG and var.FORCE_CONFIG:
    log.logger("CFG_DIS_OVR", display=False)
elif var.FORCE_CONFIG:
    log.logger("CFG_FORCED", display=False)

if var.GET_HELP:
    var.SILENT_RUN = False
    cmd.help("help")
