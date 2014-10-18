# 2014 Emanuel 'Vgr' Barry
# XML Parser for the translation.xml file
# Reuse and redistribution of this source file is ALLOWED in the following cases:
# - No profit is made
# - Proper credit is given to the original author
# - Modification of the code is accompanied with comments stating as such
# - Modification of the code for personal use only
# - Modification of the code for another project while keeping this notice
# Reuse and redistribution is NOT ALLOWED under the following circumstances:
# - Profit is made off this code
# - The original code is modified and not indicated as such
# - No credit to the original author is given
# ***
# This XML parser was developed by Vgr "E. Barry" as part of the
# Bootleg Final Fantasy VII Mod Configurator project. It is however
# entirely independent of the aforementioned project, and can be used
# with any other project. Some rewriting might need to be done, but it
# is also possible to get it working without any further modification.
# ***
# If you change and improve this code, feel free to send it to me,
# I may use it, and I'll give you full credit for the changes if I do
# ***
# What it does is it takes word from the 'origin' specified and then
# finds the relevant matching entry in 'lang'; useful for translations
# Type determines if the whole line is to be matched, or only part of it.
# Partial, used when the Type is Partial, indicates how many times it must
# loop through the string for all matches (0 means no limit - same as not specified)
# Need to call init() first, with a filename, a language to translate to, and the
# original language for the lines to look for when given. More in-depth documentation
# is not available, you'll need to test to fully understand how it works, or use
# it with the project to see how it works. -Vgr

def init(filename, lang, origin):
    global file
    global setting
    global original
    file = filename
    setting = lang[0].upper() + lang[1:].lower() # english, ENGliSH and enGLIsH all become English
    original = origin[0].upper() + origin[1:].lower()

def get_line(inp, loop=False):
    f = open(file, "r")
    checking = False
    lines = []
    type = None
    getting = None
    iteration = 0
    max_amt = 0
    if inp.lower() == inp.upper():
        return inp
    for line in f.readlines():
        line = line.replace("\n", "")
        line1 = line.replace(" ", "")
        if line1 == "":
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
        if line1 == "<Line>":
            checking = True
            continue
        if line1 == "</Line>":
            checking = False # we got what we want, now let's move on
        if checking:
            lines.append(line)
            continue
        getting = None

        for word in lines:
            origlen = len(original) + 2
            _origlen = len(original) + 3
            setlen = len(setting) + 2
            _setlen = len(setting) + 3
            while True:
                if word[0] == " ":
                    word = word[1:]
                if word[-1:] == " ":
                    word = word[:-1]
                if word[0] == "<" and word[-1:] == ">": # proper brackets and all
                    break
            if word[:6] == "<Type>" and word[-7:] == "</Type>":
                type = word[6:-7]
            if word[:9] == "<Partial>" and word[-10:] == "</Partial>":
                if type == "Partial":
                    max_amt = int(word[9:-10]) # needs to be an integer
            if "<{0}>".format(original) == word[:origlen] and "</{0}>".format(original) == word[-_origlen:]: # original one to look for
                toget = word[origlen:-_origlen]
                if (toget == inp and type == "Full") or (toget in inp and type == "Partial"):
                    getting = toget
                    continue
            if getting and "<{0}>".format(setting) == word[:setlen] and "</{0}>".format(setting) == word[-_setlen:]: # setting
                if type == "Full":
                    getting = None
                    if loop:
                        break # prevent a full line from triggering on a partial one
                    return word[setlen:-_setlen]
                if type == "Partial":
                    if not loop:
                        getting = None
                        break
                    inp = inp.replace(getting, word[setlen:-_setlen])
                    iteration += 1
                    getting = None
                    if iteration == max_amt and max_amt > 0:
                        return inp
                    break # need to parse over for multiple words
    if not loop:
        inp = get_line(inp, loop=True)
    return inp # need to return something, if all else fails