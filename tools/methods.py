# Various file manipulation methods. All the functions return a value;
# something meaningful if it can, else 0. A function returning 'None' means
# something unexpected happened. An exception is usually raised in that case.

from tools import variables as var
from tools import logger as log

import subprocess
import shutil
import os

# Get the custom exceptions

from tools.exceptions import *

def FindFile(seeker): # Finds a mod in all the mods folders. Returns a tuple of (folder, file) if successful, else raises an exception
    for folder in var.MOD_LOCATION:
        for file in os.listdir(folder):
            if file.lower() == seeker.lower():
                if not folder[-1:] in ("/", "\\"):
                    folder = folder + "\\"
                return folder, file

    raise ModFileNotFound(seeker) # Exit out if the mod could not be found

def ExecuteFile(file, params=""): # Runs an executable file. Always returns 0 if successful, else an exception is raised.
    folder, file = FindFile(file)
    params = params.split()

    log.logger("PARS_EXEC_FILE", form=[file, folder[:-1], params], display=False)
    subprocess.Popen([folder + file] + params)
    return 0

def ExtractFile(file, pw="none", dst=None): # Extracts an archive into the temp folder. Returns the folder it was extracted in.
    path, file = FindFile(file)

    if file.endswith(".rar"):
        type = "rar"
    elif file.endswith((".zip", ".7z")):
        type = "zip"
    else:
        type = None

    if dst is None:
        dst = file
    if not dst[-1:] in ("/", "\\"):
        dst = dst + "\\"

    if type == "rar": # Rar file
        subprocess.Popen([var.RAR_LOCATION, "x", "-y", "-p" + pw, path+file, var.BOOTLEG_TEMP + dst])
    if type == "zip": # Zip file
        subprocess.Popen([var.SEVENZ_LOCATION, "x", "-p" + pw, "-y", "-o" + var.BOOTLEG_TEMP + dst, path + file])
    else: # No type, just copy it over
        shutil.copy(path + file, var.BOOTLEG_TEMP + dst + file)

    log.logger("PARS_EXTR_FILE", form=[path + file], display=False)
    return var.BOOTLEG_TEMP + dst

def LaunchFile(mod, file): # Runs a file found in the folder created by ExtractFile(). Returns 0 if successful.
    if not os.path.isdir(var.BOOTLEG_TEMP + mod):
        raise InexistantFolderTemp(mod)
    if not os.path.isfile(var.BOOTLEG_TEMP + mod + "\\" + file):
        raise InexistantFileTemp(mod, file)

    if not mod[-1:] in ("/", "\\"):
        mod = mod + "\\"

    subprocess.Popen([var.BOOTLEG_TEMP + mod + file])
    return 0

def CopyFolder(src, dst): # Copies the contents of a folder in an existing location. Returns 0.
    if not src[-1:] in ("/", "\\"):
        src = src + "\\"
    if not dst[-1:] in ("/", "\\"):
        dst = dst + "\\"
    if not os.path.isdir(dst):
        os.mkdir(dst)

    for file in os.listdir(src):
        shutil.copy(src + file, dst + file)
    return 0

def CopyFile(path, file, new): # Copies a new file in the same directory with a new name. Returns 0.
    if not path[-1:] in ("/", "\\"):
        path = path + "\\"

    shutil.copy(path + file, path + new)
    return 0

def DeleteFile(path): # Deletes files and folders. Always returns 0
    for line in path:
        if os.path.isdir(line):
            shutil.rmtree(line)
        if os.path.isfile(line):
            os.remove(line)

    return 0

def RenameFile(path, org, new): # Renames item x of org to item x of new. Always returns 0
    cont = zip(org, new)
    if not path[-1:] in ("/", "\\"):
        path = path + "\\"
    for file in cont:
        if os.path.isfile(path + file[0]):
            os.rename(path + file[0], path + file[1])

    return 0

def StripFolder(path): # Brings all files of all subfolders in path. Returns a tuple of all the folders that were checked.
    if not path[-1:] in ("/", "\\"):
        path = path + "\\"
    folders = [path]
    allf = []
    while True:
        if not folders:
            return tuple(allf)
        folder = folders.pop(0)
        allf.append(folder)
        for lister in os.listdir(folder):
            if os.path.isdir(lister):
                folders.append(folder + lister + "\\")
            elif not path == folder:
                CopyFolder(folder, path)
                shutil.rmtree(folder)

def CallSkipMod(mod): # Prints a skip mod warning. Returns 0.
    if len(var.MOD_LOCATION) == 1:
        iner = "ONE_IN"
    else:
        iner = "MULT_IN_ONE"
    log.logger("PARS_SKIP", form=[mod, iner, "', '".join(var.MOD_LOCATION)])
    return 0