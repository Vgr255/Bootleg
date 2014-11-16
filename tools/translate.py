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

# Small words that are part of larger sentences by format

PLURAL = {
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
}

MULT_IN_ONE = {
English: "in one of",
}

STATUS = {
English: "status",
}

SIGNAL = {
English: "signal",
}

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

REST_FOR_CHG = { # 0 = Program name
English: "Please restart {0} for the changes to take effect.",
French: "Veuillez relancer {0} pour que les changements prennent effet.",
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

PROVIDE_TRACE = { # 0,1 = Filename/File extension
English: "Provide your '{0}.{1}' file.",
French: "Suppliez votre fichier '{0}.{1}'.",
}

# End of the 'bootleg.py' lines

# All the following entries are lines contained within files inside the 'tools' folder

# The following lines are contained in '__init__.py'

NOT_ON_WINDOWS = { # 0 = Program name
English: "{0} will not work properly on a different operating system than Windows.",
}

UPDATE_AVAIL = { # 0 = Program name
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
English: "Warning: You have local changes in:",
French: "Attention: Vous avez des modifications locales dans :",
}

WARN_NOT_RUN_ADMIN = { # 0 = Program name
English: "Warning: {0} is not running as admin. Some functions will not work.",
}

RUN_BOOT_ELEVATED = { # 0 = Program name
English: "Please run '{0}.exe' with elevated privileges.",
}

CFG_DIS_OVR = {
English: "Config was disallowed. Overriding.",
French: "La configuration était désactivée. Réactivation.",
}

CFG_FORCED = {
English: "Forcing config into var.",
French: "La configuration a été copiée de force.",
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

GIT_NOT_INST = {
English: "Error: Git is not installed. The operation cannot continue.",
French: "Erreur: Git n'est pas installé. L'opération ne peut pas continuer.",
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

ENT_EXACT_DIG = { # 0 = Amount of digits to enter (integer)
English: "Please enter exactly {0} digits.",
}

ENT_VALUE_BETWEEN = { # 0 = Max value (integer)
English: "Please choose a value between 0 and {0}.",
}

NO_CHG = {
English: "0 = No Change",
}

CHC_NO = {
English: "0 = NO",
}

CHC_YES = {
English: "1 = YES",
}

DEF_TO_USE = { # 0 = Default value for settings - Don't add a final period
English: "Default is '{0}'. It will be used if no value is given",
}

TOO_FEW_DIG = { # This is a continuity of the above line (doesn't always display) - Don't add a final period
English: ", or if there are too few digits",
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

HELP_POS_HELP_TOPICS = { # 0 = Possible helps; 1 = Plural (fill at the top)
English: "Possible help topic{1}: {0}.",
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

HELP_POSSIBLE_HELP = { # 0 = HELPERS variable; 1 = Plural (fill at the top)
English: "Possible help topic{1}: {0}.",
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