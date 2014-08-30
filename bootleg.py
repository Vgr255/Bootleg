# Copyright (c) 2014 Emanuel Barry
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
from tools import help
import config
import sys

DEBUG_MODE = config.DEBUG_MODE
VERBOSE = config.VERBOSE

def main():
    while var.ALLOW_RUN:
        if not var.INITIALIZED or var.RETRY:
            fn.initialize()
        input = sys.stdin.read()
        input = input.split()
        command = input[0]
        params = input[1:]
        if not command.lower() in con.COMMANDS:
            print("'{0}' is not a valid command.".format(command))
        elif command == "help":
            help.get_help(helping=params)
        elif command == "run":
            if params[0] == "silent":
                pro.run(silent=True, params=" ".join(params[1:]))
            elif params[0] == "extract":
                pro.extract()
            else:
                pro.run(params=" ".join(params))

if __name__ == "__main__":
    try:
        main()
    except:
        fn.logger(type="error")