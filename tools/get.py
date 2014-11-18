from tools import constants as con
from tools import variables as var
from tools import translate as tr
from tools import parser as par
from tools import logger as log

import datetime
import hashlib
import random

def parser(setting): # get function xyz() in parser.py for variable XYZ
    if hasattr(par, setting):
        return getattr(par, setting)

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