from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import process as pro
from tools import logger as log
from tools import help as helper
from tools import decorators
from tools import links
from tools import git

import webbrowser
import subprocess
import shutil
import os

for lang in con.LANGUAGES.keys():
    var.COMMANDS[lang] = {}

generator = decorators.generate(hidden=False, error=False, parse=False)

cmd_en = generator(var.COMMANDS["English"])
cmd_fr = generator(var.COMMANDS["French"])

# This holds all the commands
# Must have (inp, params=[]) in the def,
# Or (*stuff) if parameters don't matter

# To add a new command, simply make a new def block
# The name of the definition is the command

# The following commands don't require any parameter

@cmd_en("exit", error=True, arguments=False)
@cmd_fr("quitter", error=True, arguments=False)
def exit():
    var.ALLOW_RUN = False

@cmd_en("restart", "res", error=True, arguments=False)
@cmd_fr("redémarrer", "red", error=True, arguments=False)
def restart():
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

@cmd_en("clean", hidden=True, arguments=False)
@cmd_fr("clean", hidden=True, arguments=False)
def clean(*args):
    for x, y in con.LOGGERS.items():
        if "keeplog" in args and not x == "temp":
            continue
        logfile = getattr(var, y + "_FILE")
        log_ext = getattr(var, y + "_EXT")
        file = logfile + "." + log_ext
        if x == "temp":
            notdone = []
            with open(file) as f:
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
                with open(file, "w") as ft:
                    ft.write("\n".join(notdone) + "\n")
                continue # prevent temp file from being deleted if it fails
        file = logfile + "." + log_ext
        if fn.IsFile.cur(file):
            os.remove(file)
        for s in con.LANGUAGES.values():
            filel = s[0] + "_" + file
            if fn.IsFile.cur(filel):
                os.remove(filel)
    if fn.IsFile.cur("cfg.py"):
        os.remove("cfg.py")
    if fn.IsFile.cur("preset.py"):
        os.remove("preset.py")
    shutil.rmtree(os.getcwd() + '/__pycache__')
    if os.path.isdir("tools/__pycache__"):
        shutil.rmtree(os.getcwd() + '/tools/__pycache__')
    for file in os.listdir(os.getcwd()):
        if file[:4:3] == "__" and (file[1:3]+file[4:]).isalnum() and file.islower() and fn.IsFile.cur(file) and len(file) == 15:
            os.remove(os.getcwd() + "/" + file)
    var.ALLOW_RUN = False

@cmd_en("help", parse=True)
@cmd_fr("aide", parse=True)
def help(inp, params=[]):
    if not params:
        helper.get_help()
        return
    topics = var.HELPERS[var.LANGUAGE]
    poshelp = [x for x in topics]
    if params[0] in poshelp:
        helping = topics[params[0]][0]()
    else:
        helper.get_help(params[0])
        return
    formatter = params[1:]
    if helping == tuple(helping):
        formatter = list(helping[1:])
        helping = helping[0]
    log.help("", helping, type=type, form=formatter)

@cmd_en("copy", hidden=True)
@cmd_fr("copy", hidden=True)
def copy(inp, params=[]):
    if params and " ".join(params) == "config":
        shutil.copy(os.getcwd() + "/config.py", os.getcwd() + "/config.py.example")

@cmd_en("run", parse=True)
@cmd_fr("run", parse=True)
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

@cmd_en("do", hidden=True)
@cmd_fr("do", hidden=True)
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

@cmd_en("git", hidden=True)
@cmd_fr("git", hidden=True)
def _git(inp, params=[]):
    if not var.GIT_LOCATION:
        log.logger("GIT_NOT_INST")
        return
    args = [var.GIT_LOCATION]
    if params:
        line = ""
        larges = False
        larged = False
        escaper = False
        for char in inp[4:]:
            if char == "'":
                if larged or escaper:
                    line += char
                    escaper = False
                    continue
                larges = not larges
                continue
            if char == '"':
                if larges or escaper:
                    line += char
                    escaper = False
                    continue
                larged = not larged
                continue
            if char == "\\":
                if escaper:
                    line += char
                    escaper = False
                    continue
                escaper = True
                continue
            if escaper:
                escaper = False
                continue
            if char == " " and not (larged or larges):
                args.append(line)
                line = ""
                continue
            line += char
        if escaper:
            raise EOFError("Escape character at the end of sequence")
        if larges:
            raise EOFError("No closing single quote")
        if larged:
            raise EOFError("No closing double quote")
        args.append(line)
    git.do(args)

@cmd_en("read", parse=True)
@cmd_fr("lire", parse=True)
def read(inp, params=[]): # Reads a documentation file
    # Priority: 'documentation' folder with full name; same folder without file extension;
    # Language's subfolder with full name; same folder without file extension;
    # 'English' subfolder with full name; same folder without file extension;
    # The first one to match gets taken; same for extensions
    if params:
        docf = os.getcwd() + "/documentation/"
        if var.LANGUAGE in con.READ_SECTIONS.keys():
            sect = con.READ_SECTIONS[var.LANGUAGE] + " "
        else:
            sect = con.READ_SECTIONS["English"] + " "
        reader = ""
        if os.path.isfile(docf + params[0]):
            reader = docf + params[0]
        if not reader and con.DOCFILES_EXTS:
            for ext in con.DOCFILES_EXTS:
                if os.path.isfile(docf + params[0] + "." + ext):
                    reader = docf + params[0] + "." + ext
                    break
        if not reader and os.path.isdir(docf + var.LANGUAGE):
            docl = docf + var.LANGUAGE + "/"
            if os.path.isfile(docl + params[0]):
                reader = docl + params[0]
            if not reader and con.DOCFILES_EXTS:
                for ext in con.DOCFILES_EXTS:
                    if os.path.isfile(docl + params[0] + "." + ext):
                        reader = docl + params[0] + "." + ext
                        break
        if not reader and os.path.isdir(docf + "English"):
            docl = docf + "English/"
            if os.path.isfile(docl + params[0]):
                reader = docl + params[0]
            if not reader and con.DOCFILES_EXTS:
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
                    if var.LANGUAGE in con.READ_INDEX:
                        rind = con.READ_INDEX[var.LANGUAGE]
                    else:
                        rind = con.READ_INDEX["English"]
                    if rind in line.lower():
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
    else:
        log.logger("HELP_READ_CMD")

@cmd_en("get", hidden=True)
@cmd_fr("get", hidden=True)
def get(inp, params=[]):
    if params:
        if params[0] == "mod":
            lines = []
            for lnk in links.__dict__.keys():
                if not lnk.isupper():
                    continue
                getter = lnk.replace("_", "").lower()
                if "".join(params[1:]).lower() in getter or getter in "".join(params[1:]).lower():
                    lines.append(lnk)
            if lines:
                for line in lines:
                    webbrowser.open(line)
