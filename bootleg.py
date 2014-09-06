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
from tools import parser
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
    fn.logger("Config file not found: Silently copied example config file.", type="debug", display=False)
    import config

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
    fn.logger("WARNING: Initialization was disabled. System variables are not set.", type="debug")

def main():
    while var.ALLOW_RUN:
        if var.RETRY:
            fn.initialize()
        if var.ERROR:
            fn.logger("Type 'exit' or 'restart' to exit or restart Bootleg, or Ctrl+C to quit.", write=False)
        if var.FATAL_ERROR:
            if var.IGNORE_FATAL_ERROR or var.DEBUG_MODE:
                var.FATAL_ERROR = None
            else:
                fn.end_bootleg_early()
        fn.logger("\n", write=False)
        fn.logger("Please enter a command:", write=False)
        fn.logger("\n", write=False)
        inp = ""
        try:
            inp = input().strip()
        except EOFError:
            pass # probably Ctrl-C'd anyway
        fn.logger(inp, type="input", display=False)
        inp1 = inp.split()
        if not inp:
            fn.logger("No command was entered.", write=False)
            return
        command = inp1[0].lower()
        params = inp1[1:]
        if var.ERROR and command not in con.ERROR_COMMANDS:
            fn.logger("You must type either 'exit' or 'restart'.", write=False)
        elif command == "exit":
            var.ALLOW_RUN = False
        elif command == "restart":
            var.RETRY = True
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
        elif command == "do":
            done = False
            if params:
                if inp[:22] == "do call python3; exec(" and inp[-2:] == ");":
                    done = True
                    exec(inp[22:-2])
                elif inp[:27] == "do call run function; eval(" and inp[-2:] == ");":
                    done = True
                    eval(inp[27:-2])
                elif inp[:9] == "do print(" and inp[-2:] == ");":
                    done = True
                    prnt = eval(inp[9:-2])
                    fn.logger(prnt, type="debug", write=False)
                elif inp == "do call help; get help;":
                    done = True
                    fn.show_help("\nDevelopper commands:\n\n'do call python3; exec(\"command\");'\n'do call run function; eval(\"module.function\");'\n'do print(\"string\");'")
            if not done:
                fn.no_such_command(command)
        elif command == "clean":
            for x, y in con.LOGGERS.items():
                logfile = getattr(config, y + "_FILE")
                log_ext = getattr(config, y + "_EXT")
                try:
                    os.remove("{0}.{1}".format(logfile, log_ext))
                except WindowsError: # file doesn't exist
                    continue
            try:
                os.remove(os.getcwd() + "/" + var.TEMP_REG + ".reg")
            except WindowsError:
                pass
            shutil.rmtree(os.getcwd() + '/__pycache__')
            var.ALLOW_RUN = False
        elif command == "git":
            pass # still todo
        elif command == "copy":
            if params and " ".join(params) == "config":
                shutil.copy(os.getcwd() + "/config.py", os.getcwd() + "/config.py.example")
        elif command in con.COMMANDS: # command is there but it's not there?
            fn.logger("Error: '{0}' was not found but is in the database. Critical error.".format(command), type="error")
        else:
            fn.no_such_command(command) # if a hidden command is not there, let's say it doesn't exist

if __name__ == "__main__":
    while var.ALLOW_RUN:
        try:
            main()
        except KeyboardInterrupt:
            if var.ERROR:
                var.ALLOW_RUN = False
                fn.logger("Received SIGTERM.", type="debug", display=False)
            else:
                fn.logger("WARNING: SIGTERM Detected.", type="debug")
                var.ERROR = True
        except:
            if traceback.format_exc(): # if there's a traceback, let's have it
                fn.logger("", type="traceback", write=False)
                fn.logger(traceback.format_exc(), type="traceback", display=False)
                logname = con.LOGGERS["traceback"]
                if var.DEV_LOG or var.LOG_EVERYTHING:
                    logname = con.LOGGERS["all"]
                logfile = getattr(config, logname + "_FILE")
                log_ext = getattr(config, logname + "_EXT")
                fn.logger("An error occured. Please report this.\nProvide your '{0}.{1}' file.".format(logfile, log_ext), type="error", write=False)
            if str(sys.exc_info()):
                fn.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
            var.ERROR = True