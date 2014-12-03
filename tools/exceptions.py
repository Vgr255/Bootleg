# Exceptions for some random things

# These exceptions should never be called due to user input
# They should only be called for programming errors or forgetting stuff
# They don't have to do anything, so just 'pass' is fine
# They MAY be called due to user input, but only if it's absolutely necessary
# For example, someone tries to run arbitrary code or purposely make it crash
# If they are called for user-related input, it's preferred to catch it after
# Use the CustomBootException class to derive from (easier to catch)

# Default exception class for easier catching

class CustomBootException(Exception):
    pass

# Called when the process tries to find a setting that doesn't exist

class SettingNotFound(CustomBootException):
    pass

# Called if no finder is found for the given setting

class NoParserFound(CustomBootException):
    pass

# Called if no installer is found for the given setting

class NoInstallerFound(CustomBootException):
    pass

# Called if a system or fatal error is not valid

class InvalidError(CustomBootException):
    pass

# Called if the given mod could not be found in any of the mods folders

class ModFileNotFound(CustomBootException):
    pass

# Called if there was already a preset imported and the user tries to get another

class PresetAlreadyImported(CustomBootException):
    pass