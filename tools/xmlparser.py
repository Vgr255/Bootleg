# 2014 Emanuel 'Vgr' Barry
# XML Parser for the translation.xml file
# Reuse and redistribution of this source file is ALLOWED in the following cases:
# - No profit is made
# - Proper credit is given to the original author
# - Modification of the code is accompagnied with comments stating as such
# - Modification of the code for personal use only
# Reuse and redistribution is NOT ALLOWED under the following circumstances:
# - Profit is made off this code
# - The original code is modified and not indicated as such
# - No credit to the original author is given
# ***
# This XML parser was developped by Vgr "E. Barry" as part of the
# Bootleg Final Fantasy VII Mod Configurator project. It is however
# entirely independant of the aforementioned project, and can be used
# with any other project. Some rewriting might need to be done, but it
# is also possible to get it working without any further modification.
# ***
# What it does is it takes word from the 'origin' specified and then
# finds the relevant matching entry in 'lang'; useful for translations
# Type determines if the whole line is to be matched, or only part of it.

def init(filename, lang, origin):
    global file
    global checking
    global lines
    global setting
    global original
    global type
    global getting
    global result
    global partial
    file = open(filename, "r")
    checking = False
    lines = []
    setting = lang[0].upper() + lang[1:].lower() # english, ENGliSH and enGLIsH all become English
    original = origin[0].upper() + origin[1:].lower()
    type = None
    getting = None
    result = None
    partial = []

def get_line(inp):
    for line in file.readlines():
        line = line.replace("\n", "")
        if line == "":
            continue
        if "//" in line: # C++ like line comments, let's ignore them
            com = line.index("//")
            com1 = com - 1
            com2 = com + 2
            if line[com1:] == line:
                continue # full-line comment
            if line[com1:com2] == " //":
                com = com1
            line = line[:com]
        if line == "<Line>":
            checking = True
            continue
        if line == "</Line>":
            checking = False # we got what we want, now let's move on
        if checking:
            if line[:2] == "  ":
                line = line[2:]
            lines.append(line)
            continue

        for word in lines:
            origlen = len(original) + 2
            _origlen = len(original) + 3
            setlen = len(setting) + 2
            _setlen = len(setting) + 3
            if word[:6] == "<Type>" and word[-7:] == "</Type>":
                type = word[6:-7]
            if "<{0}>".format(original) == word[:origlen] and "</{0}>".format(original) == word[-_origlen:]: # original one to look for
                toget = word[origlen:-_origlen]
                if (toget == inp and type == "Full") or (toget in inp and type == "Partial"):
                    getting = toget
                    continue
            if getting and "<{0]>".format(setting) == word[:setlen] and "</{0}>".format(setting) == word[-_setlen:]: # setting
                getting = None
                return word[setlen:-_setlen]