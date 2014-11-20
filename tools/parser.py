# Finding each variable's parameter if unset
# If a setting has only a yes/no choice, do NOT put the choices here (only the question)
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

# Get the custom exceptions

from tools.exceptions import *

def ExecuteFile(seeker):
    for folder in var.MOD_LOCATION:
        for file in os.listdir(folder):
            if file.lower() == seeker.lower():
                log.logger("PARS_EXTR_FILE", form=[file, folder[:-1]])
                subprocess.Popen([folder + file])
                return # We got it

    raise ModFileNotFound(seeker) # Exit out if the mod could not be found

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
    "25 = Bloodshot's Edited TA",    ]

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
    "12 = Bloodshot's Edited TA",    ]

def find_trish_save():
    return [
    "Pick the save point model:",
    "1 = FFX Save Point Model",
    "2 = Crisis Core Save Point Model",
    "3 = Cloud's Memories Memories Save Point Model",
    "4 = Team Avalanche Save Point Model",
    "5 = Save Point with Balls",    ]

def find_trish_phoenix():
    return [
    "Pick the style of Mike's summons:",
    "1 = New Style Flaming Phoenix",
    "2 = Old Style Shaded Phoenix",
    "3 = Old Style Phoenix with Custom Brighter Texture",    ]

def find_trish_masamune():
    return [
    "Use Mike's Masamune model?",    ]

def find_aerith_revival():
    return [
    "Use Aerith Revival",    ]

def find_reunion():
    return [
    "Install DLPB's Reunion?",    ]

def find_spell_patch():
    return [
    "Install the new spells patch?",    ]

def find_avalanche():
    return [
    "Install Team Avalanche's High-Res Graphics?",    ]

def find_new_aerith():
    return [
    "Choose the new Aerith model:",
    "1 = HQ Aerith",
    "2 = Sailor Jupiter Aerith",
    "3 = Whiteraven HQ Aerith",    ]

def find_vincent_battle():
    return [
    "Choose Vincent's appearance in battle:",
    "1 = ReModel with new Handgun",
    "2 = New boots and Rifle",    ]

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
    "10 = JLOUTLAW's Hypersonic Limit",    ]

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
    "12 = Recko's Gold Hilt Buster Sword",    ]

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
    "16 = Reasonable Difficulty + Harder Items Difficult",    ]

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
    "12 = The Remix version of Grimmy's Videos",    ]

def find_field_textures():
    return [
    "Pick which set of field textures to use:",
    "1 = Bootlegged: BlackFan and SL1982 Field Art",
    "2 = BlackFan and SL1982 Field Art as Primary over FacePalmer",
    "3 = FacePalmer Field Art Only",
    "4 = BlackFan and SL1982 without FacePalmer",    ]

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
    "23 = Recko's Transparent Avatars",    ]

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
    "9 = Anxious Heart - Professional Selection",    ]

def find_opening_credits():
    return [
    "Pick which opening credits to use:",
    "1 = Grimmy's Cloud and Sephiroth Prelude Credits",
    "2 = JordieBo's Prelude Credits",
    "3 = JordieBo's Dark Prelude Credits",
    "4 = JordieBo's Glowing Prelude Credits",
    "5 = Strayoff's Prelude Credits",
    "6 = Grimmy's Cloud and Tifa Prelude Credits",    ]

def find_cloud_swords():
    return [
    "Choose Cloud's swords:",
    "\n",
    "Digit #1: Buster Sword replacement:",
    "1 = Millenia's Buster Sword",
    "2 = Slayernext's Buster Sword",
    "3 = Mike's Buster Sword",
    "4 = APZ's Buster Sword",
    "5 = Omni Buster Sword",
    "6 = Masamune as Buster Sword",
    "\n",
    "Digit #2: Mythril Saber replacement:",
    "1 = Millenia's Mythril Saber",
    "2 = Slayernext's Mythril Saber",
    "\n",
    "Digit #3: Hardedge replacement:",
    "1 = Millenia's Hardedge",
    "2 = Slayernext's Hardedge",
    "\n",
    "Digit #4: Butterfly Edge replacement:",
    "1 = Millenia's Butterfly Edge",
    "2 = Slayernext's Butterfly Edge",
    "\n",
    "Digit #5: Enhance Sword replacement:",
    "1 = Millenia's Enhance Sword",
    "2 = Slayernext's Enhance Sword",
    "\n",
    "Digit #6: Organics replacement:",
    "1 = Millenia's Organics",
    "2 = Slayernext's Organics",
    "\n",
    "Digit #7: Crystal Sword replacement:",
    "1 = Millenia's Crystal Sword",
    "2 = Slayernext's Crystal Sword",
    "\n",
    "Digit #8: Force Stealer replacement:",
    "1 = Millenia's Force Stealer",
    "2 = Slayernext's Force Stealer",
    "\n",
    "Digit #9: Rune Blade replacement:",
    "1 = Millenia's Rune Blade",
    "2 = Slayernext's Rune Blade",
    "\n",
    "Digit #10: Murasame replacement:",
    "1 = Millenia's Murasame",
    "2 = Slayernext's Murasame",
    "3 = Dragon Murasame",
    "4 = Oblivion Lovelace as Murasame",
    "\n",
    "Digit #11: Nail Bat replacement:",
    "1 = Millenia's Nail Bat",
    "2 = Slayernext's Nail Bat",
    "\n",
    "Digit #12: Yoshiyuki replacement:",
    "1 = Millenia's Yoshiyuki",
    "2 = Slayernext's Yoshiyuki",
    "\n",
    "Digit #13: Apocalypse replacement:",
    "1 = Millenia's Apocalypse",
    "2 = Slayernext's Apocalypse",
    "\n",
    "Digit #14: Heaven's Cloud replacement:",
    "1 = Millenia's Heaven's Cloud",
    "2 = Slayernext's Heaven's Cloud",
    "\n",
    "Digit #15: Ragnarok replacement:",
    "1 = Millenia's Ragnarok",
    "2 = Slayernext's Ragnarok",
    "3 = APZ's Ragnarok",
    "\n",
    "Digit #16: Ultima Weapon replacement:",
    "1 = Millenia's Ultima Weapon",
    "2 = Slayernext's Ultima Weapon",
    "3 = Mike's Ultima Weapon",
    "4 = Oblivion External Mod Ultima Weapon",    ]

def find_reasonable_diff(): # individual parsers for each kernel selection. might or might not get used
    return [
    "Install Reasonable Difficulty mod?",    ]

def find_remastered_ai():
    return [
    "Install the Remastered AI from the Remix?",    ]

def find_scene_redux():
    return [
    "Install Scene Redux?",    ]

def find_items_easy():
    return [
    "Install Harder Items Easy?",    ]

def find_items_normal():
    return [
    "Install Harder Items Normal?",    ]

def find_items_difficult():
    return [
    "Install Harder Items Difficult?",    ]

def find_lost_wings():
    return [
    "Install the Lost Wings complete overhaul?",    ]

def find_mode_switching():
    return [
    "Install Bootleg's Mode Switching?",
    ]

def find_avalanche():
    return [
    "Install Avalanche High-Res Overhaul?",
    ]

def find_avalanche_gui():
    return [
    "Install Avalanche GUI?",
    ]

def find_romeo_mat():
    return [
    "Install Romeo14's AC Style Materias for Avalanche?",
    ]

# From this point are the installer functions for each of the above parameters

# Return the mod name defined in the translate file
# Use the ExecuteFile() method to launch a mod directly
# It will automatically stop the execution if the mod can't be found

def install_avalanche():
    ExecuteFile(fl.AVALANCHE)

    for repair in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\AvalancheRepair\\magic"):
        shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\AvalancheRepair\\magic\\" + repair, fl.MAGIC_PATCH + repair)
    shutil.copy(var.FFVII_PATH + "textures\\Summons\\leviathan\\water_00.png", var.FFVII_PATH + "textures\\Summons\\leviathan\\water_1_00.png")

def install_avalanche_gui():
    ExecuteFile(fl.AVALANCHEGUI)

def install_romeo_mat():
    for file in os.listdir(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Textures\\Menu\\Romeo14\\Materia_Advent"):
        shutil.copy(var.BOOTLEG_TEMP + "Sprinkles\\Data\\Textures\\Menu\\Romeo14\\Materia_Advent\\" + file, fl.MODS_FINAL + "menu\\" + file)