# Various file manipulation methods.

# All functions return something. Usually something meaningful, otherwise 0.
# If one of these functions return None, something unexpected happened.

from tools import variables as var
from tools import filenames as fl
from tools import log

import subprocess
import shutil
import os

# Actual methods

def FindFile(seeker):
    """FindFile(file)

    Attempts to locate file in any of the mods folders.

    If file is a full path, it will attempt to use the GetFile() function
    to split the folder and file from the full path.

    Returns a tuple of (folder, file) in either case.

    If the file is not a full path and can't be found, it will raise
    FileNotFoundError, giving the file as argument."""

    for folder in var.MOD_LOCATION:
        for file in os.listdir(folder):
            if file.lower() == seeker.lower():
                if not folder.endswith(("/", "\\")):
                    folder = folder + "\\"
                return folder, file

    if True in [slash in seeker for slash in ("/", "\\")]:
        return GetFile(seeker) # Full path

    raise FileNotFoundError(seeker) # Exit out if the mod could not be found

def ExecuteFile(*args): # the docstring lies about parameters
    """ExecuteFile(file, *params)

    Runs an executable file located in (one of) the Mods location.
    Returns the process' return code."""

    folder, file = FindFile(args[0])
    params = args[1:]

    log.logger("PARS_EXEC_FILE", format=[file, folder[:-1], params], display=False)
    process = subprocess.Popen([folder + file] + list(params))
    process.communicate()
    return process.returncode

def GetFile(file):
    """GetFile(file)

    Splits the folder and file from a full path.
    Returns a tuple of (folder, file)."""

    file = file.replace("/", "\\").strip("\\")
    new = list(file)
    new.reverse()
    if "\\" not in new:
        return None, file # Don't raise an error, but there isn't any folder
    indx = new.index("\\")
    return file[:-indx], file[-indx:] # Full path and file name

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
    if not dst.endswith(("/", "\\")):
        dst = dst + "\\"
    if not path.endswith(("/", "\\")):
        path = path + "\\"

    if pw is None:
        pw = "none"

    if type == "rar": # Rar file
        subprocess.Popen([var.RAR_LOCATION, "x", "-y", "-p" + pw, path+file, var.BOOTLEG_TEMP + dst])
    elif type == "zip": # Zip file
        subprocess.Popen([var.SEVENZ_LOCATION, "x", "-p" + pw, "-y", "-o" + var.BOOTLEG_TEMP + dst, path + file])
    else: # No type, just copy it over
        shutil.copy(path + file, var.BOOTLEG_TEMP + dst + file)

    log.logger("PARS_EXTR_FILE", format=[path + file], display=False)
    return var.BOOTLEG_TEMP + dst

def ExtractMod(mod, dst=None, pw=None, range=None, overwrite=True):
    """ExtractMod(mod, dst=None, pw=None, range=None, overwrite=True)

    Checks for a mod's existence and installs it if it exists.

    'dst' will be the final location. Defaults to the temp folder if unspecified.
    'pw' will be fed as the password to the ExtractFile function.
    'range' will be the range for which to check files; it's a two-tuple.
    'overwrite' determines if it should overwrite currently existing files
    in folders if filenames clash.
    Returns the destination."""

    file = getattr(fl, mod)
    if dst is None:
        dst = var.BOOTLEG_TEMP + mod

    try:
        if range is None:
            FindFile(file)
        else: # explicit override of the range function - yay __builtins__ :D
            for num in __builtins__.range(*range):
                FindFile(file.format(num))
        log.logger("PARS_INSTALLING", format=[mod])
        ExtractFile(file, None, pw)
        CopyFolder(var.BOOTLEG_TEMP + file, dst, overwrite)
        log.logger("PARS_COMPLETED", format=[mod])
    except FileNotFoundError:
        CallSkipMod(file)
    return dst

def ExtractFolder(path):
    """ExtractFolder(path)

    Extracts all the archives from a folder into that same folder.
    Returns a tuple of all the resulting folders' names."""

    if not path.endswith(("/", "\\")):
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
        p, f = GetFile(dir)
        if f.endswith(("/", "\\")):
            f = f[:-1]
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

def CopyFolder(src, dst, overwrite=True):
    """CopyFolder(src, dst, overwrite=True)

    Copies the content of 'src' into 'dst'.
    The destination may or may not exist.
    The 'overwrite' parameter will tell the function whether to overwrite files.
    This supports nested folders.
    Always returns 0."""

    if not src.endswith(("/", "\\")):
        src = src + "\\"
    if not dst.endswith(("/", "\\")):
        dst = dst + "\\"
    if not os.path.isdir(dst):
        os.mkdir(dst)

    for file in os.listdir(src):
        if not overwrite and os.path.exists(dst + file):
            continue
        if os.path.isfile(src + file):
            shutil.copy(src + file, dst + file)
        elif os.path.isdir(src + file):
            CopyFolder(src + file, dst + file, overwrite=overwrite)
    return 0

def CopyFile(path, file, new):
    """CopyFile(path, file, new)

    Creates of copy of 'file' with name 'new' in 'path'.
    Always returns 0."""

    if not path.endswith(("/", "\\")):
        path = path + "\\"

    shutil.copy(path + file, path + new)
    return 0

def DeleteFile(*path):
    """DeleteFile(*path)

    Deletes all files and folders given.
    Always returns 0."""

    for line in path:
        if os.path.isdir(line):
            shutil.rmtree(line)
        if os.path.isfile(line):
            os.remove(line)

    return 0

def RenameFile(path, org, new):
    """RenameFile(path, org, new)

    Renames item x of 'org' to item x of 'new' in path.
    Returns 0 if all items could be renamed.
    Returns more than 0 if there were more items in 'org' than 'new'
    Returns less than 0 if there were more items in 'new' than 'org'"""

    cont = zip(org, new)
    if not path.endswith(("/", "\\")):
        path = path + "\\"
    for file in cont:
        if os.path.isfile(path + file[0]):
            os.rename(path + file[0], path + file[1])

    return len(org) - len(new)

def AttribFile(file, attr="-R -S -H -I", *params):
    """AttribFile(file, attr="-R -S -H -I", *params)

    Sets Windows file and folders attributes.
    Default attribute change is to remove all unwanted attributes.
    Parameters are optional, it's mainly to touch folders as well.
    Returns 0 if it completed successfully."""

    params = " ".join(params).split() # handle tuples and multispaced items
    if isinstance(attr, (tuple, list, set)):
        attr = " ".join(attr)
    lines = attr.split() + [file] + params
    attrib = subprocess.Popen(["C:\\Windows\\System32\\attrib.exe"] + lines)
    attrib.communicate()
    return attrib.returncode

def StripFolder(path):
    """StripFolder(path)

    Brings all files within all subfolders to the root ('path').
    Deletes all subfolders of the main path.
    Returns a tuple of all the subfolders that were copied over."""

    if not path.endswith(("/", "\\")):
        path = path + "\\"
    folders = [path]
    allf = []
    while folders:
        folder = folders.pop(0)
        allf.append(folder)
        for lister in os.listdir(folder):
            if os.path.isdir(folder + lister):
                folders.append(folder + lister + "\\")
            elif not path == folder:
                CopyFolder(folder, path)
                shutil.rmtree(folder)

    return tuple(allf)

def CallSkipMod(mod):
    """CallSkipMod(mod)

    Prints a missing mod warning using 'mod' as the missing file.
    Always returns 0."""

    if len(var.MOD_LOCATION) == 1:
        iner = "ONE_IN"
    else:
        iner = "MULT_IN_ONE"
    file = getattr(fl, mod)
    if "{0}" in file:
        file = file.format(1) # make sure it does say *something*
    log.logger("PARS_SKIP", format=[mod, file, iner, "', '".join(var.MOD_LOCATION)])
    return 0
