from tools import constants as con
from tools import variables as var
from tools import parsables as par
from datetime import datetime
import config
import os

def initialize(): # initialize variables on startup and/or retry
    log_all("{0} Bootleg operation".format("Beginning" if not var.INITIALIZED else "Restarting"), display=False)
    var.USED_HELP = False
    var.FATAL_ERROR = False
    var.PARSABLE_SETTINGS = [name for name in par.__dict__ if name.isupper()]
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.INITIALIZED = True
    var.RETRY = False

def begin_anew():
    os.system("cls") # clear the screen off everything.
    show_help(" - Bootleg Final Fantasy VII -")
    show_help("")
    show_help("Welcome to the Bootleg configurator {0}".format(con.CURRENT_RELEASE))
    show_help("Available commands: {0}{1}{2}".format(", ".join(con.COMMANDS), " " if config.SHOW_HIDDEN_COMMANDS else "", ", ".join(con.HIDDEN_COMMANDS) if config.SHOW_HIDDEN_COMMANDS else ""))

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
                var.DEBUG_MODE = True
            elif param[1] == con.VERBOSE:
                var.VERBOSE = True

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
                    setattr(var, parsable, f[2:hash])
            elif f[0] == getattr(par, parsable) and f[1:4] == " = ": # this can work
                setattr(var, parsable, f[5:])
            elif "#" in f or f == "":
                continue # ignore this
            else:
                logger("Invalid setting found in {0}: {1}".format(input, f), type="error")

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
        try:
            setattr(var, parsable, int(parsarg))
        except ValueError: # something went wrong and settings aren't integers
            if var.DEBUG_MODE:
                logger("{0} - setting not integer ({1})".format(parsable, parsarg), type="debug")
                continue # debug mode, let's assume the person knows what's going on
            else:
                logger("{0} - setting not integer ({1})".format(parsable, parsarg), type="error", display=False)
            var.FATAL_ERROR = "int"
            break

def end_bootleg_early():
    if var.FATAL_ERROR:
        logger(" - FATAL ERROR -", type="error")
        if var.FATAL_ERROR == True:
            logger("An unhandled error occured. Please report this.", type="error")
        elif var.FATAL_ERROR == "int":
            logger("Make sure your settings are numbers only (No letters allowed).", type="error")

def logger(output, logtype="", type="normal", display=True, write=True): # logs everything to file and/or screen. always use this
    timestamp = str(datetime.now())
    timestamp = "[{0}] ({1}) ".format(timestamp[:10], timestamp[11:19])
    if not logtype:
        try:
            logtype = con.LOGGERS[type]
        except KeyError: # empty type
            logtype = "LOG" # use default instead
    if config.LOG_EVERYTHING or config.DEV_LOG:
        logtype = "MIXED"
    if var.DEBUG_MODE or config.DEV_LOG: # if there's an error I'll want every possible information. that's the way to go
        write = True
    if var.DEBUG_MODE or config.DISPLAY_EVERYTHING:
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
        if logtype == "MIXED":
            output = "{0} - {1}".format(type, output)
        f.seek(0, 2)
        if (not var.INITIALIZED or var.RETRY) and not var.NEWFILE:
            f.write("\n\n" + timestamp + output + "\n")
        else:
            f.write(timestamp + output + "\n")

def log_all(output, display=True, write=True):
    if config.LOG_EVERYTHING or config.DEV_LOG:
        logger(output, type="", display=display, write=write)
        return
    log_it = []
    for logged in con.LOGGERS.keys():
        if con.LOGGERS[logged] not in log_it:
            log_it.append(con.LOGGERS[logged])
    for l in log_it:
        logger(output, logtype=l, display=display, write=write)

def show_help(output, type="help", write=False):
    logger(output, type=type, write=write)

def get_traceback(traceback):
    logger("", type="traceback")
    logger(traceback, type="traceback")