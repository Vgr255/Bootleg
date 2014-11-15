# Startup initialization

import platform

from tools import variables as var
from tools import constants as con
from tools import help

var.ON_WINDOWS = False

if platform.system() == "Windows":
    import winreg
    var.ON_WINDOWS = True

# Gets processor architecture

var.ARCHITECTURE = platform.architecture()[0]

if var.ON_WINDOWS:
    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\Git_is1".format("Wow6432Node\\" if var.ARCHITECTURE == "64bit" else ""))
        var.GIT_LOCATION = winreg.QueryValueEx(reg, "InstallLocation")[0] + "bin\\git.exe"
    except OSError:
        pass

# Converts settings into standalone variables

for x in con.SETTINGS_PREFIXES.keys():
    x = x.replace("VAR", "SETTINGS")
    y = getattr(var, x)
    for s, u in y.items():
        setattr(var, s, u)
        if x[:-9] not in con.NON_INT_SETTINGS:
            setattr(var, s, int(u)) # make sure all parameters are integers

# Fetches users and commands lists for help

var.USERS = []

usr = con.FIRST_DEV + con.USER_HELP + con.CODERS + con.GAME_CONV + con.BETA_TESTERS + con.SPECIAL_THANKS + con.EXT_HELP + con.TRANSLATORS
for user in usr:
    if user in var.USERS:
        continue
    var.USERS.append(user.lower())

var.COMMANDS = []

cmd = con.COMMANDS + con.ERROR_COMMANDS + con.DEBUG_COMMANDS + con.HIDDEN_COMMANDS
for comm in cmd:
    if comm in var.COMMANDS:
        continue
    var.COMMANDS.append(comm)

# Gets actual possibilities for helping

var.HELPERS = []

for topic in help.__dict__.keys():
    if "_" in topic or topic in (var.USERS + var.COMMANDS) or topic in ("users", "commands"):
        continue
    var.HELPERS.append(topic)

# Gets the registry entry for the game

if var.ON_WINDOWS:
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
    liner = ""
    if var.ARCHITECTURE == "64bit":
        reg = winreg.OpenKey(reg, "Wow6432Node")
        liner = "Wow6432Node\\"
    try: # 1998 original
        reg = winreg.OpenKey(reg, "Square Soft, Inc.")
        var.REGISTRY = winreg.OpenKey(reg, "Final Fantasy VII")
        var.GAME_VERSION = 1998
        var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(liner)
    except OSError: # does not exist
        try: # 2012 Square Enix store
            reg = winreg.OpenKey(reg, "Microsoft")
            reg = winreg.OpenKey(reg, "Windows")
            reg = winreg.OpenKey(reg, "CurrentVersion")
            reg = winreg.OpenKey(reg, "Uninstall")
            var.REGISTRY = winreg.OpenKey(reg, "{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1")
            var.GAME_VERSION = 2012
            var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1".format(liner)
        except OSError:
            try: # 2013 Steam
                var.REGISTRY = winreg.OpenKey(reg, "Steam App 39140")
                var.GAME_VERSION = 2013
                var.REG_ENTRY = "SOFTWARE\\{0}Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 39140".format(liner)
            except OSError:
                var.GAME_VERSION = 1999
                var.REG_ENTRY = "SOFTWARE\\{0}Square Soft, Inc.\\Final Fantasy VII".format(liner)

    if not var.GAME_VERSION == 1999:
        var.REG_SOUND = var.REG_ENTRY + "\\1.00\\Sound"
        var.REG_GRAPH = var.REG_ENTRY + "\\1.00\\Graphics"
        var.REG_MIDI = var.REG_ENTRY + "\\1.00\\MIDI"