# Exceptions for some random things

# These exceptions should never be called due to user input
# They should only be called for programming errors or forgetting stuff
# They don't have to do anything, so just 'pass' is fine
# They MAY be called due to user input, but only if it's absolutely necessary
# For example, someone tries to run arbitrary code or purposely make it crash
# If they are called for user-related input, it's preferred to catch it after
# Use the CustomBootException class to derive from (easier to catch)

class CustomBootException(Exception):
    pass

class SettingNotFound(CustomBootException):
    pass

class WrongParsingType(CustomBootException):
    pass

class NoParserFound(CustomBootException):
    pass

class NoInstallerFound(CustomBootException):
    pass

class InvalidError(CustomBootException):
    pass

class ModFileNotFound(CustomBootException):
    pass

class PresetAlreadyImported(CustomBootException):
    pass