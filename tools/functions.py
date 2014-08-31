from tools import constants as con
from tools import variables as var
from tools import parsables as par
from datetime import datetime
import config
import os

def initialize(): # initialize variables on startup and/or retry
    var.USED_HELP = False
    var.FATAL_ERROR = False
    var.PARSABLE_SETTINGS = [name for name in par.__dict__ if name.isupper()]
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.INITIALIZED = True
    var.RETRY = False
    log_all(display=False, "Beginning Bootleg operation")

def config_into_var():
    for parsable in var.PARSABLE_SETTINGS:
        parsarg = getattr(config, parsable)
        setattr(var, parsable, parsarg)

def parse_settings_from_params(input):
    for param in input:
        if param[0] == con.USER_VAR: # setting is an actual user setting
            for parsable in var.PARSABLE_SETTINGS:
                if param[1] == getattr(par, parsable):
                    setattr(var, parsable, param[2:])
        elif param[0] == con.SYS_VAR: # setting is a system/debug setting. always takes priority
            if param[1] == con.DEBUG_MODE:
                DEBUG_MODE = True
            elif param[1] == con.VERBOSE:
                VERBOSE = True

def parse_settings_from_file(input):
    fexist = os.path.isfile(os.getcwd() + "/presets/" + input)
    if not fexist:
        var.NONEXISTANT_FILE = True
        return
    else:
        file = open("/presets/" + input)
        file.seek(0) # make sure we're at the beginning of the file
        for parsable in var.PARSABLE_SETTINGS:
            f.replace("\n", "")
            f = file.readline()
            if f[0] == getattr(par, parsable) and f[1] == "=":
                setattr(var, parsable, f[2:])
                if "#" in f:
                    hash = f.index("#")
                    setattr(var, parsable, f[2:hash[)
            elif f[0] == getattr(par, parsable) and f[1:4] == " = ": # this can work
                setattr(var, parsable, f[5:])
            elif "#" in f or f == "":
                continue # ignore this
            else:
                logger(type="error", "Invalid setting found in {0}: {1}".format(input, f))

def parse_settings_from_input(input):
    if input[0] == con.USER_VAR or input[0] == con.SYS_VAR: # proper parsing
        input = input[1:] # remove the forward slash
    for parsable in var.PARSABLE_SETTINGS:
        setting = getattr(par, parsable)
        if input[0] == setting:
            var.PARSING = parsable
            parsed = input[1:]
            if " " in parsed:
                if input[1] == " ":
                    parsed = input[2:]
                    if " " in parsed:
                        space = parsed.index(" ")
                        parsed = input[2:space] # surprisingly enough, that actually works
                else:
                    space = parsed.index(" ")
                    parsed = input[1:space]
            if "=" in parsed:
                if input[1] == "=":
                    parsed = input[2:]
                    if "=" in parsed:
                        equal = parsed.index("=")
                        equal = equal - 1 # equal equal equal? now that is redundant
                        parsed = input[2:equal]
                else:
                    equal = parsed.index("=")
                    parsed = input[1:equal]

def chk_empty_settings():
    var.EMPTY_SETTINGS = []
    for parsable in var.PARSABLE_SETTINGS:
        if not getattr(var, parsable):
            var.EMPTY_SETTINGS.append(parsable)

def use_defaults(empty):
    for parsable in var.PARSABLE_SETTINGS:
        if parsable not in empty:
            continue
        parsarg = getattr(con, parsable)
        if parsarg:
            setattr(var, parsable, parsarg)
        else:
            setattr(var, parsable, 0) # Use 0 as default in case one is not specified for some reason

def settings_to_int():
    for parsable in var.PARSABLE_SETTINGS:
        parsarg = getattr(var, parsable)
        setattr(var, parsable, int(parsarg))
        except ValueError: # something went wrong and settings aren't integers
            if DEBUG_MODE:
                logger(type="debug", "{0} - setting not integer ({1})".format(parsable, parsarg))
                continue # debug mode, let's assume the person knows what's going on
            else:
                logger(type="error", display=False, "{0} - setting not integer ({1})".format(parsable, parsarg))
            var.FATAL_ERROR = "int"
            break

def end_bootleg_early():
    if var.FATAL_ERROR:
        logger(type="error", " - FATAL ERROR -")
        if var.FATAL_ERROR == True:
            logger(type="error", "An unhandled error occured. Please report this.")
        elif var.FATAL_ERROR == "int":
            logger(type="error", "Make sure your settings are numbers only (No letters allowed).")

def logger(type="normal", display=True, write=True, output): # log everything to file and/or screen. always use this
    timestamp = str(datetime.now())
    timestamp = "[{0}] ({1}) ".format(timestamp[:10], timestamp[11:19])
    if type == "normal": # regular logging
        logtype = "LOG"
    if type == "error": # all errors
        logtype = "ERROR"
    if type == "debug": # random debug stuff
        logtype = "DEBUG"
    if type == "traceback": # traceback for errors
        logtype = "TRACE"
    if type == "input": # all user input
        logtype = "INPUT"
    if config.LOG_EVERYTHING:
        logtype = "MIXED"
    logfile = getattr(config, logtype + "_FILE")
    log_ext = getattr(config, logtype + "_EXT")
    file = logfile + "." + log_ext
    f = open(os.getcwd() + "/" + file, "w")
    if DEBUG_MODE:
        display = True
        write = True
    if write:
        if logtype == "MIXED":
            output = "{0} - {1}".format(type, output)
        f.write(timestamp + output)
    if display:
        print(output)

def log_all(display=True, write=True, output):
    if config.LOG_EVERYTHING:
        logger(type="", display=display, write=write, output)
        return
    for logged in con.LOGGERS:
        logger(type=logged, display=display, write=write, output)