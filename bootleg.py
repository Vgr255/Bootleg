# Bootleg (2014) by Emanuel 'Vgr' Barry
# The developper of this software (hereafter refered to as "The Developper")
# allows for the use and redistribution of the present software and all its
# associated files (hereafter refered to as "The Software") free of charge. The
# user of the Software consents to the following if they use it in any way:
# - The Developper is not to be help responsible for any sort of damage,
#   physical, virtual or otherwise arising from the use of the Software.
# - Modification and redistribution, partial or total, of the Software is
#   allowed provided this notice is not altered in any way and the name of
#   the Developper appears in the first line of the present file.
# - The Developper is not entitled to anything towards any user of the Software.
# - As well as the present notice, the user needs to acknowledge the following
#   notice, contained in the following paragraph. Use of the present software
#   is an implicit consent to both the current and aforementioned notices.

# This software is provided "as is", in the hopes that it will be useful, but
# without any warranty of any kind, explicit or implicit. In no event is the
# Software Developper to be held accountable for any sort of damage, tort or
# otherwise, arising from the use of the present Software.

import traceback
import argparse
import tempfile
import shutil
import ctypes
import sys
import os

from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import translate as tr
from tools import commands as cmd
from tools import logger as log
from tools import get
from tools import git

if not fn.IsFile.cur("config.py"): # user did not rename their config file, let's silently copy it
    if fn.IsFile.cur("config.py.example"):
        shutil.copy(os.getcwd() + "/config.py.example", os.getcwd() + "/config.py")
    else: # if it can't use default, create a blank config
        newconf = open(os.getcwd() + "/config.py", "w")
        newconf.write("# New blank config created by {0}".format(con.PROGRAM_NAME))
        newconf.close()

import config

if fn.IsFile.cur("cfg.py"):
    import cfg
    for x in cfg.__dict__.keys():
        y = getattr(cfg, x)
        setattr(config, x, y)
    var.FORCE_CONFIG = True # we want config to carry over, overrides DISALLOW_CONFIG

for x, y in config.__dict__.items():
    if config.DISALLOW_CONFIG and not var.FORCE_CONFIG:
        break # don't carry config over if disallowed
    if not x.isupper() or y == "":
        continue
    if x == "FORCE_CONFIG":
        continue # forcing config cannot be manually set
    setattr(var, x, y)

for x, y in con.SETTINGS_PREFIXES.items():
    setattr(con, x, y)

# Launch setup

fn.format_variables()

if var.GIT_LOCATION and var.AUTO_UPDATE:
    if git.check(var.GIT_LOCATION, silent=True):
        if not git.diff(var.GIT_LOCATION, silent=True):
            if not var.SILENT_UPDATE:
                log.logger("", "UPDATE_AVAIL", form=con.PROGRAM_NAME)
                var.UPDATE_READY = True
            else:
                log.logger("", "SILENT_UPD", "REST_AFT_UPD", form=con.PROGRAM_NAME)
                git.pull(var.GIT_LOCATION, silent=True)
                var.ALLOW_RUN = False
    if git.check(var.GIT_LOCATION, silent=True) is None and var.FETCH_GIT: # not a git repo, make it so
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
        fn.attrib(os.getcwd() + "/.git", "+H", "/S /D") # sets the git folder as hidden
        git.pull(var.GIT_LOCATION, silent=True)
        cmd.clean() # cleans the folder to start anew, and takes care of the temp folder if possible
    if git.check(var.GIT_LOCATION, silent=True) and git.diff(var.GIT_LOCATION, silent=True) and not var.IGNORE_LOCAL_CHANGES and var.ALLOW_RUN:
        log.logger("", "UNCOMMITTED_FILES", "")
        line = git.diff_get(var.GIT_LOCATION, silent=True)
        log.logger(line, type="debug")

launcher = argparse.ArgumentParser(description=tr.BOOT_DESC[var.LANGUAGE].format(con.PROGRAM_NAME, con.CURRENT_RELEASE))
launcher.add_argument("--silent", action="store_true")
launcher.add_argument("--run", action="store_true")
#launcher.add_argument("--settings", action="") # still todo
var.SILENT = launcher.parse_args().silent
var.RUNNING = launcher.parse_args().run
#var.ARGUMENTS = launcher.parse_args().settings

var.LADMIN = bool(ctypes.windll.shell32.IsUserAnAdmin())

if not var.LADMIN and not var.IGNORE_NON_ADMIN:
    log.logger("", "WARN_NOT_RUN_ADMIN", "RUN_BOOT_ELEVATED", form=[con.PROGRAM_NAME, con.PROGRAM_NAME])

log.logger("LNCH_PAR", form=[str(launcher.parse_args())[10:-1]], type="debug", display=False, write=var.ALLOW_RUN)

if var.DISALLOW_CONFIG and var.FORCE_CONFIG:
    log.logger("CFG_DIS_OVR", display=False)
elif var.FORCE_CONFIG:
    log.logger("CFG_FORCED", display=False)

def main():
    while var.ALLOW_RUN:
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            log.help("RES_RET", form=con.PROGRAM_NAME)
        elif var.FATAL_ERROR or var.SYS_ERROR:
            if var.IGNORE_FATAL_ERROR or var.DEBUG_MODE:
                var.FATAL_ERROR = []
            if var.IGNORE_SYSTEM_ERROR or var.DEBUG_MODE:
                var.SYS_ERROR = []
        if var.FATAL_ERROR or var.SYS_ERROR:
            fn.end_bootleg_early()
            return
        commands = []
        commands.extend(con.COMMANDS)
        if var.SHOW_HIDDEN_COMMANDS:
            commands.extend(con.HIDDEN_COMMANDS)
            commands.extend(con.ERROR_COMMANDS)
        if var.DEBUG_MODE:
            commands.extend(con.DEBUG_COMMANDS)
        totype = "ENT_CMD"
        form = []
        if var.FINDING:
            totype = "ENT_VAL"
        if var.PARSING:
            totype = "ENT_CHC"
        if var.NEED_RESTART or var.SILENT_RUN:
            totype = ""
        if var.UPDATE_READY:
            totype = "ENT_UPD"
            form = ["YES", "NO"]
        if totype == "ENT_CMD":
            log.help("", "AVAIL_CMD", form=[", ".join(commands), "" if len(commands) == 1 else "PLURAL"])
        if totype:
            log.help("\n", totype, "", form=form)
        else: # nothing to print, either restarting after Git or silently running
            if var.SILENT_RUN:
                cmd.run("silent")
                return
        inp = ""
        try:
            inp = input(con.INPUT_PREFIX).strip()
        except EOFError:
            if var.FINDING:
                parsed = var.FINDING
                log.logger("NO_USR_INP", form=[getattr(var, parsed), parsed], display=False)
                var.FINDING = None
                return
            if var.NEED_RESTART:
                var.ALLOW_RUN = False
                return
        log.logger(con.INPUT_PREFIX, inp, type="input", display=False, splitter="", checker=False)
        if var.FINDING:
            get.setting(inp)
            return
        if var.PARSING:
            fn.parser(inp)
            return
        if var.UPDATE_READY:
            if get.bool(inp) is None:
                log.logger("ERR_INVALID_BOOL", form=["YES", "NO"])
                return
            if get.bool(inp):
                log.logger("", "WAIT_UPD", "")
                if git.pull(var.GIT_LOCATION, silent=True):
                    log.logger("SUCCESS_UPD", "REST_FOR_CHG", form=con.PROGRAM_NAME)
                    var.NEED_RESTART = True
                else:
                    log.logger("FAILED_UPD", "DIS_AUTO_UPD", form=con.PROGRAM_NAME)
            var.UPDATE_READY = False
            return
        if var.NEED_RESTART:
            var.ALLOW_RUN = False
            return
        inp1 = inp.lower().split()
        if not inp:
            log.help("NO_CMD_ENT")
            return
        command = inp1[0]
        params = inp1[1:]
        if var.ERROR and command not in con.ERROR_COMMANDS:
            log.help("NEED_RR")
        else:
            if hasattr(cmd, command):
                iscmd = getattr(cmd, command)
                iscmd(inp, params)
            else: # no such command
                fn.no_such_command(command)

if __name__ == "__main__":
    while var.ALLOW_RUN:
        try:
            main()
        except KeyboardInterrupt:
            if var.ERROR:
                var.ALLOW_RUN = False
                log.logger("SIGTERM_END", display=False)
            else:
                log.logger("SIGTERM_WARN")
                var.ERROR = True
        except:
            if traceback.format_exc(): # if there's a traceback, let's have it
                log.logger("", type="traceback", write=False)
                log.logger(traceback.format_exc(), type="traceback", display=False)
                logname = con.LOGGERS["traceback"]
                if var.DEV_LOG or var.LOG_EVERYTHING:
                    logname = con.LOGGERS["all"]
                logfile = getattr(var, logname + "_FILE")
                log_ext = getattr(var, logname + "_EXT")
                log.logger("ERR_TO_REPORT", "PROVIDE_TRACE", form=[logfile, log_ext], type="error", write=False)
            if str(sys.exc_info()):
                log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True