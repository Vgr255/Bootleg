from tools import constants as con
from tools import variables as var
from tools import filenames as fl
from tools import logger as log
from tools import get
from tools import reg

import subprocess
import datetime
import tempfile
import hashlib
import random
import locale
import shutil
import os

def initialize(): # initialize variables on startup and/or retry
    begin = "BEGIN_BOOT"
    if var.RETRY:
        begin = "RESTART_BOOT"
    log.multiple(begin, form=[con.PROGRAM_NAME], types=["all"], display=False)
    var.INITIALIZED = True
    log.logger("RUN_LANG", form=[var.LANGUAGE.upper(), con.PROGRAM_NAME], display=False)
    log.logger("RUN_OS", form=[var.ARCHITECTURE, con.PROGRAM_NAME, str(var.ON_WINDOWS).upper()], display=False)
    var.USED_HELP = False
    var.FATAL_ERROR = None
    var.EMPTY_SETTINGS = []
    var.NONEXISTANT_FILE = False
    var.PARSING = None
    var.ERROR = False
    var.RETRY = False
    begin_anew()

def do_init(): # initialize on startup only
    get.settings()
    format_variables()
    get.architecture()
    get.users()
    get.commands()
    reg.get()
    reg.git()
    initialize() # needs to be called after get.architecture()

class IsFile:
    def cur(inp):
        return os.path.isfile(os.getcwd() + "/" + inp)
    def sys(inp):
        return os.path.isfile(var.SYS_FOLDER + inp)
    def game(inp):
        return os.path.isfile(var.FFVII_PATH + inp)
    def pro(inp):
        return os.path.isfile(var.PROGRAM_FILES + inp)
    def tmp(inp):
        return os.path.isfile(var.BOOTLEG_TEMP + inp)
    def get(inp):
        return os.path.isfile(inp)

class ManipFile:
    def _7zip(file, dir=os.getcwd()):
        args = [var.SEVENZ_LOCATION, 'x', '-o"{0}"'.format(dir), '"{0}"'.format(file)]
        handler(args)

    def lgp_x(file, dir=os.getcwd()):
        args = [var.UGLP_LOCATION, "-x", '"{0}{1}{2}.lgp"'.format(dir, "\\" if dir[:-1] not in ("/", "\\") else "", file), "-C", '"{0}{1}"'.format(var.BOOTLEG_TEMP, file)]
        handler(args)

    def lgp_c(file, dir=os.getcwd()):
        args = [var.ULGP_LOCATION, "-c", '"{0}{1}{2}.lgp"'.format(dir, "\\" if dir[:-1] not in ("/", "\\") else "", file), "-C", '"{0}{1}"'.format(var.BOOTLEG_TEMP, file)]
        handler(args)

    def rar(file, dir=os.getcwd()):
        args = [var.RAR_LOCATION] # todo
        handler(args)

    def handler(args):
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

            log.logger("PROCESS_EXITED", form=[args, cause, abs(ret)])

def begin_anew():
    os.system("cls") # clear the screen off everything.
    log.help("\n".join(con.BOOT_ASCII1))
    log.help("BOOT_ARCH", form=[var.ARCHITECTURE])
    log.help(con.BOOT_ASCII2)
    log.help("BOOT_STARTUP", form=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
    log.help("\n".join(con.BOOT_ASCII3))

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
    if not var.SYS_FOLDER:
        var.SYS_FOLDER = os.getcwd() + "/utils"
    var.SYS_FOLDER = var.SYS_FOLDER.replace("/", "\\")
    if not var.SYS_FOLDER[-1:] == "\\":
        var.SYS_FOLDER += "\\"
    if not var.FFVII_PATH:
        var.FFVII_PATH = os.getcwd() + "/Final Fantasy VII"
    var.FFVII_PATH = var.FFVII_PATH.replace("/", "\\")
    if not var.FFVII_PATH[-1:] == "\\":
        var.FFVII_PATH = var.FFVII_PATH + "\\"
    if not var.BOOTLEG_TEMP:
        var.BOOTLEG_TEMP = tempfile.gettempdir() + "\\"
    if not var.BOOTLEG_TEMP[-1:] == "\\":
        var.BOOTLEG_TEMP += "\\"
    _mkdir(var.BOOTLEG_TEMP)
    var.BOOTLEG_TEMP += make_random_() + "\\"
    log.logger(var.BOOTLEG_TEMP, display=False, type="temp")
    os.mkdir(var.BOOTLEG_TEMP) # no integrity check, there's too small a chance that the folder already exists. and if it does, I want an error to occur
    if var.FFVII_IMAGE:
        if not var.FFVII_IMAGE[-4:].lower() == ".zip":
            var.FFVII_IMAGE = None
    if IsFile.sys("7za.exe"):
        var.SEVENZ_LOCATION = var.SYS_FOLDER + "7za.exe"
    if IsFile.sys("UnRAR.exe"):
        var.RAR_LOCATION = var.SYS_FOLDER + "UnRAR.exe"
    if IsFile.sys("ulgp.exe"):
        var.ULGP_LOCATION = var.SYS_FOLDER + "ulgp.exe"
    if var.LANGUAGE is not None:
        var.LANGUAGE = var.LANGUAGE.capitalize()
        if var.LANGUAGE in ("Default", "Current", "System"):
            syslng = locale.getdefaultlocale()[0]
            if locale.getlocale()[0]:
                syslng = locale.getlocale()[0]
            var.LANGUAGE = syslng[:2]
        for lang, lng in con.LANGUAGES.items():
            if var.LANGUAGE.lower() == lng[0]:
                var.LANGUAGE = lang
                break
        if var.LANGUAGE == "None":
            var.LANGUAGE = None
        if var.LANGUAGE not in con.LANGUAGES.keys():
            var.LANGUAGE = None
    if var.LANGUAGE is None:
        var.LANGUAGE = "English"
    for lang in con.LANGUAGES.keys():
        if hasattr(con, lang.upper() + "_TRANSLATORS"):
            lng = getattr(con, lang.upper() + "_TRANSLATORS")
            for trnl in lng:
                if trnl not in con.TRANSLATORS:
                    con.TRANSLATORS.append(trnl)
    for coder in con.GUI_CODERS + con.PROCESS_CODERS:
        if coder not in con.CODERS:
            con.CODERS.append(coder)

def make_random_(): # generates a random string of numbers for temporary folders
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

def make_new_bootleg(): # to call after every setting is set, before starting to install
    usr_set = ["BootOptions:"]
    for setting, prefix in con.USER_SETTINGS.items():
        usr_set.append(con.USER_VAR + prefix + getattr(var, setting))
    log.logger(usr_set, display=False, splitter=" ")
    bootset = "BootPack: {0}".format(con.BOOT_PACK_VAR)
    for value in var.BOOT_PACK_SETTINGS.values():
        bootset += str(value)
    log.logger(bootset, display=False)
    log.logger("SYST_PATHS", display=False)
    log.logger("DEST_LOCT", form=[var.FFVII_PATH], display=False)
    if var.FFVII_IMAGE:
        log.logger("INST_IMG", form=[var.FFVII_IMAGE], display=False)
    log.logger("MOD_LOCT", form=[var.MOD_LOCATION])
    log.logger("TMP_FILES", form=[var.BOOTLEG_TEMP])
    log.logger("", "BOOT_INIT", form=[con.PROGRAM_NAME])
    for p in con.ADD_PROG_NAME:
        if hasattr(fl, p):
            setattr(fl, p, getattr(fl, p).format(con.PROGRAM_NAME))
    for v in con.FFVII_PATH:
        if hasattr(fl, v):
            setattr(fl, v, var.FFVII_PATH + getattr(fl, v))
            _mkdir(getattr(fl, v))
    for l in con.LGP_TEMP:
        if hasattr(fl, l + "_PATCH"):
            setattr(fl, l + "_PATCH", var.BOOTLEG_TEMP + getattr(fl, l + "_PATCH"))
            _mkdir(getattr(fl, l + "_PATCH"))
    for t in con.TEMP_FOLDERS:
        _mkdir(var.BOOTLEG_TEMP + t.lower().replace("_", "\\"))
    for f in con.FINAL_PATCH:
        _mkdir(fl.FINAL_PATCH + "\\data\\" + f.lower())
    for m in con.MODS_FINAL:
        _mkdir(fl.MODS_FINAL + "\\" + m.lower())
    for a in con.MODS_AVALANCHE:
        _mkdir(fl.MODS_AVALANCHE + "\\" + a.lower())
    _mkdir(var.BOOTLEG_TEMP + "Data_Working\\")
    for d in con.DATA_WORKING:
        _mkdir(var.BOOTLEG_TEMP + "Data_Working\\" + d.lower())
    for u in con.FILES_UNDO:
        _mkdir(var.BOOTLEG_TEMP + u.lower() + "_undo")
    log.logger("INIT_CMPLT", "", "EXTR_SPRKL")
    _mkdir(var.BOOTLEG_TEMP + "Sprinkles")
    ManipFile._7zip(fl.SPRINKLES, var.BOOTLEG_TEMP + "Sprinkles")
    log.logger("SPRINKLES_READY")

def chk_game_language(inp=None):
    if var.LANGUAGE and not inp:
        log.help("INST_LANG", form=[getattr(tr, var.LANGUAGE.upper())])
        var.PARSING = "Language"
    elif inp:
        if var.LANGUAGE:
            if get._bool(inp) == 1:
                var.GAME_LANGUAGE = con.LANGUAGES[var.LANGUAGE][1]
                var.PARSING = None
                return
            elif get._bool(inp) == 0:
                log.help("TYPE_LANG")
                return
            else:
                log.logger("ERR_INVALID_BOOL", form=["YES", "NO"])
                return
        for lang, short in con.LANGUAGES.items():
            if lang.lower() == inp.lower():
                var.GAME_LANGUAGE = con.LANGUAGES[lang][1]
                var.PARSING = None
            elif inp.lower() == short[0]:
                var.GAME_LANGUAGE = con.LANGUAGES[lang][1]
                var.PARSING = None
            elif inp.isdigit() and int(inp) == con.LANGUAGES[lang][1]:
                var.GAME_LANGUAGE = int(inp)
    elif inp is None: # first check
        var.PARSING = "Language"
        log.help("TYPE_LANG")
    else: # empty input
        pass # for now, maybe we'll add another check sometime

def convert_se_release(): # conversion of the Square Enix Store Re-Release (Game version=2012, Install code in (1, 4, 7))
    log.logger("FND_2012_CONVERTING")
    data = var.FFVII_PATH + "data\\"
    attr = "-R -S -H -I" # not sure we need all those switches

    # Remove some attributes from the files to manipulate them
    attrib(data + "cd\\cr_us.lgp", attr)
    attrib(data + "cd\\disc_us.lgp", attr)
    attrib(data + "menu\\menu_us.lgp", attr)
    attrib(data + "wm\\world_us.lgp", attr)
    attrib(data + "field\\flevel.lgp", attr)
    attrib(data + "minigame\\chocobo.lgp", attr)
    attrib(data + "minigame\\condor.lgp", attr)
    attrib(data + "minigame\\sub.lgp", attr)
    attrib(data + "minigame\\high-us.lgp", attr)
    attrib(data + "minigame\\snowboard-us.lgp", attr)

    shutil.copy(data + "movies\\moviecam.lgp", data + "cd")

    get.language_files_2012()

    if var.KRANMER_MASTER == 0:
        var.ANY_CD = 1 # make sure to always have AnyCD enabled with the 2012 version

    log.logger("COMPL_2012_CONVERT", "")

def set_language_files():
    log.logger("VALIDATING_LANGUAGES")
    for lang in con.GAME_LANGUAGES.keys():
        if var.GAME_LANGUAGE == con.GAME_LANGUAGES[lang][4]:
            log.logger("IDENT_LANG_VERS_" + con.GAME_LANGUAGES[lang][0].upper())
            data = var.FFVII_PATH + "data\\"
            attr = "-R -S -H -I"
            attrib(data + "cd\\cr_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), attr)
            attrib(data + "cd\\disc_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), attr)
            attrib(data + "menu\\menu_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), attr)
            attrib(data + "wm\\world_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), attr)
            attrib(data + "field\\{0}flevel.lgp".format(con.GAME_LANGUAGES[lang][3]), attr)
            attrib(data + "minigame\\{0}chocobo.lgp".format(con.GAME_LANGUAGES[lang][3]), attr)
            attrib(data + "minigame\\{0}condor.lgp".format(con.GAME_LANGUAGES[lang][3]), attr)
            attrib(data + "minigame\\{0}sub.lgp".format(con.GAME_LANGUAGES[lang][3]), attr)
            attrib(data + "minigame\\high-{0}.lgp".format(con.GAME_LANGUAGES[lang][2]), attr)
            attrib(data + "minigame\\snowboard-{0}.lgp".format(con.GAME_LANGUAGES[lang][2]), attr)

            if var.GAME_LANGUAGE == 0:
                break

            os.rename(data + "cd\\cr_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), data + "cd\\cr_{0}.lgp".format(con.GAME_LANGUAGES["English"][1]))
            os.rename(data + "cd\\disc_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), data + "cd\\disc_{0}.lgp".format(con.GAME_LANGUAGES["English"][1]))
            os.rename(data + "menu\\menu_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), data + "menu\\menu_{0}.lgp".format(con.GAME_LANGUAGES["English"][1]))
            os.rename(data + "wm\\world_{0}.lgp".format(con.GAME_LANGUAGES[lang][1]), data + "wm\\world_{0}.lgp".format(con.GAME_LANGUAGES["English"][1]))
            os.rename(data + "field\\{0}flevel.lgp".format(con.GAME_LANGUAGES[lang][3]), data + "field\\{0}flevel.lgp".format(con.GAME_LANGUAGES["English"][3]))
            os.rename(data + "minigame\\{0}chocobo.lgp".format(con.GAME_LANGUAGES[lang][3]), data + "minigame\\{0}chocobo.lgp".format(con.GAME_LANGUAGES["English"][3]))
            os.rename(data + "minigame\\{0}condor.lgp".format(con.GAME_LANGUAGES[lang][3]), data + "minigame\\{0}condor.lgp".format(con.GAME_LANGUAGES["English"][3]))
            os.rename(data + "minigame\\{0}sub.lgp".format(con.GAME_LANGUAGES[lang][3]), data + "minigame\\{0}sub.lgp".format(con.GAME_LANGUAGES["English"][3]))
            os.rename(data + "minigame\\high-{0}.lgp".format(con.GAME_LANGUAGES[lang][2]), data + "minigame\\high-{0}.lgp".format(con.GAME_LANGUAGES["English"][2]))
            os.rename(data + "minigame\\snowboard-{0}.lgp".format(con.GAME_LANGUAGES[lang][2]), data + "minigame\\snowboard-{0}.lgp".format(con.GAME_LANGUAGES["English"][2]))

            ManipFile.lgp_x("condor", data + "minigame")

            tempc = var.BOOTLEG_TEMP + "condor\\"

            for file in os.listdir(tempc):
                if file == "mes02.tex":
                    continue
                for prefix in ("mes", "unit", "help"):
                    if prefix in file:
                        os.rename(tempc + file, tempc + "e" + file[1:])

            for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Condor_Tran"):
                shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Condor_Tran\\" + file, var.BOOTLEG_TEMP + "condor\\" + file)

            ManipFile.lgp_c("condor", var.BOOTLEG_TEMP)
            os.remove(data + "minigame\\condor.lgp")
            shutil.copy(var.BOOTLEG_TEMP + "condor.lgp", data + "minigame\\condor.lgp")

def _mkdir(inp):
    if not os.path.isdir(inp):
        os.mkdir(inp)

def attrib(file, attr, params=""): # sets Windows file and folders attributes
    os.system("C:\\Windows\\System32\\attrib.exe " + attr + ' "' + file + '" ' + params)

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
                            setattr(y, s, use_index(param[2:], x))
                for parsable in z.keys():
                    if param[1] == y[parsable]:
                        setattr(var, parsable, param[2:])

def parse_settings_from_file(inp):
    x = len(var.PRESET_EXT) + 1
    if not inp[-x:] == "." + var.PRESET_EXT:
        inp = inp + "." + var.PRESET_EXT
    if not IsFile.cur("presets/" + inp):
        return 1
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
                return 0
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
                    log.logger("INV_PAR_FILE", form=[inp, f], type="error")

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
                        parsed = use_index(parsed, x)
                    setattr(var, parsable, parsed)

def use_index(inp, setting): # still not sure if that'll work. mainly a placeholder
    colon = inp.index(":")
    begin = int(inp[:colon])
    end = int(inp[colon+1:])
    return setting[begin:end]

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
        log.logger("FND_EXIST_INST")
        if os.path.isdir(var.FFVII_PATH + "save"):
            shutil.move(var.FFVII_PATH + "save", var.BOOTLEG_TEMP + "IMAGE\save")
            log.logger("COPY_SAVE_FILES")
        else:
            log.logger("NO_SAVE_FND")
        if IsFile.game("ff7input.cfg"):
            shutil.copy(var.FFVII_PATH + "ff7input.cfg", var.BOOTLEG_TEMP + "IMAGE\ff7input.cfg")
            log.logger("COPY_INP_SET")
        else:
            log.logger("NO_INP_SET_FND")
    if os.path.isdir(var.FFVII_PATH):
        shutil.rmtree(var.FFVII_PATH)
        log.logger("REM_CUR_INST")
    else:
        log.logger("NO_INST_FND")

    log.logger("EXTR_IMG")
    ManipFile.Z7.extract(dir=var.FFVII_PATH, file=var.FFVII_IMAGE)
    if os.path.isdir(var.BOOTLEG_TEMP + "IMAGE"):
        shutil.copy(var.BOOTLEG_TEMP + "IMAGE", var.FFVII_PATH)
        shutil.rmtree(var.BOOTLEG_TEMP + "IMAGE")
    log.logger("IMG_REST_CMPL")
    return 0

def chk_existing_install():
    # return codes:
    # 0 = 1998 original port found by path
    # 1 = no installation found, failure
    # 2 = found 1998 installation in default 32-bit program files
    # 3 = found 1998 installation in default 64-bit program files
    # 4 = 2012 re-release found by path
    # 5 = 2013 steam release found by path
    # 6 = found 1998 by registry
    # 7 = found 2012 by registry
    # 8 = found 2013 by registry
    # might add more if the need arises
    # even if some go away, keep the current ones the same
    # so it doesn't mess up other stuff
    if IsFile.game("ff7.exe"): # 1998
        log.logger("INST_FND_1998", var.FFVII_PATH)
        retcode = 0
    elif IsFile.game("FF7_Launcher.exe"): # 2012/2013
        if "\\SteamApps\\common\\FINAL FANTASY VII\\" in var.FFVII_PATH:
            log.logger("INST_FND_2013", var.FFVII_PATH)
            retcode = 5
        else:
            log.logger("INST_FND_2012", var.FFVII_PATH)
            retcode = 4
    elif IsFile.pro("ff7.exe"): # default install
        log.logger("INST_FND_DEF", var.FFVII_PATH)
        retcode = 3 if var.ARCHITECTURE == "64bit" else 2
    # rest to check for Steam when I know how it is
    elif var.GAME_VERSION == 1998:
        game = reg.get_key("AppPath")
        if IsFile.get(game + "ff7.exe"):
            retcode = 6
    elif var.GAME_VERSION in (2012, 2013):
        game = reg.get_key("InstallLocation")
        if IsFile.get(game + "FF7_Launcher.exe"):
            retcode = 8 if var.GAME_VERSION == 2013 else 7
    else: # nothing found
        log.logger("COULD_NOT_FINST", "ABORT_BOOT", form=con.PROGRAM_NAME)
        retcode = 1
    return retcode

def end_bootleg_early():
    log.logger("\n")
    if var.FATAL_ERROR:
        log.multiple("FATAL_ERROR", "ERR_TO_REPORT", types=["error", "normal"])
        var.ERROR = True
        for reason in var.FATAL_ERROR:
            if hasattr(get.Error.Fatal, reason):
                why = getattr(get.Error.Fatal, reason)
            else:
                why = get.Error.unhandled
            log.multiple("ERR_FOUND", types=["error", "normal"], form=reason, display=False)
            log.multiple(why()[0], types=["error", "normal"], form=list(why()[1:]))
    if var.SYS_ERROR:
        log.multiple("ERR_ENC","MAY_STILL_RUN", form=con.PROGRAM_NAME, types=["error", "normal"])
        var.ERROR = True
        for reason in var.SYS_ERROR:
            if hasattr(get.Error.System, reason):
                why = getattr(get.Error.System, reason)
            else:
                why = get.Error.unhandled
            log.multiple("ERR_FOUND", types=["error", "normal"], form=reason, display=False)
            log.multiple(why()[0], types=["error", "normal"], form=list(why()[1:]))
    log.logger("\n")

def find_setting(setting): # gets parsable setting
    if not hasattr(var, setting):
        return
    parse = get._parser("find_" + setting.lower())
    if not parse:
        return
    msg = parse()
    var.FINDING = setting
    if con.RANGE[setting] < 0:
        log.help("ENT_EXACT_DIG", form=len(str(con.RANGE[setting])[1:]))
    else:
        log.help("ENT_VALUE_BETWEEN", form=con.RANGE[setting])
    log.help("\n")
    if con.RANGE[setting] > 1:
        log.help(msg[0])
        log.help("NO_CHG")
        log.help("\n".join(msg[1:]))
    if con.RANGE[setting] == 1:
        log.help(msg[0])
        log.help("CHC_NO")
        log.help("CHC_YES")
    if con.RANGE[setting] < 0:
        for line in msg:
            if line[0] == "1":
                log.help("NO_CHG")
            log.help(line)
    log.help("\n")
    tosay = "DEF_TO_USE"
    if con.RANGE[setting] < 0:
        tosay += "TOO_FEW_DIG"
    log.help(tosay + ".", form=getattr(var, setting))

def no_such_command(command):
    log.logger("ERR_INVALID_COMMAND", form=command, write=False)