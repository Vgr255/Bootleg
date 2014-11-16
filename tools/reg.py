from tools import variables as var
from tools import logger as log
import os

if var.ON_WINDOWS:
    import winreg

if var.GAME_VERSION == 1999: # No game installed, create new reg entry
    set_new()

if var.GAME_VERSION in (2012, 2013):
    change()

def add(drive=None, app=None):
    if app is None:
        app = var.FFVII_PATH
    if drive is None:
        drive = var.CD_DRIVE
    if not app[-1:] == "\\":
        app = app + "\\"
    drive = drive[0] + ":\\"
    drive = drive.replace("\\", "\\\\") # need to print two backslahses
    app = app.replace("\\", "\\\\")
    write("DataDrive", drive)
    write("AppPath", app)
    write("DataPath", "{0}Data\\\\".format(app))
    write("MoviePath", "{0}movies\\\\".format(app))
    write("DriverPath", "{0}ff7_opengl.fgd".format(app))
    write("FullInstall", "00000001", 4)
    write("DriverPath", "{0}ff7_opengl.fgd".format(app), 1, 1)
    write("Driver", "00000003", 4, 1)
    write("Mode", "00000002", 4, 1)

    write("{0}ff7.exe".format(var.FFVII_PATH), "RUNASADMIN", 1, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 1)
    write("{0}FF7Config.exe".format(var.FFVII_PATH), "RUNASADMIN", 1, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 1)

    

def write(key=None, value=None, type=1, path=0, opener=2, create=False): # There are no integrity checks
    # Possible types:
    # 0 = No type
    # 1 = String
    # 2 = String with references to system variables
    # 3 = Binary data
    # 4 = 32-bit Dword (little endian) ... whatever endian means
    # 5 = 32-bit Dword (big endian)
    # 6 = Unicode symbolic link
    # 7 = Sequence of strings
    # 8 = Device-driver resource list
    # 9 = Hardware setting
    # 10 = Hardware resource list
    # Possible path integer constants:
    # 0 = var.REG_ENTRY
    # 1 = var.REG_GRAPH
    # 2 = var.REG_SOUND
    # 3 = var.REG_MIDI
    # Possible opener integers:
    # 0 = HKEY_CLASSES_ROOT
    # 1 = HKEY_CURRENT_USER
    # 2 = HKEY_LOCAL_MACHINE
    # 3 = HKEY_PERFORMANCE_DATA
    # 4 = HKEY_CURRENT_CONFIG

    path_ints = {0: var.REG_ENTRY, 1: var.REG_GRAPH, 2: var.REG_SOUND, 3: var.REG_MIDI}

    if (not key or not value) and not create:
        return # Not allowed

    if path.isdigit():
        path = path_ints[int(path)]

    reg = winreg.OpenKey(18446744071562067968+opener, path, 0, 131078) # Do not alter these numbers
    if create:
        winreg.CreateKey(reg, path)
    else:
        winreg.SetValueEx(reg, key, 0, type, value)

def get_key(value, path=None):
    if path is None:
        path = var.REGISTRY
    try:
        reg = winreg.QueryValueEx(path, value)
    except OSError:
        reg = None
    return reg

def change(): # converts 2012/2013 registry keys to 1998
    pass # todo
    # InstallLocation holds the install path for both the 2012 and 2013 version

def set_new(): # Create a new registry entry
    write(create=True)
    write("DataDrive", "")
    write("AppPath", "")
    write("DataPath", "")
    write("MoviePath", "")
    write("DiskNo", "00000000", 4)
    write("FullInstall", "00000001", 4)
    write("SSI_DEBUG", "53,48,4f,57,4d,45,54,48,45,41,50,50,4c,4f,47,00", 3)
    write("DriverPath", "")
    write(path=1, create=True)
    write("DD_GUID", "00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00", 3, 1)
    write("DriverPath", "", 1, 1)
    write("Driver", "00000003", 4, 1)
    write("Mode", "00000002", 4, 1)
    write("Options", "00000000", 4, 1)
    write(path=3, create=True)
    write("MIDI_DeviceID", "ffffffff", 4, 3)
    write("MIDI_data", "GENERAL_MIDI", 1, 3)
    write("MusicVolume", "00000064", 4, 3)
    write("Options", "00000001", 4, 3)
    write(path=2, create=True)
    write("Sound_GUID", "00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00", 3, 2)
    write("Options", "00000000", 4, 2)
    write("SFXVolume", "00000064", 4, 2)