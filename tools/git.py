# This is the handler for all git-related commands
# Automatic checker and update also use this

from tools import constants as con
from tools import variables as var
from tools import logger as log
import subprocess

def pull(args):
    if var.USE_GIT_ORIGIN:
        args = [args[0], "pull", "origin", var.GIT_BRANCH]
    elif var.USE_GIT_LINK:
        args = [args[0], "pull", con.PROCESS_CODE + ".git", var.GIT_BRANCH]
    do(args)

def diff(args):
    do(args) # mainly a placeholder for now

def do(args):
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = child.communicate()
    ret = child.returncode

    for line in (out + err).splitlines():
        log.logger(line.decode('utf-8'), type="debug")

    if ret != 0:
        if ret < 0:
            cause = 'signal'
        else:
            cause = 'status'

        log.logger("PROCESS_EXITED", form=[args, cause, abs(ret)])