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

try:
    import config
except ImportError: # user did not rename the config file, let's silently copy it
    shutil.copy(os.getcwd() + "/config.py.example", os.getcwd() + "/config.py")
    import config

from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import commands as cmd
from tools import logger as log
from tools import get

if fn.IsFile.cur("cfg.py"):
    import cfg
    for x in cfg.__dict__.keys():
        y = getattr(cfg, x)
        setattr(config, x, y)
        var.FORCE_CONFIG = True # we want config to carry over, overrides DISALLOW_CONFIG

for x, y in config.__dict__.items():
    if not x.isupper():
        continue
    if y is "":
        continue
    if config.DISALLOW_CONFIG and not var.FORCE_CONFIG:
        if hasattr(var, x):
            continue # we carry everything over to var, but only what's not in there if disallowed
    setattr(var, x, y)

if var.DISALLOW_CONFIG and var.FORCE_CONFIG:
    log.logger("Config was disallowed. Overriding.", type="debug", display=False)
elif var.FORCE_CONFIG:
    log.logger("Forcing config into var.", display=False)

if var.ALLOW_INIT:
    fn.do_init()
else:
    log.logger("WARNING: Initialization was disabled. System variables are not set.", type="debug")

def main():
    while var.ALLOW_RUN:
        if var.PRINT:
            log.logger(var.PRINT)
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            log.help("Type 'exit' or 'restart' to exit or restart Bootleg, or Ctrl+C to quit.")
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
        log.help("\n")
        if var.FINDING:
            log.help("Please enter a value:")
        else:
            log.help("Please enter a command:")
        log.help("\n")
        inp = ""
        try:
            inp = input().strip()
        except EOFError:
            if var.FINDING:
                parsed = var.FINDING
                log.logger("No user input was detected. Using {0} for {1}.".format(getattr(var, parsed), parsed), display=False)
                var.FINDING = None
        log.logger(inp, type="input", display=False)
        if var.FINDING:
            get.setting(inp)
            return
        inp1 = inp.lower().split()
        if not inp:
            log.help("No command was entered.")
            return
        command = inp1[0]
        params = inp1[1:]
        if var.ERROR and command not in con.ERROR_COMMANDS:
            log.help("You must type either 'exit' or 'restart'.")
        else:
            iscmd = None
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
                log.logger("Received SIGTERM. Closing process.", type="debug", display=False)
            else:
                log.logger("WARNING: SIGTERM Detected.", type="debug")
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
                log.logger("An error occured. Please report this.\nProvide your '{0}.{1}' file.".format(logfile, log_ext), type="error", write=False)
            if str(sys.exc_info()):
                log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True