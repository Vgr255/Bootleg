from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import filenames as fl
from tools import parser
from tools import get
from tools import log
from tools import reg

from tools.methods import *

def exit():
    get.pause()
    sys.exit(1)

def run(params="", silent=False):
    #sprinkles = ExtractFile(var.SYS_FOLDER + fl.SPRINKLES).rstrip("\\/") + "\\"
    sprinkles = "D:\\GitHub\\Bootleg\\utils\\sprinkles\\"
    if not os.path.isfile(sprinkles + fl.AALI_OPENGL):
        log.logger("WARN_NO_AALI", type="error")
        exit()
    inst = fn.chk_existing_install()
    if not inst:
        exit()
    if var.FFVII_IMAGE:
        fn.extract_image()
    log.logger("INST_AALIS_DRIVER")
    ExtractFile(sprinkles + fl.AALI_OPENGL, "OpenGL")
    CopyFolder(var.BOOTLEG_TEMP + "OpenGL", var.FFVII_PATH, True)
    # add the registry keys
    reg.add()
    log.logger("", "AALI_INSTALLED")

# September 16th, 2014 - note to self
# ***
# The whole batch process is being ran over
# and converted to python, all except for
# the actual process itself, which will
# come in last. When the batch process is
# done going through for the first time,
# testing will need to be done on all the
# current features. Then, the second run
# through the code will be done to make
# the actual install feature (the run
# function). Once this main function is
# completed, it will need to be tested
# heavily for a couple of days before
# we can proceed. Once it has been tested
# and bugs are squashed, then the new
# features can be added to make it work
# with all the new mods and everything.
# ***
# Estimated time to code this: End of October
# Estimated release time: Aiming towards Dec 31st
# -Vgr
# ***
# Edit October 10th: lol nope
# This isn't getting coded anywhere near the end of October
# 2014 release is maybe possible, but doubtful
# Also L&M-1Y yesterday. If I'm not drunk I'll know
# what this means. Secret stuff. -Vgr
# ***
# UPDATE: March 21st, 2015
# I decided to go in a wholly different direction than
# I originall had in mind. instead of spending time
# converting over the old code, I'll start from
# scratch using the frame that's already been done.
# obviously enough this wasn't released in time for 2015
# the new logger has been added in, now time to try to
# move forward and do this. my goal is to be able to
# locate and handle the game, install a mod, then
# another, and so on. many of the pre-defined
# functions and parsers will probably be scrapped
# time to stop being lazy and work more on this -Vgr
