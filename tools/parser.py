from tools.logger import help

# Finding each variable's parameter if unset
# If a setting has only a yes/no choice, do NOT put it here
# It will be automatically added
# 0 is ALWAYS no change/no install

# Make sure to set the default in tools/variables.py
# and the maximum possible in tools/constants.py

def find_cloud_field():
    help("Pick Cloud's appearance in the field:")
    help("1 = WITHOUT sword")
    help("2 = WITH Buster sword")
    help("3 = Wielding Masamune")
    help("4 = Omni Cloud")
    help("5 = Squallff8's Rebuilded")
    help("6 = Grimmy's AC Style")
    help("7 = FMV with Sword (Weemus)")
    help("8 = FMV Without Sword (Weemus)")
    help("9 = Chibi Strife (NameSpoofer)")
    help("10 = APZ with Sword")
    help("11 = APZ without Sword")
    help("12 = APZ Black with Sword")
    help("13 = APZ Black without Sword")
    help("14 = APZ Dark with Sword")
    help("15 = APZ Dark without Sword")
    help("16 = APZ Chibi")
    help("17 = APZ Black Chibi")
    help("18 = APZ Dark Chibi")
    help("19 = BitzNCS New Chibi")
    help("20 = PRP Classic")
    help("21 = Chibi Reconstruction")
    help("22 = Dahfa's Chibi")
    help("23 = APZ Adjusted")
    help("24 = Team Avalanche Chibi")
    help("25 = Bloodshot's Edited TA")

def find_cloud_battle():
    help("Pick Cloud's appearance in battle:")
    help("1 = Classic")
    help("2 = The Remix APZ")
    help("3 = Grimmy's Hi Res")
    help("4 = Grimmy's AC Style")
    help("5 = FMV Cloud (Weemus)")
    help("6 = Strife")
    help("7 = New APZ")
    help("8 = New APZ Black")
    help("9 = New APZ Dark")
    help("10 = New APZ Mature")
    help("11 = Team Avalanche")
    help("12 = Bloodshot's Edited TA")

def find_trish_save():
    help("Pick the save point model:")
    help("1 = FFX Save Point Model")
    help("2 = Crisis Core Save Point Model")
    help("3 = Cloud's Memories Memories Save Point Model")
    help("4 = Team Avalanche Save Point Model")
    help("5 = Save Point with Balls")

def find_trish_phoenix():
    help("Pick the style of Mike's summons:")
    help("1 = New Style Flaming Phoenix")
    help("2 = Old Style Shaded Phoenix")
    help("3 = Old Style Phoenix with Custom Brighter Texture")

def find_trish_masamune():
    help("Use Mike's Masamune model?")

def find_aerith_revival():
    help("Use Aerith Revival")

def find_reunion():
    help("Install DLPB's Reunion?")

def find_spell_patch():
    help("Install the new spells patch?")

def find_avalanche():
    help("Install Team Avalanche's High-Res Graphics?")

def find_new_aerith():
    help("Choose the new Aerith model:")
    help("1 = HQ Aerith")
    help("2 = Sailor Jupiter Aerith")
    help("3 = Whiteraven HQ Aerith")

def find_vincent_battle():
    help("Choose Vincent's appearance in battle:")
    help("1 = ReModel with new Handgun")
    help("2 = New boots and Rifle")

def find_limit_break():
    help("Pick the Limit Break texture:")
    help("1 = Kela's V3 Limit in Original Colors")
    help("2 = Kela's V2 Limit in Blue")
    help("3 = Kela's V3 Limit in Blue")
    help("4 = Kela's V4 Limit in Blue")
    help("5 = Kela's V4 Limit in Original Colors")
    help("6 = Mike's Flame Limit Texture")
    help("7 = Jinkazama2k7's Green Limit")
    help("8 = Mike's Blue Flame Limit Texture")
    help("9 = Mike's Flame Limit V2 Texture")
    help("10 = JLOUTLAW's Hypersonic Limit")

def find_menu_background():
    help("Select the Start menu background:")
    help("1 = Remix Art")
    help("2 = Buster Sword in Red by Felix Leonhart")
    help("3 = HD Buster Sword by Wren Jr.")
    help("4 = Midgar")
    help("5 = Friends by Nikfrozty")
    help("6 = Cloud")
    help("7 = Simple")
    help("8 = Buster Sword")
    help("9 = Standoff")
    help("10 = Standoff with logo")
    help("11 = Zendar's AC Buster Sword")
    help("12 = Recko's Gold Hilt Buster Sword")

def find_kernel_select():
    help("Choose your game mode:")
    help("1 = Remastered - Kernel AI, stats and equipment from The Remix")
    help("2 = Scene Redux - Better Items to Steal")
    help("3 = Harder Items Easy")
    help("4 = Harder Items Normal")
    help("5 = Harder Items Difficult")
    help("6 = Harder Items Easy + Scene Redux")
    help("7 = Harder Items Normal + Scene Redux")
    help("8 = Harder Items Difficult + Scene Redux")
    help("9 = Lost Wing - Complete overhaul with extensive modifications") 
    help("10 = Gjoerulv's Hardcore mod")
    help("11 = Mode Switching - All Mods")
    help("12 = Mode Switching - Without Hardcore")
    help("13 = Reasonable Difficulty")
    help("14 = Reasonable Difficulty + Harder Items Easy")
    help("15 = Reasonable Difficulty + Harder Items Normal")
    help("16 = Reasonable Difficulty + Harder Items Difficult")

def find_movies():
    help("Choose the videos to use:")
    help("1 = DLPB's HQ videos")
    help("2 = Bootlegged - Trojak's Enhanced with DLBP and Xion999")
    help("3 = Bootlegged Further Enhanced with Grimmy")
    help("4 = Bootlegged Further Enhanced with Rumbah")
    help("5 = Rumbah Complete - 1280 Smooth")
    help("6 = Rumbah Complete - 1280 Sharp")
    help("7 = Rumbah Complete - 640 Smooth")
    help("8 = Rumbah Complete - 640 Sharp")
    help("9 = Grimmy's AC Style enhanced with Leonhart7413")
    help("10 = Grimmy's AC Style enhanced with Leonhart7413 HD Alternate")
    help("11 = Bootlegged reworked with PH03N1XFURY")
    help("12 = The Remix version of Grimmy's Videos")

def find_field_textures():
    help("Pick which set of field textures to use:")
    help("1 = Bootlegged: BlackFan and SL1982 Field Art")
    help("2 = BlackFan and SL1982 Field Art as Primary over FacePalmer")
    help("3 = FacePalmer Field Art Only")
    help("4 = BlackFan and SL1982 without FacePalmer")

def find_avatars():
    help("Select which set of avatars you want:")
    help("1 = Bloodshot's Transparant Avatars Bootleg Combo")
    help("2 = Nikfrozty's Transparent Crisis Core Avatars")
    help("3 = Nikfrozty's Tranparent Alternative Avatars")
    help("4 = Full Portrait Transparent Avatars")
    help("5 = Milo Leonhart's 10th Anniversary Photographic Avatars")
    help("6 = Milo Leonhart's Demi Face Avatars")
    help("7 = Milo Leonhart's Demi Face Avatars V2")
    help("8 = Milo Leonhart's Demi Face Avatars V3")
    help("9 = Singular One's AC Transparent Avatars")
    help("10 = Zendar's Round AC Avatars")
    help("11 = Zendar's Round AC Avatars V2")
    help("12 = Zendar's Round AC Avatars V3")
    help("13 = Zendar's Round AC Avatars V4")
    help("14 = Zendar's Round AC Avatars V5")
    help("15 = Zendar's Round AC Avatars V5.1")
    help("16 = Armorvil's Eye Avatars")
    help("17 = Grimmy's AC Style Avatars")
    help("18 = Kula Wende's AC Style Avatars")
    help("19 = Nero's AC Style Avatars")
    help("20 = Nikfrozty's AC Style Avatars")
    help("21 = Aff7iction's Beautified Avatars")
    help("22 = MinMin's Avatars")
    help("23 = Recko's Transparent Avatars")

def find_bunny_girls():
    help("Use the Bunny Girls models?")

def find_soundtrack():
    help("Pick which soundtrack to install:")
    help("1 = FinalFanTim's OGG Soundtrack")
    help("2 = PSF MIDI Soundtrack")
    help("3 = OCRemix Soundtrack")
    help("4 = Custom Soundtrack from the Remix")
    help("5 = Bootleg Soundtrack")
    help("6 = Anxious Heart - Original Selection")
    help("7 = Anxious Heart - DLPB Selection")
    help("8 = Anxious Heart - Fan Selection")
    help("9 = Anxious Heart - Professional Selection")

def find_opening_credits():
    help("Pick which opening credits to use:")
    help("1 = Grimmy's Cloud and Sephiroth Prelude Credits")
    help("2 = JordieBo's Prelude Credits")
    help("3 = JordieBo's Dark Prelude Credits")
    help("4 = JordieBo's Glowing Prelude Credits")
    help("5 = Strayoff's Prelude Credits")
    help("6 = Grimmy's Cloud and Tifa Prelude Credits")

def find_cloud_weapons():
    help("Choose Cloud's swords:")
    help("\n")
    help("Digit #1: Buster Sword replacement:")
    help("1 = Millenia's Buster Sword")
    help("2 = Slayernext's Buster Sword")
    help("3 = Mike's Buster Sword")
    help("4 = APZ's Buster Sword")
    help("5 = Omni Buster Sword")
    help("6 = Masamune as Buster Sword")
    help("\n")
    help("Digit #2: Mythril Saber replacement:")
    help("1 = Millenia's Mythril Saber")
    help("2 = Slayernext's Mythril Saber")
    help("\n")
    help("Digit #3: Hardedge replacement:")
    help("1 = Millenia's Hardedge")
    help("2 = Slayernext's Hardedge")
    help("\n")
    help("Digit #4: Butterfly Edge replacement:")
    help("1 = Millenia's Butterfly Edge")
    help("2 = Slayernext's Butterfly Edge")
    help("\n")
    help("Digit #5: Enhance Sword replacement:")
    help("1 = Millenia's Enhance Sword")
    help("2 = Slayernext's Enhance Sword")
    help("\n")
    help("Digit #6: Organics replacement:")
    help("1 = Millenia's Organics")
    help("2 = Slayernext's Organics")
    help("\n")
    help("Digit #7: Crystal Sword replacement:")
    help("1 = Millenia's Crystal Sword")
    help("2 = Slayernext's Crystal Sword")
    help("\n")
    help("Digit #8: Force Stealer replacement:")
    help("1 = Millenia's Force Stealer")
    help("2 = Slayernext's Force Stealer")
    help("\n")
    help("Digit #9: Rune Blade replacement:")
    help("1 = Millenia's Rune Blade")
    help("2 = Slayernext's Rune Blade")
    help("\n")
    help("Digit #10: Murasame replacement:")
    help("1 = Millenia's Murasame")
    help("2 = Slayernext's Murasame")
    help("3 = Dragon Murasame")
    help("4 = Oblivion Lovelace as Murasame")
    help("\n")
    help("Digit #11: Nail Bat replacement:")
    help("1 = Millenia's Nail Bat")
    help("2 = Slayernext's Nail Bat")
    help("\n")
    help("Digit #12: Yoshiyuki replacement:")
    help("1 = Millenia's Yoshiyuki")
    help("2 = Slayernext's Yoshiyuki")
    help("\n")
    help("Digit #13: Apocalypse replacement:")
    help("1 = Millenia's Apocalypse")
    help("2 = Slayernext's Apocalypse")
    help("\n")
    help("Digit #14: Heaven's Cloud replacement:")
    help("1 = Millenia's Heaven's Cloud")
    help("2 = Slayernext's Heaven's Cloud")
    help("\n")
    help("Digit #15: Ragnarok replacement:")
    help("1 = Millenia's Ragnarok")
    help("2 = Slayernext's Ragnarok")
    help("3 = APZ's Ragnarok")
    help("\n")
    help("Digit #16: Ultima Weapon replacement:")
    help("1 = Millenia's Ultima Weapon")
    help("2 = Slayernext's Ultima Weapon")
    help("3 = Mike's Ultima Weapon")
    help("4 = Oblivion External Mod Ultima Weapon")

def find_kernel_select(): # preset kernel settings for general use
    help("Pick your Kernel settings:")
    help("1 = Remastered - Kernel AI, stats and equipment from The Remix")
    help("2 = Scene Redux - Better items to steal")
    help("3 = Harder Items Easy - Items are less powerful")
    help("4 = Harder Items Normal - Items are significantly less powerful")
    help("5 = Harder Items Difficult - Items are much less powerful")
    help("6 = Harder Items Easy + Scene Redux")
    help("7 = Harder Items Normal + Scene Redux")
    help("8 = Harder Items Difficult + Scene Redux")
    help("9 = Lost Wing - Complete overhaul with extensive modifications") 
    help("10 = Gjoerulv's Hardcore Mod - The prominent difficulty mod")
    help("11 = Mode Switching - All mods")
    help("12 = Mode Switching - Without hardcore")
    help("13 = Reasonable Difficulty - Not as challenging as hardcore")
    help("14 = Reasonable Difficulty + Harder Items Easy")
    help("15 = Reasonable Difficulty + Harder Items Normal")
    help("16 = Reasonable Difficulty + Harder Items Difficult")

def find_reasonable_diff(): # individual parsers for each kernel selection. might or might not get used
    help("Install Reasonable Difficulty mod?")

def find_remastered_ai():
    help("Install the Remastered AI from the Remix?")

def find_scene_redux():
    help("Install Scene Redux?")

def find_items_easy():
    help("Install Harder Items Easy?")

def find_items_normal():
    help("Install Harder Items Normal?")

def find_items_difficult():
    help("Install Harder Items Difficult?")

def find_lost_wings():
    help("Install the Lost Wings complete overhaul?")

def find_mode_switching():
    help("Install Bootleg's Mode Switching?")