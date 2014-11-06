from tools import variables as var
from tools import logger as log
import os

try:
    import winreg
except ImportError:
    log.logger("Bootleg will not work properly on a different operating system than Windows.", type="error")
    var.ON_WINDOWS = False

def git(): # get the registry key for the git install location
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
    if var.ARCHITECTURE == "64bit":
        reg = winreg.OpenKey(reg, "Wow6432Node")
    reg = winreg.OpenKey(reg, "Microsoft")
    reg = winreg.OpenKey(reg, "Windows")
    reg = winreg.OpenKey(reg, "CurrentVersion")
    reg = winreg.OpenKey(reg, "Uninstall")
    try:
        var.GIT_REG = winreg.OpenKey(reg, "Git_is1")
        var.GIT_LOCATION = winreg.QueryValueEx(var.GIT_REG, "InstallLocation")[0] + "bin\\git.exe"
    except OSError:
        pass

def get():
    if not var.ON_WINDOWS:
        return # not on Windows
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE")
    if var.ARCHITECTURE == "64bit":
        reg = winreg.OpenKey(reg, "Wow6432Node")
    try: # 1998 original
        reg = winreg.OpenKey(reg, "Square Soft, Inc.")
        var.REGISTRY = winreg.OpenKey(reg, "Final Fantasy VII")
        var.GAME_VERSION = 1998
    except OSError: # does not exist
        try: # 2012 Square Enix store
            reg = winreg.OpenKey(reg, "Microsoft")
            reg = winreg.OpenKey(reg, "Windows")
            reg = winreg.OpenKey(reg, "CurrentVersion")
            reg = winreg.OpenKey(reg, "Uninstall")
            var.REGISTRY = winreg.OpenKey(reg, "{141B8BA9-BFFD-4635-AF64-078E31010EC3}_is1")
            var.GAME_VERSION = 2012
            change()
        except OSError:
            try: # 2013 Steam
                var.REGISTRY = winreg.OpenKey(reg, "Steam App 39140")
                var.GAME_VERSION = 2013
                change()
            except OSError:
                var.GAME_VERSION = 1999
                set_new()

def add(drive, app, new_reg=False):
    write("Windows Registry Editor Version 5.00")
    write("")
    if new_reg:
        write(var.SHORT_REG)
        write("")
    write(var.REG_ENTRY)
    if not app[-1:] == "\\":
        app = app + "\\"
    if not drive[-1:] == "\\":
        drive = drive + "\\"
    drive = drive.replace("\\", "\\\\") # need to print two backslahses
    app = app.replace("\\", "\\\\")
    write('"DataDrive"="{0}"'.format(drive))
    write('"AppPath"="{0}"'.format(app))
    write('"DataPath"="{0}Data\\\\"'.format(app))
    write('"MoviePath"="{0}movies\\\\"'.format(app))
    write('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))
    write('')
    write(var.REG_ENTRY + '\\1.00\\Graphics')
    write('"DriverPath"="{0}ff7_opengl.fgd"'.format(app))

def write(inp, dir=os.getcwd(), file=var.TEMP_REG):
    exists = False
    dir = dir.replace("/", "\\")
    if not dir[-1:] == "\\":
        dir = dir + "\\"
    if not file[-4:] == ".reg":
        file = file + ".reg"
    if inp == "Windows Registry Editor Version 5.00":
        if os.path.isfile(dir + file):
            os.remove(dir + file)
    if os.path.isfile(dir + file):
        f = open("{1}{0}".format(file, dir), "r+")
        exists = True
    elif os.path.isdir(dir):
        f = open("{1}{0}".format(file, dir), "w") # let's create the file in the same directory...
    elif os.path.isfile(os.getcwd() + "/" + file):
        f = open(os.getcwd() + "\\{0}", "r+") # let's try the already-existing file in the current directory
        exists = True
    else:
        f = open(os.getcwd() + "\\{0}", "w")
    if inp[0] == "[":
        inp = inp + "]"
    f.seek(0, 2)
    if exists:
        f.write("\n")
    f.write(inp)

def get_key(value):
    try:
        reg = winreg.QueryValueEx(var.REGISTRY, value)
    except OSError:
        reg = None
    return reg

def change(): # converts 2012/2013 registry keys to 1998
    pass # todo
    # InstallLocation holds the install path for both the 2012 and 2013 version

def set_new(): # make a new registry entry if it doesn't exist. need to call add_to_reg() after
    write("Windows Registry Editor Version 5.00")
    write("")
    write(var.SHORT_REG)
    write("")
    write(var.REG_ENTRY)
    write('"DataDrive"=""')
    write('"AppPath"=""')
    write('"DataPath"=""')
    write('"MoviePath"=""')
    write('"DiskNo"=dword:00000000')
    write('"FullInstall"=dword:00000001')
    write('"SSI_DEBUG"=hex:53,48,4f,57,4d,45,54,48,45,41,50,50,4c,4f,47,00')
    write('"DriverPath"=""')
    write('')
    write(var.REG_ENTRY + '\\1.00')
    write('')
    write(var.REG_ENTRY + '\\1.00\\Graphics')
    write('"DD_GUID"=hex:00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00')
    write('"DriverPath"=""')
    write('"Driver"=dword:00000003')
    write('"Mode"=dword:00000002')
    write('"Options"=dword:00000000')
    write('')
    write(var.REG_ENTRY + '\\1.00\\MIDI')
    write('"MIDI_DeviceID"=dword:00000000')
    write('"MIDI_data"="GENERAL_MIDI"')
    write('"MusicVolume"=dword:00000064')
    write('"Options"=dword:00000001')
    write('')
    write(var.REG_ENTRY + '\\1.00\\Sound')
    write('"Sound_GUID"=hex:dd,39,42,c5,d1,6b,e0,4f,83,42,5f,7b,7d,11,a0,f5')
    write('"Options"=dword:00000000')
    write('"SFXVolume"=dword:00000064')