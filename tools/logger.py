__doc__ = """
- Beginning of documentation -

Section 1 - Introduction

This 'logger' module was developped along with and for the Bootleg Mod
Configurator for Final Fantasy VII by Vgr. Due to its versatility, it can be
reused in other projects; this documentation is here to help other programmers
understand better what's going on in this code, should they want to use it.

Section 1.1 - Index

  Section 1      :Introduction
  + Section 1.1  :Index
  + Section 1.2  :Module definition
  Section 2      :Function documentation - logger()
  + Section 2.1  :Calling the function
  + Section 2.2  :List of positional arguments
  + Section 2.3  :In-depth documentation - Step-by-step explanation
  Section 3      :Function documentation - multiple()
  + Section 3.1  :Calling the function
  + Section 3.2  :List of positional arguments
  + Section 3.3  :In-depth documentation - Step-by-step explanation
  Section 4      :Function documentation - help()
  + Section 4.1  :Calling the function
  + Section 4.2  :List of positional arguments
  Section 5      :Conclusion
  + Section 5.1  :Credits
  + Section 5.2  :Documentation changelog

Section 1.2 - Module definition

This logger module (and more specifically, the logger() function) is used to
perform all operations to print and log various information. With various
parameters and variables, it can be fully customized to perform differing
operations based on the conditions met.

Section 2 - Function documentation: logger()

The logger() function is the core of this module, handling many operations.
It can print a string to the console or write it to a maximum of 4 files,
as well as use the proper translation for every line (provided by the module
'translate' in the 'tools' package).

Section 2.1 - Calling the function

The logger() function can be fed an arbitrary number of arguments.
Every unnamed argument not following a named argument is part of the output.
Depending on positional named arguments, it can perform a few things.

Positional named arguments can be called with name=value in the function call.
They can be called in any order, and any or all of them can be omitted without
any issue, except for the first argument, output.

Each parameter has a default value.
The default value will be used if the argument is not specified.

Section 2.2 - List of positional arguments

'output'     :A string or strings to print and/or write, depending on the
              positional named arguments.

Default      :None - This parameter is required.

'logtype'    :Raw logging type, which you should not use. It is called
              internally by some functions as a more direct approach.
              If this setting is set, it will override the value of 'type'.

Default      :"" - Empty string

'type'       :Use that to distinguish between which file to write to.
              It is defined in the constants module, more specifically
              the 'LOGGERS' dictionary. For each type is associated a
              logging type, which may be used for one or more type(s).

Default      :"normal"

'display'    :Parameter to determine whether the output should be printed to
              the screen. The variables 'DEBUG_MODE' or 'DISPLAY_EVERYTHING',
              if set to True, will override this parameter and set it to True.

Default      :True

'write'      :This parameter determines whether the output should be written to
              a log file, defined by the 'logtype' parameter, or, if it is not
              defined, it will use the 'type' parameter's value. The variables
              'DEBUG_MODE', 'DEV_LOG' or 'WRITE_EVERYTHING' will override this
              parameter's value and set it to True.

Default      :True

'splitter'   :This is only useful if the number of unnamed parameters, fed in
              as the 'output' argument, is superior ro 1. If there are more
              than one line to output, the splitter will be used to separate
              those lines. The splitter argument can be "", which will simply
              concatenate the strings together.

Default      :"\\n" - Newline

'form'       :The form parameter is a derivation of the str.format() function.
              It is a list of strings to be added into the output, not unlike
              str.format(), using the same syntax (and later calling it). The
              strings contained in form carry over all lines in the output,
              which means that the fourth string can be the second line's
              first format, assuming the first line had three formats.

Default      :[] - Empty list

'formo'
'formt'      :These arguments should not ever be called directly. They are
              only used when logger() is called recursively, if there are more
              than one line. 'formo' contains the parsed format arguments for
              the original English language , while 'formt' contains the parsed
              format arguments for the translated version, which may also be
              English.

Default      :[] - Empty lists

Section 2.3 - In-depth description - Step-by-step explanation of the function

When called, logger() performs a number of checks before printing or writing
to a file. First, it formats the output using the 'splitter' argument to make
one single string containing all the lines. It then initializes some variables,
and checks for newlines ('\\n') to not print them at once, but in separate
instances. If the raw logging type is defined, it will override the 'type'
setting with the first matching type in the 'LOGGERS' dictionary constant.

The function will then perform translation according to the settings. The
translated line is the only one that will be printed, if the 'display' argument
is True. Before printing however, it checks if the length of the line exceeds
80 characters, which is the width of the python console. If it does, it will
split the line in two at the latest space before the 80-characters limit, and
prepend two spaces to the rest, which is stored in a variable for recursive
iteration. If the line beings by two spaces, it will remove them before
performing the checks, to prevent an endless loop on long lines.

Various checks are then done to clean up some variables. If the 'write'
argument is True, it will open various log files to write the lines. If the
process is being initialized or restarted, and if the log file already exists,
it will print two newlines in the file before starting to write the contents.
This is to make an easier distinction between each run; search the file for two
blank lines. It will also write to more than one files if the proper conditions
are met, such as: There is more than one language (translated output), one of
the variables 'DEV_LOG' or 'LOG_EVERYTHING' is True (logging everything in a
single file as well as their normal file), and if both those conditions are
True, it will write to a total of 4 files.

If there was more than one line, logger() calls itself recursively with the
lines in buffer to print and write them separately.

Section 3 - Function documentation: multiple()

The multiple() function is used to log one or more lines to more than just a
single file. It calls logger() for each type. If the 'types' list parameter is
empty, it will only log once using logger()'s default type. By logging to more
than one type, the function will also make sure to display the message only
once, unless 'DISPLAY_EVERYTHING' is set to True.

Section 3.1 - Calling the function

The multiple() function can be fed a number of arguments, which are similar or
identical to logger()'s arguments. These arguments are described below.

Section 3.2 - List of positional arguments

'output'     :Identical to logger()'s parameter of the same name; it contains
              a line or multiple lines to print and/or write.

Default      :None - This parameter is required.

'types'      :Similar to logger()'s 'type' parameter, except this argument
              requires a list to be fed in. The list can contain zero or more
              parameters, and 'all' can be used to log to every logging type
              found in the 'LOGGERS' constant and not in the 'IGNORE_ALL'
              constant.

Default      :[] - Empty list

'display'
'write'
'splitter'
'form'       :All of these parameters have the exact same purpose and calls
              than the parameters of the same names in logger().

Defaults:    :All identical to their logger() counterparts.

Section 3.3 - In-depth explanation - Step-by-step explanation

When called, multiple() will check if the parameter 'all' is present in the
'types' list. If it is, it will write the output to every logging type found
in the 'LOGGERS' constant and not in the 'IGNORE_ALL' constant. It will then
iterate through every type in the 'LOGGERS' constant, to append the logging
type in a list, ignoring those already in that list and the types present in
the 'IGNORE_ALL' constant. After this iteration is done, it will call logger()
for the first logging type, then set 'display' to False to prevent the same
line from printing multiple times on the screen. It will then loop through all
of the other types and call logger() for each of them, the display now being
set to False.

If 'all' is not a parameter of the 'types' list, it will check if any type is
present in the list. If so, it will iterate through every type without any
other sort of check, displaying only the first line. If there are no types
present, it will use logger()'s default value.

Section 4 - Function documentation: help()

The help() function is an easier way to display help lines to the user, and an
explicit way to only display a line. It indeed sets the 'write' parameter to
False by default, and 'type' to "help".

Section 4.1 - Calling the function

The help() function is basically an alias of the logger() function with the
same possibilities - its only difference is that it sets write to False by
default. It is mainly used in the 'help' module to display help lines to the
users, without writing such lines to log files.

Section 4.2 - List of positional arguments

'output'     :Identical to the logger() and multiple() counterparts.

Default      :None - This parameter is required.

'type'       :Identical to the logger() counterpart.

Default      :"help"

'display'    :Identical to the logger() and multiple() counterparts.

Default      :True

'write'      :Identical to the logger() and multiple() counterparts.

Default      :False

'splitter'   :Identical to the logger() and multiple() counterparts.

Default      :"\\n" - Newline

'form'       :Identical to the logger() and multiple() counterparts.

Default      :[] - Empty list

Section 5 - Conclusion

The logger module will probably see some changes happening in the future after
the initial writing of this documentation. If there are changes that affect
the information contained in this documentation by invalidating it, obsoleting
or otherwise, it will be updated to keep up-to-date with the functions. It is
however possible that the information

Section 5.1 - Credits

The entirety of the logger module, all its functions and the current
documentation, was written by Vgr. Nobody else currently participates in the
development of Bootleg.

Section 5.2 - Documentation changelog

November 9th and 10th, 2014 - Initial writing of the documentation
November 12th - Removed the lines() function and its matching documentation
              - Added notice regarding change to the way lines are split

- End of documentation -
"""

__all__ = ["logger", "multiple", "help", "lines"]

from tools import variables as var
from tools import constants as con
from tools import translate as tr
import datetime
import os

def logger(*output, logtype="", type="normal", display=True, write=True, splitter="\n", form=[], formo=[], formt=[]):
    """Logs everything to console and/or file. Always use this."""
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
                break
    if not type:
        type = "normal"

    trout, output, toform, toforml = translater(output, type, form, formo, formt)
    pout = trout # Does a pouting trout pout a trout?
    if len(pout) > 80:
        pout, toget = line_splitter(pout, toget)

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
        print(pout)
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
            logger(output, logtype=l, display=display, write=write, splitter=splitter, form=form)
            display = False # Don't want to needlessly display the same message multiple times
    elif types:
        for t in types:
            logger(output, type=t, display=display, write=write, splitter=splitter, form=form)
            display = False
    else: # no type
        logger(output, display=display, write=write, splitter=splitter, form=form)

def help(*output, type="help", write=False, display=True, splitter="\n", form=[]):
    """Explicit way to only print to screen."""
    output = get(output, splitter)
    logger(output, type=type, write=write, display=display, splitter=splitter, form=form)

def get(output, splitter):
    output = list(output)
    msg = None
    for line in output:
        if msg is None:
            msg = line
        else:
            if line == "":
                line = "\n"
            msg += splitter + line
    return msg

def line_splitter(output, toget):
    iter = 0
    iter2 = iter
    if output[:2] == "  ": # already iterated
        output = output[2:]
    while " " in output[iter+1:]:
        if iter >= 80:
            break
        if iter < 80:
            iter2 = iter
            iter = output.index(" ", iter+1)
    toget = "  " + output[iter2+1:] + "\n" + toget
    output = output[:iter2]
    return output, toget

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
        if formo and formt:
            form = list(formo)
            forml = list(formt)
        while True:
            if "{" + str(iter) + "}" in output: # output and trout should have the same amount of formats
                for writer in form:
                    if str(writer) == writer and writer.isupper() and hasattr(tr, writer): # to translate as well
                        forml[foring] = getattr(tr, writer)[var.LANGUAGE]
                        form[foring] = getattr(tr, writer)["English"]
                    foring += 1
                foring = 0
                iter += 1
            else:
                trout = trout.format(*forml)
                output = output.format(*form)
                forml = forml[iter:]
                form = form[iter:]
                break
        return trout, output, list(form), list(forml)
    return output, output, list(form), list(form) # no translation