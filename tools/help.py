from tools import variables as var
from tools import constants as con
from tools.functions import show_help

def get_help(helping=""):
    helping = helping.lower()
    show_help("        - Final Fantasy VII Bootleg Mod Configurator -")
    show_help("                         * Help file *")
    show_help("")
    if helping and helping not in con.POSSIBLE_HELP and helping not in con.HIDDEN_HELP:
        show_help("'{0}' is not a valid help topic.".format(helping))
        if con.POSSIBLE_HELP:
            show_help("Possible help topic{1}: {0}.".format(", ".join(con.POSSIBLE_HELP), "s" if len(con.POSSIBLE_HELP) > 1 else ""))
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                show_help("Hidden help command{1}: {0}.".format(", ".join(con.HIDDEN_HELP), "s" if len(con.HIDDEN_HELP) > 1 else ""))
            show_help("Use 'help <item>' to view a specific help.")
    elif not helping:
        if con.CURRENT_RELEASE:
            show_help("Bootleg - Final Fantasy VII Configurator - Version {0}".format(con.CURRENT_RELEASE))
        if con.RELEASE_INFO and con.BUILD_INFO:
            show_help(con.BUILD_INFO + " build " + con.RELEASE_INFO)
        if con.FIRST_DEV:
            show_help("First developper{1} and base idea: {0}.".format(", ".join(con.FIRST_DEV), "s" if len(con.FIRST_DEV) >1 else ""))
        if con.USER_HELP:
            show_help("User helper{0} and support team: {1}.".format("s" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)))
        if con.CODERS:
            show_help("Current active programmer{0} and developper{0}: {1}.".format("s" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)))
        if con.GUI_CODERS:
            show_help("Programming of the Graphical User Interface (GUI): {0}.".format(", ".join(con.GUI_CODERS)))
        if con.PROCESS_CODERS:
            show_help("Programming of the Bootleg process: {0}.".format(", ".join(con.PROCESS_CODERS)))
        if con.GAME_CONV:
            show_help("Game Converter developping and support: {0}".format(", ".join(con.GAME_CONV)))
        if con.BETA_TESTERS:
            show_help("{0} tester{1}: {2}.".format(con.BUILD_INFO, "s" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)))
        if con.SPECIAL_THANKS:
            show_help("Special thanks to {0}.".format(", ".join(con.SPECIAL_THANKS)))
        if con.EMAIL:
            show_help("Official Bootleg email for support and questions: {0}".format(con.EMAIL))
        if con.POSSIBLE_HELP:
            show_help("")
            show_help("Possible help topic{1}: {0}.".format(", ".join(con.POSSIBLE_HELP), "s" if len(con.POSSIBLE_HELP) > 1 else ""))
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                show_help("Hidden help command{1}: {0}.".format(", ".join(con.HIDDEN_HELP), "s" if len(con.HIDDEN_HELP) > 1 else ""))
            show_help("Use 'help <item>' to view a specific help.")
    elif helping == "programming":
        msg = "The current version of Bootleg is coded in Python 3.2"
        if con.PROCESS_CODERS:
            msg = msg + " by {0}".format(", ".join(con.PROCESS_CODERS))
        msg = msg + ".\nThe Graphical User Interface is coded in C#"
        if con.GUI_CODERS:
            msg = msg + " by {0}".format(", ".join(con.GUI_CODERS))
        show_help(msg + ".")
    elif helping == "code":
        msg = "The {0}{1}Bootleg code is completely open-source".format(con.CURRENT_RELEASE, " " if con.CURRENT_RELEASE else "")
        if con.PROCESS_CODE:
            msg = msg + ", and can be viewed at {0}".format(con.PROCESS_CODE)
        msg = msg + "."
        show_help(msg)
    elif helping == "support":
        msg = "You can request help by going on the forums"
        if con.EMAIL:
            msg = msg + " or send an email to {0}".format(con.EMAIL)
        if con.USER_HELP:
            msg = msg + "; {0} {1} the official helper{2}".format(", ".join(con.USER_HELP), "are" if len(con.USER_HELP) > 1 else "is", "s" if len(con.USER_HELP) > 1 else "")
        msg = msg + "."
        show_help(msg)
    elif helping == "commands":
        msg = "There are no available commands."
        if con.COMMANDS:
            msg = "Available command{1}: {0}.".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else "")
        if (con.HIDDEN_COMMANDS and DEBUG_MODE) or (con.HIDDEN_COMMANDS and var.SHOW_HIDDEN_COMMANDS):
            msg = msg + "\nHidden command{1}: {0}.".format(", ".join(con.HIDDEN_COMMANDS), "s" if len(con.HIDDEN_COMMANDS) > 1 else "")
        show_help(msg)
    else:
        show_help("Error: '{0}' was not found but is in the database. Critical error.".format(helping), type="error")