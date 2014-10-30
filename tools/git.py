# This is the handler for all git-related commands
# Automatic checker and update also use this

from tools import constants as con
from tools import variables as var
from tools import logger as log
import subprocess

def __parse__(args, name):
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
    args = __parse__(args, "pull")
    if var.USE_GIT_ORIGIN:
        args = [args[0], "pull", "origin", var.GIT_BRANCH]
    elif var.USE_GIT_LINK:
        args = [args[0], "pull", con.PROCESS_CODE + ".git", var.GIT_BRANCH]
    if silent:
        return do(args, silent)
    do(args)

def diff(args, silent=False):
    args = __parse__(args, "diff")
    if silent:
        return do(args, silent)
    do(args)

def check(args, silent=False):
    args = __parse__(args, "status")
    checker = do(args, silent, needout=True)
    if len(checker) > 2:
        return True
    return False

def do(args, silent=False, needout=False):
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = child.communicate()
    ret = child.returncode

    lines = []
    for line in (out + err).splitlines():
        log.logger(line.decode('utf-8'), type="git", display=not silent)
        lines.append(line)
    if not out:
        return False
    if needout:
        return lines

    if ret != 0:
        if ret < 0:
            cause = 'signal'
        else:
            cause = 'status'

        log.logger("PROCESS_EXITED", form=[args, cause, abs(ret)])
    else:
        return True
    return ret