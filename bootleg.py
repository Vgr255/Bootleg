# Copyright (c) 2014 Emanuel 'Vgr' Barry
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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
    shutil.copy(os.getcwd() + "/config.py.example", os.getcwd() + "/config.py")

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
    try:
        cfgdict = getattr(config, x)
        vardict = getattr(var, x)
        for a, b in cfgdict.items():
            if not b:
                continue
            vardict[a] = b
    except AttributeError: # not a dict
        setattr(var, x, y)

for x, y in con.SETTINGS_PREFIXES.items():
    setattr(con, x, y)

fn.do_init() # mandatory initialization, everything fails if not initialized (including the logging function)

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
        tmpfold = tempfile.gettempdir() + "\\" + fn.make_random_()
        log.logger("", "CREATING_REPO", "FIRST_SETUP_WAIT", "REST_AFT_UPD", form=[os.getcwd(), con.PROGRAM_NAME, con.PROGRAM_NAME])
        log.logger(tmpfold, type="temp", display=False)
        git.clone([var.GIT_LOCATION, "clone", con.PROCESS_CODE + ".git", tmpfold], silent=True)
        shutil.copytree(tmpfold + "\\.git", os.getcwd() + "\\.git") # moving everything in the current directory, then pull
        for file in con.GIT_COPY_FILES:
            shutil.copy(tmpfold + "\\" + file, os.getcwd() + "\\" + file)
        os.system("C:\\Windows\\System32\\attrib.exe +H \"" + os.getcwd() + "/.git\" /S /D") # sets the git folder as hidden
        git.pull(var.GIT_LOCATION, silent=True)
        cmd.clean() # cleans the folder to start anew, and takes care of the temp folder if possible
    if git.check(var.GIT_LOCATION, silent=True) and git.diff(var.GIT_LOCATION, silent=True) and not var.IGNORE_LOCAL_CHANGES and var.ALLOW_RUN:
        log.logger("", "UNCOMMITTED_FILES")

launcher = argparse.ArgumentParser(description=tr.BOOT_DESC[var.LANGUAGE].format(con.PROGRAM_NAME, con.CURRENT_RELEASE))
launcher.add_argument("--admin", action="store_true")
launcher.add_argument("--silent", action="store_true")
launcher.add_argument("--run", action="store_true")
#launcher.add_argument("--settings", action="") # still todo
var.LADMIN = launcher.parse_args().admin
var.SILENT = launcher.parse_args().silent
var.RUNNING = launcher.parse_args().run
#var.ARGUMENTS = launcher.parse_args().settings

if var.ALLOW_RUN: # prevent it from being printed if it was a new, cloned repo
    log.logger("LNCH_PAR", form=[str(launcher.parse_args())[10:-1]], type="debug", display=False)

if var.DISALLOW_CONFIG and var.FORCE_CONFIG:
    log.logger("CFG_DIS_OVR", display=False)
elif var.FORCE_CONFIG:
    log.logger("CFG_FORCED", display=False)

def main():
    while var.ALLOW_RUN:
        if var.PRINT:
            log.logger(var.PRINT)
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            log.help("RES_RET", form=con.PROGRAM_NAME)
        if var.FATAL_ERROR and not var.ERROR:
            if var.IGNORE_FATAL_ERROR or var.DEBUG_MODE:
                var.FATAL_ERROR = []
            else:
                fn.end_bootleg_early()
                return
        if var.SYS_ERROR and not var.ERROR:
            if var.IGNORE_SYSTEM_ERROR or var.DEBUG_MODE:
                var.SYS_ERROR = []
            else:
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
        if var.FINDING:
            totype = "ENT_VAL"
        if var.PARSING:
            totype = "ENT_CHC"
        if var.UPDATE_READY:
            totype = "ENT_UPD"
        if var.NEED_RESTART:
            totype = ""
        if totype == "ENT_CMD":
            log.help("", "AVAIL_CMD", form=[", ".join(commands), "" if len(commands) == 1 else "s"])
        log.help("\n", totype, "\n")
        inp = ""
        try:
            inp = input().strip()
        except EOFError:
            if var.FINDING:
                parsed = var.FINDING
                log.logger("NO_USR_INP", form=[getattr(var, parsed), parsed], display=False)
                var.FINDING = None
                return
            if var.NEED_RESTART:
                var.ALLOW_RUN = False
                return
        log.logger(inp, type="input", display=False)
        if var.FINDING:
            get.setting(inp)
            return
        if var.PARSING:
            if var.PARSING == "Language":
                fn.chk_game_language(inp)
                return
        if var.UPDATE_READY:
            if get.bool(inp) is None:
                log.logger("ERR_INVALID_BOOL_YN")
                return
            if get.bool(inp):
                log.logger("", "WAIT_UPD", "\n")
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
            try:
                iscmd = getattr(cmd, command)
                iscmd(inp, params)
            except AttributeError: # no such command
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
                log.logger("PROVIDE_TRACE1", "PROVIDE_TRACE2", form=[logfile, log_ext], type="error", write=False)
            if str(sys.exc_info()):
                log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True