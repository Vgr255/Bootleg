import variables as var
import constants as con

def get_help(helping=""):
    helping = helping.lower()
    print(" - Final Fantasy VII Bootleg Mod Configurator -")
    print(" * Help file *")
    print("")
    if not helping:
        if var.CURRENT_RELEASE:
            print("Bootleg - Final Fantasy VII Configurator - Version {0}".format(var.CURRENT_RELEASE))
        if var.RELEASE_INFO and var.BUILD_INFO:
            print(var.BUILD_INFO, "build", var.RELEASE_INFO)
        if con.FIRST_DEV:
            print("First developper and base idea: {0}.".format(", ".join(con.FIRST_DEV)))
        if con.USER_HELP:
            print("User helper{0} and support team: {1}.".format("s" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)))
        if con.CODERS:
            print("Current active programmer{0} and developper{0}: {1}.".format("s" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)))
        if con.GUI_CODERS:
            print("Programming of the Graphical User Interface (GUI): {0}.".format(", ".join(con.GUI_CODERS)))
        if con.PROCESS_CODERS:
            print("Programming of the Bootleg process: {0}.".format(", ".join(con.PROCESS_CODERS)))
        if con.GAME_CONV:
            print("Game Converter developping and support: {0}".format(", ".join(con.GAME_CONV)))
        if con.BETA_TESTERS:
            print("{0} tester{1} for the current Bootleg release: {2}.".format(var.BUILD_INFO, "s" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)))
        if con.SPECIAL_THANKS:
            print("Special thanks to {0}.".format(", ".join(con.SPECIAL_THANKS)))
        if con.EMAIL:
            print("Official Bootleg email for support and questions: {0}".format(con.EMAIL))
        if con.POSSIBLE_HELP:
            print("")
            print("Possible help topic{1}: {0}.".format(", ".join(con.POSSIBLE_HELP), "s" if len(con.POSSIBLE_HELP) > 1 else ""))
            print("Use 'help <item>' to view a specific help.")
    if helping == "programming":
        msg = "The current version of Bootleg is coded in Python 3.2"
        if con.PROCESS_CODERS:
            msg = msg + " by {0}".format(", ".join(con.PROCESS_CODERS))
        print(msg + ".")
        msg2 = "The Graphical User Interface is coded in C#"
        if con.GUI_CODERS:
            msg2 = msg2 + " by {0}".format(", ".join(con.GUI_CODERS))
        print(msg2 + ".")
    if helping == "code":
        msg = "The {0}Bootleg code is completely open-source"
        if con.PROCESS_CODE:
            msg = msg + ", and can be viewed at {1}"
        msg = msg + "."
        msg.format(var.CURRENT_VERSION+ " ", con.PROCESS_CODE)
        print(msg)
    if helping == "support":
        msg = "You can request help by going on the forums"
        if con.EMAIL:
            msg = msg + " or send an email to {0}"
        if con.USER_HELP:
            msg = msg + "; {1} {2} the official helper{3}"
        msg = msg + "."
        msg.format(con.EMAIL, ", ".join(con.USER_HELP), "are" if len(con.USER_HELP) > 1 else "is", "s" if len(con.USER_HELP) > 1 else "")
        print(msg)