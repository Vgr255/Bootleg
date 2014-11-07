# Languages constants

English = "English"
French = "French"

# Use the constants to define languages, that makes it easier to change later on

# Various constants

ENGLISH = {
English: "English",
French: "Anglais",
}

FRENCH = {
English: "French",
French: "Français",
}

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

# The following lines are contained in 'bootleg.py'

UPDATE_AVAIL = {
English: "A {0} update is available!",
French: "Une mise à jour de {0} est disponible!",
}

SILENT_UPD = {
English: "An update is available. Downloading . . .",
French: "Une mise à jour est disponible. Téléchargement . . .",
}

REST_AFT_UPD = {
English: "Launch {0} again once it finishes.",
French: "Relancez {0} une fois terminé.",
}

CREATING_REPO = {
English: "Performing first-time setup for {1} in '{0}'.",
French: "Installation de {1} dans '{0}'.",
}

FIRST_SETUP_WAIT = {
English: "Please wait while setup is installing the files. . .",
French: "Veuillez patienter pendant que l'assistant installe les fichiers. . .",
}

UNCOMMITTED_FILES = {
English: "Warning: You have uncommitted changes.",
French: "Attention: Vous avez des modifications non synchronisées.",
}

BOOT_DESC = {
English: "{0} Final Fantasy VII Mod Configurator {1}",
French: "Configurateur {0} pour Final Fantasy VII {1}",
}

LNCH_PAR = {
English: "Launch parameters: {0}",
French: "Paramètres de lancement : {0}",
}

CFG_DIS_OVR = {
English: "Config was disallowed. Overriding.",
French: "La configuration était désactivée. Réactivation.",
}

CFG_FORCED = {
English: "Forcing config into var.",
French: "La configuration a été copiée de force.",
}

RES_RET = {
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

ENT_UPD = {
English: "Update now? ({0}/{1})",
French: "Mettre à jour maintenant? ({0}/{1})",
}

NO_USR_INP = {
English: "No user input was detected. Using {0} for {1}.",
French: "Aucun choix n'a été détecté. {0} est utilisé pour {1}.",
}

ERR_INVALID_BOOL = {
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

PROVIDE_TRACE1 = {
English: "An error occured. Please report this.",
French: "Une erreur est survenue. Veuillez le rapporter.",
}

PROVIDE_TRACE2 = {
English: "Provide your '{0}.{1}' file.",
French: "Suppliez votre fichier '{0}.{1}'.",
}

# End of the 'bootleg.py' lines

# All the following entries are lines contained within files inside the 'tools' folder

# The following lines are contained in 'commands.py'

NOT_DEFINED = {
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

IDENT_LANG_VERS_DE = {
English: "Identified German Version.",
}

# Note: Those lines are part of the ASCII, and need to stay the same length

BOOT_ARCH = {
English: "    by    \ \    / / ____|  __ \   Running on {0}  |___/",
French: "    par   \ \    / / ____|  __ \   Exécution: {0}  |___/",
}

BOOT_STARTUP = {
English: "            \ \/ /| | |_ |  _  /   Welcome to the {1} configurator {0}",
French: "            \ \/ /| | |_ |  _  /   Bienvenue au configurateur {1} {0}",
}

# End of the 'constants.py' lines

# The following lines are contained in 'errors.py'

UNH_ERR_TOREP = {
English: "An unhandled error has occured. Please report this.",
}

MIS_FILE_FROM_SYS = {
English: "'{0}' is missing from {1}.",
}

# End of the 'errors.py' lines

# The following lines are contained in 'functions.py'

BEGIN_BOOT = {
English: "Beginning {0} operation.",
French: "Commencement du processus {0}.",
}

RESTART_BOOT = {
English: "Restarting {0} operation.",
French: "Recommencement du processus {0}.",
}

RUN_LANG = {
English: "Running {1} in {0}.",
French: "Exécution de {1} en {0}.",
}

RUN_OS = {
English: "Running {1} on {0} (Windows: {2}).",
French: "Exécution de {1} sous {0} (Windows: {2}).",
}

PROCESS_EXITED = {
English: "Process '{0}' exited with {1} {2}",
French: "Le processus '{0}' s'est terminé de {1} {2}",
}

AVAIL_CMD = {
English: "Available command{1}: {0}.",
French: "Commande{1} disponible{1}: {0}.",
}

SYST_PATHS = {
English: "- System paths -",
French: "- Chemins système -",
}

DEST_LOCT = {
English: 'Destination location: "{0}"',
French: 'Emplacement de l\'installation: "{0}"',
}

INST_IMG = {
English: 'Install image: "{0}"',
French: 'Installation de l\'image: "{0}"',
}

MOD_LOCT = {
English: 'Mods Location: "{0}"',
}

TMP_FILES = {
English: 'Temporary files: "{0}"',
}

BOOT_INIT = {
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

INST_LANG = {
English: "Do you want to install the game in {0}? (Yes/No)",
French: "Voulez-vous installer le jeu en {0}? (Oui/Non)",
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

VALIDATING_LANGUAGES = {
English: "Validating Language Files . . .",
}

COMPL_2012_CONVERT = {
English: "Completed 2012 Re-Release conversion.",
}

INV_PAR_FILE = {
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

ABORT_BOOT = {
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

MAY_STILL_RUN = {
English:  "{0} may still run if you wish to.",
}

ERR_FOUND = {
English: "Error found: {0}",
}

ENT_EXACT_DIG = {
English: "Please enter exactly {0} digits.",
}

ENT_VALUE_BETWEEN = {
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

DEF_TO_USE = {
English: "Default is '{0}'. It will be used if no value is given",
}

TOO_FEW_DIG = {
English: ", or if there are too few digits",
}

ERR_INVALID_COMMAND = {
English: "'{0}' is not a valid command.",
}

# End of the 'functions.py' lines

# The following lines are contained in 'get.py'

ENTER_ONLY_NUMS = {
English: "Please enter only numbers.",
}

ERR_VALUE_OUTBOUNDS = {
English: "Error: Value out of bounds at position {0}: {1} (Max: {2}).",
}

USR_INP_SET_USING = {
English: "Using '{0}' for {1}.",
}

SET_DEF_NO_INP_USED = {
English: "Setting used for {0}: {1}.",
}

# End of the 'get.py' lines

# The following lines are contained in 'help.py'

HELP_NOT_FOUND = {
English: "Error: '{0}' was not found but is in the database. Critical error.",
French: "Erreur: '{0}' se trouve dans la base de données mais n'a pas été trouvé. Erreur critique.",
}

HELP_FILE_BOOT_CONF = {
English: "               - Final Fantasy VII {0} Mod Configurator -",
}

HELP_FILE_NEW_HELP = {
English: "                                * Help file *",
}

HELP_NOT_VALID_HELP = {
English: "'{0}' is not a valid help topic.",
}

HELP_POS_HELP_TOPICS = {
English: "Possible help topic{1}: {0}.",
}

HELP_HIDDEN_COMMANDS = {
English: "Hidden help command{1}: {0}.",
}

HELP_USE_ITEM_SPEC = {
English: "Use 'help <item>' to view a specific help topic.",
}

HELP_BOOT_CUR_REL = {
English: "{1} - Final Fantasy VII Configurator - Version {0}",
}

HELP_FIRST_DEV = {
English: "First developper{1} and base idea: {0}.",
}

HELP_USER_HELPING = {
English: "User helper{0} and support team: {1}.",
}

HELP_CODERS = {
English: "Current active programmer{0} and developper{0}: {1}.",
}

HELP_GUI_CODERS = {
English: "Programming of the Graphical User Interface (GUI): {0}.",
}

HELP_PROCESS_CODERS = {
English: "Programming of the {1} process: {0}.",
}

HELP_GAME_CONV = {
English: "Game Converter developping and support: {0}.",
}

HELP_BETA_TESTERS = {
English: "Beta tester{0}: {1}.",
}

HELP_TRANSLATORS = {
English: "Translator{0}: {1}.",
}

HELP_FRENCH_TRANSLATORS = {
English: "French Translator{0}: {1}.",
}

HELP_OTHER_SUPPORT = {
English: "Other helper{0}: {1}.",
}

HELP_SPECIAL_THANKS = {
English: "Special thanks to: {0}.",
}

HELP_EXT_HELP = {
English: "Helper{0} external to the project: {1}.",
}

HELP_EMAIL = {
English: "Official {1} email for support and questions: {0}",
}

HELP_POSSIBLE_HELP = {
English: "Possible help topic{1}: {0}.",
}

HELP_HIDDEN_HELP = {
English: "Hidden help topic{1}: {0}.",
}

HELP_VIEW_SPEC_TOP = {
English: "Use 'help <item>' to view a specific help topic.",
}

HELP_VIEW_SPEC_USR = {
English: "Type 'help <user>' to view information on a specific person.",
}

HELP_VIEW_SPEC_CMD = {
English: "You can do 'help <command>' to get help on a specific command.",
}