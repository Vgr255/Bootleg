from tools import constants as con
from tools import variables as var
from tools import filenames as fl
from tools import logger as log
from tools import get
from tools import reg
import config
import os

def initialize(): # initialize variables on startup and/or retry
    log.multiple("{0} Bootleg operation.".format("Beginning" if not var.INITIALIZED else "Restarting"), types=["all"], display=False)
    var.USED_HELP = False
    var.FATAL_ERROR = None
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.ERROR = False
    var.INITIALIZED = True
    var.RETRY = False
    begin_anew()

def do_init(): # initialize on startup only
    get.settings()
    get.architecture()
    reg.get()
    format_variables()
    initialize() # needs to be called after get.architecture()

def _isfile(inp):
    def cur(inp):
        return os.path.isfile(os.getcwd() + "/" + inp)
    def sys(inp):
        return os.path.isfile(var.SYS_FOLDER + "/" + inp)
    return os.path.isfile(inp)

def begin_anew():
    os.system("cls") # clear the screen off everything.
    log.help("\n".join(con.BOOT_ASCII))
    log.help("       Running Bootleg on {0}                      |___/".format(var.ARCHITECTURE))
    log.help("")
    log.help("Welcome to the Bootleg configurator {0}".format(con.CURRENT_RELEASE))
    commands = con.COMMANDS
    if var.SHOW_HIDDEN_COMMANDS:
        commands.extend(con.HIDDEN_COMMANDS)
        commands.extend(con.ERROR_COMMANDS)
    if var.DEBUG_MODE:
        commands.extend(con.DEBUG_COMMANDS)
    log.help("Available commands: {0}.".format(", ".join(commands)))

def format_variables(): # formats a few variables to make sure they're correct
    for x, y in var.PATH_SETTINGS.items(): # convert NoneType into strings
        z = getattr(var, x)
        setattr(var, x, str(y))
    if not var.FFVII_PATH[-1:] == "/":
        var.FFVII_PATH = var.FFVII_PATH + "/"
    var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
    if var.BOOTLEG_TEMP:
        boot_temp = var.BOOTLEG_TEMP.split(";")
        bttmp = []
        for semicolon in boot_temp:
            if semicolon == "":
                continue
            bttmp.append(semicolon)
        if bttmp:
            var.BOOTLEG_TEMP = bttmp
    if var.SYS_FOLDER is None:
        var.SYS_FOLDER = os.getcwd()

def parse_settings_from_params(inp): # parse settings from launch parameters
    for x, prefix in con.SETTINGS_PREFIXES.items():
        for param in inp:
            u = x.replace("_VAR", "")
            x = x.replace("VAR", "SETTINGS")
            if param[0] == prefix:
                y = getattr(con, x)
                z = getattr(var, x)
                for l in con.USE_INDEX:
                    for s in y.keys():
                        if s == l and param[1] == y[s]: # so many letters
                            use_index(param[2:])
                            return
                for parsable in z.keys():
                    if param[1] == y[parsable]:
                        setattr(var, parsable, param[2:])

def parse_settings_from_file(inp):
    x = len(config.PRESET_EXT) + 1
    if not inp[-x:] == "." + config.PRESET_EXT:
        inp = inp + "." + config.PRESET_EXT
    fexist = _isfile.cur("presets/" + inp)
    if not fexist:
        var.NONEXISTANT_FILE = True
        return
    else:
        file = open(os.getcwd() + "/presets/" + inp)
        file.seek(0) # make sure we're at the beginning of the file
        for y in con.SETTINGS_PREFIXES.keys():
            t = y.replace("_VAR", "")
            y = y.replace("VAR", "SETTINGS")
            u = getattr(con, y)
            if t in con.USE_INDEX:
                f = file.readlines()
                fp = []
                for p in f:
                    p = p.replace("\n", "")
                    fp.append(p)
                use_index(fp)
                return
            for e, i in u.items():
                f = file.readline()
                f.replace("\n", "")
                if f[0] == i and f[1] == "=":
                    setattr(var, e, f[2:])
                    if "#" in f:
                        hash = f.index("#")
                        setattr(var, e, f[2:hash])
                elif f[0] == i and f[1:4] == " = ": # this can work
                    setattr(var, e, f[5:])
                elif "#" in f or f == "":
                    continue # ignore this
                else:
                    log.logger("Invalid setting found in {0}: {1}".format(inp, f), type="error")

def parse_settings_from_input(inp):
    for x, y in con.SETTINGS_PREFIXES.items(): # proper parsing
        if inp[0] == y:
            inp = inp[1:] # remove the prefix
        p = x.replace("_VAR", "")
        x = x.replace("VAR", "SETTING")
        q = getattr(con, x)
        s = getattr(var, x)
        for parsable in s.keys():
            setting = getattr(con, parsable)
            for t, u in setting.items():
                if inp[0] == u:
                    var.PARSING = parsable
                    parsed = inp[1:]
                    if " " in parsed:
                        if inp[1] == " ":
                            parsed = inp[2:]
                            if " " in parsed:
                                space = parsed.index(" ")
                                parsed = inp[2:space]
                        else:
                            space = parsed.index(" ")
                            parsed = inp[1:space]
                    if "=" in parsed:
                        if inp[1] == "=":
                            parsed = inp[2:]
                            if "=" in parsed:
                                equal = parsed.index("=")
                                equal = equal - 1 # equal equal equal? now that is redundant
                                parsed = inp[2:equal]
                        else:
                            equal = parsed.index("=")
                            parsed = inp[1:equal]
                    if p in con.USE_INDEX and u == q[p]:
                        use_index(parsed)
                    setattr(var, parsable, parsed)

def use_index(inp):
    pass # still todo
    # need to convert to integers. index(":") and before and after or something

def chk_empty_settings():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        for parsable in y.keys():
            if not hasattr(var, parsable):
                var.EMPTY_SETTINGS.append(parsable)

def chk_missing_run_files():
    if not _isfile.sys(fl.SPRINKLES):
        var.FATAL_ERROR.append("sprinkles")
    if not _isfile.cur(fl.README):
        var.SYS_ERROR.append("readme")
    if not _isfile.cur(fl.DOCUMENTATION):
        var.SYS_ERROR.append("documentation")
    if not _isfile.sys("7za.exe")
        var.FATAL_ERROR.append("_7za")

def use_defaults(empty):
    for x in con.SETTINGS_PREFIXES.keys():
        u = x.replace("_VAR", "")
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        if u not in con.ALLOWED_DEFAULTS:
            continue
        for parsable in y.keys():
            if parsable not in empty:
                continue
            if parsable in y.keys():
                setattr(var, parsable, "0")

def settings_to_int():
    for x in con.SETTINGS_PREFIXES:
        u = x.replace("_VAR", "")
        if u in con.NON_INT_SETTINGS:
            continue
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
    for parsable in y.keys():
        parsarg = getattr(var, parsable)
        try:
            setattr(var, parsable, int(parsarg))
        except ValueError: # something went wrong and settings aren't integers
            if var.DEBUG_MODE:
                log.logger("{0} - {2} setting not integer ({1})".format(parsable, parsarg, u.lower()), type="debug")
                continue # debug mode, let's assume the person knows what's going on
            else:
                log.logger("{0} - {2} setting not integer ({1})".format(parsable, parsarg, u.lower()), type="error", display=False)
                var.SYS_ERROR.append("int")
                break

def end_bootleg_early():
    if var.FATAL_ERROR:
        log.logger(" - FATAL ERROR -", type="error")
        log.logger("An unhandled error occured. Please report this.", type="error")
        for reason in var.FATAL_ERROR:
            why = getattr(get.error.fatal, reason)
            log.logger(why(), type="error")
    if var.SYS_ERROR:
        log.logger("An error has been encountered.", type="error")
        log.logger("Bootleg may still run if you wish to.", type="error")
        var.ERROR = True
        for reason in var.SYS_ERROR:
            why = getattr(get.error.system, reason)
            log.logger(why(), type="error")

def find_setting(setting): # gets parsable setting
    if not hasattr(var, setting):
        return
    parse = get.parser("find_" + setting.lower())
    if not parse:
        return
    var.FINDING = setting
    if con.RANGE[setting] < 0:
        log.help("Please enter exactly {0} digits.".format(len(str(con.RANGE[setting])[1:])))
        log.help("Entering '0' as any digit will not install the specific option.")
    else:
        log.help("Please choose a value between 0 and {0}.".format(con.RANGE[setting]))
    log.help("\n")
    if con.RANGE[setting] > 1:
        log.help("Entering '0' will not install the selected option.")
        log.help("\n")
    parse()
    if con.RANGE[setting] == 1:
        log.help("0 = NO")
        log.help("1 = YES")
    log.help("\n")
    log.help("Default is '{0}'. It will be used if no value is given.".format(getattr(var, setting)))

def no_such_command(command):
    log.logger("'{0}' is not a valid command.".format(command), write=False)
    log.logger("Available command{1}: {0}".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else ""), write=False)
    if var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS:
        hidc = con.HIDDEN_COMMANDS
        hidc.extend(con.ERROR_COMMANDS)
        log.logger("Hidden command{1}: {0}".format(", ".join(hidc), "s" if len(con.HIDDEN_COMMANDS) > 1 else ""), write=False)
        log.logger("Keep in mind that hidden commands will appear as non-existant if not used properly or if the proper conditions aren't met.", write=False)
    if var.DEBUG_MODE:
        log.logger("Debug command{1}: {0}".format(", ".join(con.DEBUG_COMMANDS), "s" if len(con.DEBUG_COMMANDS) > 1 else ""))