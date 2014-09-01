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

from tools import process as pro
from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools.help import get_help
import shutil
import argparse
import sys
import os
import traceback

try:
    import config
except ImportError: # user did not rename the config file, let's silently copy it
    shutil.copy(os.getcwd() + "/config.py.example", os.getcwd() + "/config.py")
    import config

for x in var.__dict__.keys():
    if not x.isupper():
        continue
    if config.DISALLOW_CONFIG:
        break # let's not copy config if disallowed
    if x in config.__dict__.keys():
        setting = getattr(config, x)
        setattr(var, x, setting)

fn.get_settings()

def main():
    while var.ALLOW_RUN:
        if not var.INITIALIZED or var.RETRY:
            fn.initialize()
            fn.begin_anew()
        fn.logger("\n", write=False)
        inp = input().strip()
        fn.logger(inp, type="input", display=False)
        inp = inp.split()
        command = inp[0]
        params = inp[1:]
        if command.lower() not in con.COMMANDS and command.lower() not in con.HIDDEN_COMMANDS:
            fn.logger("'{0}' is not a valid command.".format(command), write=False)
            fn.logger("Available command{1}: {0}".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else ""), write=False)
            if var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS:
                fn.logger("Hidden command{1}: {0}".format(", ".join(con.HIDDEN_COMMANDS), "s" if len(con.HIDDEN_COMMANDS) > 1 else ""))
            if var.DEBUG_MODE:
                fn.logger("Debug command{1}: {0}".format(", ".join(con.DEBUG_COMMANDS), "s" if len(con.DEBUG_COMMANDS) > 1 else ""))
        elif command == "help":
            get_help(helping=" ".join(params))
        elif command == "run":
            if params:
                if params[0] == "silent":
                    pro.run(params=" ".join(params[1:]), silent=True)
                elif params[0] == "extract":
                    pro.extract()
                else:
                    pro.run(params=" ".join(params))
        else: # command is there but it's not there?
            fn.logger("Error: '{0}' was not found but is in the database. Critical error.".format(command), type="error")

if __name__ == "__main__":
    try:
        main()
    except:
        if traceback.format_exc(): # if there's a traceback, let's have it
            fn.logger("", type="traceback")
            fn.logger(traceback.format_exc(), type="traceback")
            logname = con.LOGGERS["traceback"]
            if var.DEV_LOG or var.LOG_EVERYTHING:
                logname = con.LOGGERS["all"]
            logfile = getattr(config, logname + "_FILE")
            log_ext = getattr(config, logname + "_EXT")
            fn.logger("An error occured. Please report this.\nProvide your '{0}.{1}' file.".format(logfile, log_ext))
        fn.logger(sys.exc_info(), type="error", display=False) # log which exception occured