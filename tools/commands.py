from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import process as pro
from tools import logger as log
from tools import help as helper
from tools import git as _git
from tools import links

import webbrowser
import subprocess
import shutil
import os

__ignore__ = ["con", "var", "fn", "pro", "log", "helper", "_git", "links", "webbrowser", "shutil", "os"]

# This holds all the commands
# Must have (inp, params=[]) in the def,
# Or (*stuff) if parameters don't matter

# To add a new command, simply make a new def block
# The name of the definition is the command

# The following commands don't require any parameter

def exit(*args):
    var.ALLOW_RUN = False

def restart(*args):
    var.ALLOW_RUN = False
    args = [os.getcwd() + "/" + con.PROGRAM_NAME + ".exe", "--retry"]
    if var.SILENT_RUN:
        args.append("--silent")
    if var.DEV_LOG:
        args.append("--dump")
    if var.DISPLAY_EVERYTHING:
        args.append("--verbose")
    if var.DEBUG_MODE:
        args.append("--debug")
    if var.LOG_EVERYTHING:
        args.append("--logall")
    if var.WRITE_EVERYTHING:
        args.append("--writeall")
    if var.PREVIOUS_PRESET:
        args.append("--preset " + var.PRESET)
    if var.LADMIN:
        subprocess.Popen(args)
    else:
        var.ALLOW_RUN = True
        var.RETRY = True

# The following commands may or may not require additional parameters

def clean(inp="", params=[]):
    for x, y in con.LOGGERS.items():
        if "keeplog" in inp and not x == "temp":
            continue
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
            f.close()
            if notdone:
                ft = open(file, "w")
                ft.write("\n".join(notdone))
                ft.write("\n")
                ft.close()
                continue # prevent temp file from being deleted if it fails
        file = logfile + "." + log_ext
        if fn.IsFile.cur(file):
            os.remove(os.getcwd() + "\\" + file)
        for s in con.LANGUAGES.values():
            filel = s[0] + "_" + file
            if fn.IsFile.cur(filel):
                os.remove(os.getcwd() + "\\" + filel)
    if fn.IsFile.cur("cfg.py"):
        os.remove(os.getcwd() + "/cfg.py")
    if fn.IsFile.cur("preset.py"):
        os.remove(os.getcwd() + "/preset.py")
    shutil.rmtree(os.getcwd() + '/__pycache__')
    if os.path.isdir(os.getcwd() + "/tools/__pycache__"):
        shutil.rmtree(os.getcwd() + '/tools/__pycache__')
    for file in os.listdir(os.getcwd()):
        if file[:4:3] == "__" and (file[1:3]+file[4:]).isalnum() and file.islower() and fn.IsFile.cur(file) and len(file) == 15:
            os.remove(os.getcwd() + "/" + file)
    var.ALLOW_RUN = False

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
            getattr(_git, params[0])(args)
            return
    _git.do(args)

def read(inp, params=[]): # Reads a documentation file
    if params:
        docf = os.getcwd() + "/documentation/"
        if var.LANGUAGE in con.READ_SECTIONS.keys():
            sect = con.READ_SECTIONS[var.LANGUAGE] + " "
        else:
            sect = con.READ_SECTIONS["English"] + " "
        reader = ""
        if os.path.isfile(docf + params[0]):
            reader = docf + params[0]
        if con.DOCFILES_EXTS:
            for ext in con.DOCFILES_EXTS:
                if os.path.isfile(docf + params[0] + "." + ext):
                    reader = docf + params[0] + "." + ext
                    break
        if os.path.isdir(docf + var.LANGUAGE):
            docl = docf + var.LANGUAGE + "/"
            if os.path.isfile(docl + params[0]):
                reader = docl + params[0]
            if con.DOCFILES_EXTS:
                for ext in con.DOCFILES_EXTS:
                    if os.path.isfile(docl + params[0] + "." + ext):
                        reader = docl + params[0] + "." + ext
                        break
        if reader:
            digits = False
            lister = False
            viewer = False
            sections = []
            if len(params) > 1:
                digits = True
                if not params[1][0].isdigit():
                    digits = False
                for digit in params[1]:
                    if digit not in "0123456789.":
                        digits = False
                        break
                if digits:
                    digits = params[1]
                elif params[1].lower() in con.READ_GET_SECTIONS:
                    lister = True
            file = open(reader, "r")
            jumper = True if digits else False
            log.help("")
            for line in file.readlines():
                line = line.replace("\n", "")
                if digits:
                    if line.startswith(sect + digits) or digits[0] == "0":
                        jumper = False
                    if "." not in digits:
                        if line.startswith(sect + str(int(digits)+1)):
                            break
                    else:
                        dot = digits.index(".")
                        newdig = int(digits[dot+1:])
                        if line.startswith(sect + digits[:dot] + "." + str(newdig + 1)):
                            break
                        if line.startswith(sect + str(int(digits[:dot]) + 1)):
                            break
                if lister:
                    if "index" in line.lower():
                        viewer = True
                        continue
                if viewer:
                    if line.startswith(sect):
                        break
                    if line[2:].startswith(sect):
                        sections.append("")
                    if line:
                        sections.append(line[2:].replace(":", " "))
                    continue
                if not jumper and not lister:
                    log.help(line)
                    continue
            if sections:
                log.help(sections)
            file.close()
        else:
            log.logger("ERR_DOC_NOT_FOUND", form=params[0])

def get(inp, params=[]):
    if params:
        if params[0] == "mod":
            lines = []
            for lnk in links.__dict__.keys():
                if not lnk.isupper():
                    continue
                getter = lnk.replace("_", "")
                if "".join(params[1:]) in getter or getter in "".join(params[1:]):
                    lines.append(lnk)
            if lines:
                for line in lines:
                    webbrowser.open(line)