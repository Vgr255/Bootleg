from tools import constants as con
from tools import variables as var
from tools import parsables as par
from tools import translate as tr
from tools import logger as log

import datetime
import hashlib
import msvcrt
import random
import os

def bool(inp):
    if tr.YES[var.LANGUAGE].lower() == inp.lower():
        return True
    if tr.YES[var.LANGUAGE].lower()[0] == inp.lower():
        return True
    if tr.TRUE[var.LANGUAGE].lower() == inp.lower():
        return True
    if tr.TRUE[var.LANGUAGE].lower()[0] == inp.lower():
        return True
    if inp.isdigit() and int(inp) == 1:
        return True
    if tr.NO[var.LANGUAGE].lower() == inp.lower():
        return False
    if tr.NO[var.LANGUAGE].lower()[0] == inp.lower():
        return False
    if tr.FALSE[var.LANGUAGE].lower() == inp.lower():
        return False
    if tr.FALSE[var.LANGUAGE].lower()[0] == inp.lower():
        return False
    if inp.isdigit() and int(inp) == 0:
        return False

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

def random_small(length, allow_upper=False): # similar as above, except for other stuff
    chars = list("abcdefghijklmnopqrstuvwxyz0123456789")
    if allow_upper:
        chars.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    msg = ""
    while True:
        msg += random.choice(chars)
        if len(msg) >= length:
            return msg

def setting(inp, finder): # sets variables
    if inp and not inp.isdigit():
        log.logger("ENTER_ONLY_NUMS")
        return 1
    if not inp:
        log.logger("NO_USR_INP", form=[getattr(var, finder), finder], display=False)
        return 1
    inp = int(inp)
    getter = 2
    if finder in con.RANGE.keys():
        getter = con.RANGE[finder] + 1
    if inp in range(0, getter):
        setattr(var, finder, inp)
        log.logger("SET_DEF_NO_INP_USED", form=[finder, inp], display=False)
        return 0
    log.logger("INT_OUTBOUNDS", "ENT_VALUE_BETWEEN", form=getter-1)
    return 1

def pause(): # Generates a pause until the user presses a key
    msvcrt.getwch()

def preset(): # makes a preset file with current settings
    lines = []
    for setting in par.__dict__.keys():
        if not setting.isupper():
            continue
        lines.append(setting + " = " + getattr(var, setting))
    log.logger(lines, display=False, type="preset")
    logfile = getattr(var, con.LOGGERS["preset"] + "_FILE")
    log_ext = getattr(var, con.LOGGERS["preset"] + "_EXT")
    name = random_small(12)
    os.rename("{0}/{1}.{2}".format(os.getcwd(), logfile, log_ext), "{0}/presets/{1}.{2}".format(os.getcwd(), name, log_ext))
    log.logger("PRESET_SAVED", form=[os.getcwd(), name, log_ext])
