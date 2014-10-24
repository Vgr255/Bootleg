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

import argparse
import traceback
import shutil
import os
import sys

from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import translate as tr
from tools import commands as cmd
from tools import logger as log
from tools import get

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

launcher = argparse.ArgumentParser(description=tr.BOOT_DESC.format(con.PROGRAM_NAME, con.CURRENT_RELEASE))
launcher.add_argument("--admin", action="store_true")
launcher.add_argument("--silent", action="store_true")
launcher.add_argument("--run", action="store_true")
#launcher.add_argument("--settings", action="") # still todo
var.LADMIN = launcher.parse_args().admin
var.SILENT = launcher.parse_args().silent
var.RUNNING = launcher.parse_args().run
#var.ARGUMENTS = launcher.parse_args().settings

log.logger(tr.LNCH_PAR.format(str(launcher.parse_args())[10:-1]), type="debug", display=False)

if var.DISALLOW_CONFIG and var.FORCE_CONFIG:
    log.logger(tr.CFG_DIS_OVR, display=False)
elif var.FORCE_CONFIG:
    log.logger(tr.CFG_FORCED, display=False)

def main():
    while var.ALLOW_RUN:
        if var.PRINT:
            log.logger(var.PRINT)
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            log.help(tr.RES_RET.format(con.PROGRAM_NAME))
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
        totype = tr.ENT_CMD
        if var.FINDING:
            totype = tr.ENT_VAL
        if var.PARSING:
            totype = tr.ENT_CHC
        log.help("\n", totype, "\n")
        inp = ""
        try:
            inp = input().strip()
        except EOFError:
            if var.FINDING:
                parsed = var.FINDING
                log.logger(tr.NO_USR_INP.format(getattr(var, parsed), parsed), display=False)
                var.FINDING = None
                return
        log.logger(inp, type="input", display=False)
        if var.FINDING:
            get.setting(inp)
            return
        elif var.PARSING:
            if var.PARSING == "Language":
                fn.chk_game_language(inp)
                return
        inp1 = inp.lower().split()
        if not inp:
            log.help(tr.NO_CMD_ENT)
            return
        command = inp1[0]
        params = inp1[1:]
        if var.ERROR and command not in con.ERROR_COMMANDS:
            log.help(tr.NEED_RR)
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
                log.logger(tr.SIGTERM_END, display=False)
            else:
                log.logger(tr.SIGTERM_WARN)
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
                log.logger(tr.PROVIDE_TRACE.format(logfile, log_ext), type="error", write=False)
            if str(sys.exc_info()):
                log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True