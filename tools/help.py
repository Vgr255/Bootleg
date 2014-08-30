import variables as var
import constants as con

def get_help(helping=""):
    if not helping:
        if not var.CURRENT_RELEASE:
            print("Welcome to the Bootleg Mod Configurator for Final Fantasy VII")
        else:
            print("Bootleg - Final Fantasy VII Configurator - Version {}".format(var.CURRENT_RELEASE))
        if var.RELEASE_INFO:
            print(var.RELEASE_INFO)
        if con.FIRST_DEV:
            print("First developper and base idea: {0}.".format(", ".join(con.FIRST_DEV)))
        if con.USER_HELP:
            print("User helper{0} and support team: {1}.".format("s" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)))
        if con.CODERS:
            print("Current active programmer{0} and developper{0}: {1}.".format("s" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)))
        if con.GAME_CONV:
            print("Game Converter developping and support: {0}".format(", ".join(con.GAME_CONV)))