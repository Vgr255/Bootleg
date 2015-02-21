__all__ = ["logger", "multiple", "help", "doc", "parser"]

from tools import variables as var
from tools import constants as con
from tools import translate as tr
import datetime
import time
import os

def logger(*output, logtype="", type="normal", display=True, write=True, checker=True, splitter="\n", form=None, formo=None, formt=None, split=True, **params):
    """Logs everything to console and/or file. Always use this."""
    output = get(output, splitter)
    timestamp = get_timestamp()
    logall = None
    toget = ""
    if form is None:
        form = []
    if form and form != list(form):
        form = [form]
    toform = list(form)
    toforml = list(form)
    if formo and formt:
        toform = list(formo)
        toforml = list(formt)
    if "\n" in output:
        indx = output.index("\n")
        toget = output[indx+1:]
        output = output[:indx]

    if logtype:
        for typed in con.LOGGERS.keys():
            if con.LOGGERS[typed] == logtype:
                type = typed
                break
    if not type:
        type = "normal"

    trout = output
    if output.isupper() and type not in con.IGNORE_CHECK and checker:
        trout, output, toform, toforml = translater(output, type, form, formo, formt)
    pout = trout # Does a pouting trout pout a trout?

    if type in con.IGNORE_TIMESTAMP:
        timestamp = ""
    if var.LOG_EVERYTHING or var.DEV_LOG:
        logall = con.LOGGERS["all"]
    if not logtype:
        if type not in con.LOGGERS.keys():
            type = "normal"
        logtype = con.LOGGERS[type]

    write, display = getview(write, display)

    if len(pout) > 80 and display and type not in con.IGNORE_SPLITTER and split:
        pout = line_splitter(pout)

    if display:
        print(pout)
    if write:
        trans = var.LANGUAGE != "English" and type not in con.IGNORE_TRANSLATE
        alines = [x for x in con.LOGGERS if not x in con.IGNORE_MIXED]
        gett = [logtype]
        if logall: gett.append(logall)
        for x in gett:
            logfile = getattr(var, x + "_FILE")
            log_ext = getattr(var, x + "_EXT")
            file = logfile + "." + log_ext
            filel = con.LANGUAGES[var.LANGUAGE][0] + "_" + file
            newfile = os.path.isfile(file)
            newfilel = os.path.isfile(filel)
            atypes = lambda out: "type.{0} - {1}".format(type, out)
            output = output + "\n"
            trout = trout + "\n"
            with open(file, "a", encoding="utf-8") as f:
                while "\n" in output:
                    writer = output[:output.index("\n")]
                    if x == logall:
                        if type in alines:
                            f.write("{0}{1}{2}\n".format("\n\n" if (not var.INITIALIZED or var.RETRY) and type not in
                                con.IGNORE_NEWLINE and newfile and var.NEWFILE_ALL else "", timestamp, atypes(writer)))
                            var.NEWFILE_ALL = False
                    else: # Normal
                        f.write("{0}{1}{2}\n".format("\n\n" if (not var.INITIALIZED or var.RETRY) and
                            type not in con.IGNORE_NEWLINE and newfile and var.NEWFILE_NOR else "", timestamp, writer))
                        var.NEWFILE_NOR = False
                    output = output[output.index("\n")+1:]
            if trans:
                with open(filel, "a", encoding="utf-8") as fl:
                    while "\n" in trout:
                        writer = trout[:trout.index("\n")]
                        if x == logall:
                            if type in alines:
                                fl.write("{0}{1}{2}\n".format("\n\n" if (not var.INITIALIZED or var.RETRY) and type not in
                                    con.IGNORE_NEWLINE and newfilel and var.NEWFILE_TRA else "", timestamp, atypes(writer)))
                                var.NEWFILE_TRA = False
                        else:
                            fl.write("{0}{1}{2}\n".format("\n\n" if (not var.INITIALIZED or var.RETRY) and
                                type not in con.IGNORE_NEWLINE and newfilel and var.NEWFILE_TRO else "", timestamp, writer))
                            var.NEWFILE_TRO = False
                        trout = trout[trout.index("\n")+1:]
    if toget:
        logger(toget, logtype=logtype, display=display, write=write, checker=checker, formo=toform, formt=toforml, split=split) # don't iterate again if already translated

def multiple(*output, types=[], display=True, write=True, checker=True, splitter="\n", form=[], split=True):
    """Logs one or more lines to multiple files."""
    output = get(output, splitter)
    if "all" in types:
        log_it = []
        for logged in con.LOGGERS.keys():
            if logged in con.IGNORE_ALL:
                continue
            if con.LOGGERS[logged] not in log_it:
                log_it.append(con.LOGGERS[logged])
        for l in log_it:
            logger(output, logtype=l, display=display, write=write, checker=checker, splitter=splitter, form=form, split=split)
            display = False # Don't want to needlessly display the same message multiple times
    elif types:
        for t in types:
            logger(output, type=t, display=display, write=write, checker=checker, splitter=splitter, form=form, split=split)
            display = False
    else: # no type
        logger(output, display=display, write=write, checker=checker, splitter=splitter, form=form, split=split)

def help(*output, type="help", write=False, display=True, checker=True, splitter="\n", form=[], split=True):
    """Explicit way to only print to screen."""
    output = get(output, splitter)
    logger(output, type=type, write=write, display=display, checker=checker, splitter=splitter, form=form, split=split)

def doc(output, type="docstring", write=False, display=True, form=[], split=True):
    """Prints a docstring using proper formatting."""
    newlined = False
    newdone = False
    indent = 0
    lines = output.split("\n")
    newlines = []
    for line in lines:
        if not newlined and not line.replace(" ", ""): # First empty line
            newlined = True
        if newlined and not newdone and line.replace(" ", ""):
            newdone = True
            for char in line:
                if char == " ":
                    indent += 1
                else:
                    break
        if indent:
            if line and line[:indent+1] == " " * indent:
                line = line[indent:]
            elif line: # Not proper formatting, proper handling
                for char in line[:]:
                    if line[0] == " ":
                        line = line[1:]
                    else:
                        break
        newlines.append(line)

    logger(newlines, type=type, write=write, display=display, form=form, split=split)

def parser(setting):
    """Prints a setting prompt properly."""
    if not hasattr(var, setting) or not hasattr(tr, setting):
        raise ValueError(setting)
    trout, output, form, forml = translater("PARS_FIND_" + setting, "normal", (), (), ())
    getter = 1
    if setting in con.RANGE.keys():
        getter = con.RANGE[setting]
    var.FINDING = setting
    help("ENT_VALUE_BETWEEN", "", form=getter)
    msg = trout.split("\n")
    logger(output.split("\n"), type="normal", display=False)
    if getter > 1:
        help(msg.pop(0))
        help("NO_CHG")
        help("\n".join(msg))
    if getter == 1:
        help(msg[0], form=setting)
        help("CHC_NO")
        help("CHC_YES")
    help("", "DEF_TO_USE", form=getattr(var, setting))

def get(output, splitter):
    if len(output) == 1 and list(output[0]) == output[0]:
        output = output[0]
    if not output: # Called without any argument
        output = ['']
    msg = None
    for line in output:
        if msg is None:
            msg = line
        else:
            if line == "":
                line = "\n"
            msg += splitter + line
    return msg

def line_splitter(output):
    iter = 0
    iter2 = -1
    newout = ""
    while True:
        if output[-1] == " ":
            output = output[-1:]
        else:
            output = output + " "
            break
    while True:
        if len(output) <= 80:
            newout = newout + output
            break
        while " " in output[81:]:
            if iter >= 80:
                newout = newout + output[:iter2] + "\n"
                output = output[iter2+1:]
                iter = 0
                iter2 = -1
            if not output:
                break
            if iter < 80:
                iter2 = iter
                iter = output.index(" ", iter+1)
                if "\n" in output[:iter]:
                    if output.index("\n") < 81:
                        iter2 = output.index("\n")
        if iter2 >= 0 and iter >= 80:
            if newout:
                newout = newout + "\n"
            newout = newout + output[:iter2]
            output = output[iter2+1:]
    if not newout:
        return output
    return newout

def getview(write, display):
    if var.DEBUG_MODE or var.DEV_LOG or var.WRITE_EVERYTHING: # if there's an error I'll want every possible information. that's the way to go
        write = True
    if var.DEBUG_MODE or var.DISPLAY_EVERYTHING:
        display = True
    return write, display

def translater(output, type, form, formo, formt):
    forml = list(form)
    if not hasattr(tr, output):
        return output, output, list(form), list(form)
    newout = getattr(tr, output)
    outlang = "English" if type in con.IGNORE_TRANSLATE else var.LANGUAGE
    if not outlang in newout.keys():
        outlang = "English"
    trout = newout[outlang]
    output = newout["English"]
    iter = 0
    if formo and formt:
        form = list(formo)
        forml = list(formt)
    while True:
        if "{" + str(iter) + "}" in output: # output and trout should have the same amount of formats
            for i, writer in enumerate(form):
                if str(writer) == writer and writer.isupper() and hasattr(tr, writer): # to translate as well
                    forml[i] = getattr(tr, writer)[var.LANGUAGE]
                    form[i] = getattr(tr, writer)["English"]
            iter += 1
        else:
            trout = trout.format(*forml)
            output = output.format(*form)
            forml = forml[iter:]
            form = form[iter:]
            break
    return trout, output, list(form), list(forml)

def get_timestamp(use_utc=None, timestamp_format=None):
    """Returns a timestamp with timezone + offset from UTC."""
    if timestamp_format is None:
        timestamp_format = var.TIMESTAMP_FORMAT
    if use_utc is None:
        use_utc = var.USE_UTC
    if use_utc:
        tmf = datetime.datetime.utcnow().strftime(timestamp_format)
        return tmf.format(tzname="UTC", tzoffset="+0000").strip() + " "
    tmf = time.strftime(timestamp_format).strip() + " "
    tz = time.strftime("%Z")
    utctime = datetime.datetime.utcnow().strftime("%H")
    nowtime = datetime.datetime.now().strftime("%H")
    offset = "-" if int(utctime) > int(nowtime) else "+"
    offset += str(time.timezone // 36).zfill(4)
    return tmf.format(tzname=tz, tzoffset=offset).upper()
