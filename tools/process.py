from tools import constants as con
from tools import variables as var
from tools import functions as fn
from tools import filenames as fl
from tools import logger as log
from tools import parser
import config
import os

def run(params="", silent=False):
    pass # last thing to do, see below

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