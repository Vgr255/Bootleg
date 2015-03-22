# Languages constants

# Use the constants to define languages, that makes it easier to change later on

English = "English"
French = "French"

# Various constants

# Languages checking

ENGLISH = {
English: "English",
French: "Anglais",
}

FRENCH = {
English: "French",
French: "Français",
}

# Boolean values

TRUE = {
English: "True",
French: "Vrai",
}

FALSE = {
English: "False",
French: "Faux",
}

YES = {
English: "Yes",
French: "Oui",
}

NO = {
English: "No",
French: "Non",
}

# Read values

READ_SECTIONS = {
English: "Section",
French: "Section",
}

READ_INDEX = {
English: "index",
French: "index",
}

READ_GET_SECTIONS = { # This needs to be a list/tuple
English: ("sections", "list"),
French: ("sections", "liste"),
}

# Small words that are part of larger sentences by format

PLURAL = { # Gets added if plural at the end of some words
English: "s",
French: "s",
}

SING_IS = {
English: "is",
French: "est",
}

PLUR_ARE = {
English: "are",
French: "sont",
}

ONE_IN = {
English: "in",
French: "dans",
}

MULT_IN_ONE = {
English: "in one of",
French: "dans l'un de",
}

STATUS = {
English: "status",
French: "status",
}

SIGNAL = {
English: "signal",
French: "signal",
}

# Mods names

TRISH_MASAMUNE = {
English: "Mike's Masamune model",
}

AERITH_REVIVAL = {
English: "Aerith Revival",
}

REUNION = {
English: "DLPB's Reunion",
}

SPELL_PATCH = {
English: "he new spells Patch",
}

AVALANCHE = {
English: "Team Avalanche High-Res Overhaul",
}

REASONABLE_DIFF = {
English: "the Reasonable Difficulty mod",
}

REMASTERED_AI = {
English: "the Remastered AI from the Remix",
}

SCENE_REDUX = {
English: "the Scene Redux",
}

ITEMS_EASY = {
English: "Harder Items (Easy)",
}

ITEMS_NORMAL = {
English: "Harder Items (Normal)",
}

ITEMS_DIFFICULT = {
English: "Harder Items (Difficult)",
}

AVALANCHE_GUI = {
English: "Avalanche GUI",
}

LOST_WINGS = {
English: "the Lost Wings complete overhaul",
}

MODE_SWITCHING = {
English: "the Gameplay Modes Switching",
}

NEW_THREAT = {
English: "the New Threat mod by Sega Chief",
}

NEW_60_FPS = {
English: "the 60 FPS mod",
}

ROMEO_MAT = {
English: "Romeo14's AC Style Materias for Avalanche",
}

HARDCORE_GJOERULV = {
English: "Gjoerulv's Hardcore mod",
}

RUMBAHSMOOTH1280 = {
English: "Rumbah's FMV with Smooth Filter @ 1280p",
}

RUMBAHSMOOTH640 = {
English: "Rumbah's FMV with Smooth Filter @ 640p",
}

RUMBAHSHARP1280 = {
English: "Rumbah's FMV with Sharp Filter @ 1280p",
}

RUMBAHSHARP640 = {
English: "Rumbah's FMV with Sharp Filter @ 640p",
}

FMVRES = {
English: "the FMV Restoration cutscenes",
}

LOGO = {
English: "the Eidos logo",
}

ENHANCED_MOVIES1 = {
English: "Enhanced Movies pack 1",
}

ENHANCED_MOVIES2 = {
English: "Enhanced Movies pack 2",
}

GRIMMY_MOVIES = {
English: "Grimmy's movies",
}

RUMBAH_MOVIES = {
English: "Rumbah's Opening movies",
}

LEONHART_MOVIES = {
English: "Leonhart7413's Intro movies",
}

LEONHART_OPENING = {
English: "Leonhart7413's Alternate Opening movie",
}

LEONHART_LOG = {
English: "Leonhart7413's Alternate Logo movie",
}

FURY_FMVS = {
English: "PH03N1XFURY's Ending and Meteo FMVs",
}

FUNERAL_FMVS = {
English: "PH03N1XFURY's Funeral and Nibelheim FMVs",
}

FIELD_TEXTURES = {
English: "Field Art as PNG to Mods folder",
}

FACEPALMERV2 = {
English: "FacePalmer V2 Field Textures",
}

FACEPALMER = {
English: "FacePalmer Field Textures",
}

FACEPALMERPART = {
English: "FacePalmer Field Textures in parts",
}

# End of the mods names

# The following lines are contained in 'bootleg.py'

RES_RET = { # 0 = Program name
English: "Type 'exit' or 'restart' to exit or restart {0}, or Ctrl+C to quit.",
French: "Entrez 'exit' ou 'restart' pour quitter ou recommencer {0}, ou Ctrl+C pour quitter.",
}

ENT_CMD = {
English: "Please enter a command:",
French: "Veuillez entrer une commande :",
}

ENT_CHC = {
English: "Please make a choice:",
French: "Veuillez faire un choix :",
}

ENT_VAL = {
English: "Please enter a value:",
French: "Veuillez entrer une valeur :",
}

ENT_UPD = { # 0,1 = Yes/No (fill at the top)
English: "Update now? ({0}/{1})",
French: "Mettre à jour maintenant? ({0}/{1})",
}

AVAIL_CMD = { # 0 = Commands; 1 = Plural (fill at the top)
English: "Available command{1}: {0}.",
French: "Commande{1} disponible{1}: {0}.",
}

NO_USR_INP = { # 0 = Default value; 1 = Setting
English: "No user input was detected. Using {0} for {1}.",
French: "Aucun choix n'a été détecté. {0} est utilisé pour {1}.",
}

ERR_INVALID_BOOL = { # 0,1 = Yes/No/True/False (fill at the top)
English: "Error: Invalid boolean value (Enter either '{0}' or '{1}').",
French: "Erreur: Valeur binaire invalide (Entrez soit '{0}' ou '{1}').",
}

WAIT_UPD = {
English: "Updating files . . .",
French: "Mise à jour des fichiers . . .",
}

SUCCESS_UPD = {
English: "Files successfully updated.",
French: "Fichiers mis à jour avec succès.",
}

REST_FOR_CHG = {
English: "Press any key to restart.",
French: "Appuyez sur une touche pour redémarrer.",
}

FAILED_UPD = {
English: "Update failed. Please try again later.",
French: "Mise à jour ratée. Essayez à nouveau plus tard.",
}

DIS_AUTO_UPD = {
English: "Disable Auto-Update in the configuration if it fails too often.",
French: "Désactivez la mise à jour automatique (Auto-Update) dans la configuration si cela rate trop souvent.",
}

NO_CMD_ENT = {
English: "No command was entered.",
French: "Aucune commande n'a été entrée.",
}

NEED_RR = {
English: "You must type either 'exit' or 'restart'.",
French: "Vous devez entrez soit 'exit' ou 'restart'.",
}

SIGTERM_END = {
English: "Received SIGTERM. Closing process.",
French: "SIGTERM reçu. Fermeture du processus.",
}

SIGTERM_WARN = {
English: "WARNING: SIGTERM Detected.",
French: "ATTENTION: SIGTERM Détecté.",
}

MOD_NOT_FOUND = { # 0 = Mod file; 1 = "in" or "in one of" (fill above); 2 = MOD_LOCATION variable
English: "Error: {0} could not be found {1} '{2}'.",
}

PRESET_ALIMPORTED = { # 0(1) = Preset file; 0(2) = Program name
English: "Warning: The preset '{0}' is already loaded.\nYou need to restart {0} to be able to load another preset.",
}

PROVIDE_TRACE = { # 0,1 = Filename/File extension
English: "Provide your '{0}.{1}' file.",
French: "Suppliez votre fichier '{0}.{1}'.",
}

# End of the 'bootleg.py' lines

# All the following entries are lines contained within files inside the 'tools' folder

# The following lines are contained in '__init__.py'

GENERATING_DECORATORS = {
English: "Performing startup initialization . . .\nThis may take a while.",
}

NOT_ON_WINDOWS = { # 0 = Program name
English: "{0} will not work properly on a different operating system than Windows.",
}

UPDATE_AVAIL = { # 0 = Program name; 1 = Version number
English: "A {0} update is available!",
French: "Une mise à jour de {0} est disponible!",
}

SILENT_UPD = {
English: "An update is available. Downloading . . .",
French: "Une mise à jour est disponible. Téléchargement . . .",
}

REST_AFT_UPD = { # 0 = Program name
English: "Launch {0} again once it finishes.",
French: "Relancez {0} une fois terminé.",
}

CREATING_REPO = { # 0 = Current folder; 1 = Program name
English: "Performing first-time setup for {1} in '{0}'.",
French: "Installation de {1} dans '{0}'.",
}

FIRST_SETUP_WAIT = {
English: "Please wait while setup is installing the files. . .",
French: "Veuillez patienter pendant que l'assistant installe les fichiers. . .",
}

UNCOMMITTED_FILES = {
English: "Warning: You have local changes.",
French: "Attention: Vous avez des modifications locales.",
}

WARN_NOT_RUN_ADMIN = { # 0 = Program name
English: "Warning: {0} is not running as admin. Some functions will not work.",
}

RUN_BOOT_ELEVATED = { # 0 = Program name
English: "Please run '{0}.exe' with elevated privileges.",
}

LNCH_PAR = { # 0 = Launch parameters
English: "Launch parameters: {0}",
French: "Paramètres de lancement : {0}",
}

# End of the '__init__.py' lines

# The following lines are contained in 'commands.py'

NOT_DEFINED = { # 0 = Can be anything
English: "Error: {0} is not defined.",
French: "Erreur: {0} n'est pas défini.",
}

ERR_DOC_NOT_FOUND = { # 0 = File
English: "Error: The documentation file '{0}' could not be found.",
}

GIT_NOT_INST = {
English: "Error: Git is not installed. The operation cannot continue.",
French: "Erreur: Git n'est pas installé. L'opération ne peut pas continuer.",
}

COMM_NOT_EXIST = { # 0 = Command
English: "Error: Command {0} does not exist.",
}

NO_DOC_AVAIL = {
English: "Documentation for this command is not available.",
}

PLEASE_ENT_CMD = {
English: "Please input a command.",
}

# End of the 'commands.py' lines

# The following lines are contained in 'constants.py'

# Those are for language detection

IDENT_LANG_VERS_EN = {
English: "Identified Compatible US Version.",
}

IDENT_LANG_VERS_FR = {
English: "Identified French Version.",
}

IDENT_LANG_VERS_DE = {
English: "Identified German Version.",
}

IDENT_LANG_VERS_ES = {
English: "Identified Spanish Version.",
}

IDENT_LANG_VERS_IT = {
English: "Identified Italian Version.",
}

# Note: Those lines are part of the ASCII, and need to stay the same length

BOOT_ARCH = { # 0 = '32bit' or '64bit' depending on architecture
English: "    by    \ \    / / ____|  __ \   Running on {0}   |___/",
French: "    par   \ \    / / ____|  __ \   Exécution: {0}   |___/",
}

BOOT_STARTUP = { # 0 = Version number; 1 = Program name
English: "            \ \/ /| | |_ |  _  /   Welcome to the {1} configurator {0}",
French: "            \ \/ /| | |_ |  _  /   Bienvenue au configurateur {1} {0}",
}

# End of the 'constants.py' lines

# The following lines are contained in 'errors.py'

UNH_ERR_TOREP = {
English: "An unhandled error has occured. Please report this.",
}

MIS_FILE_FROM_SYS = { # 0 = Filename; 1 = Folder
English: "'{0}' is missing from '{1}'.",
}

OLD_OPENGL_INST = {
English: "An older version of Aali's driver has been detected.",
}

NO_OPENGL_ABORTING = {
English: "Aali's OpenGL driver was not detected.",
}

# End of the 'errors.py' lines

# The following lines are contained in 'exceptions.py'

CUSTOM_BOOT_EXCEPTION = { # This should never be called
English: "Default Exception. No action taken.",
}

SETTING_NOT_FOUND = { # 0 = Setting
English: "Error: '{0}' is not a valid setting.",
}

NO_PARSER_FOUND = { # 0 = Setting
English: "Error: No parser was found for '{0}'.",
}

NO_INSTALLER_FOUND = { # 0 = Setting
English: "Error: No installer was found for '{0}'.",
}

INVALID_ERROR = { # 0 = Invalid error
English: "Error: '{0}' cannot be used as an error.",
}

MOD_FILE_NOT_FOUND = { # 0 = Mod file; 1 = "in" or "in one of" (fill at the top); 2 = MOD_LOCATION variable
English: "Error: '{0}' could not be found {1} '{2}'.",
}

PRESET_ALREADY_IMPORTED = { # 0 = Preset file
English: "Error: The preset '{0}' is already loaded.\nYou may not load more than one preset at once.\nPlease restart to load another preset.",
}

INVALID_PARAMETER = { # 0 = Module; 1 = Function; 2 = Parameter; 3 = Value
English: "Invalid value: {0}.{1}(*params, {2}=\"{3}\").",
}

INT_OUT_OF_BOUNDS = { # 0 = Setting; 1 = Value; 2 = Max
English: "Error: Value out of bounds for {0}: {1} (Max: {2}).",
}

NEED_INTEGER = { # 0 = Setting; 1 = Value
English: "Error: Need a number for {0} (Got {1}).",
}

# End of the 'exceptions.py' lines

# The following lines are contained in 'functions.py'

BEGIN_BOOT = { # 0 = Program name
English: "Beginning {0} operation.",
French: "Commencement du processus {0}.",
}

RESTART_BOOT = { # 0 = Program name
English: "Restarting {0} operation.",
French: "Recommencement du processus {0}.",
}

RUN_LANG = { # 0 = Language; 1 = Program name
English: "Running {1} in {0}.",
French: "Exécution de {1} en {0}.",
}

RUN_OS = { # 0 = Architecture (32/64); 1 = Program name; 2 = True/False (fill at the top)
English: "Running {1} on {0} (Windows: {2}).",
French: "Exécution de {1} sous {0} (Windows: {2}).",
}

PROCESS_EXITED = { # 0 = Called process; 1 = 'status' or 'signal' (fill at the top); 2 = Integer
English: "Process '{0}' exited with {1} {2}",
French: "Le processus '{0}' s'est terminé de {1} {2}",
}

LOGGING_SETTINGS = {
English: "Settings:",
}

SYST_PATHS = {
English: "- System paths -",
French: "- Chemins système -",
}

DEST_LOCT = { # 0 = Installation location (duh)
English: 'Destination location: "{0}"',
French: 'Emplacement de l\'installation: "{0}"',
}

INST_IMG = { # 0 = Name of the .zip image
English: 'Install image: "{0}"',
French: 'Installation de l\'image: "{0}"',
}

MOD_LOCT = { # 0 = Mods location
English: 'Mods Location: "{0}"',
}

TMP_FILES = { # 0 = Temporary files location
English: 'Temporary files: "{0}"',
}

BOOT_INIT = { # 0 = Program name
English: "Initializing {0} . . .",
}

INIT_CMPLT = {
English: "Initialization completed.",
}

EXTR_SPRKL = {
English: "Now extracting Sprinkles . . .",
}

SPRINKLES_READY = {
English: "Sprinkles are ready.",
}

INST_LANG = { # 0 = Language; 1,2 = Yes/No (fill at the top)
English: "Do you want to install the game in {0}? ({1}/{2})",
French: "Voulez-vous installer le jeu en {0}? ({1}/{2})",
}

TYPE_LANG = {
English: "Please enter a language.",
French: "Veuillez entrer une langue.",
}

INT_OUTBOUNDS = {
English: "Error: Value out of bounds.",
French: "Erreur: Valeur hors limites.",
}

FND_2012_CONVERTING = {
English: "Found 2012 Square Enix Store Re-Release. Converting . . .",
}

COMPL_2012_CONVERT = {
English: "Completed 2012 Re-Release conversion.",
}

VALIDATING_LANGUAGES = {
English: "Validating Language Files . . .",
}

LANG_FILES_CONV_COMPL = {
English: "Language conversion completed.",
}

BACKUP_VANILLA = {
English: "Backing up Vanilla Data. . .",
}

FILES_BACKUP_COMPL = {
English: "Files backup completed.",
}

CONV_2012_SES_FLEVEL = {
English: "Converting 2012 Square Enix Store flevel. . .",
}

COMPL_2012_FLEVEL_CONV = {
English: "Completed flevel Conversion.",
}

APPLYING_102_PATCH = {
English: "Applying the Official Final Fantasy VII 1.02 English patch . . .",
}

COMPL_102_PATCH_INST = {
English: "Completed Final Fantasy VII 1.02 Patch Installation.",
}

ADJUSTING_ALPHA_BLEND = {
English: "Adjusting Alpha Blending for NPC Battle Models . . .",
}

COMPL_BAT_MODELS_ADJ = {
English: "Completed Battle Model Adjustements.",
}

WARN_OLDER_AALI = {
English: "Warning: You have an older version of Aali's driver.",
}

RUN_BOOT_CLEAN = {
English: "Please run Bootleg on a fresh install.",
}

INST_AALIS_DRIVER = {
English: "Installing Aali's OpenGL Driver . . .",
}

AALI_INSTALLED = {
English: "Installed Aali's OpenGL Custom Driver.",
}

WARN_NO_AALI = {
English: "Warning: Aali's OpenGL driver wasn't detected. Aborting.",
}

ADD_AALI_TO_MOD = { # 0 = Zip file of Aali's driver; 1 = 'in' or 'in one of' (fill at the top); 2 = Mods location(s)
English: "Please add '{0}' {1} '{2}' and retry.",
}

INST_BOOT_SYS_FILES = { # 0 = Program names
English: "Installing {0} System files.",
}

COMPL_BOOT_SYS_FILES = { # 0 = Program name
English: "Completed {0} System files.",
}

REG_LOCATING_DATADRIVE = {
English: "Locating Data Drive . . .",
}

CANT_LOCATE_FF7_DRIVE = {
English: "Unable to locate the Final Fantasy VII Installation Drive.",
}

ENTER_VALID_DRIVE_LETTER = {
English: "Please enter a valid drive letter.",
}

ERR_DRIVE_NOT_EXIST_READY = {
English: "Error: Drive does not exist or is not ready.",
}

USING_DRIVE_FOR_CDS = { # 0 = Drive letter
English: "Using Drive '{0}:' for the Final Fantasy VII CDs.",
}

BUILDING_SYS_FILES = {
English: "Building system files . . .",
}

UPDATING_REG_SILENT = {
English: "Updating Registry . . .",
}

COMPL_REG_SILENT = {
English: "Registry successfully updated.",
}

REGISTERING_AUDIO_DEVICES = {
English: "Registering audio devices . . .",
}

CONFIG_SND_MIDI_DEVICES = {
English: "Please configure the SOUND and MIDI devices.",
}

COMPL_AUDIO_DEVICES = {
English: "Completed Audio devices.",
}

PREPARING_LGP_FILES = {
English: "Preparing LGP Files . . .",
}

COMPLETED_LGP_FILES = {
English: "Completed LGP Preparation.",
}

PREPARING_DATA_FILE = {
English: "Preparing '{0}' . . .",
}

COMPLETED_DATA_FILE = {
English: "Completed '{0}'.",
}

COPYING_DUMMY_TEX = {
English: "Copying Dummy Textures . . .",
}

INV_PAR_FILE = { # 0 = File name; 1 = Setting
English: "Invalid setting found in {0}: {1}",
}

FND_EXIST_INST = {
English: "Found existing FF7 installation.",
}

COPY_SAVE_FILES = {
English: "Copying save files.",
}

NO_SAVE_FND = {
English: "No save files found.",
}

COPY_INP_SET = {
English: "Copying Input settings.",
}

NO_INP_SET_FND = {
English: "No input settings found.",
}

REM_CUR_INST = {
English: "Removing current installation.",
}

NO_INST_FND = {
English: "No current installation found.",
}

EXTR_IMG = {
English: "Extracting Final Fantasy VII Image . . .",
}

IMG_REST_CMPL = {
English: "Final Fantasy VII Image Restoration Completed.",
}

INST_FND_1998 = {
English: "Final Fantasy VII Installation Found:",
}

INST_FND_2013 = {
English: "Final Fantasy VII 2013 Steam Installation Found:",
}

INST_FND_2012 = {
English: "Final Fantasy VII 2012 Square Enix Store Installation Found:",
}

INST_FND_DEF = {
English: "Final Fantasy VII Default Installation Found:",
}

COULD_NOT_FINST = {
English: "Could not find a Final Fantasy VII Installation.",
}

ABORT_BOOT = { # 0 = Program name
English: "Aborting {0}...",
}

FATAL_ERROR = {
English: " - FATAL ERROR -",
}

ERR_TO_REPORT = {
English: "An error occured. Please report this.",
}

ERR_ENC = {
English: "An error has been encountered.",
}

MAY_STILL_RUN = { # 0 = Program name
English:  "{0} may still run if you wish to.",
}

ERR_FOUND = { # 0 = Error (... did you really need to ask?)
English: "Error found: {0}",
}

ENT_VALUE_BETWEEN = { # 0 = Max value (integer)
English: "Please choose a value between 0 and {0}.",
}

NO_CHG = {
English: "0 = No Change",
}

INST_SPEC_SET = {
English: "Install {0}?",
}

CHC_NO = {
English: "0 = NO",
}

CHC_YES = {
English: "1 = YES",
}

DEF_TO_USE = { # 0 = Default value for settings
English: "Default is '{0}'. It will be used if no value is given.",
}

PARSER_NOT_FOUND = { # 0 = setting (filled above)
English: "Error: No installer for {0} was found.",
}

PARS_INSTALLING = {
English: "Beginning installation of {0} . . .",
}

PLEASE_REMAIN_PATIENT = { # This name is too confusing and not obvious enough
English: "Please remain patient.",
}

PARS_COMPL_INST_SUCCESS = {
English: "Completed installation of {0} successfully.",
}

ERR_INVALID_COMMAND = { # 0 = Name of the invalid command
English: "'{0}' is not a valid command.",
}

# End of the 'functions.py' lines

# The following lines are contained in 'get.py'

ENTER_ONLY_NUMS = {
English: "Please enter only numbers.",
}

ERR_VALUE_OUTBOUNDS = { # 0 = Position of the faulty value; 1 = Value; 2 = Max value - All integers
English: "Error: Value out of bounds at position {0}: {1} (Max: {2}).",
}

USR_INP_SET_USING = { # 0 = Default value; 1 = Setting
English: "Using '{0}' for {1}.",
}

SET_DEF_NO_INP_USED = { # 0 = Setting; 1 = Value
English: "Setting used for {0}: {1}.",
}

PRESET_SAVED = { # 0 = Current directory; 1 = Filename; 2 = File extension
English: "Preset saved as '{0}/presets/{1}.{2}'",
}

# End of the 'get.py' lines

# The following lines are contained in 'help.py'

HELP_NOT_FOUND = { # 0 = Help topic
English: "Error: '{0}' was not found but is in the database. Critical error.",
French: "Erreur: '{0}' se trouve dans la base de données mais n'a pas été trouvé. Erreur critique.",
}

HELP_FILE_BOOT_CONF = { # 0 = Program name
English: "               - Final Fantasy VII {0} Mod Configurator -",
}

HELP_FILE_NEW_HELP = {
English: "                                * Help file *",
}

HELP_NOT_VALID_HELP = { # 0 = Invalid help topic
English: "'{0}' is not a valid help topic.",
}

HELP_USE_ITEM_SPEC = {
English: "Use 'help <item>' to view a specific help topic.",
}

HELP_BOOT_CUR_REL = { # 0 = Program name; 1 = Version number
English: "{1} - Final Fantasy VII Configurator - Version {0}",
}

HELP_FIRST_DEV = { # 0 = FIRST_DEV constant; 1 = Plural (fill at the top)
English: "First developper{1} and base idea: {0}.",
}

HELP_USER_HELPING = { # 0 = Plural (fill at the top); 1 = USER_HELP constant
English: "User helper{0} and support team: {1}.",
}

HELP_CODERS = { # 0 = Plural (fill at the top); 1 = CODERS constant
English: "Current active programmer{0} and developper{0}: {1}.",
}

HELP_GUI_CODERS = { # 0 = GUI_CODERS constant
English: "Programming of the Graphical User Interface (GUI): {0}.",
}

HELP_PROCESS_CODERS = { # 0 = PROCESS_CODERS constant; 1 = Program name
English: "Programming of the {1} process: {0}.",
}

HELP_BETA_TESTERS = { # 0 = Plural (fill at the top); 1 = BETA_TESTERS constant
English: "Beta tester{0}: {1}.",
}

HELP_TRANSLATORS = { # 0 = Plural (fill at the top); 1 = TRANSLATORS constant
English: "Translator{0}: {1}.",
}

HELP_FRENCH_TRANSLATORS = { # 0 = Plural (fill at the top); 1 = FRENCH_TRANSLATORS constant
English: "French Translator{0}: {1}.",
}

HELP_OTHER_SUPPORT = { # 0 = Program name; 1 = OTHER_SUPPORT constant
English: "Direct support to {0}: {1}.",
}

HELP_SPECIAL_THANKS = { # 0 = SPECIAL_THANKS constant
English: "Special thanks to: {0}.",
}

HELP_EXT_HELP = { # 0 = Plural (fill at the top); 1 = EXT_HELP constant
English: "Helper{0} external to the project: {1}.",
}

HELP_EMAIL = { # 0 = Email; 1 = Program name
English: "Official {1} email for support and questions: {0}",
}

HELP_DEVELOPERS = { # 0 = Plural (fill at the top); 1 = DEVELOPERS constant
English: "Current active programmer{0} and developer{0}: {1}.",
}

HELP_POSSIBLE_HELP = {
English: "Possible help topics: {0}.",
}

HELP_VIEW_SPEC_TOP = {
English: "Type 'help <item>' to view a specific help topic.",
}

HELP_VIEW_SPEC_USR = {
English: "Type 'help <user>' to view information on a specific person.",
}

HELP_VIEW_SPEC_CMD = {
English: "Type 'help <command>' to get help on a specific command.",
}

HELP_PROGRAMMING_PROCESS = { # 0 = Program name; PROCESS_CODERS constant
English: "The current version of {0} is written in Python 3 by {1}.",
}

HELP_PROGRAMMING_GUI = { # 0 = GUI_CODERS constant
English: "The User Interface is written in C# by {0}.",
}

HELP_PROGRAMMING_NONE = { # 0 = Program name
English: "{0} is written in Python 3; the User Interface is in C#.",
}

HELP_CODE_PROCESS = { # 0 = Program name; 1 = Version number; 2 = Link to the code
English: "The {1} {0} code is completely open-source, and can be viewed at:\n'{2}'\n\nType 'get code' to access the code.",
}

HELP_CODE_NONE = { # 0 = Program name; 1 = Version number
English: "The {1} {0} code is completely open-source.",
}

HELP_SUPPORT_EMAIL_HELP = { # 0 = Email; 1 = USER_HELP constant
English: "You can request help by going on the forums, or by sending an email.\nEmail: '{0}'\nHelper{1}: {2}",
}

HELP_SUPPORT_EMAIL = { # 0 = Email (duh)
English: "To request help, you can go on the forums or send an email.\nEmail: '{0}'",
}

HELP_SUPPORT_HELP = { # 0 = PLURAL (fill at the top); 1 = "is" or "are" (fill at the top); 2 = USER_HELP constant
English: "You can request help on the forums; the helper{0} {1} {2}.",
}

HELP_SUPPORT_NONE = {
English: "You can go on the forums to ask for help.",
}

HELP_COMM = { # 0 = PLURAL (fill at the top); 1 = Commands
English: "Available command{0}: {1}",
}

HELP_NO_AVAIL_CMD = {
English: "There are no available commands.",
}

HELP_USERS = { # 0 = Program name; 1 = Users; 2 = PLURAL (fill at the top)
English: "User{2} with or without a direct link to {0}: {1}",
}

HELP_NO_USERS = {
English: "There are no users.",
}

HELP_NO_TOPICS = {
English: "There are no topics.",
}

HELP_PITBRAT = { # The backslashes are needed to ignore the line change and concatenate the strings
English: "PitBrat started Bootleg as a personal project.\n" \
         "After a while, he decided to release it for the public to use.\n" \
         "After 040's release, life took over and he couldn't work on Bootleg anymore.",
}

HELP_ALYZA = {
English: "EQ2Alyza made Tifa's Bootleg Tutorial, which significantly helped users.\n" \
         "She helped many users to troubleshoot various issues.",
}

HELP_VGR = {
English: "Vgr joined the development of Bootleg not long after it became public.\n" \
         "He did a lot of debugging and beta-testing of many versions.\n" \
         "Along with PitBrat, he was the only one with access to the code.\n" \
         "He also provides user support for Bootleg.\n\n" \
         "After PitBrat left the scene, he decided to give a new life to Bootleg.\n" \
         "He converted the old and buggy code in Python 3 and made it open-source.\n" \
         "He is so far the only Bootleg programmer.",
}

HELP_HELP_CMD = {
English: "The help command is used to display various information.\n" \
         "This is what you're currently viewing.",
}

HELP_RUN = {
English: "Use this command to run the Bootleg process.",
}

HELP_READ_CMD = {
English: "The 'read' command can be used to read various documentation.\n" \
         "The syntax is 'read <file> [section]'\n" \
         "The file can be any setting. It will attempt to find the matching file.\n" \
         "The optional 'section' parameter can be used to read only a part of the file.\n" \
         "You can use 'read <file> sections' to view all the available sections.\n" \
         "You may specify a number in the form '5' or '4.3' for example.\n",
}

# End of the 'help.py' lines

# These lines are for the settings (called dynamically on runtime)

PARS_FIND_CLOUD_FIELD = {
English: "Pick Cloud's appearance in the field:\n" \
         "1 = WITHOUT sword\n" \
         "2 = WITH Buster sword\n" \
         "3 = Wielding Masamune\n" \
         "4 = Omni Cloud\n" \
         "5 = Squallff8's Rebuilded\n" \
         "6 = Grimmy's AC Style\n" \
         "7 = FMV with Sword (Weemus)\n" \
         "8 = FMV Without Sword (Weemus)\n" \
         "9 = Chibi Strife (NameSpoofer)\n" \
         "10 = APZ with Sword\n" \
         "11 = APZ without Sword\n" \
         "12 = APZ Black with Sword\n" \
         "13 = APZ Black without Sword\n" \
         "14 = APZ Dark with Sword\n" \
         "15 = APZ Dark without Sword\n" \
         "16 = APZ Chibi\n" \
         "17 = APZ Black Chibi\n" \
         "18 = APZ Dark Chibi\n" \
         "19 = BitzNCS New Chibi\n" \
         "20 = PRP Classic\n" \
         "21 = Chibi Reconstruction\n" \
         "22 = Dahfa's Chibi\n" \
         "23 = APZ Adjusted\n" \
         "24 = Team Avalanche Chibi\n" \
         "25 = Bloodshot's Edited TA",
}

PARS_FIND_CLOUD_BATTLE = {
English: "Pick Cloud's appearance in battle:\n" \
         "1 = Classic\n" \
         "2 = The Remix APZ\n" \
         "3 = Grimmy's Hi Res\n" \
         "4 = Grimmy's AC Style\n" \
         "5 = FMV Cloud (Weemus)\n" \
         "6 = Strife\n" \
         "7 = New APZ\n" \
         "8 = New APZ Black\n" \
         "9 = New APZ Dark\n" \
         "10 = New APZ Mature\n" \
         "11 = Team Avalanche\n" \
         "12 = Bloodshot's Edited TA",
}

PARS_FIND_TRISH_SAVE = {
English: "Pick the save point model:\n" \
         "1 = FFX Save Point Model\n" \
         "2 = Crisis Core Save Point Model\n" \
         "3 = Cloud's Memories Memories Save Point Model\n" \
         "4 = Team Avalanche Save Point Model\n" \
         "5 = Save Point with Balls",
}

PARS_FIND_TRISH_PHOENIX = {
English: "Pick the style of Mike's summons:\n" \
         "1 = New Style Flaming Phoenix\n" \
         "2 = Old Style Shaded Phoenix\n" \
         "3 = Old Style Phoenix with Custom Brighter Texture",
}

PARS_FIND_NEW_AERITH = {
English: "Choose the new Aerith model:\n" \
         "1 = HQ Aerith\n" \
         "2 = Sailor Jupiter Aerith\n" \
         "3 = Whiteraven HQ Aerith",
}

PARS_FIND_VINCENT_BATTLE = {
English: "Choose Vincent's appearance in battle:\n" \
         "1 = ReModel with new Handgun\n" \
         "2 = New boots and Rifle",
}

PARS_FIND_LIMIT_BREAK = {
English: "Pick the Limit Break texture:\n" \
         "1 = Kela's V3 Limit in Original Colors\n" \
         "2 = Kela's V2 Limit in Blue\n" \
         "3 = Kela's V3 Limit in Blue\n" \
         "4 = Kela's V4 Limit in Blue\n" \
         "5 = Kela's V4 Limit in Original Colors\n" \
         "6 = Mike's Flame Limit Texture\n" \
         "7 = Jinkazama2k7's Green Limit\n" \
         "8 = Mike's Blue Flame Limit Texture\n" \
         "9 = Mike's Flame Limit V2 Texture\n" \
         "10 = JLOUTLAW's Hypersonic Limit",
}

PARS_FIND_MENU_BACKGROUND = {
English: "Select the Start menu background:\n" \
         "1 = Remix Art\n" \
         "2 = Buster Sword in Red by Felix Leonhart\n" \
         "3 = HD Buster Sword by Wren Jr.\n" \
         "4 = Midgar\n" \
         "5 = Friends by Nikfrozty\n" \
         "6 = Cloud\n" \
         "7 = Simple\n" \
         "8 = Buster Sword\n" \
         "9 = Standoff\n" \
         "10 = Standoff with logo\n" \
         "11 = Zendar's AC Buster Sword\n" \
         "12 = Recko's Gold Hilt Buster Sword",
}

PARS_FIND_KERNEL_SELECT = {
English: "Choose your game mode:\n" \
         "1 = Remastered - Kernel AI, stats and equipment from The Remix\n" \
         "2 = Scene Redux - Better Items to Steal\n" \
         "3 = Harder Items Easy\n" \
         "4 = Harder Items Normal\n" \
         "5 = Harder Items Difficult\n" \
         "6 = Harder Items Easy + Scene Redux\n" \
         "7 = Harder Items Normal + Scene Redux\n" \
         "8 = Harder Items Difficult + Scene Redux\n" \
         "9 = Lost Wing - Complete overhaul with extensive modifications\n" \
         "10 = Gjoerulv's Hardcore mod\n" \
         "11 = Mode Switching - All Mods\n" \
         "12 = Mode Switching - Without Hardcore\n" \
         "13 = Reasonable Difficulty\n" \
         "14 = Reasonable Difficulty + Harder Items Easy\n" \
         "15 = Reasonable Difficulty + Harder Items Normal\n" \
         "16 = Reasonable Difficulty + Harder Items Difficult",
}

PARS_FIND_MOVIES = {
English: "Choose the videos to use:\n" \
         "1 = DLPB's HQ videos\n" \
         "2 = Bootlegged - Trojak's Enhanced with DLBP and Xion999\n" \
         "3 = Bootlegged Further Enhanced with Grimmy\n" \
         "4 = Bootlegged Further Enhanced with Rumbah\n" \
         "5 = Rumbah Complete - 1280 Smooth\n" \
         "6 = Rumbah Complete - 1280 Sharp\n" \
         "7 = Rumbah Complete - 640 Smooth\n" \
         "8 = Rumbah Complete - 640 Sharp\n" \
         "9 = Grimmy's AC Style enhanced with Leonhart7413\n" \
         "10 = Grimmy's AC Style enhanced with Leonhart7413 HD Alternate\n" \
         "11 = Bootlegged reworked with PH03N1XFURY",
}

PARS_FIND_RUMBAH_MOVIES = {
English: "Choose which pick of Rumbah's opening videos to use:\n" \
         "You may pick a number from 0 to 5\n" \
         "Don't change anything if you don't know what to pick.",
}

PARS_FIND_FIELD_TEXTURES = {
English: "Pick which set of field textures to use:\n" \
         "1 = Bootlegged: BlackFan and SL1982 Field Art\n" \
         "2 = BlackFan and SL1982 Field Art as Primary over FacePalmer\n" \
         "3 = FacePalmer Field Art Only\n" \
         "4 = BlackFan and SL1982 without FacePalmer",
}

PARS_FIND_AVATARS = {
English: "Select which set of avatars you want:\n" \
         "1 = Bloodshot's Transparant Avatars Bootleg Combo\n" \
         "2 = Nikfrozty's Transparent Crisis Core Avatars\n" \
         "3 = Nikfrozty's Tranparent Alternative Avatars\n" \
         "4 = Full Portrait Transparent Avatars\n" \
         "5 = Milo Leonhart's 10th Anniversary Photographic Avatars\n" \
         "6 = Milo Leonhart's Demi Face Avatars\n" \
         "7 = Milo Leonhart's Demi Face Avatars V2\n" \
         "8 = Milo Leonhart's Demi Face Avatars V3\n" \
         "9 = Singular One's AC Transparent Avatars\n" \
         "10 = Zendar's Round AC Avatars\n" \
         "11 = Zendar's Round AC Avatars V2\n" \
         "12 = Zendar's Round AC Avatars V3\n" \
         "13 = Zendar's Round AC Avatars V4\n" \
         "14 = Zendar's Round AC Avatars V5\n" \
         "15 = Zendar's Round AC Avatars V5.1\n" \
         "16 = Armorvil's Eye Avatars\n" \
         "17 = Grimmy's AC Style Avatars\n" \
         "18 = Kula Wende's AC Style Avatars\n" \
         "19 = Nero's AC Style Avatars\n" \
         "20 = Nikfrozty's AC Style Avatars\n" \
         "21 = Aff7iction's Beautified Avatars\n" \
         "22 = MinMin's Avatars\n" \
         "23 = Recko's Transparent Avatars",
}

PARS_FIND_SOUNDTRACK = {
English: "Pick which soundtrack to install:\n" \
         "1 = FinalFanTim's OGG Soundtrack\n" \
         "2 = PSF MIDI Soundtrack\n" \
         "3 = OCRemix Soundtrack\n" \
         "4 = Custom Soundtrack from the Remix\n" \
         "5 = Bootleg Soundtrack\n" \
         "6 = Anxious Heart - Original Selection\n" \
         "7 = Anxious Heart - DLPB Selection\n" \
         "8 = Anxious Heart - Fan Selection\n" \
         "9 = Anxious Heart - Professional Selection",
}

PARS_FIND_OPENING_CREDITS = {
English: "Pick which opening credits to use:\n" \
         "1 = Grimmy's Cloud and Sephiroth Prelude Credits\n" \
         "2 = JordieBo's Prelude Credits\n" \
         "3 = JordieBo's Dark Prelude Credits\n" \
         "4 = JordieBo's Glowing Prelude Credits\n" \
         "5 = Strayoff's Prelude Credits\n" \
         "6 = Grimmy's Cloud and Tifa Prelude Credits",
}

PARS_FIND_BUSTER_SWORD = {
English: "Pick the Buster Sword replacement:\n" \
         "1 = Millenia's Buster Sword\n" \
         "2 = Slayernext's Buster Sword\n" \
         "3 = Mike's Buster Sword\n" \
         "4 = APZ's Buster Sword\n" \
         "5 = Omni Buster Sword\n" \
         "6 = Masamune as Buster Sword",
}

PARS_FIND_MYTHRIL_SABER = {
English: "Pick the Mythril Saber replacement:\n" \
         "1 = Millenia's Mythril Saber\n" \
         "2 = Slayernext's Mythril Saber",
}

PARS_FIND_HARDEDGE = {
English: "Pick the Hardedge replacement:\n" \
         "1 = Millenia's Hardedge\n" \
         "2 = Slayernext's Hardedge",
}

PARS_FIND_BUTTERFLY_EDGE = {
English: "Pick the Butterfly Edge replacement:\n" \
         "1 = Millenia's Butterfly Edge\n" \
         "2 = Slayernext's Butterfly Edge",
}

PARS_FIND_ENHANCE_SWORD = {
English: "Pick the Enhance Sword replacement:\n" \
         "1 = Millenia's Butterfly Edge\n" \
         "2 = Slayernext's Butterfly Edge",
}

PARS_FIND_ORGANICS = {
English: "Pick the Organics replacement:\n" \
         "1 = Millenia's Organics\n" \
         "2 = Slayernext's Organics",
}

PARS_FIND_CRYSTAL_SWORD = {
English: "Pick the Crystal Sword replacement:\n" \
         "1 = Millenia's Crystal Sword\n" \
         "2 = Slayernext's Crystal Sword",
}

PARS_FIND_FORCE_STEALER = {
English: "Pick the Force Stealer replacement:\n" \
         "1 = Millenia's Force Stealer\n" \
         "2 = Slayernext's Force Stealer",
}

PARS_FIND_RUNE_BLADE = {
English: "Pick the Rune Blade replacement:\n" \
         "1 = Millenia's Rune Blade\n" \
         "2 = Slayernext's Rune Blade",
}

PARS_FIND_MURASAME = {
English: "Pick the Murasame replacement:\n" \
         "1 = Millenia's Murasame\n" \
         "2 = Slayernext's Murasame\n" \
         "3 = Dragon Murasame\n" \
         "4 = Oblivion Lovelace as Murasame",
}

PARS_FIND_NAIL_BAT = {
English: "Pick the Nail Bat replacement:\n" \
         "1 = Millenia's Nail Bat\n" \
         "2 = Slayernext's Nail Bat",
}

PARS_FIND_YOSHIYUKI = {
English: "Pick the Yoshiyuki replacement:\n" \
         "1 = Millenia's Yoshiyuki\n" \
         "2 = Slayernext's Yoshiyuki",
}

PARS_FIND_APOCALYPSE = {
English: "Pick the Apocalypse replacement:\n" \
         "1 = Millenia's Apocalypse\n" \
         "2 = Slayernext's Apocalypse",
}

PARS_FIND_HEAVENS_CLOUD = {
English: "Pick the Heaven's Cloud replacement:\n" \
         "1 = Millenia's Heaven's Cloud\n" \
         "2 = Slayernext's Heaven's Cloud",
}

PARS_FIND_RAGNAROK = {
English: "Pick the Ragnarok replacement:\n" \
         "1 = Millenia's Ragnarok\n" \
         "2 = Slayernext's Ragnarok\n" \
         "3 = APZ's Ragnarok",
}

PARS_FIND_ULTIMA_WEAPON = {
English: "Pick the Ultima Weapon replacement:\n" \
         "1 = Millenia's Ultima Weapon\n" \
         "2 = Slayernext's Ultima Weapon\n" \
         "3 = Mike's Ultima Weapon\n" \
         "4 = Oblivion External Mod Ultima Weapon",
}

# End of the parsers

# The following lines are contained within 'parser.py'

PARS_EXEC_FILE = { # 0 = File; 1 = Folder; 2 = Parameters
English: "Currently exexcuting '{0}' from '{1}' with parameters '{2}'.",
}

PARS_EXTR_FILE = { # 0 = File
English: "Extracting '{0}' . . .",
}

SET_LOCATION = {
English: "Set the destination location to:",
}

PICK_1997_2012 = {
English: "Select 'Original (1997)' even if using the 2012 Square Enix Store version.",
}

PICK_1997_2013 = {
English: "Select 'Original (1997)' even if using the 2013 Steam version.",
}

PARS_SKIP = { # 0 = Filename; 1 = "in" or "in one of" (fill at the top); 2 = Mods location(s)
English: "Error: '{0}' could not be found. Please add '{0}' {1} '{2}' and retry.",
}

PARS_SKIP_MOD_DEFAULT = { # 0 = Mod name (filled above) - 'Set' is also past tense
English: "Skipping {0} installation (Set to 0 in settings).",
}

PARS_INSTALLING = { # 0 = Mod name
English: "Installing {0} . . .",
}

PARS_COMPLETED = { # 0 = Mod name
English: "Completed installation of {0}.",
}

FP_EXTR_TEXTURES = {
English: "Extracting Textures . . .\nThis will take a few minutes.",
}

MIS_ALL_FP = {
English: "Missing FacePalmer files. Skipping FacePalmer.",
}
