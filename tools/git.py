# This is the handler for all git-related commands
# Automatic checker and update also use this

from tools import constants as con
from tools import variables as var
from tools import log as _log
import subprocess

def parse(args, name):
    if args != list(args):
        args = [args]
    if len(args) < 2:
        args.append(name)
    if args[1] != name:
        argsp = [args[0], name]
        argsp.extend(args[1:])
        args = list(argsp)
    return args

def pull(args, silent=False):
    args = parse(args, "pull")
    args.append(con.PROCESS_CODE)
    args.append(con.BRANCH_NAME)
    return do(args, silent)

def diff(args, silent=False):
    args = parse(args, "diff")
    return do(args, silent)

def check(args, silent=False):
    args = parse(args, "status")
    do([args[0], "fetch", con.PROCESS_CODE], silent=True, quiet=True)
    checker = do(args, silent, needout=True)
    if checker:
        if len(checker) > 2:
            return True
        if len(checker) == 1: # fatal: not a git repo
            return None
    return False

def diff_get(args, silent=False):
    args = parse(args, "status")
    checker = do(args, silent, needout=True)
    lines = []
    if checker:
        for line in checker:
            if line[:11] == b"#\tmodified:":
                lines.append(line.decode("utf-8")[14:])
    return lines

def log(args, sha, silent=False):
    args = parse(args, "log")
    args.extend(["--oneline", sha + ".."])
    return do(args, silent, needout=True)

def rev(args, silent=False):
    args = parse(args, "rev-parse")[:2]
    args.append("HEAD")
    return do(args, silent, needout=True)[0].decode("utf-8")

def clone(args, silent=False): # use only if not a git repo
    args = parse(args, "clone")
    do(args, silent)

def do(args, silent=False, quiet=False, needout=False):
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    ret = child.returncode

    lines = []
    for line in (out + err).splitlines():
        _log.logger(line.decode('utf-8'), type="git", display=not silent, write=var.ALLOW_RUN, check=False) # Make sure it doesn't write anything if it stops running to prevent orphan log file
        lines.append(line)
    if not (out + err):
        return False
    if needout:
        return lines

    if ret != 0 and len(args) > 1:
        if ret < 0:
            cause = 'SIGNAL'
        else:
            cause = 'STATUS'

        if not quiet:
            _log.logger("PROCESS_EXITED", format=[args[0], cause, abs(ret)])
    else:
        return True
    return ret
