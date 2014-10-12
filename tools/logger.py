from tools import variables as var
from tools import constants as con
from tools import xmlparser as xml
from datetime import datetime
import os

def logger(*output, logtype="", type="normal", display=True, write=True, splitter="\n"): # logs everything to file and/or screen. always use this
    output = get(output, splitter)
    timestamp = str(datetime.now())
    timestamp = "[{0}] ({1}) ".format(timestamp[:10], timestamp[11:19])
    toget = ""
    if "\n" in output:
        indx = output.index("\n")
        toget = output[indx+1:]
        output = output[:indx]
    if var.LOG_EVERYTHING or var.DEV_LOG:
        logtype = con.LOGGERS["all"]
    if not logtype:
        try:
            logtype = con.LOGGERS[type]
        except KeyError: # empty type
            logtype = "LOG" # use default instead
    if var.DEBUG_MODE or var.DEV_LOG: # if there's an error I'll want every possible information. that's the way to go
        write = True
    if var.DEBUG_MODE or var.DISPLAY_EVERYTHING:
        display = True
    if display:
        if var.LANGUAGE:
            print(xml.get_line(output))
        else:
            print(output)
    if write:
        newfile = False
        logfile = getattr(var, logtype + "_FILE")
        log_ext = getattr(var, logtype + "_EXT")
        file = logfile + "." + log_ext
        if var.LANGUAGE:
            newfilel = False
            filel = con.LANGUAGES[var.LANGUAGE] + "_" + logfile + "." + log_ext
            try:
                fl = open(os.getcwd() + "/" + filel, "r+")
            except IOError:
                fl = open(os.getcwd() + "/" + filel, "w")
                newfilel = True
            fl.seek(0, 2)
        try:
            f = open(os.getcwd() + "/" + file, "r+")
        except IOError:
            f = open(os.getcwd() + "/" + file, "w") # file doesn't exist, let's create it
            newfile = True
        if logtype == con.LOGGERS["all"]:
            output = "type.{0} - {1}".format(type, output)
        f.seek(0, 2)
        if (not var.INITIALIZED or var.RETRY) and not newfile:
            f.write("\n\n" + timestamp + output + "\n")
        else:
            f.write(timestamp + output + "\n")
        if var.LANGUAGE:
            if (not var.INITIALIZED or var.RETRY) and not newfilel:
                fl.write("\n\n" + timestamp + xml.get_line(output) + "\n")
            else:
                fl.write(timestamp + xml.get_line(output) + "\n")
    if toget:
        logger(toget, logtype=logtype, display=display, write=write)

def multiple(*output, types=[], display=True, write=True, splitter="\n"):
    output = get(output, splitter)
    if "all" in types:
        if var.LOG_EVERYTHING or var.DEV_LOG:
            logger(output, type="all", display=display, write=write, splitter=splitter)
            return
        log_it = []
        for logged in con.LOGGERS.keys():
            if logged in con.IGNORE_ALL:
                continue
            if con.LOGGERS[logged] not in log_it:
                log_it.append(con.LOGGERS[logged])
        for l in log_it:
            logger(output, logtype=l, display=display, write=write, splitter=splitter)
    elif types:
        for t in types:
            logger(output, type=t, display=display, write=write, splitter=splitter)
    else: # no type
        logger(output, display=display, write=write, splitter=splitter)

def help(*output, type="help", write=False, display=True, splitter="\n"):
    output = get(output, splitter)
    logger(output, type=type, write=write, display=display, splitter=splitter)

def get(output, splitter):
    output = list(output)
    msg = None
    for line in output:
        if msg is None:
            msg = line
        else:
            msg += splitter + line
    return msg

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
    for setting in var.BRAT_SETTINGS.keys():
        value = getattr(var, setting)
        for set in con.BOOT_PACK_SETTINGS.keys():
            if set == setting:
                bootset.append(value)
                break
    logger("SETTINGS: {0}".format(" ".join(userset)))
    logger("")
    logger("BOOTLEG PACK: {0}{1}".format(con.BOOT_PACK_VAR, "".join(bootset)))
    logger("\n".join(_usrset), con.BOOT_PACK_VAR + "=" + "".join(bootset), type="settings", display=False, splitter="\n")