from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import process as pro
from tools import logger as log
from tools import help as helper
from tools import git as _git
import shutil
import os

# This holds all the commands
# Must have (inp, params=[]) in the def all the time, even if not used
# Or (*stuff) if parameters don't matter

# To add a new command, simply make a new def block
# The name of the definition is the command

# The following commands don't require any parameter

def exit(*args):
    var.ALLOW_RUN = False

def restart(*args):
    var.RETRY = True

def clean(*args):
    for x, y in con.LOGGERS.items():
        logfile = getattr(var, y + "_FILE")
        log_ext = getattr(var, y + "_EXT")
        if x == "temp":
            notdone = []
            file = "{0}\\{1}.{2}".format(os.getcwd(), logfile, log_ext)
            f = open(file, "r")
            for line in f.readlines():
                line = line.replace("\n", "")
                if not line:
                    continue
                if not os.path.isdir(line):
                    continue
                try:
                    shutil.rmtree(line)
                except OSError:
                    notdone.append(line)
            if notdone:
                ft = open(file, "w")
                ft.write("\n".join(notdone))
                ft.write("\n")
                ft.close()
                continue # prevent temp file from being deleted if it fails
            f.close()
        file = logfile + "." + log_ext
        if fn.IsFile.cur(file):
            os.remove(os.getcwd() + "\\" + file)
        for s in con.LANGUAGES.values():
            filel = s[0] + "_" + file
            if fn.IsFile.cur(filel):
                os.remove(os.getcwd() + "\\" + filel)
    if fn.IsFile.cur("cfg.py"):
        os.remove(os.getcwd() + "/cfg.py")
    shutil.rmtree(os.getcwd() + '/__pycache__')
    if os.path.isdir(os.getcwd() + "/tools/__pycache__"):
        shutil.rmtree(os.getcwd() + '/tools/__pycache__')
    var.ALLOW_RUN = False

# The following commands may or may not require additional parameters

def help(inp, params=[]):
    if helper.get_help(" ".join(params)):
        formatter = params[0]
        helping = helper.unhandled
        type = "help"
        if hasattr(helper, params[0]):
            helping = getattr(helper, params[0])()
        if helping == helper.unhandled:
            type = "error"
            var.ERROR = True
        elif helping == list(helping):
            helping = "\n".join(helping)
        elif helping == tuple(helping):
            formatter = list(helping[1:])
            helping = helping[0]
        log.help(helping, type=type, form=formatter)

def copy(inp, params=[]):
    if params and " ".join(params) == "config":
        shutil.copy(os.getcwd() + "/config.py", os.getcwd() + "/config.py.example")

def run(inp, params=[]):
    if params:
        if params[0] == "silent":
            pro.run(params=" ".join(params[1:]), silent=True)
        elif params[0] == "extract":
            pro.extract()
        else:
            pro.run(params=" ".join(params))
    elif inp == "silent": # Ran directly from the command line
        pro.run(silent=True)
    else:
        pro.run()

def do(inp, params=[]):
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
            try:
                prnt = str(eval(inp[9:-2]))
            except NameError:
                prnt = "NOT_DEFINED"
            log.logger(prnt, type="debug", write=False, form=inp[9:-2])
        elif inp == "do call help; get help;":
            done = True
            log.help("",
                     "Developper commands:",
                     "",
                     "'do call python3; exec(\"command\");'",
                     "'do call run function; eval(\"module.function\");'",
                     "'do print(\"string\");'")
    if not done:
        fn.no_such_command("do")

def git(inp, params=[]):
    if not var.GIT_LOCATION:
        log.logger("GIT_NOT_INST")
        return
    args = [var.GIT_LOCATION]
    if params:
        args.extend(params)
        if hasattr(_git, params[0]) and params[0] not in ("con", "var", "log", "subprocess", "parse"):
            getattr(_git, " ".join(params))(args)
            return
    _git.do(args)