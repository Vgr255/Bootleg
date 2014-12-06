# Various file manipulation methods.

# All functions return something. Usually something meaningful, otherwise 0.
# If one of these functions return None, something unexpected happened.

from tools import variables as var
from tools import logger as log

import subprocess
import shutil
import os

# Get the custom exceptions

from tools.exceptions import *

def FindFile(seeker):
    """FindFile(file)

    Attempts to locate file in any of the mods folders.

    If file is a full path, it will attempt to use the GetFile() function
    to split the folder and file from the full path.

    Returns a tuple of (folder, file) in either case.

    If the file is not a full path and can't be found, it will raise
    ModFileNotFound, giving the file as argument."""

    for folder in var.MOD_LOCATION:
        for file in os.listdir(folder):
            if file.lower() == seeker.lower():
                if not folder[-1:] in ("/", "\\"):
                    folder = folder + "\\"
                return folder, file

    if True in [slash in seeker for slash in ("/", "\\")]:
        return GetFile(seeker) # Full path

    raise ModFileNotFound(seeker) # Exit out if the mod could not be found

def ExecuteFile(*args):
    """ExecuteFile(file, *params)

    Runs an executable file located in (one of) the Mods location.
    Returns the process' return code."""

    folder, file = FindFile(args[0])
    params = args[1:]

    log.logger("PARS_EXEC_FILE", form=[file, folder[:-1], params], display=False)
    process = subprocess.Popen([folder + file] + params)
    process.communicate()
    return process.returncode

def GetFile(file):
    """GetFile(file)

    Splits the folder and file from a full path.
    Returns a tuple of (folder, file)."""

    new = list(file)
    new.reverse()
    indx = len(new) + 1
    for slash in ("/", "\\"):
        if not shash in new:
            continue
        if new.index(slash[1:]) < indx:
            indx = new.index(slash)
    if indx < len(new):
        return file[:-indx], file[-indx:] # Full path and file name
    return None, file # Don't raise an error, but there isn't any folder

def GetName(file):
    """GetName(file)

    Removes the extension from a file.
    Returns a tuple of (file, extension)."""

    new = list(file)
    new.reverse()
    if not "." in new:
        return file, None
    indx = new.index(".")
    return file[:indx], file[indx+1:]

def ExtractFile(file, dst=None, pw=None):
    """ExtractFile(file, dst=None, pw=None)

    Extracts an archive into the temp folder.
    Specify a file, a destination and a password.
    If 'file' is not an archive, it will simply copy it over.
    If 'dst' is not specified, it will use the file's name.
    Returns the location of the resulting files."""

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
    if not path[-1:] in ("/", "\\"):
        path = path + "\\"

    if pw is None:
        pw = "none"

    if type == "rar": # Rar file
        subprocess.Popen([var.RAR_LOCATION, "x", "-y", "-p" + pw, path+file, var.BOOTLEG_TEMP + dst])
    if type == "zip": # Zip file
        subprocess.Popen([var.SEVENZ_LOCATION, "x", "-p" + pw, "-y", "-o" + var.BOOTLEG_TEMP + dst, path + file])
    else: # No type, just copy it over
        shutil.copy(path + file, var.BOOTLEG_TEMP + dst + file)

    log.logger("PARS_EXTR_FILE", form=[path + file], display=False)
    return var.BOOTLEG_TEMP + dst

def ExtractFolder(path):
    """ExtractFolder(path)

    Extracts all the archives from a folder into that same folder.
    Returns a tuple of all the resulting folders' names."""

    if not path[-1:] in ("/", "\\"):
        path = path + "\\"
    folders = []
    files = []
    for file in os.listdir(path):
        files.append(path + file)
        _file, ext = GetName(file)
        folder = ExtractFile(path + file)
        CopyFolder(folder, path + _file)
        folders.append(path + _file)

    DeleteFile(*files)
    return tuple(folders)

def ExtractLGP(file, dir=None):
    """ExtractLGP(file, dir=None)

    Extracts the contents of a LGP archive in a folder.
    Returns the resulting directory."""

    if dir is None:
        p, f = GetFile(file)
        dir = var.BOOTLEG_TEMP + f
    subprocess.Popen([var.ULGP_LOCATION, "-x", file, "-C", dir])
    return dir

def RepackLGP(dir, file=None):
    """RepackLGP(dir, file=None)

    Packs the contents of a folder into a LGP archive.
    Returns the resulting file."""

    if file is None:
        if dir[-1:] in ("/", "\\"):
            dir = dir[:-1]
        p, f = GetFile(dir)
        file = var.BOOTLEG_TEMP + f + ".lgp"
    subprocess.Popen([var.ULGP_LOCATION, "-c", file, "-C", dir])
    return file

def LaunchFile(*params):
    """LaunchFile(file, *params)

    Runs a raw executable file.
    The parameters are to feed to the process. Can be multiple parameters.
    Returns the process' return code."""

    file = subprocess.Popen(params)
    file.communicate()
    return file.returncode

def CopyFolder(src, dst):
    """CopyFolder(src, dst)

    Copies the content of 'src' into 'dst'.
    The destination may or may not exist.
    Always returns 0."""

    if not src[-1:] in ("/", "\\"):
        src = src + "\\"
    if not dst[-1:] in ("/", "\\"):
        dst = dst + "\\"
    if not os.path.isdir(dst):
        os.mkdir(dst)

    for file in os.listdir(src):
        shutil.copy(src + file, dst + file)
    return 0

def CopyFile(path, file, new):
    """CopyFile(path, file, new)

    Creates of copy of 'file' with name 'new' in 'path'.
    Always returns 0."""

    if not path[-1:] in ("/", "\\"):
        path = path + "\\"

    shutil.copy(path + file, path + new)
    return 0

def DeleteFile(*path):
    """DeleteFile(*path)

    Deletes all files and folders given.
    Always returns 0."""

    if not path[-1:] in ("/", "\\"):
        path = path + "\\"

    for line in path:
        if os.path.isdir(path + line):
            shutil.rmtree(path + line)
        if os.path.isfile(path + line):
            os.remove(path + line)

    return 0

def RenameFile(path, org, new):
    """RenameFile(path, org, new)

    Renames item x of 'org' to item x of 'new' in path.
    Returns 0 if all items could be renamed.
    Returns more than 0 if there were more items in 'org' than 'new'
    Returns less than 0 if there were more items in 'new' than 'org'"""

    cont = zip(org, new)
    if not path[-1:] in ("/", "\\"):
        path = path + "\\"
    for file in cont:
        if os.path.isfile(path + file[0]):
            os.rename(path + file[0], path + file[1])

    return len(org) - len(new)

def AttribFile(file, attr="-R -S -H -I", params=""):
    """AttribFile(file, attr="-R -S -H -I", params="")

    Sets Windows file and folders attributes.
    Default attribute change is to remove all unwanted attributes.
    Parameters are optional, it's mainly to touch folders as well.
    Returns 0 if it completed successfully."""

    attrib = subprocess.Popen(["C:\\Windows\\System32\\attrib.exe"] + attr.split() + [file] + params.split())
    attrib.communicate()
    return attrib.returncode

def StripFolder(path):
    """StripFolder(path)

    Brings all files within all subfolders to the root ('path').
    Deletes all subfolders of the main path.
    Returns a tuple of all the subfolders that were copied over."""

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

def CallSkipMod(mod):
    """CallSkipMod(mod)

    Prints a missing mod warning using 'mod' as the missing file.
    Always returns 0."""

    if len(var.MOD_LOCATION) == 1:
        iner = "ONE_IN"
    else:
        iner = "MULT_IN_ONE"
    log.logger("PARS_SKIP", form=[mod, iner, "', '".join(var.MOD_LOCATION)])
    return 0