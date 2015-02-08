# Finding each variable's parameter if unset
# If a setting has only a yes/no choice, do NOT put it here
# It will be automatically added
# Do not add the '0' choice, it will be added automatically
# 0 is ALWAYS no change/no install

# Make sure to set the default in tools/variables.py
# and the maximum possible in tools/constants.py

from tools import variables as var
from tools import filenames as fl
from tools import logger as log

import subprocess
import shutil
import os

# Import the various file manipulation methods

from tools.methods import *

# The following are for finding the settings

def find_cloud_field():
    return [
    "Pick Cloud's appearance in the field:",
    "1 = WITHOUT sword",
    "2 = WITH Buster sword",
    "3 = Wielding Masamune",
    "4 = Omni Cloud",
    "5 = Squallff8's Rebuilded",
    "6 = Grimmy's AC Style",
    "7 = FMV with Sword (Weemus)",
    "8 = FMV Without Sword (Weemus)",
    "9 = Chibi Strife (NameSpoofer)",
    "10 = APZ with Sword",
    "11 = APZ without Sword",
    "12 = APZ Black with Sword",
    "13 = APZ Black without Sword",
    "14 = APZ Dark with Sword",
    "15 = APZ Dark without Sword",
    "16 = APZ Chibi",
    "17 = APZ Black Chibi",
    "18 = APZ Dark Chibi",
    "19 = BitzNCS New Chibi",
    "20 = PRP Classic",
    "21 = Chibi Reconstruction",
    "22 = Dahfa's Chibi",
    "23 = APZ Adjusted",
    "24 = Team Avalanche Chibi",
    "25 = Bloodshot's Edited TA",
    ]

def find_cloud_battle():
    return [
    "Pick Cloud's appearance in battle:",
    "1 = Classic",
    "2 = The Remix APZ",
    "3 = Grimmy's Hi Res",
    "4 = Grimmy's AC Style",
    "5 = FMV Cloud (Weemus,",
    "6 = Strife",
    "7 = New APZ",
    "8 = New APZ Black",
    "9 = New APZ Dark",
    "10 = New APZ Mature",
    "11 = Team Avalanche",
    "12 = Bloodshot's Edited TA",
    ]

def find_trish_save():
    return [
    "Pick the save point model:",
    "1 = FFX Save Point Model",
    "2 = Crisis Core Save Point Model",
    "3 = Cloud's Memories Memories Save Point Model",
    "4 = Team Avalanche Save Point Model",
    "5 = Save Point with Balls",
    ]

def find_trish_phoenix():
    return [
    "Pick the style of Mike's summons:",
    "1 = New Style Flaming Phoenix",
    "2 = Old Style Shaded Phoenix",
    "3 = Old Style Phoenix with Custom Brighter Texture",
    ]

def find_new_aerith():
    return [
    "Choose the new Aerith model:",
    "1 = HQ Aerith",
    "2 = Sailor Jupiter Aerith",
    "3 = Whiteraven HQ Aerith",
    ]

def find_vincent_battle():
    return [
    "Choose Vincent's appearance in battle:",
    "1 = ReModel with new Handgun",
    "2 = New boots and Rifle",
    ]

def find_limit_break():
    return [
    "Pick the Limit Break texture:",
    "1 = Kela's V3 Limit in Original Colors",
    "2 = Kela's V2 Limit in Blue",
    "3 = Kela's V3 Limit in Blue",
    "4 = Kela's V4 Limit in Blue",
    "5 = Kela's V4 Limit in Original Colors",
    "6 = Mike's Flame Limit Texture",
    "7 = Jinkazama2k7's Green Limit",
    "8 = Mike's Blue Flame Limit Texture",
    "9 = Mike's Flame Limit V2 Texture",
    "10 = JLOUTLAW's Hypersonic Limit",
    ]

def find_menu_background():
    return [
    "Select the Start menu background:",
    "1 = Remix Art",
    "2 = Buster Sword in Red by Felix Leonhart",
    "3 = HD Buster Sword by Wren Jr.",
    "4 = Midgar",
    "5 = Friends by Nikfrozty",
    "6 = Cloud",
    "7 = Simple",
    "8 = Buster Sword",
    "9 = Standoff",
    "10 = Standoff with logo",
    "11 = Zendar's AC Buster Sword",
    "12 = Recko's Gold Hilt Buster Sword",
    ]

def find_kernel_select():
    return [
    "Choose your game mode:",
    "1 = Remastered - Kernel AI, stats and equipment from The Remix",
    "2 = Scene Redux - Better Items to Steal",
    "3 = Harder Items Easy",
    "4 = Harder Items Normal",
    "5 = Harder Items Difficult",
    "6 = Harder Items Easy + Scene Redux",
    "7 = Harder Items Normal + Scene Redux",
    "8 = Harder Items Difficult + Scene Redux",
    "9 = Lost Wing - Complete overhaul with extensive modifications", 
    "10 = Gjoerulv's Hardcore mod",
    "11 = Mode Switching - All Mods",
    "12 = Mode Switching - Without Hardcore",
    "13 = Reasonable Difficulty",
    "14 = Reasonable Difficulty + Harder Items Easy",
    "15 = Reasonable Difficulty + Harder Items Normal",
    "16 = Reasonable Difficulty + Harder Items Difficult",
    ]

def find_movies():
    return [
    "Choose the videos to use:",
    "1 = DLPB's HQ videos",
    "2 = Bootlegged - Trojak's Enhanced with DLBP and Xion999",
    "3 = Bootlegged Further Enhanced with Grimmy",
    "4 = Bootlegged Further Enhanced with Rumbah",
    "5 = Rumbah Complete - 1280 Smooth",
    "6 = Rumbah Complete - 1280 Sharp",
    "7 = Rumbah Complete - 640 Smooth",
    "8 = Rumbah Complete - 640 Sharp",
    "9 = Grimmy's AC Style enhanced with Leonhart7413",
    "10 = Grimmy's AC Style enhanced with Leonhart7413 HD Alternate",
    "11 = Bootlegged reworked with PH03N1XFURY",
    ]

def find_rumbah_movies():
    return [
    "Choose which pick of Rumbah's opening videos to use:",
    "You may pick a number from 1 to 5",
    "Don't change anything if you don't know what to pick",
    ]

def find_field_textures():
    return [
    "Pick which set of field textures to use:",
    "1 = Bootlegged: BlackFan and SL1982 Field Art",
    "2 = BlackFan and SL1982 Field Art as Primary over FacePalmer",
    "3 = FacePalmer Field Art Only",
    "4 = BlackFan and SL1982 without FacePalmer",
    ]

def find_avatars():
    return [
    "Select which set of avatars you want:",
    "1 = Bloodshot's Transparant Avatars Bootleg Combo",
    "2 = Nikfrozty's Transparent Crisis Core Avatars",
    "3 = Nikfrozty's Tranparent Alternative Avatars",
    "4 = Full Portrait Transparent Avatars",
    "5 = Milo Leonhart's 10th Anniversary Photographic Avatars",
    "6 = Milo Leonhart's Demi Face Avatars",
    "7 = Milo Leonhart's Demi Face Avatars V2",
    "8 = Milo Leonhart's Demi Face Avatars V3",
    "9 = Singular One's AC Transparent Avatars",
    "10 = Zendar's Round AC Avatars",
    "11 = Zendar's Round AC Avatars V2",
    "12 = Zendar's Round AC Avatars V3",
    "13 = Zendar's Round AC Avatars V4",
    "14 = Zendar's Round AC Avatars V5",
    "15 = Zendar's Round AC Avatars V5.1",
    "16 = Armorvil's Eye Avatars",
    "17 = Grimmy's AC Style Avatars",
    "18 = Kula Wende's AC Style Avatars",
    "19 = Nero's AC Style Avatars",
    "20 = Nikfrozty's AC Style Avatars",
    "21 = Aff7iction's Beautified Avatars",
    "22 = MinMin's Avatars",
    "23 = Recko's Transparent Avatars",
    ]

def find_soundtrack():
    return [
    "Pick which soundtrack to install:",
    "1 = FinalFanTim's OGG Soundtrack",
    "2 = PSF MIDI Soundtrack",
    "3 = OCRemix Soundtrack",
    "4 = Custom Soundtrack from the Remix",
    "5 = Bootleg Soundtrack",
    "6 = Anxious Heart - Original Selection",
    "7 = Anxious Heart - DLPB Selection",
    "8 = Anxious Heart - Fan Selection",
    "9 = Anxious Heart - Professional Selection",
    ]

def find_opening_credits():
    return [
    "Pick which opening credits to use:",
    "1 = Grimmy's Cloud and Sephiroth Prelude Credits",
    "2 = JordieBo's Prelude Credits",
    "3 = JordieBo's Dark Prelude Credits",
    "4 = JordieBo's Glowing Prelude Credits",
    "5 = Strayoff's Prelude Credits",
    "6 = Grimmy's Cloud and Tifa Prelude Credits",
    ]

def find_buster_sword():
    return [
    "Pick the Buster Sword replacement:",
    "1 = Millenia's Buster Sword",
    "2 = Slayernext's Buster Sword",
    "3 = Mike's Buster Sword",
    "4 = APZ's Buster Sword",
    "5 = Omni Buster Sword",
    "6 = Masamune as Buster Sword",
    ]

def find_mythril_saber():
    return [
    "Pick the Mythril Saber replacement:",
    "1 = Millenia's Mythril Saber",
    "2 = Slayernext's Mythril Saber",
    ]

def find_hardedge():
    return [
    "Pick the Hardedge replacement:",
    "1 = Millenia's Hardedge",
    "2 = Slayernext's Hardedge",
    ]

def find_butterfly_edge():
    return [
    "Pick the Butterfly Edge replacement:",
    "1 = Millenia's Butterfly Edge",
    "2 = Slayernext's Butterfly Edge",
    ]

def find_enhance_sword():
    return [
    "Pick the Enhance Sword replacement:",
    "1 = Millenia's Butterfly Edge",
    "2 = Slayernext's Butterfly Edge",
    ]

def find_organics():
    return [
    "Pick the Organics replacement:",
    "1 = Millenia's Organics",
    "2 = Slayernext's Organics",
    ]

def find_crystal_sword():
    return [
    "Pick the Crystal Sword replacement:",
    "1 = Millenia's Crystal Sword",
    "2 = Slayernext's Crystal Sword",
    ]

def find_force_stealer():
    return [
    "Pick the Force Stealer replacement:",
    "1 = Millenia's Force Stealer",
    "2 = Slayernext's Force Stealer",
    ]

def find_rune_blade():
    return [
    "Pick the Rune Blade replacement:",
    "1 = Millenia's Rune Blade",
    "2 = Slayernext's Rune Blade",
    ]

def find_murasame():
    return [
    "Pick the Murasame replacement:",
    "1 = Millenia's Murasame",
    "2 = Slayernext's Murasame",
    "3 = Dragon Murasame",
    "4 = Oblivion Lovelace as Murasame",
    ]

def find_nail_bat():
    return [
    "Pick the Nail Bat replacement:",
    "1 = Millenia's Nail Bat",
    "2 = Slayernext's Nail Bat",
    ]

def find_yoshiyuki():
    return [
    "Pick the Yoshiyuki replacement:",
    "1 = Millenia's Yoshiyuki",
    "2 = Slayernext's Yoshiyuki",
    ]

def find_apocalypse():
    return [
    "Pick the Apocalypse replacement:",
    "1 = Millenia's Apocalypse",
    "2 = Slayernext's Apocalypse",
    ]

def find_heavens_cloud():
    return [
    "Pick the Heaven's Cloud replacement:",
    "1 = Millenia's Heaven's Cloud",
    "2 = Slayernext's Heaven's Cloud",
    ]

def find_ragnarok():
    return [
    "Pick the Ragnarok replacement:",
    "1 = Millenia's Ragnarok",
    "2 = Slayernext's Ragnarok",
    "3 = APZ's Ragnarok",
    ]

def find_ultima_weapon():
    return [
    "Pick the Ultima Weapon replacement:",
    "1 = Millenia's Ultima Weapon",
    "2 = Slayernext's Ultima Weapon",
    "3 = Mike's Ultima Weapon",
    "4 = Oblivion External Mod Ultima Weapon",
    ]

# From this point are the installer functions for each of the above parameters

# Use the ExecuteFile() method to launch a mod directly
# It will automatically stop the execution if the mod can't be found

def avalanche():
    ExecuteFile(fl.AVALANCHE)

    CopyFolder(var.BOOTLEG_TEMP + "Sprinkles\\AvalancheRepair\\magic", fl.MAGIC_PATCH)

    CopyFile(var.FFVII_PATH + "textures\\Summons\\leviathan", "water_00.png", "water_1_00.png")

def avalanche_gui():
    ExecuteFile(fl.AVALANCHEGUI)

def romeo_mat():
    CopyFolder(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Textures\\Menu\\Romeo14\\Materia_Advent", fl.MODS_FINAL + "menu")

def hardcore_gjoerulv():
    ExtractFile(fl.HARDCORE)

    log.help("SET_LOCATION", "'{0}data'".format(var.FFVII_PATH), "")
    if var.GAME_VERSION in (2012, 2013):
        log.help("PICK_1997_" + str(var.GAME_VERSION))

    shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Patch102\\ff7.exe", var.FFVII_PATH + "ff7.exe")

    LaunchFile(fl.HARDCORE, "Gjoerulv.exe")

    for file in ("kernel\\KERNEL.BIN", "kernel\\kernel2.bin", "battle\\scene.bin"):
        shutil.copy(var.FFVII_PATH + "data\\" + file, var.BOOTLEG_TEMP + "hardcore_backup\\" + file)

def aerith_revival():
    ExtractFile(fl.AERISREVIVAL)

    CopyFolder(var.BOOTLEG_TEMP + "Sprinkles\\Revival\\Flevel", var.BOOTLEG_TEMP + fl.AERISREVIVAL)

    shutil.copy(var.FFVII_PATH + "data\\field\\flevel.lgp", fl.FLEVEL_REVIVAL + "flevel.lgp")

def movies():
    if var.MOVIES in range(5, 9): # Rumbah's FMVs
        movies = {5: (7, "RUMBAHSMOOTH1280"), 6: (10, "RUMBAHSHARP1280"), 7: (4, "RUMBAHSMOOTH640"), 8: (4, "RUMBAHSHARP640")}
        max, file = movies[var.MOVIES]
        filef = getattr(fl, file)

        for num in range(1, max):
            FindFile(filef.format(num))

        ExtractFile(filef.format(1), "RumbahFMVs")

        # We got so far, so all the parts do exist and got successfully extracted
        CopyFolder(var.BOOTLEG_TEMP + "RumbahFMVs", var.FFVII_PATH + "movies")
        for mov in ("hit0", "hit1", "off"):
            DeleteFile(var.FFVII_PATH + "movies\\rcket{0}.avi".format(mov))
        RenameFile(var.FFVII_PATH + "movies", ["rckthit0.avi", "rckthit1.avi", "rcktoff.avi"], ["rckethit0.avi", "rckethit1.avi", "rcketoff.avi"])
        return

    for num in range(0, 7): # Install DLPB's videos - add others on top if needed
        FindFile(getattr(fl, "FMVRES" + str(num)))

    # All the files do exist
    log.logger("PARS_INSTALLING", form="FMVRES")
    ExecuteFile(fl.FMVRES0, "/verysilent")
    log.logger("PARS_COMPLETED", form="FMVRES")

    if var.MOVIES == 1: # DLPB's HQ videos
        return

    for part in (1, 2): # Trojak's Enhanced movies
        file = ""
        try:
            for num in range(1, 4):
                FindFile(fl.ENHANCEDMOVIESPARTS.format(num, part))
            if part == 2:
                FindFile(fl.ENHANCEDMOVIESPARTS.format(4, 2))
            file = fl.ENHANCEDMOVIESPARTS.format(1, part)
        except FileNotFoundError:
            try:
                FindFile(fl.ENHANCEDMOVIES.format(part))
                file = fl.ENHANCEDMOVIES.format(part)
            except FileNotFoundError:
                CallSkipMod(fl.ENHANCEDMOVIES.format(part)) # We want to go on and install the rest

        if file:
            log.logger("PARS_INST", form="ENHANCED_MOVIES" + str(part))
            ExtractFile(file, "EnhancedMovies")

    try: # Eidos Logo
        log.logger("PARS_INSTALLING", form="LOGO")
        logo, folder = FindFile(fl.LOGO)
        shutil.copy(folder + logo, var.FFVII_PATH + "movies\\eidoslogo.avi")
        log.logger("PARS_COMPLETED", form="LOGO")
    except FileNotFoundError:
        CallSkipMod(fl.LOGO)

    if var.MOVIES in (3, 9): # Grimmy's movies
        log.logger("PARS_INSTALLING", form="GRIMMY_MOVIES")
        for num in range(1, 8):
            try:
                ExtractFile(getattr(fl, "GRIMMY" + str(num)), "GrimmyMovies")
            except FileNotFoundError:
                continue
        if os.path.isdir(var.BOOTLEG_TEMP + "GrimmyMovies"):
            StripFolder(var.BOOTLEG_TEMP + "GrimmyMovies")
            CopyFolder(var.BOOTLEG_TEMP + "GrimmyMovies", var.FFVII_PATH + "movies")

    if var.MOVIES == 4: # Rumbah's movies
        try:
            FindFile(fl.MOVIE)
            log.logger("PARS_INSTALLING", form="RUMBAH_MOVIES")
            ExtractFile(fl.MOVIE)
            CopyFolder("{0}{1}\\{2}".format(var.BOOTLEG_TEMP, fl.MOVIE, var.RUMBAH_MOVIES), var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="RUMBAH_MOVIES")
        except FileNotFoundError:
            CallSkipMod(fl.MOVIE)

    if var.MOVIES in (9, 10): # Enhanced with Leonhart7413
        exists = True
        for num in range(1, 5):
            try:
                FindFile(fl.LEONHARTMOVIES.format(num))
            except FileNotFoundError:
                CallSkipMod(fl.LEONHARTMOVIES)
                exists = False
                break
        if exists:
            log.logger("PARS_INSTALLING", form="LEONHART_MOVIES")
            ExtractFile(fl.LEONHARTMOVIES.format(1), "LeonhartMovies")
            CopyFolder(var.BOOTLEG_TEMP + "LeonhartMovies", var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="LEONHART_MOVIES")

    if var.MOVIES == 10: # Enhanced with Leonhart7413 HD Alternate
        try:
            FindFile(fl.LEONHARTOPENING)
            log.logger("PARS_INSTALLING", form="LEONHART_OPENING")
            ExtractFile(fl.LEONHARTOPENING, "LeonhartOpening")
            CopyFolder(var.BOOTLEG_TEMP + "LeonhartOpening", var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="LEONHART_OPENING")
        except FileNotFoundError:
            CallSkipMod(fl.LEONHARTOPENING)

        try:
            for num in range(1, 4):
                FindFile(fl.LEONHARTLOGO.format(num))
            log.logger("PARS_INSTALLING", form="LEONHART_LOGO")
            ExtractFile(fl.LEONHARTLOGO.format(1), "LeonhartLogo")
            CopyFolder(var.BOOTLEG_TEMP + "LeonhartLogo", var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="LEONHART_LOGO")
        except FileNotFoundError:
            CallSkipMod(fl.LEONHARTLOGO)

    if var.MOVIES == 11: # Bootlegged reworked with PH03N1XFURY
        try:
            FindFile(fl.FMVSFMV)
            log.logger("PARS_INSTALLING", form="FURY_FMVS")
            ExtractFile(fl.FMVSFMV, "FuryFMVs")
            CopyFolder(var.BOOTLEG_TEMP + "FuryFMVs", var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="FURY_FMVS")
        except FileNotFoundError:
            CallSkipMod(fl.FMVSFMV)

        try:
            FindFile(fl.FUNERALFMV)
            log.logger("PARS_INSTALLING", form="FUNERAL_FMVS")
            ExtractFile(fl.FUNERALFMV, "FuneralFMV")
            CopyFolder(var.BOOTLEG_TEMP + "FuneralFMV", var.FFVII_PATH + "movies")
            log.logger("PARS_COMPLETED", form="FUNERAL_FMVS")
        except FileNotFoundError:
            CallSkipMod(fl.FUNERALFMV)

def fmv_no_cait():
    ExecuteFile(fl.FMVNOCAIT, "/verysilent")

def retranslated_fmv():
    ExecuteFile(fl.FMVRETRANS, "/verysilent")
