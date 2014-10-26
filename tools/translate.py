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

# The following lines are contained in 'bootleg.py'

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

NO_USR_INP = {
English: "No user input was detected. Using {0} for {1}.",
French: "Aucun choix n'a été détecté. {0} est utilisé pour {1}.",
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

PROVIDE_TRACE = {
English: "An error occured. Please report this.\nProvide your '{0}.{1}' file.",
French: "Une erreur est survenue. Veuillez le rapporter.\nSuppliez votre fichier '{0}.{1}'.",
}

# End of the 'bootleg.py' lines

# All the following entries are lines contained within files inside the 'tools' folder

# The following lines are contained in 'commands.py'

HELP_NOT_FOUND = {
English: "Error: '{0}' was not found but is in the database. Critical error.",
French: "Erreur: '{0}' se trouve dans la base de données mais n'a pas été trouvé. Erreur critique.",
}

NOT_DEFINED = {
English: "Error: {0} is not defined.",
French: "Erreur: {0} n'est pas défini.",
}

PROCESS_EXITED = {
English: "Process {0} exited with {1} {2}",
French: "Le processus {0} s'est terminé de {1} {2}",
}

# End of the 'commands.py' lines

# The following lines are contained in 'constants.py'

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