# Exceptions for some random things

# These exceptions should never be called due to user input
# They should only be called for programming errors or forgetting stuff
# They don't have to do anything, so just 'pass' is fine
# They MAY be called due to user input, but only if it's absolutely necessary
# For example, someone tries to run arbitrary code or purposely make it crash
# If they are called for user-related input, it's preferred to catch it after

class SettingNotFound(Exception):
    pass

class WrongParsingType(Exception):
    pass

class NoParserFound(Exception):
    pass

class NoInstallerFound(Exception):
    pass

class InvalidError(Exception):
    pass

class ModFileNotFound(Exception):
    pass