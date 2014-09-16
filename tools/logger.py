from tools import variables as var
from tools import constants as con
from datetime import datetime
import config
import os

def logger(output, logtype="", type="normal", display=True, write=True): # logs everything to file and/or screen. always use this
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
        print(output)
    if write:
        logfile = getattr(config, logtype + "_FILE")
        log_ext = getattr(config, logtype + "_EXT")
        file = logfile + "." + log_ext
        try:
            f = open(os.getcwd() + "/" + file, "r+")
        except IOError:
            f = open(os.getcwd() + "/" + file, "w") # file doesn't exist, let's create it
            var.NEWFILE = True
        if logtype == con.LOGGERS["all"]:
            output = "type.{0} - {1}".format(type, output)
        f.seek(0, 2)
        try:
            if (not var.INITIALIZED or var.RETRY) and not var.NEWFILE:
                f.write("\n\n" + timestamp + output + "\n")
            else:
                f.write(timestamp + output + "\n")
        except TypeError:
            output = str(output)
            logger(output, logtype=logtype, type=type, display=False, write=write) # display is false because it already displayed anyway

def multiple(output, types=[], display=True, write=True):
    if "all" in types:
        if var.LOG_EVERYTHING or var.DEV_LOG:
            logger(output, type="all", display=display, write=write)
            return
        log_it = []
        for logged in con.LOGGERS.keys():
            if logged == "all":
                continue
            if con.LOGGERS[logged] not in log_it:
                log_it.append(con.LOGGERS[logged])
        for l in log_it:
            logger(output, logtype=l, display=display, write=write)
    elif types:
        for t in types:
            logger(output, type=t, display=display, write=write)
    else: # no type
        logger(output, display=display, write=write)

def help(output, type="help", write=False, display=True):
    logger(output, type=type, write=write, display=display)