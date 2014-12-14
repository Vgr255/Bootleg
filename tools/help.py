# Whenever typing 'help [stuff]', this is called
# If there are no arguments, get_help() is called
# If there are arguments, the according function is called
# If no function matches, 'unhandled' is used
# Functions (except get_help()) may return either a string or a list

from tools import variables as var
from tools import constants as con
from tools import logger as log
from tools import decorators

for lang in con.LANGUAGES.keys():
    var.HELPERS[lang] = {}

generator = decorators.generate(arguments=False, command=False, topic=False, user=False)

help_en = generator(var.HELPERS["English"])
help_fr = generator(var.HELPERS["French"])

unhandled = "HELP_NOT_FOUND"

def get_help(helping=""):
    helping = helping.lower()
    log.help("", "HELP_FILE_BOOT_CONF", form=con.PROGRAM_NAME)
    log.help("HELP_FILE_NEW_HELP", "\n")
    if helping:
        log.help("HELP_NOT_VALID_HELP", form=helping)
        if var.HELPERS:
            log.help("HELP_POSSIBLE_HELP")
            log.help("HELP_USE_ITEM_SPEC")
            return False
    elif not helping:
        if con.CURRENT_RELEASE:
            log.help("HELP_BOOT_CUR_REL", form=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
        if con.RELEASE_INFO and con.BUILD_INFO and con.VERSION_INFO:
            log.help(con.BUILD_INFO, con.VERSION_INFO, con.RELEASE_INFO, splitter=" ")
        if con.FIRST_DEV:
            log.help("HELP_FIRST_DEV", form=[", ".join(con.FIRST_DEV), "PLURAL" if len(con.FIRST_DEV) > 1 else ""])
        if con.USER_HELP:
            log.help("HELP_USER_HELPING", form=["PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)])
        if con.CODERS:
            log.help("HELP_CODERS", form=["PLURAL" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)])
            if con.GUI_CODERS:
                log.help("HELP_GUI_CODERS", form=", ".join(con.GUI_CODERS))
            if con.PROCESS_CODERS:
                log.help("HELP_PROCESS_CODERS", form=[", ".join(con.PROCESS_CODERS), con.PROGRAM_NAME])
        if con.BETA_TESTERS:
            log.help("HELP_BETA_TESTERS", form=["PLURAL" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)])
        if con.TRANSLATORS:
            log.help("HELP_TRANSLATORS", form=["PLURAL" if len(con.TRANSLATORS) > 1 else "", ", ".join(con.TRANSLATORS)])
            if con.FRENCH_TRANSLATORS:
                log.help("HELP_FRENCH_TRANSLATORS", form=["PLURAL" if len(con.FRENCH_TRANSLATORS) > 1 else "", ", ".join(con.FRENCH_TRANSLATORS)])
        if con.OTHER_SUPPORT:
            log.help("HELP_OTHER_SUPPORT", form=[con.PROGRAM_NAME, ", ".join(con.OTHER_SUPPORT)])
        if con.SPECIAL_THANKS:
            log.help("HELP_SPECIAL_THANKS", form=", ".join(con.SPECIAL_THANKS))
        if con.EXT_HELP:
            log.help("HELP_EXT_HELP", form=["PLURAL" if len(con.EXT_HELP) > 1 else "", ", ".join(con.EXT_HELP)])
        if con.EMAIL:
            log.help("HELP_EMAIL", form=[con.EMAIL, con.PROGRAM_NAME])
        if con.DEVELOPERS:
            log.help("", "HELP_DEVELOPERS", form=["PLURAL" if len(con.DEVELOPERS) > 1 else "", ", ".join(con.DEVELOPERS)])
        topics = var.HELPERS[var.LANGUAGE]
        log.help("", "HELP_POSSIBLE_HELP", "HELP_VIEW_SPEC_TOP")
        log.help("HELP_VIEW_SPEC_USR")
        log.help("HELP_VIEW_SPEC_CMD")
        return False
    return True

# Various help topics

@help_en("programming", topic=True)
@help_fr("programmation", topic=True)
def programming():
    if con.PROCESS_CODERS and con.GUI_CODERS:
        return ["HELP_PROGRAMMING_PROCESS", "HELP_PROGRAMMING_GUI"], con.PROGRAM_NAME, ", ".join(con.PROCESS_CODERS), ", ".join(con.GUI_CODERS)
    if con.PROCESS_CODERS:
        return "HELP_PROGRAMMING_PROCESS", con.PROGRAM_NAME, ", ".join(con.PROCESS_CODERS)
    if con.GUI_CODERS:
        return "HELP_PROGRAMMING_GUI", ", ".join(con.GUI_CODERS)
    return "HELP_PROGRAMMING_NONE", con.PROGRAM_NAME

@help_en("code", "coding", topic=True)
@help_fr("code", topic=True)
def code():
    if con.PROCESS_CODE:
        return "HELP_CODE_PROCESS", con.PROGRAM_NAME, con.CURRENT_RELEASE, con.PROCESS_CODE
    return "HELP_CODE_NONE", con.PROGRAM_NAME, con.CURRENT_RELEASE

@help_en("support", topic=True)
@help_fr("support", topic=True)
def support():
    if con.EMAIL and con.USER_HELP:
        return "HELP_SUPPORT_EMAIL_HELP", con.EMAIL, "PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)
    if con.EMAIL:
        return "HELP_SUPPORT_EMAIL", con.EMAIL
    if con.USER_HELP:
        return "HELP_SUPPORT_HELP", "PLURAL" if len(con.USER_HELP) > 1 else "", "PLUR_ARE" if len(con.USER_HELP) > 1 else "SING_IS", ", ".join(con.USER_HELP)
    return "HELP_SUPPORT_NONE"

@help_en("commands", topic=True)
@help_fr("commandes", topic=True)
def commands():
    topics = var.HELPERS[var.LANGUAGE]
    poshelp = [x for x in topics if topics[x][0].command]
    if poshelp:
        return "HELP_COMM", "PLURAL" if len(poshelp) > 1 else "", ", ".join(poshelp)
    return "HELP_NO_AVAIL_CMD"

@help_en("users", topic=True)
@help_fr("utilisateurs", topic=True)
def see_users():
    usr = var.HELPERS[var.LANGUAGE]
    poshelp = [x for x in usr if usr[x][0].user]
    if poshelp:
        return "HELP_USERS", con.PROGRAM_NAME, ", ".join(poshelp), "PLURAL" if len(poshelp) > 1 else ""
    return "HELP_NO_USERS"

@help_en("topics", topic=True)
@help_fr("topics", topic=True)
def view_topics():
    top = var.HELPERS[var.LANGUAGE]
    poshelp = [x for x in top if top[x][0].topic]
    if poshelp:
        return "HELP_POSSIBLE_HELP", ", ".join(poshelp), "PLURAL" if len(poshelp) > 1 else ""
    return "HELP_NO_TOPIC"

# Users are down here

@help_en("pitbrat", user=True)
@help_fr("pitbrat", user=True)
def pitbrat():
    return "HELP_PITBRAT"

@help_en("eq2alyza", user=True)
@help_fr("eq2alyza", user=True)
def eq2alyza():
    return "HELP_ALYZA"

@help_en("vgr", user=True)
@help_fr("vgr", user=True)
def vgr():
    return "HELP_VGR"

# Commands are down here

@help_en("help", command=True)
@help_fr("aide", command=True)
def help():
    return "HELP_HELP_CMD"

@help_en("run", command=True)
@help_fr("run", command=True)
def run():
    return "HELP_RUN"

@help_en("read", command=True)
@help_fr("lire", command=True)
def read():
    return "HELP_READ_CMD"
