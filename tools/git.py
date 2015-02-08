# This is the handler for all git-related commands
# Automatic checker and update also use this

from tools import constants as con
from tools import variables as var
from tools import logger as log
import subprocess

def parse(args, name):
    if not args == list(args):
        args = [args]
    if len(args) < 2:
        args.append(name)
    if not args[1] == name:
        argsp = [args[0], name]
        argsp.extend(args[1:])
        args = list(argsp)
    return args

def pull(args, silent=False):
    args = parse(args, "pull")
    if not len(args) == 4:
        if var.USE_GIT_ORIGIN:
            args = [args[0], "pull", "origin", var.GIT_BRANCH]
        elif var.USE_GIT_LINK:
            args = [args[0], "pull", con.PROCESS_CODE + ".git", var.GIT_BRANCH]
    if silent:
        return do(args, silent)
    do(args)

def diff(args, silent=False):
    args = parse(args, "diff")
    if silent:
        return do(args, silent)
    do(args)

def rev(args, silent=False):
    args = parse(args, "rev-parse")
    args.append("HEAD")
    if silent:
        return do(args, silent, needout=True)
    do(args)

def check(args, silent=False):
    args = parse(args, "status")
    do([args[0], "fetch", "origin"], silent=True)
    checker = do(args, silent, needout=True)
    if checker:
        if checker[-1:] == b"nothing to commit (working directory clean)":
            return False
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

def clone(args, silent=False): # use only if not a git repo
    args = parse(args, "clone")
    do(args, silent)

def do(args, silent=False, needout=False):
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = child.communicate()
    ret = child.returncode

    lines = []
    for line in (out + err).splitlines():
        log.logger(line.decode('utf-8'), type="git", display=not silent, write=var.ALLOW_RUN, checker=False) # Make sure it doesn't write anything if it stops running to prevent orphan log file
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

        log.logger("PROCESS_EXITED", form=[args[0], cause, abs(ret)])
    else:
        return True
    return ret
