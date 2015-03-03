# A Final Fantasy VII Mod Package and Installer
# Copyright (C) 2014-2015 Emanuel 'Vgr' Barry
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import traceback

try:
    from tools import constants as con
    from tools import variables as var
    from tools import functions as fn
    from tools import commands as cmd
    from tools import logger as log
    from tools import get
    from tools import git
except:
    print(traceback.format_exc())
    while True: pass
    quit()

def main():
    if not var.INITIALIZED or var.RETRY:
        fn.initialize()
    if var.ERROR:
        log.help("RES_RET", form=con.PROGRAM_NAME)
    if var.FATAL_ERROR or var.SYS_ERROR:
        fn.end_bootleg_early()
        return
    comm = var.COMMANDS
    commands = [x for x in comm if not comm[x].hidden and not comm[x].error and not x in comm[x].aliases]
    errcomms = [x for x in comm if comm[x].error and not comm[x].hidden and not x in comm[x].aliases]
    errcomm_ = [x for x in comm if comm[x].error]
    hidcomms = [x for x in comm if comm[x].hidden and not x in comm[x].aliases]
    allcomms = [x for x in comm if comm[x].parse]
    if var.ERROR:
        commands = errcomms
    if var.DEBUG_MODE or var.SHOW_HIDDEN_COMMANDS:
        commands.extend(hidcomms)
    totype = "ENT_CMD"
    formatter = []
    if var.PARSING:
        totype = "ENT_CHC"
    if var.NEED_RESTART or var.SILENT_RUN or var.REINSTALL or var.UNINSTALL:
        totype = ""
    if var.UPDATE_READY:
        totype = "ENT_UPD"
        formatter = ["YES", "NO"]
    if totype == "ENT_CMD":
        commands.sort()
        log.help("", "AVAIL_CMD", form=[", ".join(commands), "" if len(commands) == 1 else "PLURAL"])
    if totype:
        log.help("\n", totype, "", form=formatter)
    else: # nothing to print, either restarting after Git or silently running
        if var.SILENT_RUN:
            cmd.run("silent")
        if var.REINSTALL:
            cmd.run("reinstall")
        if var.UNINSTALL:
            cmd.run("uninstall")
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
    if var.ERROR and not command in errcomm_:
        log.help("NEED_RR")
    elif command in comm:
        comm[command](inp, params)
    else:
        fn.no_such_command(command)

while var.ALLOW_RUN:
    try:
        main()
    except KeyboardInterrupt:
        if var.ERROR:
            var.ALLOW_RUN = False
            log.logger("SIGTERM_END", display=False)
        else:
            log.logger("SIGTERM_WARN")
            var.ERROR = True
    except: # fallback catcher
        log.logger(traceback.format_exc(), type="traceback", display=var.DISPLAY_TRACEBACK)
        logname = con.LOGGERS["traceback"]
        if var.DEV_LOG or var.LOG_EVERYTHING:
            logname = con.LOGGERS["all"]
        logfile = getattr(var, logname + "_FILE")
        log_ext = getattr(var, logname + "_EXT")
        if not var.DISPLAY_TRACEBACK:
            log.logger("", "ERR_TO_REPORT", "PROVIDE_TRACE", form=[logfile, log_ext], type="error", write=False)
        var.ERROR = True
