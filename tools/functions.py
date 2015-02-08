from tools import constants as con
from tools import variables as var
from tools import parsables as par
from tools import filenames as fl
from tools import parser as pars
from tools import logger as log
from tools import errors
from tools import get
from tools import reg

import configparser
import tempfile
import shutil
import sys
import os

# Get file manipulation methods

from tools.methods import *

def initialize(): # initialize variables on startup and/or retry
    begin = "BEGIN_BOOT"
    if var.RETRY:
        begin = "RESTART_BOOT"
    log.multiple(begin, form=[con.PROGRAM_NAME], types=["all"], display=False)
    var.INITIALIZED = True
    var.RETRY = False
    log.logger("LNCH_PAR", form=", ".join(["=".join(x) for x in var.LAUNCH_PARAMS]), type="debug", display=False)
    log.logger("RUN_LANG", form=[var.LANGUAGE.upper(), con.PROGRAM_NAME], display=False)
    log.logger("RUN_OS", form=[var.ARCHITECTURE, con.PROGRAM_NAME, str(var.ON_WINDOWS).upper()], display=False)
    log.multiple("Python", sys.version, display=False, splitter=" ", types=["normal", "debug"])
    var.FATAL_ERROR = []
    var.SYS_ERROR = []
    var.PARSING = None
    var.FINDING = None
    var.ERROR = False

    os.system("cls") # clear the screen off everything.
    log.help("\n".join(con.BOOT_ASCII1))
    log.help("BOOT_ARCH", form=[var.ARCHITECTURE])
    log.help(con.BOOT_ASCII2)
    log.help("BOOT_STARTUP", form=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
    log.help("\n".join(con.BOOT_ASCII3))

    if not var.ON_WINDOWS:
        log.logger("", "NOT_ON_WINDOWS", form=[con.PROGRAM_NAME], type="error")

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

def make_new_bootleg(): # to call after every setting is set, before starting to install
    usr_set = ["LOGGING_SETTINGS"]
    for setting, prefix in par.__dict__.items():
        if not setting.isupper():
            continue
        usr_set.append(prefix + getattr(var, setting))
    log.logger(usr_set, display=False, type="settings")
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
        setattr(fl, "WORKING_" + d, var.BOOTLEG_TEMP + "Data_Working\\" + d.lower() + "\\")
        _mkdir(getattr(fl, "WORKING_" + d))
    for u in con.FILES_UNDO:
        setattr(fl, u + "_UNDO", var.BOOTLEG_TEMP + u.lower() + "_undo\\")
        _mkdir(getattr(fl, u + "_UNDO"))
    log.logger("INIT_CMPLT", "", "EXTR_SPRKL")
    _mkdir(var.BOOTLEG_TEMP + "Sprinkles")
    ExtractFile(fl.SPRINKLES, var.BOOTLEG_TEMP + "Sprinkles")
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

    # Remove some attributes from the files to manipulate them
    for file in con.TRANSLATE_CHANGER:
        AttribFile(data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp")

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
    tmp = var.BOOTLEG_TEMP + "lang_files\\"
    _mkdir(tmp)
    for lang in con.GAME_LANGUAGES.keys():
        if var.GAME_LANGUAGE == con.GAME_LANGUAGES[lang][4]:
            log.logger("IDENT_LANG_VERS_" + con.GAME_LANGUAGES[lang][0].upper())

            for file in con.TRANSLATE_CHANGER:
                AttribFile(data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp")

            if var.GAME_LANGUAGE == 0:
                break

            for file in con.TRANSLATE_CHANGER:
                os.rename(data + file.format(con.GAME_LANGUAGES[lang][1], con.GAME_LANGUAGES[lang][3], con.GAME_LANGUAGES[lang][2]) + ".lgp",
                          data + file.format(con.GAME_LANGUAGES["English"][1], con.GAME_LANGUAGES["English"][3], con.GAME_LANGUAGES["English"][2]) + ".lgp")

            # Condor minigame translation

            ExtractLGP(data + "minigame\\condor.lgp", tmp + "condor")

            tempc = tmp + "condor\\"

            for file in os.listdir(tempc):
                if file == "mes02.tex":
                    continue
                for prefix in ("mes", "unit", "help"):
                    if prefix in file:
                        os.rename(tempc + file, tempc + "e" + file[1:])

            for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Condor_Tran"):
                shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Condor_Tran\\" + file, var.BOOTLEG_TEMP + "condor\\" + file)

            os.remove(data + "minigame\\condor.lgp")
            RepackLGP(tempc, data + "minigame\\condor.lgp")

            # Snowboard minigame translation

            ExtractLGP(data + "minigame\\snowboard-us.lgp", tmp + "snowboard")

            tempc = tmp + "snowboard\\"

            for file in os.listdir(tempc):
                for prefix in ("_k.tex", "stamp", "time"):
                    if prefix in file:
                        e = "e"
                        if prefix == "time":
                            e = ""
                        os.rename(tempc + file, tempc + e + file[1:])

            os.remove(data + "minigame\\snowboard-us.lgp")
            RepackLGP(tempc, data + "minigame\\snowboard-us.lgp")

            # Submarine minigame translation

            ExtractLGP(data + "minigame\\sub.lgp", tmp + "sub")

            tempc = tmp + "sub\\"

            for file in os.listdir(tempc):
                os.rename(tempc + file, tempc + file[1:])

            os.remove(data + "minigame\\sub.lgp")
            RepackLGP(tempc, data + "minigame\\sub.lgp")

            # Disc files translation

            ExtractLGP(data + "cd\\disc-us.lgp", tmp + "disc")

            tempc = tmp + "disc\\"

            for file in os.listdir(tempc):
                for prefix in ("disc", "over"):
                    if prefix in file:
                        e = "e" if prefix == "over" else ""
                        os.rename(tempc + file, tempc + e + file[1:])

            os.remove(data + "cd\\disc-us.lgp")
            RepackLGP(tempc, data + "cd\\disc-us.lgp")

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

    LaunchFile(var.FFVII_PATH + "patch.exe", "flevel.pat", "data\\field\\flevel.lgp", "data\\field\\conv_flevel.lgp")

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

    if IsFile.game("ff7_opengl.fgd"): # It was already installed
        log.logger("WARN_OLDER_AALI", "RUN_BOOT_CLEAN")
        var.FATAL_ERROR.append("old_opengl")
        return
    try:
        FindFile(fl.OPENGL)
        log.logger("INST_AALIS_DRIVER")
        ExtractFile(fl.OPENGL, var.BOOTLEG_TEMP + "OpenGL")
        for gl in os.listdir(var.BOOTLEG_TEMP + "OpenGL"):
            shutil.copy(var.BOOTLEG_TEMP + "OpenGL\\" + gl, var.FFVII_PATH + gl)

        for shader in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Shaders"):
            if shader == "nolight":
                continue # That's a folder
            shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\" + shader, var.FFVII_PATH + "shaders\\" + shader)

        for shader in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\nolight"):
            shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Shaders\\nolight\\" + shader, var.FFVII_PATH + "shaders\\nolight\\" + shader)

        log.logger("AALI_INSTALLED")
    except FileNotFoundError:
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
            log.logger("", "CANT_LOCATE_FF7_DRIVE", "ENTER_VALID_DRIVE_LETTER")
            var.PARSING = "DataDrive"
            return
    else:
        cdrom = inp
    cdrom = cdrom[0]
    if not os.system("vol {0}: 2>nul>nul".format(cdrom)) and not var.DEBUG_MODE: # Drive doesn't exist/not ready (and not in debug mode)
        log.logger("ERR_DRIVE_NOT_EXIST_READY", "ENTER_VALID_DRIVE_LETTER")
        return

    log.logger("", "USING_DRIVE_FOR_CDS", form=cdrom)
    var.CD_DRIVE = cdrom + ":"
    var.PARSING = None

    log.logger("", "BUILDING_SYS_FILES", "UPDATING_REG_SILENT")
    reg.add()
    log.logger("", "COMPL_REG_SILENT", "")

    audio_device = reg.get_key("Sound_GUID", 2)

    log.logger("REGISTERING_AUDIO_DEVICES")
    if IsFile.game("FF7Config.exe"):
        log.logger("CONFIG_SND_MIDI_DEVICES")
        LaunchFile(var.FFVII_PATH + "FF7Config.exe")
    else:
        var.FATAL_ERROR.append("ff7config")

    log.logger("COMPL_AUDIO_DEVICES", "")

def prepare_data_files():
    log.logger("PREPARING_LGP_FILES")

    # Battle LGP
    log.logger("PREPARING_DATA_FILE", "COPYING_DUMMY_TEX", form="battle.lgp")
    CopyFolder(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Battle\\Battle.lgp\\Bootleg\\Dummy_Textures", fl.BATTLE_UNDO)
    AttribFile(var.FFVII_PATH + "data\\battle\\battle.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\battle\\battle.lgp", fl.BATTLE_UNDO)
    log.logger("COMPLETED_DATA_FILE", form="battle.lgp")

    log.help()

    # Magic LGP
    log.logger("PREPARING_DATA_FILE", form="magic.lgp")
    AttribFile(var.FFVII_PATH + "data\\battle\\magic.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\battle\\magic.lgp", fl.MAGIC_UNDO)
    log.logger("COMPLETED_DATA_FILE", form="magic.lgp")

    log.help()

    # Char LGP
    log.logger("PREPARING_DATA_FILE", form="char.lgp")
    AttribFile(var.FFVII_PATH + "data\\field\\char.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\field\\char.lgp", fl.CHAR_UNDO)
    log.logger("COMPLETED_DATA_FILE", form="char.lgp")

    log.help()

    # High LGP
    log.logger("PREPARING_DATA_FILE", form="high-us.lgp")
    AttribFile(var.FFVII_PATH + "data\\minigame\\high-us.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\minigame\\high-us.lgp", fl.HIGH_UNDO)
    log.logger("COMPLETED_DATA_FILE", form-"high-us.lgp")

    log.help()

    # Chocobo LGP
    log.logger("PREPARING_DATA_FILE", form="chocobo.lgp")
    AttribFile(var.FFVII_PATH + "data\\minigame\\chocobo.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\minigame\\chocobo.lgp", fl.CHOCOBO_UNDO)
    log.logger("COMPLETED_DATA_FILE", form="chocobo.lgp")

    log.help()

    # World LGP
    log.logger("PREPARING_DATA_FILE", form="world_us.lgp")
    AttribFile(var.FFVII_PATH + "data\\wm\\world_us.lgp")
    ExtractLGP(var.FFVII_PATH + "data\\wm\\world_us.lgp", fl.WORLD_UNDO)
    log.logger("COMPLETED_DATA_FILE", form="world_us.lgp")

    log.logger("COMPLETED_LGP_FILES")

    log.help()

def _mkdir(inp):
    if not os.path.isdir(inp):
        os.mkdir(inp)

def parser(inp):
    if var.PARSING == "Language":
        chk_game_language(inp)
    if var.PARSING == "DataDrive":
        find_data_drive(inp)

def parse_settings(preset=None):
    if preset is None:
        preset = var.PRESET
    newpre = "temp/preset_{0}.tmp".format(get.random_small(4))
    with open(os.getcwd() + "/presets/" + preset) as p, open(newpre, "x") as n:
        if lines[0] != "[preset]\n":
            n.write("[preset]\n")
        lines = p.readlines()
        while lines:
            n.write(lines.pop(0))

    preset_parser = configparser.ConfigParser()
    preset_parser.read(newpre)

    for setting, value in preset_parser["preset"].items():
        setting = setting.replace(" ", "_").upper()
        if not hasattr(var, setting):
            continue
        num = 1
        if setting in con.RANGE.keys():
            num = con.RANGE[setting]
        if setting not in con.NON_INT_SETTINGS:
            if value.isdigit():
                if int(value) in range(num+1):
                    value = int(value)
                else: # not in range
                    raise ValueError("value out of bound for " + setting +
                          " (value: " + value + " - max: " + num + ")")
            else: # not a digit
                raise TypeError(setting + " needs to be an integer (value: " + value + ")")
        if value.lower() in ("no", "off", "0", "false"):
            value = False
        if value.lower() in ("yes", "on", "1", "true"):
            value = True
        var.OLD_SETTINGS[setting] = getattr(var, setting)
        setattr(var, setting, value)

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
    ExtractFile(var.FFVII_IMAGE, var.FFVII_PATH)
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
    if var.DEBUG_MODE:
        var.FATAL_ERROR = []
        var.SYS_ERROR = []
    if var.IGNORE_FATAL_ERROR:
        var.FATAL_ERROR = []
    if var.IGNORE_SYSTEM_ERROR:
        var.SYS_ERROR = []
    if not (var.FATAL_ERROR + var.SYS_ERROR):
        return
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
            if reason in errors:
                why = errors[reason]
                formlist = []
                if "Format" in why:
                    toformat = why["Format"]
                    for lister in toformat:
                        if hasattr(*lister):
                            if getattr(*lister) == list(getattr(*lister)):
                                formlist.append("', '".join(lister))
                                continue
                            formlist.append(getattr(*lister))
                        else:
                            formlist.append(toformat)

                log.multiple(why["Message"], types=["error", "normal"], form=formlist)
            else:
                log.multiple("UNH_ERR_TOREP", types=["error", "normal"])
    log.logger("\n")

def find(setting): # Prompts the user for settings
    if not hasattr(var, setting):
        raise SettingNotFound(setting)

    getter = 1
    if setting in con.RANGE.keys():
        getter = con.RANGE[setting]
    parse = get.parser("find_" + setting.lower())
    if not parse:
        if getter != 1:
            raise NoParserFound(setting)
        msg = "INST_SPEC_SET"
    if parse:
        msg = parse()
        if getter == 1:
            msg = msg[0]
    var.FINDING = setting
    log.help("ENT_VALUE_BETWEEN", "", form=getter)
    if getter > 1:
        log.help(msg.pop(0))
        log.help("NO_CHG")
        log.help("\n".join(msg))
    if getter == 1:
        log.help(msg, form=setting)
        log.help("CHC_NO")
        log.help("CHC_YES")
    log.help("", "DEF_TO_USE", form=getattr(var, setting))

def install(setting): # Installs each setting
    if not hasattr(var, setting):
        raise ValueError(setting)

    parse = get.parser("install_" + setting.lower())

    log.logger("PARS_INSTALLING", "PLEASE_REMAIN_PATIENT", form=setting)
    ret = parse()
    formatt = setting
    if ret:
        formatt = ret
    log.logger("PARS_COMPL_INST_SUCCESS", form=formatt)

def no_such_command(command):
    log.logger("ERR_INVALID_COMMAND", form=command, write=False)
