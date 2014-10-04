from tools import variables as var
from tools import constants as con
from tools import xmlparser as xml
from datetime import datetime
import os

def logger(*output, logtype="", type="normal", display=True, write=True, splitter=" "): # logs everything to file and/or screen. always use this
    output = get(output, splitter)
    timestamp = str(datetime.now())
    timestamp = "[{0}] ({1}) ".format(timestamp[:10], timestamp[11:19])
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
        logfile = getattr(var, logtype + "_FILE")
        log_ext = getattr(var, logtype + "_EXT")
        file = logfile + "." + log_ext
        try:
            f = open(os.getcwd() + "/" + file, "r+")
        except IOError:
            f = open(os.getcwd() + "/" + file, "w") # file doesn't exist, let's create it
            var.NEWFILE = True
        if logtype == con.LOGGERS["all"]:
            output = "type.{0} - {1}".format(type, output)
        f.seek(0, 2)
        if (not var.INITIALIZED or var.RETRY) and not var.NEWFILE:
            f.write("\n\n" + timestamp + output + "\n")
        else:
            f.write(timestamp + output + "\n")

def multiple(*output, types=[], display=True, write=True, splitter=" "):
    output = get(output, splitter)
    if "all" in types:
        if var.LOG_EVERYTHING or var.DEV_LOG:
            logger(output, type="all", display=display, write=write, splitter=splitter)
            return
        log_it = []
        for logged in con.LOGGERS.keys():
            if logged == "all":
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

def help(*output, type="help", write=False, display=True, splitter=" "):
    output = get(output, splitter)
    logger(output, type=type, write=write, display=display, splitter=splitter)

def get(output, splitter):
    output = list(output)
    msg = ""
    for line in output:
        msg = "{0}{1}{2}".format(msg, splitter if msg else "", line)
    return msg