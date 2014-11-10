from tools import constants as con
from tools import variables as var
from tools import translate as tr
from tools import parser as par
from tools import logger as log

import datetime
import platform
import hashlib
import random
import shutil

def settings():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        for s, u in y.items():
            setattr(var, s, u)
            if x[:-9] not in con.NON_INT_SETTINGS:
                setattr(var, s, int(u)) # make sure all parameters are integers

def parser(setting): # get function xyz() in parser.py for variable XYZ
    parse = None
    for x in par.__dict__.keys():
        y = setting.lower()
        if not x == y:
            continue
        parse = getattr(par, y)
        break # we got what we wanted
    return parse

def bool(inp):
    if tr.YES[var.LANGUAGE].lower() == inp.lower():
        return 1
    if tr.YES[var.LANGUAGE].lower()[0] == inp.lower():
        return 1
    if tr.TRUE[var.LANGUAGE].lower() == inp.lower():
        return 1
    if tr.TRUE[var.LANGUAGE].lower()[0] == inp.lower():
        return 1
    if inp.isdigit() and int(inp) == 1:
        return 1
    if tr.NO[var.LANGUAGE].lower() == inp.lower():
        return 0
    if tr.NO[var.LANGUAGE].lower()[0] == inp.lower():
        return 0
    if tr.FALSE[var.LANGUAGE].lower() == inp.lower():
        return 0
    if tr.FALSE[var.LANGUAGE].lower()[0] == inp.lower():
        return 0
    if inp.isdigit() and int(inp) == 0:
        return 0
    return None

def _type(inp): # Here for sake of being here, but don't use that unless absolutely necessary
    return str(type(inp))[8:-2] # "foo" is "str", ["foo", "bar"] is "list", etc

def random_string(): # generates a random string of numbers for temporary folders
    iter = random.randrange(1, 10)
    tmpnum = str(datetime.datetime.now())
    tmpnum = tmpnum.replace("-", "").replace(" ", "").replace(":", "").replace(".", "") # make the whole thing only numbers
    tmpnum = int(tmpnum) * random.randrange(1, 9)
    tmpnum = str(random.randrange(100, 999)) + str(tmpnum) + str(random.randrange(100, 999))
    tmpnum = tmpnum[:13] + str(random.randrange(1000, 9999)) + tmpnum[13:26]
    tmpnum = "[" + tmpnum + "]"
    if iter % 2:
        return tmpnum
    tmpnum = hashlib.md5(bytes(tmpnum, "utf-8")).hexdigest().upper()
    tmpnum = "{" + tmpnum[:18] + "-"
    tmpnum = tmpnum + hashlib.md5(bytes(tmpnum, "utf-8")).hexdigest().upper()
    tmpnum = tmpnum[:31] + "}"
    return tmpnum

def setting(inp): # sets variables
    if not inp.isdigit():
        log.logger("ENTER_ONLY_NUMS")
        return
    inp2 = int(inp)
    if con.RANGE[var.FINDING] < 0:
        rng = str(con.RANGE[var.FINDING])[1:]
        if len(str(inp2)) == len(rng):
            for x in range(0, int(len(rng))):
                if int(str(inp2)[x]) in range(0, int(rng[x]) + 1):
                    continue
                else:
                    log.logger("ERR_VALUE_OUTBOUNDS", form=[x + 1, str(inp2)[x], rng[x]])
                    return
            setattr(var, var.FINDING, inp2)
            log.logger("USR_INP_SET_USING", form=[inp2, var.FINDING], display=False)
            var.FINDING = None
        else:
            log.logger("ENT_EXACT_DIG", form=len(rng))
    elif inp2 in range(0, con.RANGE[var.FINDING] + 1):
        setattr(var, var.FINDING, inp2)
        log.logger("SET_DEF_NO_INP_USED", form=[var.FINDING, inp2], display=False)
        var.FINDING = None

def architecture(): # find processor architecture
    var.ARCHITECTURE = platform.architecture()[0]
    if str(platform.architecture()[1]) == "WindowsPE":
        var.ON_WINDOWS = True
    rgent = "[HKEY_LOCAL_MACHINE\\SOFTWARE\\"
    if var.ARCHITECTURE == "64bit":
        rgent = rgent + "Wow6432Node\\"
    var.SHORT_REG = rgent + "Square Soft, Inc."
    var.REG_ENTRY = var.SHORT_REG + "\\Final Fantasy VII"
    var.PROGRAM_FILES = "C:\\Program Files{0}\\Square Soft, Inc\\Final Fantasy VII\\".format(" (x86)" if var.ARCHITECTURE == "64bit" else "")

def users():
    var.USERS = []
    usr = con.FIRST_DEV + con.USER_HELP + con.CODERS + con.GAME_CONV + con.BETA_TESTERS + con.SPECIAL_THANKS + con.EXT_HELP + con.TRANSLATORS
    for user in usr:
        if user in var.USERS:
            continue
        var.USERS.append(user.lower())

def commands():
    var.COMMANDS = []
    cmd = con.COMMANDS + con.ERROR_COMMANDS + con.DEBUG_COMMANDS + con.HIDDEN_COMMANDS
    for comm in cmd:
        if comm in var.COMMANDS:
            continue
        var.COMMANDS.append(comm)

def preset(): # makes a preset file with current settings
    userset = []
    _usrset = []
    bootset = []
    for setting in var.USER_SETTINGS.keys():
        value = getattr(var, setting)
        for set, prefix in con.USER_SETTINGS.items():
            if set == setting:
                userset.append("{2}{0}{1}".format(prefix, value, con.USER_VAR))
                _usrset.append("{0}={1}".format(prefix, value))
                break
    for setting in var.PATH_SETTINGS.keys():
        value = getattr(var, setting)
        for set, prefix in con.PATH_SETTINGS.items():
            if set == setting:
                userset.append("{2}{0}{1}".format(prefix, value, con.PATH_VAR))
                _usrset.append("{0}={1}".format(prefix, value))
                break
    for setting in var.BOOT_PACK_SETTINGS.keys():
        value = getattr(var, setting)
        for set in con.BOOT_PACK_SETTINGS.keys():
            if set == setting:
                bootset.append(value)
                break
    log.logger("SETTINGS: {0}".format(" ".join(userset)))
    log.logger("", "{2} PACK: {0}{1}".format(con.BOOT_PACK_VAR, "".join(bootset), con.PROGRAM_NAME.upper()))
    log.logger("\n".join(_usrset), con.BOOT_PACK_VAR + "=" + "".join(bootset), type="settings", display=False, splitter="\n")