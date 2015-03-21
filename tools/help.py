# Whenever typing 'help [stuff]', this is called
# If there are no arguments, get_help() is called
# If there are arguments, the according function is called
# If no function matches, 'unhandled' is used
# Functions (except get_help()) may return either a string or a list

from tools import variables as var
from tools import constants as con
from tools import decorators
from tools import log

generator = decorators.generate(arguments=False, command=False, topic=False, user=False)

help_en = generator(var.HELPERS, id="English")
help_fr = generator(var.HELPERS, id="French")

unhandled = "HELP_NOT_FOUND"

def get_help(helping=""):
    topics = var.HELPERS
    poshelp = [x for x in topics if topics[x].topic and not x in topics[x].aliases]
    poshelp.sort()
    helping = helping.lower()
    log.show("", "HELP_FILE_BOOT_CONF", format=[con.PROGRAM_NAME])
    log.show("HELP_FILE_NEW_HELP", "\n")
    if helping:
        log.show("HELP_NOT_VALID_HELP", format=[helping])
        if var.HELPERS:
            log.show("HELP_POSSIBLE_HELP", format=[", ".join(poshelp)])
            log.show("HELP_USE_ITEM_SPEC")
            return False
    elif not helping:
        if con.CURRENT_RELEASE:
            log.show("HELP_BOOT_CUR_REL", format=[con.CURRENT_RELEASE, con.PROGRAM_NAME])
        if con.RELEASE_INFO and con.BUILD_INFO and con.VERSION_INFO:
            log.show(con.BUILD_INFO, con.VERSION_INFO, con.RELEASE_INFO, sep=" ")
        if con.FIRST_DEV:
            log.show("HELP_FIRST_DEV", format=[", ".join(con.FIRST_DEV), "PLURAL" if len(con.FIRST_DEV) > 1 else ""])
        if con.USER_HELP:
            log.show("HELP_USER_HELPING", format=["PLURAL" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)])
        if con.CODERS:
            log.show("HELP_CODERS", format=["PLURAL" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)])
            if con.GUI_CODERS:
                log.show("HELP_GUI_CODERS", format=[", ".join(con.GUI_CODERS)])
            if con.PROCESS_CODERS:
                log.show("HELP_PROCESS_CODERS", format=[", ".join(con.PROCESS_CODERS), con.PROGRAM_NAME])
        if con.BETA_TESTERS:
            log.show("HELP_BETA_TESTERS", format=["PLURAL" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)])
        if con.TRANSLATORS:
            log.show("HELP_TRANSLATORS", format=["PLURAL" if len(con.TRANSLATORS) > 1 else "", ", ".join(con.TRANSLATORS)])
            if con.FRENCH_TRANSLATORS:
                log.show("HELP_FRENCH_TRANSLATORS", format=["PLURAL" if len(con.FRENCH_TRANSLATORS) > 1 else "", ", ".join(con.FRENCH_TRANSLATORS)])
        if con.OTHER_SUPPORT:
            log.show("HELP_OTHER_SUPPORT", format=[con.PROGRAM_NAME, ", ".join(con.OTHER_SUPPORT)])
        if con.SPECIAL_THANKS:
            log.show("HELP_SPECIAL_THANKS", format=[", ".join(con.SPECIAL_THANKS)])
        if con.EXT_HELP:
            log.show("HELP_EXT_HELP", format=["PLURAL" if len(con.EXT_HELP) > 1 else "", ", ".join(con.EXT_HELP)])
        if con.EMAIL:
            log.show("HELP_EMAIL", format=[con.EMAIL, con.PROGRAM_NAME])
        if con.DEVELOPERS:
            log.show("", "HELP_DEVELOPERS", format=["PLURAL" if len(con.DEVELOPERS) > 1 else "", ", ".join(con.DEVELOPERS)])
        log.show("", "HELP_POSSIBLE_HELP", "HELP_VIEW_SPEC_TOP", format=[", ".join(poshelp)])
        log.show("HELP_VIEW_SPEC_USR")
        log.show("HELP_VIEW_SPEC_CMD")
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
    topics = var.HELPERS
    poshelp = [x for x in topics if topics[x].command]
    poshelp.sort()
    if poshelp:
        return "HELP_COMM", "PLURAL" if len(poshelp) > 1 else "", ", ".join(poshelp)
    return "HELP_NO_AVAIL_CMD"

@help_en("users", topic=True)
@help_fr("utilisateurs", topic=True)
def see_users():
    usr = var.HELPERS
    poshelp = [x for x in usr if usr[x].user]
    poshelp.sort()
    for y in poshelp:
        for z in set(con.FIRST_DEV + con.USER_HELP + con.CODERS + con.OTHER_SUPPORT +
            con.BETA_TESTERS + con.SPECIAL_THANKS + con.EXT_HELP + con.DEVELOPERS + con.TRANSLATORS):
            if z.lower() == y:
                poshelp[poshelp.index(y)] = z
                break
    if poshelp:
        return "HELP_USERS", con.PROGRAM_NAME, ", ".join(poshelp), "PLURAL" if len(poshelp) > 1 else ""
    return "HELP_NO_USERS"

@help_en("topics", topic=True)
@help_fr("topics", topic=True)
def view_topics():
    top = var.HELPERS
    poshelp = [x for x in top if top[x].topic]
    poshelp.sort()
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
