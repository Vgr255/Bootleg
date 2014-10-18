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
    if logtype:
        for typed in con.LOGGERS.keys():
            if con.LOGGERS[typed] == logtype:
                type = typed
    if var.LOG_EVERYTHING or var.DEV_LOG:
        logtype = con.LOGGERS["all"]
    if not logtype:
        try:
            logtype = con.LOGGERS[type]
        except KeyError: # empty type
            logtype = con.LOGGERS["normal"] # use default instead
    if var.DEBUG_MODE or var.DEV_LOG: # if there's an error I'll want every possible information. that's the way to go
        write = True
    if var.DEBUG_MODE or var.DISPLAY_EVERYTHING:
        display = True
    trout = output # not a fish
    logfile = getattr(var, logtype + "_FILE")
    log_ext = getattr(var, logtype + "_EXT")
    file = logfile + "." + log_ext

    newfile = False
    if not os.path.isfile(os.getcwd() + "/" + file):
        newfile = True
    if var.LANGUAGE and type not in con.IGNORE_TRANSLATE:
        newfilel = False
        filel = con.LANGUAGES[var.LANGUAGE] + "_" + file
        if not os.path.isfile(os.getcwd() + "/" + filel):
            newfilel = True
        fl = open(os.getcwd() + "/" + filel, "w" if newfilel else "r+")
        fl.seek(0, 2)
        trout = xml.get_line(trout)
    if display:
        print(trout)
    if write:
        if logtype == con.LOGGERS["all"]:
            output = "type.{0} - {1}".format(type, output)
        f = open(os.getcwd() + "/" + file, "w" if newfile else "r+")
        f.seek(0, 2)
        if (not var.INITIALIZED or var.RETRY) and not newfile:
            f.write("\n\n" + timestamp + output + "\n")
        else:
            f.write(timestamp + output + "\n")
        if var.LANGUAGE and type not in con.IGNORE_TRANSLATE:
            if (not var.INITIALIZED or var.RETRY) and not newfilel:
                fl.write("\n\n" + timestamp + trout + "\n")
            else:
                fl.write(timestamp + trout + "\n")
            fl.close()
        f.close()
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
    for setting in var.BOOT_PACK_SETTINGS.keys():
        value = getattr(var, setting)
        for set in con.BOOT_PACK_SETTINGS.keys():
            if set == setting:
                bootset.append(value)
                break
    logger("SETTINGS: {0}".format(" ".join(userset)))
    logger("")
    logger("{2} PACK: {0}{1}".format(con.BOOT_PACK_VAR, "".join(bootset), con.PROGRAM_NAME.upper()))
    logger("\n".join(_usrset), con.BOOT_PACK_VAR + "=" + "".join(bootset), type="settings", display=False, splitter="\n")