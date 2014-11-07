# Whenever typing 'help [stuff]', this is called
# If there are no arguments, get_help() is called
# If there are arguments, the according function is called
# If no function matches, 'unhandled' is used
# Functions (except get_help()) may return either a string or a list

from tools import variables as var
from tools import constants as con
from tools.logger import help

unhandled = "HELP_NOT_FOUND"

def get_help(helping=""):
    helping = helping.lower()
    help("", "HELP_FILE_BOOT_CONF", form=con.PROGRAM_NAME)
    help("HELP_FILE_NEW_HELP", "")
    if helping and helping not in (con.POSSIBLE_HELP + con.HIDDEN_HELP + var.USERS + var.COMMANDS):
        help("HELP_NOT_VALID_HELP", form=helping)
        if con.POSSIBLE_HELP:
            help("HELP_POS_HELP_TOPICS", form=[", ".join(con.POSSIBLE_HELP), "PLURAL" if len(con.POSSIBLE_HELP) > 1 else ""])
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                help("HELP_HIDDEN_COMMANDS", form=[", ".join(con.HIDDEN_HELP), "PLURAL" if len(con.HIDDEN_HELP) > 1 else ""])
            help("HELP_USE_ITEM_SPEC")
            return False
    elif not helping:
        if con.CURRENT_RELEASE:
            help("HELP_BOOT_CUR_REL", form=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
        if con.RELEASE_INFO and con.BUILD_INFO:
            help(con.BUILD_INFO, con.VERSION_INFO, con.RELEASE_INFO)
        if con.FIRST_DEV:
            help("HELP_FIRST_DEV", form=[", ".join(con.FIRST_DEV), "PLURAL" if len(con.FIRST_DEV) >1 else ""])
        if con.USER_HELP:
            help("HELP_USER_HELPING", form=["PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)])
        if con.CODERS:
            help("HELP_CODERS", form=["PLURAL" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)])
            if con.GUI_CODERS:
                help("HELP_GUI_CODERS", form=", ".join(con.GUI_CODERS))
            if con.PROCESS_CODERS:
                help("HELP_PROCESS_CODERS", form=[", ".join(con.PROCESS_CODERS), con.PROGRAM_NAME])
        if con.GAME_CONV:
            help("HELP_GAME_CONV", form=", ".join(con.GAME_CONV))
        if con.BETA_TESTERS:
            help("HELP_BETA_TESTERS", form=["PLURAL" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)])
        if con.TRANSLATORS:
            help("HELP_TRANSLATORS", form=["PLURAL" if len(con.TRANSLATORS) > 1 else "", ", ".join(con.TRANSLATORS)])
            if con.FRENCH_TRANSLATORS:
                help("HELP_FRENCH_TRANSLATORS", form=["PLURAL" if len(con.FRENCH_TRANSLATORS) > 1 else "", ", ".join(con.FRENCH_TRANSLATORS)])
        if con.OTHER_SUPPORT:
            help("HELP_OTHER_SUPPORT", form=["PLURAL" if len(con.OTHER_SUPPORT) > 1 else "", ", ".join(con.OTHER_SUPPORT)])
        if con.SPECIAL_THANKS:
            help("HELP_SPECIAL_THANKS", form=", ".join(con.SPECIAL_THANKS))
        if con.EXT_HELP:
            help("HELP_EXT_HELP", form=["PLURAL" if len(con.EXT_HELP) > 1 else "", ", ".join(con.EXT_HELP)])
        if con.EMAIL:
            help("HELP_EMAIL", form=[con.EMAIL, con.PROGRAM_NAME])
        if con.POSSIBLE_HELP:
            help("", "HELP_POSSIBLE_HELP", form=[", ".join(con.POSSIBLE_HELP), "PLURAL" if len(con.POSSIBLE_HELP) > 1 else ""])
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                help("HELP_HIDDEN_HELP", form=[", ".join(con.HIDDEN_HELP), "PLURAL" if len(con.HIDDEN_HELP) > 1 else ""])
            help("HELP_VIEW_SPEC_TOP", "HELP_VIEW_SPEC_USR", "HELP_VIEW_SPEC_CMD")
        return False
    return True

# Various help topics

def programming():
    msg = "The current version of {0} is coded in Python 3".format(con.PROGRAM_NAME)
    if con.PROCESS_CODERS:
        msg = msg + " by {0}".format(", ".join(con.PROCESS_CODERS))
    msg = msg + ".\nThe Graphical User Interface is coded in C#"
    if con.GUI_CODERS:
        msg = msg + " by {0}".format(", ".join(con.GUI_CODERS))
    return msg + "."

def code():
    msg = "The {0}{1} code is completely open-source".format(con.CURRENT_RELEASE + " ", con.PROGRAM_NAME)
    if con.PROCESS_CODE:
        msg = msg + ", and can be viewed at \n{0}".format(con.PROCESS_CODE)
    msg = msg + "."
    return msg

def support():
    msg = "You can request help by going on the forums"
    if con.EMAIL:
        msg = msg + " or send an email to {0}".format(con.EMAIL)
    if con.USER_HELP:
        msg = msg + "; {0} {1} the official helper{2}".format(", ".join(con.USER_HELP), "PLUR_ARE" if len(con.USER_HELP) > 1 else "SING_IS", "PLURAL" if len(con.USER_HELP) > 1 else "")
    msg = msg + "."
    return msg

def commands():
    msg = "There are no available commands."
    if con.COMMANDS:
        msg = "Available command{1}: {0}.".format(", ".join(con.COMMANDS), "PLURAL" if len(con.COMMANDS) > 1 else "")
    if (con.HIDDEN_COMMANDS and var.DEBUG_MODE) or (con.HIDDEN_COMMANDS and var.SHOW_HIDDEN_COMMANDS):
        msg = msg + "\nHidden command{1}: {0}.".format(", ".join(con.HIDDEN_COMMANDS), "PLURAL" if len(con.HIDDEN_COMMANDS) > 1 else "")
    return msg

def users():
    msg = "There are no users."
    if var.USERS:
        msg = "Users with or without direct link to {0}: {1}".format(con.PROGRAM_NAME, ", ".join(var.USERS))

# Users are down here

def pitbrat():
    return ["PitBrat started Bootleg as a personal project.",
            "After a while, he decided to release it for the public to use.",
            "After 040's release, life took over and he couldn't work on Bootleg anymore."]

def eq2alyza():
    return ["EQ2Alyza made Tifa's Bootleg Tutorial, which significantly helped users.",
            "She helped many users to troubleshoot various issues."]

def vgr():
    return ["Vgr joined the development of Bootleg not long after it became public.",
            "He did a lot of debugging and beta-testing of many versions.",
            "He also provides user support for Bootleg.", "",
            "After PitBrat left the scene, he decided to give a new life to Bootleg.",
            "He converted the old and buggy code in Python 3 and made it open-source.",
            "He is so far the only Bootleg programmer."]

# Commands are down here

def help():
    return ["The help command is used to display various information.",
            "This is what you're currently viewing."]

def run():
    return "Use this command to run the Bootleg process."