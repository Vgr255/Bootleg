from tools import constants as con
from tools import variables as var
from datetime import datetime
from tools import parser
import config
import os
import platform

try:
    import winreg
except ImportError:
    logger("Bootleg will not work properly on a different operating system than Windows.", type="error")
    var.ON_WINDOWS = False

def initialize(): # initialize variables on startup and/or retry
    log_multiple("{0} Bootleg operation.".format("Beginning" if not var.INITIALIZED else "Restarting"), types=["all"], display=False)
    var.USED_HELP = False
    var.FATAL_ERROR = False
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.ERROR = False
    var.INITIALIZED = True
    var.RETRY = False

def do_init(): # initialize on startup only
    get_settings()
    get_architecture()
    get_registry()

def begin_anew():
    os.system("cls") # clear the screen off everything.
    show_help("\n".join(con.BOOT_ASCII))
    show_help("       Running Bootleg on {0}                      |___/".format(var.ARCHITECTURE))
    show_help("")
    show_help("Welcome to the Bootleg configurator {0}".format(con.CURRENT_RELEASE))
    commands = con.COMMANDS
    if var.SHOW_HIDDEN_COMMANDS:
        commands.extend(con.HIDDEN_COMMANDS)
        commands.extend(con.ERROR_COMMANDS)
    if var.DEBUG_MODE:
        commands.extend(con.DEBUG_COMMANDS)
    show_help("Available commands: {0}.".format(", ".join(commands)))

def parse_settings_from_params(input):
    for param in input:
        if param[0] == con.USER_VAR: # setting is an actual user setting
            for parsable in var.USER_SETTINGS.keys():
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
        file = open(os.getcwd() + "/presets/" + input)
        file.seek(0) # make sure we're at the beginning of the file
        for parsable in var.USER_SETTINGS.keys():
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
    for parsable in var.USER_SETTINGS.keys():
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
    for parsable in var.USER_SETTINGS.keys():
        if not getattr(var, parsable):
            var.EMPTY_SETTINGS.append(parsable)

def use_defaults(empty):
    for parsable in var.USER_SETTINGS.keys():
        if parsable not in empty:
            continue
        parsarg = getattr(var, parsable)
        if parsable in var.USER_SETTINGS.keys():
            setattr(var, parsable, 0) # Use 0 as default for every setting
        if parsable in var.SYSTEM_SETTINGS.keys():
            setattr(var, parsable, "")
        if parsarg:
            setattr(var, parsable, parsarg)

def settings_to_int():
    for parsable in var.USER_SETTINGS.keys():
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
    if var.LOG_EVERYTHING or var.DEV_LOG:
        type = "all"
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
            logger(output, logtype=logtype, display=False, write=write) # display false because it already displayed anyway

def log_multiple(output, types=[], display=True, write=True):
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

def show_help(output, type="help", write=False, display=True):
    logger(output, type=type, write=write, display=display)

def get_settings():
    for s, x in var.USER_SETTINGS.items():
        setattr(var, s, x)
    for t, y in var.SYS_VARIABLES.items():
        setattr(var, t, y)

def get_config():
    for s, x in config.USER_SETTINGS.items():
        setattr(var, s, x)
    for t, y in config.SYS_VARIABLES.items():
        setattr(var, t, y)

def get_parser(setting): # get function xyz() in parser.py for variable XYZ
    parse = None
    for x in parser.__dict__.keys():
        if not x == setting.lower():
            continue
        parse = getattr(parser, x)
        break # we got what we wanted
    return parse

def get_architecture(): # find processor architecture
    var.ARCHITECTURE = platform.architecture()[0]
    logger("Operating System: {0} on {1}.".format(str(platform.architecture()[1]), var.ARCHITECTURE), display=False, type="debug")
    logger("Running Bootleg on {0}.".format(var.ARCHITECTURE), display=False)

def get_registry():
    if not var.ON_WINDOWS:
        return # not on Windows
    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
        if var.ARCHITECTURE == "64bit":
            reg = winreg.OpenKey(reg, "Wow6432Node")
        reg = winreg.OpenKey(reg, "Square Soft, Inc.")
        var.REGISTRY = winreg.OpenKey(reg, "Final Fantasy VII")
    except WindowsError: # it failed
        set_new_reg()

def get_reg_key(value):
    reg = None
    try:
        reg = winreg.QueryValueEx(var.REGISTRY, value)
    except WindowsError:
        make_reg_key(value) # totally not a safe thing to do
    return reg

def add_to_reg(drive, app):
    write_reg("Windows Registry Editor Version 5.00")
    write_reg("")
    if var.ARCHITECTURE == "64bit":
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII]")
    else:
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII]")
    if not app[-1:] == "\\":
        app = app + "\\"
    if not drive[-1:] == "\\":
        drive = drive + "\\"
    drive = drive.replace("\\", "\\\\") # need to print two backslahses
    app = app.replace("\\", "\\\\")
    write_reg('"DataDrive"="{0}"'.format(drive))
    write_reg('"AppPath"="{0}"'.format(app))
    write_reg('"DataPath"="{0}Data\\\\"'.format(app))
    write_reg('"MoviePath"="{0}movies\\\\"'.format(app))
    write_reg('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))
    write_reg('')
    if var.ARCHITECTURE == "64bit":
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Graphics]')
    else:
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Graphics]')
    write_reg('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))

def set_new_reg(): # make a new registry entry if it doesn't exist. need to call append_to_reg() after
    write_reg("Windows Registry Editor Version 5.00")
    write_reg("")
    if var.ARCHITECTURE == "64bit":
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII]")
        write_reg("")
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.]")
    else:
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII]")
        write_reg("")
        write_reg("[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.]")
    write_reg('"DataDrive"=""')
    write_reg('"AppPath"=""')
    write_reg('"DataPath"=""')
    write_reg('"MoviePath"=""')
    write_reg('"DiskNo"=dword:00000000')
    write_reg('"FullInstall"=dword:00000001')
    write_reg('"SSI_DEBUG"=hex:53,48,4f,57,4d,45,54,48,45,41,50,50,4c,4f,47,00')
    write_reg('"DriverPath"=""')
    write_reg('')
    if var.ARCHITECTURE == "64bit":
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII\\1.00]')
        write_reg('')
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Graphics]')
    else:
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII\\1.00]')
        write_reg('')
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Graphics]')
    write_reg('"DD_GUID"=hex:00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00')
    write_reg('"DriverPath"=""')
    write_reg('"Driver"=dword:00000003')
    write_reg('"Mode"=dword:00000002')
    write_reg('"Options"=dword:00000000')
    write_reg('')
    if var.ARCHITECTURE == "64bit":
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\MIDI]')
    else:
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\MIDI]')
    write_reg('"MIDI_DeviceID"=dword:00000000')
    write_reg('"MIDI_data"="GENERAL_MIDI"')
    write_reg('"MusicVolume"=dword:00000064')
    write_reg('"Options"=dword:00000001')
    write_reg('')
    if var.ARCHITECTURE == "64bit":
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Sound]')
    else:
        write_reg('[HKEY_LOCAL_MACHINE\\SOFTWARE\\Square Soft, Inc.\\Final Fantasy VII\\1.00\\Sound]')
    write_reg('"Sound_GUID"=hex:dd,39,42,c5,d1,6b,e0,4f,83,42,5f,7b,7d,11,a0,f5')
    write_reg('"Options"=dword:00000000')
    write_reg('"SFXVolume"=dword:00000064')

def write_reg(input, dir=os.getcwd(), file=var.TEMP_REG):
    exists = False
    if not dir[-1:] == "/":
        dir = dir + "/"
    dir = dir.replace("/", "\\")
    if not file[-4:] == ".reg":
        file = file + ".reg"
    if input == "Windows Registry Editor Version 5.00":
        try:
            os.remove(dir + file)
        except WindowsError:
            pass
    try:
        f = open("{1}{0}".format(file, dir), "r+")
        exists = True
    except IOError: # path or file is inexistant
        f = open(os.getcwd() + "\\{0}".format(file), "w") # let's use the current directory and/or create the file
    f.seek(0, 2)
    if exists:
        f.write("\n")
    f.write(input)

def no_such_command(command):
    logger("'{0}' is not a valid command.".format(command), write=False)
    logger("Available command{1}: {0}".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else ""), write=False)
    if var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS:
        hidc = con.HIDDEN_COMMANDS
        hidc.extend(con.ERROR_COMMANDS)
        logger("Hidden command{1}: {0}".format(", ".join(hidc), "s" if len(con.HIDDEN_COMMANDS) > 1 else ""), write=False)
        logger("Keep in mind that hidden commands will appear as non-existant if not used properly or if the proper conditions aren't met.", write=False)
    if var.DEBUG_MODE:
        logger("Debug command{1}: {0}".format(", ".join(con.DEBUG_COMMANDS), "s" if len(con.DEBUG_COMMANDS) > 1 else ""))