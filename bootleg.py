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
import config
import sys
import traceback

var.DEBUG_MODE = config.DEBUG_MODE
var.VERBOSE = config.VERBOSE

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
            fn.logger("Available commands: {0}".format(", ".join(con.COMMANDS)), write=False)
            if var.DEBUG_MODE or config.SHOW_HIDDEN_COMMANDS:
                fn.logger("Hidden commands: {0}".format(", ".join(con.HIDDEN_COMMANDS)))
        elif command == "help":
            get_help(helping=" ".join(params))
        elif command == "run":
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
    except Exception:
        fn.get_traceback(traceback.format_exc())
    except:
        fn.logger(sys.exc_info(), type="error")