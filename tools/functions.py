from tools import constants as con
from tools import variables as var
from tools import parsables as par
from tools import process as pro
import config

def initialize(): # initialize variables on startup and/or retry
    var.INITIALIZE = True
    var.USED_HELP = False
    var.FATAL_ERROR = False

def config_into_var():
    parsable_settings = [name for name in par.__dict__ if name.isupper()]
    for parsable in parsable_settings:
        parsarg = getattr(config, parsable)
        setattr(var, parsable, parsarg)

def parse_settings(input):
    parsable_settings = [name for name in par.__dict__ if name.isupper()]
    for param in input:
        if param[0] == con.USER_VAR: # setting is an actual user setting
            for parsable in parsable_settings:
                if param[1] == getattr(con, parsable):
                    setattr(var, parsable, param[2:])

def chk_empty_settings():
    parsable_settings = [name for name in par.__dict__ if name.isupper()]
    empty_settings = []
    for parsable in parsable_settings:
        if not getattr(var, parsable):
            empty_settings.append(parsable)
    if not empty_settings:
        return
    else: # at least one variable is blank
        use_defaults(empty_settings)

def use_defaults(empty):
    parsable_settings = [name for name in par.__dict__ if name.isupper()]
    for parsable in parsable_settings:
        if parsable not in empty:
            continue
        parsarg = getattr(con, parsable)
        setattr(var, parsable, parsarg)

def get_help(help=""):
    # todo - help="" is to get help for a specific parameter