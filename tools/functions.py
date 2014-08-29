from tools import constants as con
from tools import variables as var
from tools import parsables as par
import config

def initialize(): # initialize variables on startup and/or retry
    var.INITIALIZE = True
    var.USED_HELP = False
    var.FATAL_ERROR = False
    var.PARSABLE_SETTINGS = [name for name in par.__dict__ if name.isupper()]
    var.EMPTY_SETTINGS = []

def config_into_var():
    for parsable in var.PARSABLE_SETTINGS:
        parsarg = getattr(config, parsable)
        setattr(var, parsable, parsarg)

def parse_settings(input):
    for param in input:
        if param[0] == con.USER_VAR: # setting is an actual user setting
            for parsable in var.PARSABLE_SETTINGS:
                if param[1] == getattr(con, parsable):
                    setattr(var, parsable, param[2:])

def chk_empty_settings():
    var.EMPTY_SETTINGS = []
    for parsable in var.PARSABLE_SETTINGS:
        if not getattr(var, parsable):
            var.EMPTY_SETTINGS.append(parsable)

def use_defaults(empty):
    for parsable in var.PARSABLE_SETTINGS:
        if parsable not in empty:
            continue
        parsarg = getattr(con, parsable)
        setattr(var, parsable, parsarg)

def settings_to_int():
    for parsable in var.PARSABLE_SETTINGS:
        parsarg = getattr(var, parsable)
        setattr(var, parsable, int(parsarg))