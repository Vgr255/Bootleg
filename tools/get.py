from tools import logger as log
from tools import constants as con
from tools import variables as var
from tools import parser
import platform

def settings():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(var, x)
        for s, u in y.items():
            setattr(var, s, u)

def config():
    for x in con.SETTINGS_PREFIXES.keys():
        x = x.replace("VAR", "SETTINGS")
        y = getattr(config, x)
        for s, u in y.items():
            setattr(var, s, u)

def parser(setting): # get function xyz() in parser.py for variable XYZ
    parse = None
    for x in parser.__dict__.keys():
        y = setting.lower()
        if not x == y:
            continue
        parse = getattr(parser, y)
        break # we got what we wanted
    return parse

def setting(inp): # sets variables
    try:
        inp2 = int(inp)
    except ValueError:
        log.logger("Please enter only numbers.")
        return
    if con.RANGE[var.FINDING] < 0:
        rng = str(con.RANGE[setting])[1:]
        if len(str(inp2)) == len(rng):
            for x in range(0, int(len(rng))):
                if str(inp2)[x] in range(0, int(rng[x]) + 1):
                    continue
                else:
                    log.logger("Error: Value out of bounds at position {0}: {1} (Max: {2}).".format(x + 1, str(inp2)[x], rng[x]))
                    return
            setattr(var, var.FINDING, inp2)
            var.FINDING = None
        else:
            log.logger("Please enter exactly {0} digits.".format(len(rng)))
    elif inp2 in range(0, con.RANGE[var.FINDING] + 1):
        setattr(var, var.FINDING, inp2)
        log.logger("Setting used for {0}: {1}".format(var.FINDING, inp2), display=False)
        var.FINDING = None

def architecture(): # find processor architecture
    var.ARCHITECTURE = platform.architecture()[0]
    log.logger("Operating System: {0} on {1}.".format(str(platform.architecture()[1]), var.ARCHITECTURE), display=False, type="debug")
    log.logger("Running Bootleg on {0}.".format(var.ARCHITECTURE), display=False)
    if str(platform.architecture()[1]) == "WindowsPE":
        var.ON_WINDOWS = True
    rgent = "HKEY_LOCAL_MACHINE\\SOFTWARE\\"
    if var.ARCHITECTURE == "64bit":
        rgent = rgent + "Wow6432Node\\"
    var.SHORT_REG = rgent + "Square Soft, Inc."
    var.REG_ENTRY = var.SHORT_REG + "\\Final Fantasy VII"