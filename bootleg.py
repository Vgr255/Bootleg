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

from tools import process as pro
from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import logger as log
from tools import commands as cmd
from tools import parser

for x in var.__dict__.keys():
    if not x.isupper():
        continue
    if config.DISALLOW_CONFIG:
        break # let's not copy config if disallowed
    if x in config.__dict__.keys():
        setting = getattr(config, x)
        setattr(var, x, setting)

if var.ALLOW_INIT:
    fn.do_init()
else:
    log.logger("WARNING: Initialization was disabled. System variables are not set.", type="debug")

def main():
    while var.ALLOW_RUN:
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            log.logger("Type 'exit' or 'restart' to exit or restart Bootleg, or Ctrl+C to quit.", write=False)
        if var.FATAL_ERROR:
            if var.IGNORE_FATAL_ERROR or var.DEBUG_MODE:
                var.FATAL_ERROR = None
            else:
                fn.end_bootleg_early()
        log.logger("\n", write=False)
        if var.FINDING:
            log.logger("Please select your setting:")
        else:
            log.logger("Please enter a command:", write=False)
        log.logger("\n", write=False)
        inp = ""
        try:
            inp = input().strip()
        except EOFError:
            pass # probably Ctrl-C'd anyway
        log.logger(inp, type="input", display=False)
        if var.FINDING:
            try:
                inp2 = int(inp)
            except ValueError:
                log.logger("Please enter a number.")
                return
            if inp2 in range(0, con.RANGE[var.FINDING] + 1):
                setattr(var, var.FINDING, inp2)
                var.FINDING = None
        inp1 = inp.split()
        if not inp:
            log.logger("No command was entered.", write=False)
            return
        command = inp1[0].lower()
        params = inp1[1:]
        if var.ERROR and command not in con.ERROR_COMMANDS:
            log.logger("You must type either 'exit' or 'restart'.", write=False)
        else:
            iscmd = None
            try:
                iscmd = getattr(cmd, command)
            except AttributeError: # no such command
                fn.no_such_command(command)
            if iscmd:
                iscmd(inp, params)

if __name__ == "__main__":
    while var.ALLOW_RUN:
        try:
            main()
        except KeyboardInterrupt:
            if var.ERROR:
                var.ALLOW_RUN = False
                log.logger("Received SIGTERM.", type="debug", display=False)
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
                logfile = getattr(config, logname + "_FILE")
                log_ext = getattr(config, logname + "_EXT")
                log.logger("An error occured. Please report this.\nProvide your '{0}.{1}' file.".format(logfile, log_ext), type="error", write=False)
            if str(sys.exc_info()):
                log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True