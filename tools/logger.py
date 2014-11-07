from tools import variables as var
from tools import constants as con
from tools import translate as tr
import datetime
import os

def logger(*output, logtype="", type="normal", display=True, write=True, splitter="\n", form=[], formo=[], formt=[]): # logs everything to file and/or screen. always use this
    output = get(output, splitter)
    timestamp = str(datetime.datetime.now())
    timestamp = "[{0}] ({1}) ".format(timestamp[:10], timestamp[11:19])
    logall = None
    toget = ""
    if form and not form == list(form):
        form = [form]
    if "\n" in output:
        indx = output.index("\n")
        toget = output[indx+1:]
        output = output[:indx]

    if logtype:
        for typed in con.LOGGERS.keys():
            if con.LOGGERS[typed] == logtype:
                type = typed
    if not type:
        type = "normal"

    trout, output, toform, toforml = translater(output, type, form, formo, formt)

    if type in con.IGNORE_TIMESTAMP:
        timestamp = ""
    if var.LOG_EVERYTHING or var.DEV_LOG:
        logall = con.LOGGERS["all"]
    if not logtype:
        if type not in con.LOGGERS.keys():
            type = "normal"
        logtype = con.LOGGERS[type]

    write, display, file = getfile(write, display, logtype)

    newfile = not os.path.isfile(os.getcwd() + "/" + file)
    if display:
        print(trout)
    if write:
        f = open(os.getcwd() + "/" + file, "w" if newfile else "r+")
        f.seek(0, 2)
        if not var.LANGUAGE == "English" and type not in con.IGNORE_TRANSLATE:
            filel = con.LANGUAGES[var.LANGUAGE][0] + "_" + file
            newfilel = not os.path.isfile(os.getcwd() + "/" + filel)
            fl = open(os.getcwd() + "/" + filel, "w" if newfilel else "r+")
            fl.seek(0, 2)
        if type in con.IGNORE_NEWLINE:
            newfile = True
            newfilel = True
        if (not var.INITIALIZED or var.RETRY) and not newfile:
            f.write("\n\n" + timestamp + output + "\n")
        else:
            f.write(timestamp + output + "\n")
        if logall:
            outputa = "type.{0} - {1}".format(type, output)
            filea = getattr(var, logall + "_FILE") + "." + getattr(var, logall + "_EXT")
            fa = open(os.getcwd() + "/" + filea, "w" if var.NEWFILE_ALL else "r+")
            var.NEWFILE_ALL = False
            fa.seek(0, 2)
            alines = list(con.LOGGERS)

            for lang in alines:
                if lang in con.IGNORE_MIXED:
                    alines.remove(lang)
            if type in alines:
                if var.RETRY:
                    fa.write("\n\n" + timestamp + outputa + "\n")
                else:
                    fa.write(timestamp + outputa + "\n")
            fa.close()
            if not var.LANGUAGE == "English" and type not in con.IGNORE_MIXED:
                trouta = "type.{0} - {1}".format(type, trout)
                filet = con.LANGUAGES[var.LANGUAGE][0] + "_" + filea
                ft = open(os.getcwd() + "/" + filet, "w" if var.NEWFILE_TRA else "r+")
                var.NEWFILE_TRA = False
                ft.seek(0, 2)
                if var.RETRY:
                    ft.write("\n\n" + timestamp + trouta + "\n")
                else:
                    ft.write(timestamp + trouta + "\n")
                ft.close()
        if not var.LANGUAGE == "English" and type not in con.IGNORE_TRANSLATE:
            if (not var.INITIALIZED or var.RETRY) and not newfilel:
                fl.write("\n\n" + timestamp + trout + "\n")
            else:
                fl.write(timestamp + trout + "\n")
            fl.close()
        f.close()
    if toget:
        logger(toget, logtype=logtype, display=display, write=write, formo=toform, formt=toforml) # don't iterate again if already translated

def multiple(*output, types=[], display=True, write=True, splitter="\n", form=[]):
    output = get(output, splitter)
    if "all" in types:
        log_it = []
        for logged in con.LOGGERS.keys():
            if logged in con.IGNORE_ALL:
                continue
            if con.LOGGERS[logged] not in log_it:
                log_it.append(con.LOGGERS[logged])
        for l in log_it:
            logger(output, logtype=l, display=display, write=write, splitter=splitter, form=form)
    elif types:
        for t in types:
            logger(output, type=t, display=display, write=write, splitter=splitter, form=form)
    else: # no type
        logger(output, display=display, write=write, splitter=splitter, form=form)

def help(*output, type="help", write=False, display=True, splitter="\n", form=[]):
    output = get(output, splitter)
    logger(output, type=type, write=write, display=display, splitter=splitter, form=form)

def get(output, splitter):
    output = list(output)
    msg = None
    for line in output:
        if msg is None:
            msg = line
        else:
            msg += splitter + line
    return msg

def getfile(write, display, logtype):
    if var.DEBUG_MODE or var.DEV_LOG or var.WRITE_EVERYTHING: # if there's an error I'll want every possible information. that's the way to go
        write = True
    if var.DEBUG_MODE or var.DISPLAY_EVERYTHING:
        display = True
    logfile = getattr(var, logtype + "_FILE")
    log_ext = getattr(var, logtype + "_EXT")
    file = logfile + "." + log_ext
    return write, display, file

def translater(output, type, form, formo, formt):
    if output.isupper() and type not in con.IGNORE_CHECK: # to fetch in translate
        forml = list(form)
        newout = getattr(tr, output)
        outlang = "English" if type in con.IGNORE_TRANSLATE else var.LANGUAGE
        if not outlang in newout.keys():
            outlang = "English"
        trout = newout[outlang]
        output = newout["English"]
        iter = 0
        foring = 0
        while True:
            if "{" + str(iter) + "}" in output: # output and trout should have the same amount of formats
                for writer in form:
                    if writer.isupper() and hasattr(tr, writer): # to translate as well
                        forml[foring] = getattr(tr, writer)[var.LANGUAGE]
                        form[foring] = getattr(tr, writer)["English"]
                    foring += 1
                foring = 0
                iter += 1
            else:
                if formo and formt:
                    form = formo
                    forml = formt
                trout = trout.format(*forml)
                output = output.format(*form)
                forml = forml[iter:]
                form = form[iter:]
                break
        return trout, output, list(form), list(forml)
    return output, output, list(form), list(form) # no translation