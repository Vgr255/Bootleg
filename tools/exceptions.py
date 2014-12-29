# Exceptions for some random things

# These exceptions should never be called due to user input
# They should only be called for programming errors or forgetting stuff
# They don't have to do anything, so just 'pass' is fine
# They MAY be called due to user input, but only if it's absolutely necessary
# For example, someone tries to run arbitrary code or purposely make it crash
# If they are called for user-related input, it's preferred to catch it after
# Use the CustomBootException class to derive from (easier to catch)

# Each class should defined __init__, arguments and formatter
# __init__ should define name
# arguments is the total of all arguments fed in
# formatter is used for the format of the message
# The message is the name of the exception in caps

from tools import variables as var

# Default exception class for easier catching
class CustomBootException(Exception):
    def __init__(self):
        self.name = "Custom Boot Exception"

    def arguments(self):
        return None

    def formatter(self):
        return None

# Called when the process tries to find a setting that doesn't exist
class SettingNotFound(CustomBootException):
    def __init__(self, setting):
        self.name = "Setting Not Found"
        self.setting = setting

    def arguments(self):
        return self.setting

    def formatter(self):
        return self.setting

# Called if no finder is found for the given setting
class NoParserFound(CustomBootException):
    def __init__(self, setting):
        self.name = "No Parser Found"
        self.setting = setting

    def arguments(self):
        return self.setting

    def formatter(self):
        return self.setting

# Called if no installer is found for the given setting
class NoInstallerFound(CustomBootException):
    def __init__(self, setting):
        self.name = "No Installer Found"
        self.setting = setting

    def arguments(self):
        return self.setting

    def formatter(self):
        return self.setting

# Called if the given mod could not be found in any of the mods folders
class ModFileNotFound(CustomBootException):
    def __init__(self, mod):
        self.name = "Mod File Not Found"
        self.mod = mod

    def arguments(self):
        return self.mod

    def formatter(self):
        return [self.mod, "ONE_IN" if len(var.MOD_LOCATION) == 1 else "MULT_IN_ONE", "', '".join(var.MOD_LOCATION)]

# Called if there was already a preset imported and the user tries to get another
class PresetAlreadyImported(CustomBootException):
    def __init__(self, preset):
        self.name = "Preset Already Imported"
        self.preset = preset

    def arguments(self):
        return self.preset

    def formatter(self):
        return self.preset

# Called if invalid parameters are fed to functions
class InvalidParameter(CustomBootException):
    def __init__(self, module, func, param, value):
        self.name = "Invalid Parameter"
        self.module = module
        self.func = func
        self.param = param
        self.value = value

    def arguments(self):
        return '{0}.{1}(*args, {2}="{3}")'.format(self.module, self.func, self.param, self.value)

    def formatter(self):
        return [self.module, self.func, self.param, self.value]

# Called if the setting is not in the range
class IntOutOfBounds(CustomBootException):
    def __init__(self, setting, value, max):
        self.name = "Int Out Of Bounds"
        self.setting = setting
        self.value = value
        self.max = max

    def arguments(self):
        return "{0}.value={1}; max={2}".format(self.setting, self.value, self.max)

    def formatter(self):
        return [self.setting, self.value, self.max]

# Called if the setting needs to be an integer but isn't
class NeedInteger(CustomBootException):
    def __init__(self, setting, value):
        self.name = "Need Integer"
        self.setting = setting
        self.value = value

    def arguments(self):
        return "{0}: '{1}'".format(self.setting, self.value)

    def formatter(self):
        return [self.setting, self.value]
