from tools import constants as con
from tools import variables as var
from tools import xmlparser as xml
from tools import filenames as fl
from tools import logger as log
from tools import get
from tools import reg
import subprocess
import tempfile
import os

def initialize(): # initialize variables on startup and/or retry
    log.multiple("{0} {1} operation.".format("Beginning" if not var.INITIALIZED else "Restarting", con.PROGRAM_NAME), types=["all"], display=False)
    log.logger("Running {1} in {0}.".format("English" if var.LANGUAGE is None else var.LANGUAGE, con.PROGRAM_NAME), display=False)
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
    format_variables()
    get.architecture()
    get.users()
    get.commands()
    reg.get()
    initialize() # needs to be called after get.architecture()

class IsFile:
    def cur(inp):
        return os.path.isfile(os.getcwd() + "/" + inp)
    def sys(inp):
        return os.path.isfile(var.SYS_FOLDER + inp)
    def game(inp):
        return os.path.isfile(var.FFVII_PATH  + inp)
    def pro(inp):
        return os.path.isfile(var.PROGRAM_FILES + inp)
    def get(inp):
        return os.path.isfile(inp)

class ManipFile: # currently a placeholder, will change in the future
    class Z7:
        def extract(file, dir=""):
            if dir:
                args = ['7za.exe', 'x', '-o"{0}"'.format(dir), '"{0}"'.format(file)]
            else:
                args = ['7za.exe', 'x', '-o"{0}"'.format(os.getcwd()), '"{0}"'.format(file)]
            __handler__(args)

    class Lgp:
        pass

    class Rar:
        pass

    def __handler__(args):
        child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = child.communicate()
        ret = child.returncode
        for line in (out + err).splitlines():
            log.logger(line.decode('utf-8'), type="debug")

        if ret != 0:
            if ret < 0:
                cause = 'signal'
            else:
                cause = 'status'

            log.logger('Process {0} exited with {1} {2}'.format(args, cause, abs(ret)))

def begin_anew():
    os.system("cls") # clear the screen off everything.
    log.help("\n".join(con.BOOT_ASCII1))
    if var.ARCHITECTURE == "64bit":
        log.help(con.BOOT_ARCH64)
    else:
        log.help(con.BOOT_ARCH32)
    log.help("\n".join(con.BOOT_ASCII2))
    commands = []
    commands.extend(con.COMMANDS)
    if var.SHOW_HIDDEN_COMMANDS:
        commands.extend(con.HIDDEN_COMMANDS)
        commands.extend(con.ERROR_COMMANDS)
    if var.DEBUG_MODE:
        commands.extend(con.DEBUG_COMMANDS)
    if not var.RUNNING:
        log.help("", "Available command{1}: {0}.".format(", ".join(commands), "" if len(commands) == 1 else "s"))

def format_variables(): # formats a few variables to make sure they're correct
    if var.MOD_LOCATION:
        mod_loc = var.MOD_LOCATION.split(";")
        moloc = []
        for semicolon in mod_loc:
            if semicolon == "":
                continue
            semicolon = semicolon.replace("/", "\\")
            if not semicolon[-1:] == "\\":
                semicolon = semicolon + "\\"
            moloc.append(semicolon)
        if moloc:
            var.MOD_LOCATION = moloc
    else:
        var.MOD_LOCATION = [os.getcwd()]
    if var.SYS_FOLDER is None:
        var.SYS_FOLDER = os.getcwd()
    if var.FFVII_PATH is None:
        var.FFVII_PATH = os.getcwd() + "/Final Fantasy VII"
    var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
    if not var.FFVII_PATH[-1:] == "\\":
        var.FFVII_PATH = var.FFVII_PATH + "\\"
    if var.BOOTLEG_TEMP is None:
        var.BOOTLEG_TEMP = tempfile.gettempdir() + "\\"
    if var.FFVII_IMAGE is not None:
        if not var.FFVII_IMAGE[-4:].lower() == ".zip":
            var.FFVII_IMAGE = None
    if var.LANGUAGE is not None:
        var.LANGUAGE = var.LANGUAGE[0].upper() + var.LANGUAGE[1:].lower()
        for lang in con.LANGUAGES.keys():
            if con.LANGUAGES[lang] == var.LANGUAGE.lower():
                var.LANGUAGE = lang
                break
        if var.LANGUAGE in ["English", "None"]:
            var.LANGUAGE = None
        if var.LANGUAGE not in con.LANGUAGES.keys():
            var.LANGUAGE = None
        if var.TRANSLATIONS_FILE and var.LANGUAGE:
            if os.path.isfile(os.getcwd() + "/" + var.TRANSLATIONS_FILE):
                xml.init(os.getcwd() + "/" + var.TRANSLATIONS_FILE, var.LANGUAGE, "English")
            else:
                var.LANGUAGE = None
        if not var.TRANSLATIONS_FILE:
            var.LANGUAGE = None
    for lang in con.LANGUAGES.keys():
        if hasattr(con, lang.upper() + "_TRANSLATORS"):
            lng = getattr(con, lang.upper() + "_TRANSLATORS")
            for trnl in lng:
                if trnl not in con.TRANSLATORS:
                    con.TRANSLATORS.append(trnl)

def make_new_bootleg(): # to call after every setting is set
    usr_set = ["INFO: {0} options:".format(con.PROGRAM_NAME)]
    for setting, prefix in con.USER_SETTINGS.items():
        usr_set.append(con.USER_VAR + prefix + getattr(var, setting))
    log.logger(usr_set, display=False, splitter=" ")
    bootset = "INFO: {0} pack settings: {1}".format(con.PROGRAM_NAME, con.BOOT_PACK_VAR)
    for x, value in var.BOOT_PACK_SETTINGS.items():
        bootset += str(value)
    log.logger(bootset, display=False)

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
                            use_index(param[2:], x)
                            return
                for parsable in z.keys():
                    if param[1] == y[parsable]:
                        setattr(var, parsable, param[2:])

def parse_settings_from_file(inp):
    x = len(var.PRESET_EXT) + 1
    if not inp[-x:] == "." + var.PRESET_EXT:
        inp = inp + "." + var.PRESET_EXT
    if not IsFile.cur("presets/" + inp):
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
                use_index(fp, y)
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
        x = x.replace("VAR", "SETTINGS")
        q = getattr(con, x)
        s = getattr(var, x)
        for parsable in s.keys():
            setting = getattr(q, parsable)
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
                        use_index(parsed, x)
                    setattr(var, parsable, parsed)

def use_index(inp, setting):
    pass # todo. ugh o-o
    return # temporary
    colon = inp.index(":")
    begin = inp[:colon]
    end = inp[colon+1:]
    toget = getattr(con, setting)
    # need to convert to integers. index(":") and before and after or something

def chk_missing_run_files():
    if not IsFile.sys(fl.SPRINKLES):
        var.FATAL_ERROR.append("sprinkles")
    if not IsFile.cur(fl.README):
        var.SYS_ERROR.append("readme")
    if not IsFile.cur(fl.DOCUMENTATION):
        var.SYS_ERROR.append("documentation")

def extract_image():
    if var.FFVII_IMAGE is None:
        return 1
    if IsFile.game("ff7.exe"):
        log.logger("Found existing FF7 installation.")
        try:
            shutil.move(var.FFVII_PATH + "save", var.BOOTLEG_TEMP + "IMAGE\save")
            log.logger("Copying save files.")
        except OSError:
            log.logger("No save files found.")
        try:
            shutil.copy(var.FFVII_PATH + "ff7input.cfg", var.BOOTLEG_TEMP + "IMAGE\ff7input.cfg")
            log.logger("Copying Input settings.")
        except OSError:
            log.logger("No input settings found.")
    try:
        shutil.rmtree(var.FFVII_PATH)
        log.logger("Removing current installation.")
    except OSError:
        log.logger("No current installation found.")

    log.logger("Extracting Final Fantasy VII Image . . .")
    ManipFile.Z7.extract(dir=var.FFVII_PATH, file=var.FFVII_IMAGE)
    if os.path.isdir(var.BOOTLEG_TEMP + "IMAGE"):
        shutil.copy(var.BOOTLEG_TEMP + "IMAGE", var.FFVII_PATH)
        shutil.rmtree(var.BOOTLEG_TEMP + "IMAGE")
    log.logger("Final Fantasy VII Image Restoration Completed.")
    return 0

def chk_existing_install():
    # return codes:
    # 0  = 1998 original port found by path
    # 1  = no installation found, failure
    # 2  = found 1998 installation in default 32-bit program files
    # 3  = found 1998 installation in default 64-bit program files
    # 4  = 2012 re-release found by path
    # 5  = 2013 steam release found by path
    # 6  = found 2013 steam install in default 32-bit install
    # 7  = found 2013 steam install in default 64-bit install
    # 8  = found 1998 by registry
    # 9  = found 2012 by registry
    # 10 = found 2013 by registry
    # might add more if the need arises
    # even if some go away, keep the current ones the same
    # so it doesn't mess up other stuff
    if IsFile.game("ff7.exe"): # 1998
        log.logger("Final Fantasy VII Installation Found:", var.FFVII_PATH)
        retcode = 0
    elif IsFile.game("FF7_Launcher.exe"): # 2012
        log.logger("Final Fantasy VII 2012 Re-Release Installation Found:", var.FFVII_PATH)
        retcode = 4
    elif IsFile.pro("ff7.exe"): # default install
        log.logger("Final Fantasy VII Default Installation Found:", var.FFVII_PATH)
        retcode = 3 if var.ARCHITECTURE == "64bit" else 2
    # rest to check for Steam when I know how it is
    elif var.GAME_VERSION == 1998:
        game = reg.get_key("AppPath")
        if IsFile.get(game + "ff7.exe"):
            retcode = 8
    elif var.GAME_VERSION in (2012, 2013):
        game = reg.get_key("InstallLocation")
        if IsFile.get(game + "FF7_Launcher.exe"):
            retcode = 10 if var.GAME_VERSION == 2013 else 9
    else: # nothing found
        log.logger("Could not find a Final Fantasy VII Installation.", "Aborting {0}...".format(con.PROGRAM_NAME))
        retcode = 1
    return retcode

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
    log.logger("\n")
    if var.FATAL_ERROR:
        log.multiple(" - FATAL ERROR -", types=["error", "normal"])
        log.multiple("An error occured. Please report this.", types=["error", "normal"])
        var.ERROR = True
        for reason in var.FATAL_ERROR:
            try:
                why = getattr(get.Error.Fatal, reason)
            except AttributeError:
                why = get.Error.__unhandled__
            finally:
                log.multiple("Error found: {0}".format(reason), types=["error", "normal"], display=False)
                log.multiple(why(), types=["error", "normal"])
    if var.SYS_ERROR:
        log.multiple("An error has been encountered.", types=["error", "normal"])
        log.multiple("{0} may still run if you wish to.".format(con.PROGRAM_NAME), types=["error", "normal"])
        var.ERROR = True
        for reason in var.SYS_ERROR:
            try:
                why = getattr(get.Error.System, reason)
            except AttributeError:
                why = get.Error.__unhandled__
            finally:
                log.multiple("Error found: {0}".format(reason), types=["error", "normal"], display=False)
                log.multiple(why(), types=["error", "normal"])
    log.logger("\n")

def find_setting(setting): # gets parsable setting
    if not hasattr(var, setting):
        return
    parse = get.parser("find_" + setting.lower())
    if not parse:
        return
    msg = parse()
    var.FINDING = setting
    if con.RANGE[setting] < 0:
        log.help("Please enter exactly {0} digits.".format(len(str(con.RANGE[setting])[1:])))
        log.help("Entering '0' as any digit will not install the specific option.")
    else:
        log.help("Please choose a value between 0 and {0}.".format(con.RANGE[setting]))
    log.help("\n")
    if con.RANGE[setting] > 1:
        log.help(msg[0])
        log.help("0 = No Change")
        log.help("\n".join(msg[1:]))
    if con.RANGE[setting] == 1:
        log.help(msg[0])
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
        log.logger("Hidden command{1}: {0}".format(", ".join(hidc), "s" if len(hidc) > 1 else ""), write=False)
        log.logger("Keep in mind that hidden commands will appear as non-existant if not used properly or if the proper conditions aren't met.", write=False)
    if var.DEBUG_MODE:
        log.logger("Debug command{1}: {0}".format(", ".join(con.DEBUG_COMMANDS), "s" if len(con.DEBUG_COMMANDS) > 1 else ""), write=False)