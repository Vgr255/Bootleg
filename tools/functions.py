from tools import constants as con
from tools import variables as var
from tools import filenames as fl
from tools import logger as log
from tools import errors
from tools import get
from tools import reg

import subprocess
import tempfile
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
    var.FATAL_ERROR = []
    var.SYS_ERROR = []
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

    def raw(*args): # Handler for any other process than above
        args = list(args)
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
    var.BOOTLEG_TEMP += get.random_string() + "\\"
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
            setattr(fl, v, var.FFVII_PATH + getattr(fl, v) + "\\")
            _mkdir(getattr(fl, v))
    for l in con.LGP_TEMP:
        if hasattr(fl, l + "_PATCH"):
            setattr(fl, l + "_PATCH", var.BOOTLEG_TEMP + getattr(fl, l + "_PATCH") + "\\")
            _mkdir(getattr(fl, l + "_PATCH"))
    for t in con.TEMP_FOLDERS:
        setattr(fl, t, var.BOOTLEG_TEMP + t.lower().replace("_", "\\") + "\\")
        _mkdir(getattr(fl, t))
    for f in con.FINAL_PATCH:
        setattr(fl, f + "_PATCH", fl.FINAL_PATCH + "\\data\\" + f.lower() + "\\")
        _mkdir(getattr(fl, f + "_PATCH"))
    for m in con.MODS_FINAL:
        setattr(fl, "FINAL_" + m, fl.MODS_FINAL + "\\" + m.lower() + "\\")
        _mkdir(getattr(fl, "FINAL_" + m))
    for a in con.MODS_AVALANCHE:
        setattr(fl, "AVALANCHE_" + a, fl.MODS_AVALANCE + "\\" + a.lower() + "\\")
        _mkdir(getattr(fl, "AVALANCHE_" + a))
    _mkdir(var.BOOTLEG_TEMP + "Data_Working\\")
    for d in con.DATA_WORKING:
        setattr(fl, "DATA_WORKING_" + d, var.BOOTLEG_TEMP + "Data_Working\\" + d.lower() + "\\")
        _mkdir(getattr(fl, "DATA_WORKING_" + d))
    for u in con.FILES_UNDO:
        setattr(fl, "FILES_UNDO_" + u, var.BOOTLEG_TEMP + u.lower() + "_undo\\")
        _mkdir(getattr(fl, "FILES_UNDO_" + u))
    log.logger("INIT_CMPLT", "", "EXTR_SPRKL")
    _mkdir(var.BOOTLEG_TEMP + "Sprinkles")
    ManipFile._7zip(fl.SPRINKLES, var.BOOTLEG_TEMP + "Sprinkles")
    log.logger("SPRINKLES_READY")

def chk_game_language(inp=None):
    if var.LANGUAGE and not inp:
        log.help("INST_LANG", form=[var.LANGUAGE.upper(), "YES", "NO"])
        var.PARSING = "Language"
    elif inp:
        if var.LANGUAGE:
            if get.bool(inp) == 1:
                var.GAME_LANGUAGE = con.GAME_LANGUAGES[var.LANGUAGE][4]
                var.PARSING = None
                return
            elif get.bool(inp) == 0:
                log.help("TYPE_LANG")
                return
            else:
                log.logger("ERR_INVALID_BOOL", form=["YES", "NO"])
                return
        for lang, short in con.GAME_LANGUAGES.items():
            if lang.lower() == inp.lower():
                var.GAME_LANGUAGE = con.GAME_LANGUAGES[lang][4]
                var.PARSING = None
            elif inp.lower() == short[0]:
                var.GAME_LANGUAGE = con.GAME_LANGUAGES[lang][4]
                var.PARSING = None
            elif inp.isdigit() and int(inp) == con.GAME_LANGUAGES[lang][4]:
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
    for file in con.TRANSLATE_CHANGER:
        attrib(data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp", attr)

    shutil.copy(data + "movies\\moviecam.lgp", data + "cd")

    for lang in con.GAME_LANGUAGES.keys():
        if var.GAME_LANGUAGE == con.GAME_LANGUAGES[lang][4]:
            if not os.path.isdir(var.FFVII_PATH + "data\\lang-" + con.GAME_LANGUAGES[lang][0]):
                lang = "English"
            for i in ("battle", "kernel", "movies"):
                for file in os.listdir(var.FFVII_PATH + "data\\lang-{0}\\{1}".format(con.GAME_LANGUAGES[lang][0], i)):
                    shutil.copy("{0}data\\lang-{1}\\{2}\\{3}".format(var.FFVII_PATH, con.GAME_LANGUAGES[lang][0], i, file), "{0}data\\{1}\\{2}".format(var.FFVII_PATH, i, file))
            shutil.move(data + "movies", var.FFVII_PATH + "movies")
            os.rename("FF7_{0}.exe".format(con.GAME_LANGUAGES[lang][0]), "FF7.exe")
            var.GAME_LANGUAGE = con.GAME_LANGUAGES[lang][4] # makes sure to set that back to 0 if it couldn't be found
            if var.GAME_LANGUAGE is not 0: # Backup English files
                for lgp in con.TRANSLATE_CHANGER:
                    lgp = lgp.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2])
                    if os.path.isfile(var.FFVII_PATH + "data\\" + lgp + ".lgp"):
                        os.rename(var.FFVII_PATH + "data\\" + lgp + ".lgp", var.FFVII_PATH + "data\\" + lgp + ".bak")

    if var.KRANMER_MASTER == 0:
        var.ANY_CD = 1 # make sure to always have AnyCD enabled with the 2012 version

    log.logger("COMPL_2012_CONVERT", "")

def set_language_files(): # Converts any language to a working English version
    log.logger("VALIDATING_LANGUAGES")
    data = var.FFVII_PATH + "data\\"
    for lang in con.GAME_LANGUAGES.keys():
        if var.GAME_LANGUAGE == con.GAME_LANGUAGES[lang][4]:
            log.logger("IDENT_LANG_VERS_" + con.GAME_LANGUAGES[lang][0].upper())
            attr = "-R -S -H -I"

            for file in con.TRANSLATE_CHANGER:
                attrib(data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp", attr)

            if var.GAME_LANGUAGE == 0:
                break

            for file in con.TRANSLATE_CHANGER:
                os.rename(data + file.format(con.GAME_LANGUAGES[lang][1], con.GAME_LANGUAGES[lang][3], con.GAME_LANGUAGES[lang][2]) + ".lgp",
                          data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp")

            # Condor minigame translation

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

            # Snowboard minigame translation

            ManipFile.lgp_x("snowboard-us", data + "minigame")

            tempc = var.BOOTLEG_TEMP + "snowboard-us\\"

            for file in os.listdir(tempc):
                for prefix in ("_k.tex", "stamp", "time"):
                    if prefix in file:
                        e = "e"
                        if prefix == "time":
                            e = ""
                        os.rename(tempc + file, tempc + e + file[1:])

            ManipFile.lgp_c("snowboard-us", var.BOOTLEG_TEMP)
            os.remove(data + "minigame\\snowboard-us.lgp")
            shutil.copy(var.BOOTLEG_TEMP + "snowboard-us.lgp", data + "minigame\\snowboard-us.lgp")

            # Submarine minigame translation

            ManipFile.lgp_x("sub", data + "minigame")

            tempc = var.BOOTLEG_TEMP + "sub\\"

            for file in os.listdir(tempc):
                os.rename(tempc + file, tempc + file[1:])

            ManipFile.lgp_c("sub", var.BOOTLEG_TEMP)
            os.remove(data + "minigame\\sub.lgp")
            shutil.copy(var.BOOTLEG_TEMP + "sub.lgp", data + "minigame\\sub.lgp")

            # Disc files translation

            ManipFile.lgp_x("disc-us", data + "cd")

            tempc = var.BOOTLEG_TEMP + "cd\\"

            for file in os.listdir(tempc):
                for prefix in ("disc", "over"):
                    if prefix in file:
                        e = "e"
                        if prefix == "disk":
                            e = ""
                        os.rename(tempc + file, tempc + e + file[1:])

            ManipFile.lgp_c("disc-us", var.BOOTLEG_TEMP)
            os.remove(data + "cd\\disc-us.lgp")
            shutil.copy(var.BOOTLEG_TEMP + "disc-us.lgp", data + "cd\\disc-us.lgp")

            # End of conversion, break out
            break

    log.logger("LANG_FILES_CONV_COMPL", "", "BACKUP_VANILLA")

    for file in ("kernel\\KERNEL.BIN", "kernel\\kernel2.bin", "kernel\\window.bin", "wm\\world_us.lgp", "battle\\scene.bin", "battle\\battle.lgp"):
        shutil.copy(data + file, var.BOOTLEG_TEMP + "vanilla_Backup\\" + file)

    log.logger("FILES_BACKUP_COMPL", "")

def convert_rerelease_flevel(): # Converts the Square Enix Store Flevel to a 1998-compatible version
    log.logger("CONV_2012_SES_FLEVEL")

    for flevel in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Tools\\NewToOld"):
        shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Tools\\NewToOld" + flevel, var.FFVII_PATH + flevel)

    ManipFile.raw(var.FFVII_PATH + "patch.exe", "flevel.pat", "data\\field\\flevel.lgp", "data\\field\\conv_flevel.lgp")

    os.rename(var.FFVII_PATH + "data\\field\\flevel.lgp", var.FFVII_PATH + "data\\field\\flevel.bak")
    os.remove(var.FFVII_PATH + "data\\field\\flevel.lgp")
    os.rename(var.FFVII_PATH + "data\\field\\conv_flevel.lgp", var.FFVII_PATH + "data\\field\\flevel.lgp")
    os.remove(var.FFVII_PATH + "patch.exe")
    os.remove(var.FFVII_PATH + "flevel.pat")

    log.logger("COMPL_2012_FLEVEL_CONV", "")

def install_setup_files():
    log.logger("APPLYING_102_PATCH")
    for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Patch102"):
        shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Patch102\\" + file, var.FFVII_PATH + file)

    log.logger("COMPL_102_PATCH_INST", "")

    if not var.BASE_MODELS == 0:
        log.logger("ADJUSTING_ALPHA_BLEND")

        for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Battle\\Battle.lgp\\Alpha_Fixes\\Various"):
            shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Battle\\Battle.lgp\\Alpha_Fixes\\Various\\" + file, fl.BATTLE_PATCH + file)

        log.logger("COMPL_BAT_MODELS_ADJ", "")

    aali = False
    if IsFile.game("ff7_opengl.fgd"): # It was already installed
        log.logger("WARN_OLDER_AALI", "RUN_BOOT_CLEAN")
        var.FATAL_ERROR.append("old_opengl")
        return
    for path in var.MOD_LOCATION:
        for file in os.listdir(path):
            if fl.OPENGL == file:
                aali = True
                log.logger("INST_AALIS_DRIVER")
                ManipFile._7zip(path + "\\" if path[-1] not in ("/", "\\") else "" + file, var.BOOTLEG_TEMP + "OpenGL")
                for gl in os.listdir(var.BOOTLEG_TEMP + "OpenGL"):
                    shutil.copy(var.BOOTLEG_TEMP + "OpenGL\\" + gl, var.FFVII_PATH + gl)

                for shader in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Shaders"):
                    if shader == "nolight":
                        continue # That's a folder
                    shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\" + shader, var.FFVII_PATH + "shaders\\" + shader)

                for shader in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\nolight"):
                    shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\nolight\\" + shader, var.FFVII_PATH + "shaders\\nolight\\" + shader)

    if aali: # Aali's driver installed properly
        log.logger("AALI_INSTALLED")
    else:
        log.logger("WARN_NO_AALI", "ADD_AALI_TO_MOD", form=[fl.OPENGL, "MULT_IN_ONE" if len(var.MOD_LOCATION) > 1 else "ONE_IN", "', '".join(var.MOD_LOCATION)])
        var.FATAL_ERROR.append("no_opengl")
        return

    log.logger("", "INST_BOOT_SYS_FILES", form=con.PROGRAM_NAME)
    for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Bootleg"):
        shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Bootleg\\" + file, var.FFVII_PATH + file)

    log.logger("COMPL_BOOT_SYS_FILES", form=con.PROGRAM_NAME)

def find_data_drive(inp=None):
    if inp is None:
        log.logger("REG_LOCATING_DATADRIVE")
        cdrom = reg.get_key("DataDrive")
        if not cdrom:
            log.logger("", "CANT_LOCATE_FF7_DRIVE", "ENTER_VALID_DRIVE_LET")
            var.PARSING = "DataDrive"
            return
    else:
        cdrom = inp
    cdrom = cdrom[0]
    if os.system("vol {0}: 2>nul>nul".format(cdrom)) == 0 or var.DEBUG_MODE: # Drive exists and is ready (or in debug mode)
        log.logger("USING_DRIVE_FOR_CDS", form=cdrom)
        var.CD_DRIVE = cdrom + ":"
        var.PARSING = None
    else:
        log.logger("ERR_DRIVE_NOT_EXIST_READY", "ENT_VALID_DRIVE_LETTER")

def _mkdir(inp):
    if not os.path.isdir(inp):
        os.mkdir(inp)

def attrib(file, attr, params=""): # sets Windows file and folders attributes
    os.system("C:\\Windows\\System32\\attrib.exe " + attr + ' "' + file + '" ' + params)

def parser(inp):
    if var.PARSING == "Language":
        chk_game_language(inp)
    if var.PARSING == "DataDrive":
        find_data_drive(inp)

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
    if not IsFile.sys(fl.SEVENZ):
        var.FATAL_ERROR.append("sevenz")

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
    elif var.SYS_ERROR:
        log.multiple("ERR_ENC", "MAY_STILL_RUN", form=con.PROGRAM_NAME, types=["error", "normal"])
    if var.FATAL_ERROR or var.SYS_ERROR:
        var.ERROR = True
        for reason in var.FATAL_ERROR + var.SYS_ERROR:
            reason = reason.capitalize()
            log.multiple("ERR_FOUND", types=["error", "normal"], form=reason, display=False)
            if hasattr(errors, reason):
                why = getattr(errors, reason)
                formlist = []
                if "Format" in why:
                    toformat = why["Format"]
                    for lister in toformat:
                        if hasattr(*lister):
                            formlist.append(getattr(*lister))
                        else:
                            formlist.append(toformat)

                log.multiple(why["Message"], types=["error", "normal"], form=formlist)
            else:
                log.multiple(errors.unhandled, types=["error", "normal"])
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
        log.help("ENT_EXACT_DIG", form=len(str(con.RANGE[setting])[1:]))
    else:
        log.help("ENT_VALUE_BETWEEN", form=con.RANGE[setting])
    log.help("")
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
    log.help("")
    tosay = "DEF_TO_USE"
    if con.RANGE[setting] < 0:
        tosay += "TOO_FEW_DIG"
    log.help(tosay + ".", form=getattr(var, setting))

def no_such_command(command):
    log.logger("ERR_INVALID_COMMAND", form=command, write=False)