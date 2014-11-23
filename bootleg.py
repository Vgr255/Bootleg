# Bootleg (2014) by Emanuel 'Vgr' Barry
# The developper of this software (hereafter refered to as "The Developper")
# allows for the use and redistribution of the present software and all its
# associated files (hereafter refered to as "The Software") free of charge. The
# user of the Software consents to the following if they use it in any way:
# - The Developper is not to be help responsible for any sort of damage,
#   physical, virtual or otherwise arising from the use of the Software.
# - Modification and redistribution, partial or total, of the Software is
#   allowed provided this notice is not altered in any way and the name of
#   the Developper appears in the first line of the present file.
# - The Developper is not entitled to anything towards any user of the Software.
# - As well as the present notice, the user needs to acknowledge the following
#   notice, contained in the following paragraph. Use of the present software
#   is an implicit consent to both the current and aforementioned notices.

# This software is provided "as is", in the hopes that it will be useful, but
# without any warranty of any kind, explicit or implicit. In no event is the
# Software Developper to be held accountable for any sort of damage, tort or
# otherwise, arising from the use of the present Software.

import traceback
import sys

from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import commands as cmd
from tools import logger as log
from tools import get
from tools import git

# Get custom exceptions for handling

from tools.exceptions import *

def main():
    if not var.INITIALIZED or var.RETRY:
        fn.initialize()
    if var.ERROR:
        log.help("RES_RET", form=con.PROGRAM_NAME)
    if var.FATAL_ERROR or var.SYS_ERROR:
        fn.end_bootleg_early()
        return
    commands = []
    commands.extend(con.COMMANDS)
    if var.SHOW_HIDDEN_COMMANDS:
        commands.extend(con.HIDDEN_COMMANDS)
        commands.extend(con.ERROR_COMMANDS)
    if var.DEBUG_MODE:
        commands.extend(con.DEBUG_COMMANDS)
    totype = "ENT_CMD"
    form = []
    if var.PARSING:
        totype = "ENT_CHC"
    if var.NEED_RESTART or var.SILENT_RUN:
        totype = ""
    if var.UPDATE_READY:
        totype = "ENT_UPD"
        form = ["YES", "NO"]
    if totype == "ENT_CMD":
        log.help("", "AVAIL_CMD", form=[", ".join(commands), "" if len(commands) == 1 else "PLURAL"])
    if totype:
        log.help("\n", totype, "", form=form)
    else: # nothing to print, either restarting after Git or silently running
        if var.SILENT_RUN:
            cmd.run("silent")
            return
    if var.NEED_RESTART:
        get.pause()
        cmd.restart()
        return
    inp = input(con.INPUT_PREFIX).strip()
    log.logger(con.INPUT_PREFIX, inp, type="input", display=False, splitter="", checker=False)
    if var.PARSING:
        fn.parser(inp)
        return
    if var.UPDATE_READY:
        if get.bool(inp) is None:
            log.logger("ERR_INVALID_BOOL", form=["YES", "NO"])
            return
        if get.bool(inp):
            log.logger("", "WAIT_UPD", "")
            if git.pull(var.GIT_LOCATION, silent=True):
                log.logger("SUCCESS_UPD", "REST_FOR_CHG")
                var.NEED_RESTART = True
            else:
                log.logger("FAILED_UPD", "DIS_AUTO_UPD", form=con.PROGRAM_NAME)
        var.UPDATE_READY = False
        return
    inp1 = inp.lower().split()
    if not inp:
        log.help("NO_CMD_ENT")
        return
    command = inp1[0]
    params = inp1[1:]
    if var.ERROR and command not in con.ERROR_COMMANDS:
        log.help("NEED_RR")
    else:
        if hasattr(cmd, command) and command not in cmd.__ignore__:
            getattr(cmd, command)(inp, params)
        else: # no such command
            fn.no_such_command(command)

while var.ALLOW_RUN:
    try:
        main()
    except CustomBootException as Catcher:
        log.multiple("Exception: {0}".format(Catcher.__class__.__name__), ":".join(Catcher.args), display=False, checker=False, types=["normal", "error", "debug"])
        raise # We're catching and logging custom exceptions, but we want them to be handled if needed
    except KeyboardInterrupt:
        if var.ERROR:
            var.ALLOW_RUN = False
            log.logger("SIGTERM_END", display=False)
        else:
            log.logger("SIGTERM_WARN")
            var.ERROR = True
    except PresetAlreadyImported:
        log.logger("PRESET_ALIMPORTED", form=[var.PRESET, con.PROGRAM_NAME])
    except Exception: # Don't want to catch everything
        if traceback.format_exc(): # if there's a traceback, let's have it
            log.logger("", type="traceback", write=False)
            log.logger(traceback.format_exc(), type="traceback", display=False)
            logname = con.LOGGERS["traceback"]
            if var.DEV_LOG or var.LOG_EVERYTHING:
                logname = con.LOGGERS["all"]
            logfile = getattr(var, logname + "_FILE")
            log_ext = getattr(var, logname + "_EXT")
            log.logger("ERR_TO_REPORT", "PROVIDE_TRACE", form=[logfile, log_ext], type="error", write=False)
        if str(sys.exc_info()):
            log.logger(str(sys.exc_info()), type="error", display=False) # log which exception occured
        var.ERROR = True