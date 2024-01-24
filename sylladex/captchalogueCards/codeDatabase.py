import json
from random import *
from math import *
from sylladex.captchalogueCards.codeData import CodeData

from uiElement import UIElement

code_cypher = {

    # SPEACIAL CHARACTERS
    '!': {
        '1': 'Humankind',
        '2': 'GUSHER',
        '3': 'MIND',
        '4': 'MIND',
        '5': 'ASSAIL',
        '6': 'ASSAIL',
        '7': 'ASSAIL',
        '8': 'ASSAIL',
    },
    '?': {
        '1': 'Trollkind',
        '2': 'DIAMOND',
        '3': 'META',
        '4': 'META',
        '5': 'ASTONISH',
        '6': 'ASTONISH',
        '7': 'ASTONISH',
        '8': 'ASTONISH',
    },

    # NUMBERED CHARCTERS
    '0': {
        '1': 'Artifactkind',
        '2': 'DROP',
        '3': 'GENERIC',
        '4': 'GENERIC',
        '5': 'ASTRICT',
        '6': 'ASTRICT',
        '7': 'ASTRICT',
        '8': 'ASTRICT'
    },
    '1': {
        '1': 'Moduskind',
        '2': 'DROP',
        '3': 'STORAGE',
        '4': 'STORAGE',
        '5': 'NO ACTION',
        '6': 'NO ACTION',
        '7': 'NO ACTION',
        '8': 'NO ACTION'
    },
    '2': {
        '1': 'Hammerkind',
        '2': 'BLOCK',
        '3': 'LIGHTWEIGHT',
        '4': 'HOPE',
        '5': 'ASS',
        '6': 'ASS',
        '7': 'ASS',
        '8': 'ASS'
    },
    '3': {
        '1': 'Needlekind',
        '2': 'GUSHER',
        '3': 'MEAT',
        '4': 'TIME',
        '5': 'ASSERT',
        '6': 'ASSERT',
        '7': 'ASSERT',
        '8': 'ASSERT'
    },
    '4': {
        '1': 'Bladekind',
        '2': 'DIAMOND',
        '3': 'JPEG',
        '4': 'TRICKSTER',
        '5': 'ASTOUND',
        '6': 'ASTOUND',
        '7': 'ASTOUND',
        '8': 'ASTOUND'
    },
    '5': {
        '1': 'Bladekind',
        '2': 'DROP',
        '3': 'MAGNETIC',
        '4': 'RAGE',
        '5': 'ASPHIXIATE',
        '6': 'ASPHIXIATE',
        '7': 'ASPHIXIATE',
        '8': 'ASPHIXIATE'
    },
    '6': {
        '1': 'Bladekind',
        '2': 'BLOCK',
        '3': 'COMPUTER',
        '4': 'BLOOD',
        '5': 'ASTUN',
        '6': 'ASTUN',
        '7': 'ASTUN',
        '8': 'ASTUN'
    },
    '7': {
        '1': 'Bladekind',
        '2': 'GUSHER',
        '3': 'HEAVYWEIGHT',
        '4': 'DOOM',
        '5': 'ASSAULT',
        '6': 'ASSAULT',
        '7': 'ASSAULT',
        '8': 'ASSAULT'
    },
    '8': {
        '1': 'Bladekind',
        '2': 'DIAMOND',
        '3': 'FOOD',
        '4': 'WELSH',
        '5': 'ASTRINGE',
        '6': 'ASTRINGE',
        '7': 'ASTRINGE',
        '8': 'ASTRINGE'
    },
    '9': {
        '1': 'Pistolkind',
        '2': 'DROP',
        '3': 'SHARP',
        '4': 'LIGHT',
        '5': 'ASSECURE',
        '6': 'ASSECURE',
        '7': 'ASSECURE',
        '8': 'ASSECURE'
    },

    # UPPERCASE CHARACTERS
    'A': {
        '1': 'Lancekind',
        '2': 'BLOCK',
        '3': 'STICKY',
        '4': 'VOID',
        '5': 'ASSESS',
        '6': 'ASSESS',
        '7': 'ASSESS',
        '8': 'ASSESS'
    },
    'B': {
        '1': 'Thrwstarkind',
        '2': 'GUSHER',
        '3': 'BLUNT',
        '4': 'BREATH',
        '5': 'ASSUBJUGATE',
        '6': 'ASSUBJUGATE',
        '7': 'ASSUBJUGATE',
        '8': 'ASSUBJUGATE'
    },
    'C': {
        '1': 'Sicklekind',
        '2': 'DIAMOND',
        '3': 'CUTE',
        '4': 'GRIMDARK',
        '5': 'ASSURE',
        '6': 'ASSURE',
        '7': 'ASSURE',
        '8': 'ASSURE'
    },
    'D': {
        '1': 'Clawkind',
        '2': 'DROP',
        '3': 'PLANT',
        '4': 'LIFE',
        '5': 'ASSASINATE',
        '6': 'ASSASINATE',
        '7': 'ASSASINATE',
        '8': 'ASSASINATE'
    },
    'E': {
        '1': 'Chainsawkind',
        '2': 'BLOCK',
        '3': 'CANDY',
        '4': 'HEART',
        '5': 'ASSEVERATE',
        '6': 'ASSEVERATE',
        '7': 'ASSEVERATE',
        '8': 'ASSEVERATE'
    },
    'F': {
        '1': 'Canekind',
        '2': 'GUSHER',
        '3': 'VEHICLE',
        '4': 'SPACE',
        '5': 'ARRIVE',
        '6': 'ARRIVE',
        '7': 'ARRIVE',
        '8': 'ARRIVE'
    },
    'G': {
        '1': 'Dicekind',
        '2': 'DIAMOND',
        '3': 'SERIOUS',
        '4': 'ROCKET',
        '5': 'ARGUFY',
        '6': 'ARGUFY',
        '7': 'ARGUFY',
        '8': 'ARGUFY'
    },
    'H': {
        '1': 'Bowkind',
        '2': 'DROP',
        '3': 'RAD',
        '4': 'FAIRY',
        '5': 'ARSONATE',
        '6': 'ARSONATE',
        '7': 'ARSONATE',
        '8': 'ARSONATE'
    },
    'I': {
        '1': 'Clubkind',
        '2': 'BLOCK',
        '3': 'MUSICAL',
        '4': 'FROG',
        '5': 'ARTILLERATE',
        '6': 'ARTILLERATE',
        '7': 'ARTILLERATE',
        '8': 'ARTILLERATE'
    },
    'J': {
        '1': 'Wandkind',
        '2': 'GUSHER',
        '3': 'CHARLATAN',
        '4': 'NUCLEAR',
        '5': 'ARRANGE',
        '6': 'ARRANGE',
        '7': 'ARRANGE',
        '8': 'ARRANGE'
    },
    'K': {
        '1': 'Spearkind',
        '2': 'DIAMOND',
        '3': 'COMFY',
        '4': 'AVIAN',
        '5': 'ARREST',
        '6': 'ARREST',
        '7': 'ARREST',
        '8': 'ARREST'
    },
    'L': {
        '1': 'Bunnykind',
        '2': 'DROP',
        '3': 'HARLEQUIN',
        '4': 'NAUTICAL',
        '5': 'AROMATIZE',
        '6': 'AROMATIZE',
        '7': 'AROMATIZE',
        '8': 'AROMATIZE'
    },
    'M': {
        '1': 'Paperkind',
        '2': 'BLOCK',
        '3': 'WIZARD',
        '4': 'ARACHNID',
        '5': 'ARBITERATE',
        '6': 'ARBITERATE',
        '7': 'ARBITERATE',
        '8': 'ARBITERATE'
    },
    'N': {
        '1': 'Fncysntakind',
        '2': 'GUSHER',
        '3': 'FURRY',
        '4': 'DRACONIC',
        '5': 'ARCHIVE',
        '6': 'ARCHIVE',
        '7': 'ARCHIVE',
        '8': 'ARCHIVE'
    },
    'O': {
        '1': 'Umbrellakind',
        '2': 'DIAMOND',
        '3': 'FIRE',
        '4': 'PROSPIT',
        '5': 'ARROGATE',
        '6': 'ARROGATE',
        '7': 'ARROGATE',
        '8': 'ARROGATE'
    },
    'P': {
        '1': 'Broomkind',
        '2': 'DROP',
        '3': 'ICE',
        '4': 'EQUINE',
        '5': 'ARBORIZE',
        '6': 'ARBORIZE',
        '7': 'ARBORIZE',
        '8': 'ARBORIZE'
    },
    'Q': {
        '1': 'Flshlghtkind',
        '2': 'BLOCK',
        '3': 'SPOOKY',
        '4': 'CAPRINE',
        '5': 'ARMAMENTIFY',
        '6': 'ARMAMENTIFY',
        '7': 'ARMAMENTIFY',
        '8': 'ARMAMENTIFY'
    },
    'R': {
        '1': 'Sawkind',
        '2': 'GUSHER',
        '3': 'FELINE',
        '4': 'ANGELIC',
        '5': 'ARITHMETIZE',
        '6': 'ARITHMETIZE',
        '7': 'ARITHMETIZE',
        '8': 'ARITHMETIZE'
    },
    'S': {
        '1': 'Wrenchkind',
        '2': 'DIAMOND',
        '3': 'ELECTRIC',
        '4': 'DERSE',
        '5': 'ARTICULATE',
        '6': 'ARTICULATE',
        '7': 'ARTICULATE',
        '8': 'ARTICULATE'
    },
    'T': {
        '1': 'Scrwdrvrkind',
        '2': 'DROP',
        '3': 'BOUNCY',
        '4': 'VAMPIRIC',
        '5': 'ARISE',
        '6': 'ARISE',
        '7': 'ARISE',
        '8': 'ARISE'
    },
    'U': {
        '1': 'Plierkind',
        '2': 'BLOCK',
        '3': 'CANINE',
        '4': 'ANIME',
        '5': 'ARSENALIZE',
        '6': 'ARSENALIZE',
        '7': 'ARSENALIZE',
        '8': 'ARSENALIZE'
    },
    'V': {
        '1': 'Nailkind',
        '2': 'GUSHER',
        '3': 'PLUSH',
        '4': 'NOIR',
        '5': 'ACCEDE',
        '6': 'ACCEDE',
        '7': 'ACCEDE',
        '8': 'ACCEDE'
    },
    'W': {
        '1': 'Crowbarkind',
        '2': 'DIAMOND',
        '3': 'NOIR',
        '4': 'PLUSH',
        '5': 'ACCUSE',
        '6': 'ACCUSE',
        '7': 'ACCUSE',
        '8': 'ACCUSE'
    },
    'X': {
        '1': 'Bookkind',
        '2': 'DROP',
        '3': 'ANIME',
        '4': 'CANINE',
        '5': 'ACCOST',
        '6': 'ACCOST',
        '7': 'ACCOST',
        '8': 'ACCOST'
    },
    'Y': {
        '1': 'Yoyokind',
        '2': 'BLOCK',
        '3': 'VAMPIRIC',
        '4': 'BOUNCY',
        '5': 'ACCRUE',
        '6': 'ACCRUE',
        '7': 'ACCRUE',
        '8': 'ACCRUE'
    },
    'Z': {
        '1': 'Staplerkind',
        '2': 'GUSHER',
        '3': 'DERSE',
        '4': 'ELECTRIC',
        '5': 'ACQUIRE',
        '6': 'ACQUIRE',
        '7': 'ACQUIRE',
        '8': 'ACQUIRE'
    },

    # LOWERCASE CHARACTERS
    'a': {
        '1': 'Shotgunkind',
        '2': 'DIAMOND',
        '3': 'ANGELIC',
        '4': 'FELINE',
        '5': 'ACCOY',
        '6': 'ACCOY',
        '7': 'ACCOY',
        '8': 'ACCOY'
    },
    'b': {
        '1': 'Pencilkind',
        '2': 'DROP',
        '3': 'CAPRINE',
        '4': 'SPOOKY',
        '5': 'ACQUIT',
        '6': 'ACQUIT',
        '7': 'ACQUIT',
        '8': 'ACQUIT'
    },
    'c': {
        '1': 'Brushkind',
        '2': 'BLOCK',
        '3': 'EQUINE',
        '4': 'ICE',
        '5': 'ACCOUNT',
        '6': 'ACCOUNT',
        '7': 'ACCOUNT',
        '8': 'ACCOUNT'
    },
    'd': {
        '1': 'Scythekind',
        '2': 'GUSHER',
        '3': 'PROSPIT',
        '4': 'FIRE',
        '5': 'ACCESSORIZE',
        '6': 'ACCESSORIZE',
        '7': 'ACCESSORIZE',
        '8': 'ACCESSORIZE'
    },
    'e': {
        '1': 'Scissorkind',
        '2': 'DIAMOND',
        '3': 'DRACONIC',
        '4': 'FURRY',
        '5': 'ACTUALIZE',
        '6': 'ACTUALIZE',
        '7': 'ACTUALIZE',
        '8': 'ACTUALIZE'
    },
    'f': {
        '1': 'Knifekind',
        '2': 'DROP',
        '3': 'ARACHNID',
        '4': 'WIZARD',
        '5': 'ACCUMULATE',
        '6': 'ACCUMULATE',
        '7': 'ACCUMULATE',
        '8': 'ACCUMULATE'
    },
    'g': {
        '1': 'Shovelkind',
        '2': 'BLOCK',
        '3': 'NAUTICAL',
        '4': 'HARLEQUIN',
        '5': 'ACCELERATE',
        '6': 'ACCELERATE',
        '7': 'ACCELERATE',
        '8': 'ACCELERATE'
    },
    'h': {
        '1': 'Cordkind',
        '2': 'GUSHER',
        '3': 'AVIAN',
        '4': 'COMFY',
        '5': 'ACCLIMATE',
        '6': 'ACCLIMATE',
        '7': 'ACCLIMATE',
        '8': 'ACCLIMATE'
    },
    'i': {
        '1': 'Axekind',
        '2': 'DIAMOND',
        '3': 'NUCLEAR',
        '4': 'CHARLATAN',
        '5': 'ACERBATE',
        '6': 'ACERBATE',
        '7': 'ACERBATE',
        '8': 'ACERBATE'
    },
    'j': {
        '1': 'Dartkind',
        '2': 'DROP',
        '3': 'FROG',
        '4': 'MUSICAL',
        '5': 'ACCLAIM',
        '6': 'ACCLAIM',
        '7': 'ACCLAIM',
        '8': 'ACCLAIM'
    },
    'k': {
        '1': 'Chainkind',
        '2': 'BLOCK',
        '3': 'FAIRY',
        '4': 'RAD',
        '5': 'ACHIEVE',
        '6': 'ACHIEVE',
        '7': 'ACHIEVE',
        '8': 'ACHIEVE'
    },
    'l': {
        '1': 'Ballkind',
        '2': 'GUSHER',
        '3': 'ROCKET',
        '4': 'SERIOUS',
        '5': 'ABASH',
        '6': 'ABASH',
        '7': 'ABASH',
        '8': 'ABASH'
    },
    'm': {
        '1': 'Rockkind',
        '2': 'DIAMOND',
        '3': 'SPACE',
        '4': 'VEHICLE',
        '5': 'ABSIST',
        '6': 'ABSIST',
        '7': 'ABSIST',
        '8': 'ABSIST'
    },
    'n': {
        '1': 'Hckystckkind',
        '2': 'DROP',
        '3': 'HEART',
        '4': 'CANDY',
        '5': 'ABSTAIN',
        '6': 'ABSTAIN',
        '7': 'ABSTAIN',
        '8': 'ABSTAIN'
    },
    'o': {
        '1': 'Tridentkind',
        '2': 'BLOCK',
        '3': 'LIFE',
        '4': 'PLANT',
        '5': 'ABJUDGE',
        '6': 'ABJUDGE',
        '7': 'ABJUDGE',
        '8': 'ABJUDGE'
    },
    'p': {
        '1': 'Razorkind',
        '2': 'GUSHER',
        '3': 'GRIMDARK',
        '4': 'CUTE',
        '5': 'ABERRATE',
        '6': 'ABERRATE',
        '7': 'ABERRATE',
        '8': 'ABERRATE'
    },
    'q': {
        '1': 'Fankind',
        '2': 'DIAMOND',
        '3': 'BREATH',
        '4': 'BLUNT',
        '5': 'ABDUCT',
        '6': 'ABDUCT',
        '7': 'ABDUCT',
        '8': 'ABDUCT'
    },
    'r': {
        '1': 'Cardkind',
        '2': 'DROP',
        '3': 'VOID',
        '4': 'STICKY',
        '5': 'ABJURE',
        '6': 'ABJURE',
        '7': 'ABJURE',
        '8': 'ABJURE'
    },
    's': {
        '1': 'Armorkind',
        '2': 'BLOCK',
        '3': 'LIGHT',
        '4': 'SHARP',
        '5': 'ABOLISH',
        '6': 'ABOLISH',
        '7': 'ABOLISH',
        '8': 'ABOLISH'
    },
    't': {
        '1': 'Disckind',
        '2': 'GUSHER',
        '3': 'WELSH',
        '4': 'FOOD',
        '5': 'ABSORB',
        '6': 'ABSORB',
        '7': 'ABSORB',
        '8': 'ABSORB'
    },
    'u': {
        '1': 'Hatkind',
        '2': 'DIAMOND',
        '3': 'DOOM',
        '4': 'HEAVYWEIGHT',
        '5': 'ABBREVIATE',
        '6': 'ABBREVIATE',
        '7': 'ABBREVIATE',
        '8': 'ABBREVIATE'
    },
    'v': {
        '1': 'Glasseskind',
        '2': 'DROP',
        '3': 'BLOOD',
        '4': 'COMPUTER',
        '5': 'ABATE',
        '6': 'ABATE',
        '7': 'ABATE',
        '8': 'ABATE'
    },
    'w': {
        '1': 'Picturekind',
        '2': 'BLOCK',
        '3': 'RAGE',
        '4': 'MAGNETIC',
        '5': 'ABORT',
        '6': 'ABORT',
        '7': 'ABORT',
        '8': 'ABORT'
    },
    'x': {
        '1': 'Shoekind',
        '2': 'GUSHER',
        '3': 'TRICKSTER',
        '4': 'JPEG',
        '5': 'ABUSE',
        '6': 'ABUSE',
        '7': 'ABUSE',
        '8': 'ABUSE'
    },
    'y': {
        '1': 'Furniturekind',
        '2': 'DIAMOND',
        '3': 'TIME',
        '4': 'MEAT',
        '5': 'ABIDE',
        '6': 'ABIDE',
        '7': 'ABIDE',
        '8': 'ABIDE'
    },
    'z': {
        '1': 'Consortkind',
        '2': 'DROP',
        '3': 'HOPE',
        '4': 'LIGHTWEIGHT',
        '5': 'ABHOR',
        '6': 'ABHOR',
        '7': 'ABHOR',
        '8': 'ABHOR'
    },
}

# Weaponkind Data

weaponkind_type = {
    'Humankind': 'NA',
    'Trollkind': 'NA',
    'Artifactkind': 'NA',
    'Moduskind': 'NA',
    'Hammerkind': 'MELEE',
    'Needlekind': 'MELEE',
    'Bladekind': 'MELEE',
    'Riflekind': 'RANGED',
    'Utensilkind': 'MELEE',
    'Fistkind': 'MELEE',
    'Puppetkind': 'MAGIC',
    'Pistolkind': 'RANGED',
    'Lancekind': 'MELEE',
    'Thrwstarkind': 'RANGED',
    'Sicklekind': 'MELEE',
    'Clawkind': 'MELEE',
    'Chainsawkind': 'MELEE',
    'Canekind': 'MELEE',
    'Dicekind': 'MAGIC',
    'Disckind': 'NA',
    'Bowkind': 'RANGED',
    'Clubkind': 'MELEE',
    'Wandkind': 'MAGIC',
    'Spearkind': 'RANGED',
    'Bunnykind': 'MAGIC',
    'Paperkind': 'MELEE',
    'Fncysntakind': 'MAGIC',
    'Umbrellakind': 'MAGIC',
    'Broomkind': 'MAGIC',
    'Flshlghtkind': 'MAGIC',
    'Sawkind': 'MELEE',
    'Wrenchkind': 'MELEE',
    'Scrwdrvrkind': 'MELEE',
    'Plierkind': 'MELEE',
    'Nailkind': 'MELEE',
    'Crowbarkind': 'MELEE',
    'Bookkind': 'MAGIC',
    'Yoyokind': 'RANGED',
    'Staplerkind': 'RANGED',
    'Shotgunkind': 'RANGED',
    'Pencilkind': 'MAGIC',
    'Brushkind': 'MAGIC',
    'Scythekind': 'MELEE',
    'Scissorkind': 'MELEE',
    'Knifekind': 'MELEE',
    'Shovelkind': 'MELEE',
    'Cordkind': 'MELEE',
    'Axekind': 'MELEE',
    'Dartkind': 'RANGED',
    'Chainkind': 'MELEE',
    'Ballkind': 'RANGED',
    'Rockkind': 'RANGED',
    'Hckystckkind': 'MELEE',
    'Tridentkind': 'MELEE',
    'Razorkind': 'MELEE',
    'Fankind': 'MAGIC',
    'Cardkind': 'MAGIC',
    'Armorkind': 'NA',
    'Disckind': 'NA',
    'Hatkind': 'NA',
    'Glasseskind': 'NA',
    'Picturekind': 'NA',
    'Shoekind': 'NA',
    'Furniturekind': 'NA',
    'Consortkind': 'NA'
}

kind_image = {
    'Armorkind': 'sylladex/uiElements/asset/KINDS/ArmorKind.png',
    'Artifactkind': 'sylladex/uiElements/asset/KINDS/ArtifactKind.png',
    'Axekind': 'sylladex/uiElements/asset/KINDS/AxeKind.png',
    'Ballkind': 'sylladex/uiElements/asset/KINDS/BallKind.png',
    'Bladekind': 'sylladex/uiElements/asset/KINDS/BladeKind.png',
    'Bookkind': 'sylladex/uiElements/asset/KINDS/BookKind.png',
    'Bowkind': 'sylladex/uiElements/asset/KINDS/BowKind.png',
    'Broomkind': 'sylladex/uiElements/asset/KINDS/BroomKind.png',
    'Brushkind': 'sylladex/uiElements/asset/KINDS/BrushKind.png',
    'Bunnykind': 'sylladex/uiElements/asset/KINDS/BunnyKind.png',
    'Canekind': 'sylladex/uiElements/asset/KINDS/CaneKind.png',
    'Cardkind': 'sylladex/uiElements/asset/KINDS/CardKind.png',
    'Chainkind': 'sylladex/uiElements/asset/KINDS/ChainKind.png',
    'Chainsawkind': 'sylladex/uiElements/asset/KINDS/ChainsawKind.png',
    'Clawkind': 'sylladex/uiElements/asset/KINDS/ClawKind.png',
    'Clubkind': 'sylladex/uiElements/asset/KINDS/ClubKind.png',
    'Consortkind': 'sylladex/uiElements/asset/KINDS/BustKind.png',
    'Cordkind': 'sylladex/uiElements/asset/KINDS/CordKind.png',
    'Crowbarkind': 'sylladex/uiElements/asset/KINDS/CrowbarKind.png',
    'Customkind': 'sylladex/uiElements/asset/KINDS/CustomKind.png',
    'Dartkind': 'sylladex/uiElements/asset/KINDS/DartKind.png',
    'Dicekind': 'sylladex/uiElements/asset/KINDS/DiceKind.png',
    'Disckind': 'sylladex/uiElements/asset/KINDS/BallKind.png',
    'Fankind': 'sylladex/uiElements/asset/KINDS/FanKind.png',
    'Fistkind': 'sylladex/uiElements/asset/KINDS/FistKind.png',
    'Flshlghtkind': 'sylladex/uiElements/asset/KINDS/FlshlghtKind.png',
    'Fncysntakind': 'sylladex/uiElements/asset/KINDS/FncysntaKind.png',
    'Furniturekind': 'sylladex/uiElements/asset/KINDS/FurnitureKind.png',
    'Glasseskind': 'sylladex/uiElements/asset/KINDS/GlassesKind.png',
    'Hammerkind': 'sylladex/uiElements/asset/KINDS/HammerKind.png',
    'Hatkind': 'sylladex/uiElements/asset/KINDS/HatKind.png',
    'Hckystckkind': 'sylladex/uiElements/asset/KINDS/HckystckKind.png',
    'Humankind': 'sylladex/uiElements/asset/KINDS/BustKind.png',
    'Knifekind': 'sylladex/uiElements/asset/KINDS/KnifeKind.png',
    'Lancekind': 'sylladex/uiElements/asset/KINDS/LanceKind.png',
    'Moduskind': 'sylladex/uiElements/asset/KINDS/ModusKind.png',
    'Nailkind': 'sylladex/uiElements/asset/KINDS/NailKind.png',
    'Needlekind': 'sylladex/uiElements/asset/KINDS/NeedleKind.png',
    'Paperkind': 'sylladex/uiElements/asset/KINDS/PaperKind.png',
    'Pencilkind': 'sylladex/uiElements/asset/KINDS/PencilKind.png',
    'Picturekind': 'sylladex/uiElements/asset/KINDS/PictureKind.png',
    'Pistolkind': 'sylladex/uiElements/asset/KINDS/PistolKind.png',
    'Plierkind': 'sylladex/uiElements/asset/KINDS/PlierKind.png',
    'Puppetkind': 'sylladex/uiElements/asset/KINDS/PuppetKind.png',
    'Razorkind': 'sylladex/uiElements/asset/KINDS/RazorKind.png',
    'Riflekind': 'sylladex/uiElements/asset/KINDS/RifleKind.png',
    'Rockkind': 'sylladex/uiElements/asset/KINDS/RockKind.PNG',
    'Sawkind': 'sylladex/uiElements/asset/KINDS/SawKind.png',
    'Scissorkind': 'sylladex/uiElements/asset/KINDS/ScissorKind.png',
    'Scrwdrvrkind': 'sylladex/uiElements/asset/KINDS/ScrwdrvrKind.png',
    'Scythekind': 'sylladex/uiElements/asset/KINDS/ScytheKind.png',
    'Shoekind': 'sylladex/uiElements/asset/KINDS/ShoeKind.png',
    'Shotgunkind': 'sylladex/uiElements/asset/KINDS/ShotgunKind.png',
    'Shovelkind': 'sylladex/uiElements/asset/KINDS/ShovelKind.png',
    'Sicklekind': 'sylladex/uiElements/asset/KINDS/SickleKind.png',
    'Spearkind': 'sylladex/uiElements/asset/KINDS/SpearKind.png',
    'Staplerkind': 'sylladex/uiElements/asset/KINDS/StaplerKind.png',
    'Thrwstarkind': 'sylladex/uiElements/asset/KINDS/ThrwstarKind.png',
    'Tridentkind': 'sylladex/uiElements/asset/KINDS/TridentKind.png',
    'Trollkind': 'sylladex/uiElements/asset/KINDS/BustKind.png',
    'Umbrellakind': 'sylladex/uiElements/asset/KINDS/UmbrellaKind.png',
    'Utensilkind': 'sylladex/uiElements/asset/KINDS/UtensilKind.png',
    'Wandkind': 'sylladex/uiElements/asset/KINDS/WandKind.png',
    'Wrenchkind': 'sylladex/uiElements/asset/KINDS/WrenchKind.png',
    'Yoyokind': 'sylladex/uiElements/asset/KINDS/YoyoKind.png',
}

kind_image_small = {
    'Armorkind': 'sylladex/uiElements/asset/KINDS/SMALL/ArmorKind.png',
    'Artifactkind': 'sylladex/uiElements/asset/KINDS/SMALL/ArtifactKind.png',
    'Axekind': 'sylladex/uiElements/asset/KINDS/SMALL/AxeKind.png',
    'Ballkind': 'sylladex/uiElements/asset/KINDS/SMALL/BallKind.png',
    'Bladekind': 'sylladex/uiElements/asset/KINDS/SMALL/BladeKind.png',
    'Bookkind': 'sylladex/uiElements/asset/KINDS/SMALL/BookKind.png',
    'Bowkind': 'sylladex/uiElements/asset/KINDS/SMALL/BowKind.png',
    'Broomkind': 'sylladex/uiElements/asset/KINDS/SMALL/BroomKind.png',
    'Brushkind': 'sylladex/uiElements/asset/KINDS/SMALL/BrushKind.png',
    'Bunnykind': 'sylladex/uiElements/asset/KINDS/SMALL/BunnyKind.png',
    'Bustkind': 'sylladex/uiElements/asset/KINDS/SMALL/BustKind.png',
    'Canekind': 'sylladex/uiElements/asset/KINDS/SMALL/CaneKind.png',
    'Cardkind': 'sylladex/uiElements/asset/KINDS/SMALL/CardKind.png',
    'Chainkind': 'sylladex/uiElements/asset/KINDS/SMALL/ChainKind.png',
    'Chainsawkind': 'sylladex/uiElements/asset/KINDS/SMALL/ChainsawKind.png',
    'Clawkind': 'sylladex/uiElements/asset/KINDS/SMALL/ClawKind.png',
    'Clubkind': 'sylladex/uiElements/asset/KINDS/SMALL/ClubKind.png',
    'Cordkind': 'sylladex/uiElements/asset/KINDS/SMALL/CordKind.png',
    'Crowbarkind': 'sylladex/uiElements/asset/KINDS/SMALL/CrowbarKind.png',
    'Customkind': 'sylladex/uiElements/asset/KINDS/SMALL/CustomKind.png',
    'Dartkind': 'sylladex/uiElements/asset/KINDS/SMALL/DartKind.png',
    'Dicekind': 'sylladex/uiElements/asset/KINDS/SMALL/DiceKind.png',
    'Disckind': 'sylladex/uiElements/asset/KINDS/SMALL/BallKind.png',
    'Fankind': 'sylladex/uiElements/asset/KINDS/SMALL/FanKind.png',
    'Fistkind': 'sylladex/uiElements/asset/KINDS/SMALL/FistKind.png',
    'Flshlghtkind': 'sylladex/uiElements/asset/KINDS/SMALL/FlshlghtKind.png',
    'Fncysntakind': 'sylladex/uiElements/asset/KINDS/SMALL/FncysntaKind.png',
    'Furniturekind': 'sylladex/uiElements/asset/KINDS/SMALL/FurnitureKind.png',
    'Glasseskind': 'sylladex/uiElements/asset/KINDS/SMALL/GlassesKind.png',
    'Hammerkind': 'sylladex/uiElements/asset/KINDS/SMALL/HammerKind.png',
    'Hatkind': 'sylladex/uiElements/asset/KINDS/SMALL/HatKind.png',
    'Hckystckkind': 'sylladex/uiElements/asset/KINDS/SMALL/HckystckKind.png',
    'Knifekind': 'sylladex/uiElements/asset/KINDS/SMALL/KnifeKind.png',
    'Lancekind': 'sylladex/uiElements/asset/KINDS/SMALL/LanceKind.png',
    'Moduskind': 'sylladex/uiElements/asset/KINDS/SMALL/ModusKind.png',
    'Nailkind': 'sylladex/uiElements/asset/KINDS/SMALL/NailKind.png',
    'Needlekind': 'sylladex/uiElements/asset/KINDS/SMALL/NeedleKind.png',
    'Paperkind': 'sylladex/uiElements/asset/KINDS/SMALL/PaperKind.png',
    'Pencilkind': 'sylladex/uiElements/asset/KINDS/SMALL/PencilKind.png',
    'Picturekind': 'sylladex/uiElements/asset/KINDS/SMALL/PictureKind.png',
    'Pistolkind': 'sylladex/uiElements/asset/KINDS/SMALL/PistolKind.png',
    'Plierkind': 'sylladex/uiElements/asset/KINDS/SMALL/PlierKind.png',
    'Puppetkind': 'sylladex/uiElements/asset/KINDS/SMALL/PuppetKind.png',
    'Razorkind': 'sylladex/uiElements/asset/KINDS/SMALL/RazorKind.png',
    'Riflekind': 'sylladex/uiElements/asset/KINDS/SMALL/RifleKind.png',
    'Rockkind': 'sylladex/uiElements/asset/KINDS/SMALL/RockKind.PNG',
    'Sawkind': 'sylladex/uiElements/asset/KINDS/SMALL/SawKind.png',
    'Scissorkind': 'sylladex/uiElements/asset/KINDS/SMALL/ScissorKind.png',
    'Scrwdrvrkind': 'sylladex/uiElements/asset/KINDS/SMALL/ScrwdrvrKind.png',
    'Scythekind': 'sylladex/uiElements/asset/KINDS/SMALL/ScytheKind.png',
    'Shoekind': 'sylladex/uiElements/asset/KINDS/SMALL/ShoeKind.png',
    'Shotgunkind': 'sylladex/uiElements/asset/KINDS/SMALL/ShotgunKind.png',
    'Shovelkind': 'sylladex/uiElements/asset/KINDS/SMALL/ShovelKind.png',
    'Sicklekind': 'sylladex/uiElements/asset/KINDS/SMALL/SickleKind.png',
    'Spearkind': 'sylladex/uiElements/asset/KINDS/SMALL/SpearKind.png',
    'Staplerkind': 'sylladex/uiElements/asset/KINDS/SMALL/StaplerKind.png',
    'Thrwstarkind': 'sylladex/uiElements/asset/KINDS/SMALL/ThrwstarKind.png',
    'Tridentkind': 'sylladex/uiElements/asset/KINDS/SMALL/TridentKind.png',
    'Umbrellakind': 'sylladex/uiElements/asset/KINDS/SMALL/UmbrellaKind.png',
    'Utensilkind': 'sylladex/uiElements/asset/KINDS/SMALL/UtensilKind.png',
    'Vehiclekind': 'sylladex/uiElements/asset/KINDS/SMALL/VehicleKind.png',
    'Wandkind': 'sylladex/uiElements/asset/KINDS/SMALL/WandKind.png',
    'Wrenchkind': 'sylladex/uiElements/asset/KINDS/SMALL/WrenchKind.png',
    'Yoyokind': 'sylladex/uiElements/asset/KINDS/SMALL/YoyoKind.png',
}

# Trait data

trait_data = {
    'GENERIC': {
        'INTERACTION': '/',
        'MODUS SORT': 'CAPTCHALOGUED items are sorted onto the TOP of the STACK',
        'MODUS RETRIEVE': 'Items on the TOP of a STACK are retrievable',
        'STRIKE': '/',
        'EQUIPPED': '/',
        'SORT NAME': 'BASIC',
        'RETRIEVE NAME': 'STACK',
        'PASSIVE': '/'
    },
    'STORAGE': {
        'INTERACTION': 'Store Target Item within this Item',
        'MODUS SORT': 'This item is a CAPTCHALOGUE CARD.',
        'MODUS RETRIEVE': 'This item is a CAPTCHALOGUE CARD.',
        'STRIKE': 'If you would Strike using this Item and it has Items stored within it, you instead Strike using the first Item within it. That Item is Ejected.',
        'EQUIPPED': 'Whenever you are hit by a Launched Item, it is stored in this Item.',
        'SORT NAME': 'CAPTCHA',
        'RETRIEVE NAME': 'CARD',
        'PASSIVE': 'This Item can store a number of Items within it equal to X-3. Any Action that could Target this Item can Target any Item stored within it. This Inventory uses the Sort rules of a Stack Modus.'
    },
    'LIGHTWEIGHT': {
        'INTERACTION': 'Add +1 to your next AGILITY die roll, exhaust',
        'MODUS SORT': 'Items are sorted in order of GRIST COST, lowest on the bottom. If two items have the same cost, put the most recently CAPTCHALOGUED item on top.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, Any item can be retrieved from a STACK, but doing so will EJECT all items above it. Items EJECTED this way do not make STRIKE CHECKS.',
        'STRIKE': 'Add +1 to Strike Check, -1 to Damage Dice',
        'EQUIPPED': 'Strike Checks rolled against you get -1, Damage Dice rolled against you get +1',
        'SORT NAME': 'FLOAT',
        'RETRIEVE NAME': 'LIST',
        'PASSIVE': 'Item Die is 1 Size smaller and has +1 whenever rolled'
    },
    'MEAT': {
        'INTERACTION': 'Target Creature Consumes this Item.',
        'MODUS SORT': 'In addition to basic STACK rules, items with the MEAT trait are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to generic STACK effects, any item with the MEAT TRAIT is retrievable',
        'STRIKE': 'On a critical hit, add 1dX to the Damage Roll. Stress.',
        'EQUIPPED': 'When consuming a Meat item, add 1 additional Damage to your next Damage Roll',
        'SORT NAME': 'DELI',
        'RETRIEVE NAME': 'COLDCUT',
        'PASSIVE': 'When consumed by a creature, that creature adds 1dX to their next Damage Roll.'
    },
    'JPEG': {
        'INTERACTION': 'Watch an Advertisement, you get 1dX Boondollars. The DM gets any real money earned from watching the advertisement.',
        'MODUS SORT': 'Items are sorted randomly into this MODUS, and resorted randomly every interaction',
        'MODUS RETRIEVE': 'The retrieved item is randomized',
        'STRIKE': 'You just fucking miss',
        'EQUIPPED': 'The JPEG artifacting pixels dig into your skin. Take 1 damage when you are the target of an effect.',
        'SORT NAME': 'TURN',
        'RETRIEVE NAME': 'WAYS',
        'PASSIVE': 'The Grist Type of this Item is Artifact, it has a d2 Item Die, and every action taken with it has Stress. This Item is fucking useless.'
    },
    'MAGNETIC': {
        'INTERACTION': 'Active Items and Equipped Items of a Creature you would be able to target with an Interaction from this source can be the Target of this Interaction. Captchalogue target Item. Exhaust.',
        'MODUS SORT': 'Items are evenly sorted on either side of a root card.',
        'MODUS RETRIEVE': 'Either the TOP or BOTTOM items of a stack can be retrieved.',
        'STRIKE': 'Strike Checks made with this item get +1',
        'EQUIPPED': 'You can innately target the Equipped and Active Items of any Creature you would be able to innately target.',
        'SORT NAME': 'DOUBLE',
        'RETRIEVE NAME': 'POLAR',
        'PASSIVE': 'This Item die does not Stress when launched'
    },
    'COMPUTER': {
        'INTERACTION': 'Use a software interaction.',
        'MODUS SORT': 'As items are captchalogued, it is assigned a value based on the letters in it\'s name (constanant=1, vowel=2) which is then divided by the number of captchalogue cards in the SYLLADEX. The remainder is it\'s INDEX, and any item already in that position is ejected.',
        'MODUS RETRIEVE': 'An item can be retrieved from the MODUS using a KEYWORD that is then assigend a value based on it\'s letters (constanant=1, vowel=2) which is then divided by the number of captchalogue cards in the SYLLADEX. The remainder is the INDEX of the item retrieved.',
        'STRIKE': 'Damage Dice roll the average of that die for non-critical hits',
        'EQUIPPED': 'Damage Dice roll the average for non-critical hits against you',
        'SORT NAME': 'HASH',
        'RETRIEVE NAME': 'MAP',
        'PASSIVE': 'This Item can have software installed on it.'
    },
    'HEAVYWEIGHT': {
        'INTERACTION': 'Add +1 to your next VIM die roll, exhaust',
        'MODUS SORT': 'Items are sorted in order of GRIST COST, highest on the bottom. If two items have the same cost, put the most recently CAPTCHALOGUED item on top.',
        'MODUS RETRIEVE': 'Items are retrieved from the BOTTOM of a STACK.',
        'STRIKE': 'Add +1 to Damage Dice, -1 to Strike Check',
        'EQUIPPED': 'Damage Dice rolled against you get -1, Strike Checks rolled against you get +1',
        'SORT NAME': 'WEIGHT',
        'RETRIEVE NAME': 'QUEUE',
        'PASSIVE': 'Item Die is 1 Size larger and has -1 whenever rolled'
    },
    'FOOD': {
        'INTERACTION': 'Target Creature Consumes this Item.',
        'MODUS SORT': 'In addition to basic STACK rules, items with the FOOD trait are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, any item with the FOOD TRAIT is retrievable',
        'STRIKE': 'On a critical hit, roll a VIM save +1dX and heal for the result. Stress.',
        'EQUIPPED': 'When consuming a food item, add 2 additional Vitality',
        'SORT NAME': 'DISPLAY',
        'RETRIEVE NAME': 'BUFFET',
        'PASSIVE': 'When consumed by a creature, that creature rolls a VIM Save + 1dX and heals for the result.'
    },
    'SHARP': {
        'INTERACTION': 'Target creature makes a AGILITY Save against 1dX, on a failiure inflict Bleed. Exhaust, Stress',
        'MODUS SORT': 'In addition to basic STACK rules, this MODUS is evenly sorted into two STACKS',
        'MODUS RETRIEVE': 'The item in the middle of a STACK (rounded up) is retrievable',
        'STRIKE': 'On a crit, inflict Bleed',
        'EQUIPPED': 'When a creature targets you, they take 1 damage.',
        'SORT NAME': 'SPLIT',
        'RETRIEVE NAME': 'SLICE',
        'PASSIVE': 'When consumed inflict Bleed'
    },
    'STICKY': {
        'INTERACTION': 'Target Creature makes an AGILITY Save against 1dX, on a failiure inflict Stuck. Exhaust, Stress',
        'MODUS SORT': 'In addition to basic STACK rules, items with the STICKY TRAIT are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to normal STACK effects, when an item is RETRIEVED the item ABOVE and BELOW are EJECTED.',
        'STRIKE': 'On a crit, inflict Stuck',
        'EQUIPPED': 'You can ascend vertical surfaces',
        'SORT NAME': 'ADHESIVE',
        'RETRIEVE NAME': 'BIND',
        'PASSIVE': 'This item cannot be launched'
    },
    'BLUNT': {
        'INTERACTION': 'Target creature makes a WIT Save against 1dX, on a failiure inflict Daze. Exhaust, Stress',
        'MODUS SORT': 'Items are sorted based on DIE SIZE, largest on bottom.',
        'MODUS RETRIEVE': 'Items with the largest die size are retrievable.',
        'STRIKE': 'On a crit, inflict Daze',
        'EQUIPPED': 'Actions targetting you have Exhaust',
        'SORT NAME': 'GREAT',
        'RETRIEVE NAME': 'JUMBO',
        'PASSIVE': 'When consumed inflict Daze'
    },
    'CUTE': {
        'INTERACTION': 'Target creature makes a CHR Save or inflict Charm. Exhaust.',
        'MODUS SORT': 'Items are sorted based on DIE SIZE, smallest on bottom.',
        'MODUS RETRIEVE': 'Items with the smallest die size are retrievable.',
        'STRIKE': 'On a crit, inflict CHARM',
        'EQUIPPED': 'Whenever you take the Calm Action, add 1dX to the Diplomacy Check',
        'SORT NAME': 'MICRO',
        'RETRIEVE NAME': 'TWINK',
        'PASSIVE': 'Any check made with this Item against a charmed creature has +1'
    },
    'PLANT': {
        'INTERACTION': 'Target gets 1 VIT, Stress',
        'MODUS SORT': 'The first item CAPTCHALOGUED is the ROOT CARD. Any more items that are picked up are Branches attached to an existing card. Each card may have up to two branches of their own. Branches with no further branches of their own are called Leaf Cards. Leaf cards are considered to be on top of the STACK.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, Any item can be retrieved from a STACK, but doing so will launch all items below it. Items launched this way do not make STRIKE CHECKS.',
        'STRIKE': 'Whenever you roll a DMG die, this item gets 1 VIT',
        'EQUIPPED': 'At the start of your turn, this item gets 1dX VIT',
        'SORT NAME': 'TREE',
        'RETRIEVE NAME': 'TIMBER',
        'PASSIVE': 'This Item has X GV, and any time it would be Stressed it instead takes 1 DMG. If this Item has less than 1 Vitality, it is broken.'
    },
    'CANDY': {
        'INTERACTION': 'Target Creature Consumes this Item.',
        'MODUS SORT': 'In addition to basic STACK rules, items with the CANDY trait are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, any item with the CANDY TRAIT is retrievable',
        'STRIKE': 'On a critical hit, add 1dX Charge. Stress.',
        'EQUIPPED': 'When consuming a Candy item, it adds 1 additional Charge',
        'SORT NAME': 'SWEET',
        'RETRIEVE NAME': 'JAR',
        'PASSIVE': 'When consumed by a creature, that creature gets 1dX Charge.'
    },
    'VEHICLE': {
        'INTERACTION': 'Move to a location you have access to.',
        'MODUS SORT': 'The first time an item is captchalogued, it is considered the "KEY". If the key is not in the modus, no items can be captchalogued unless it is the KEY.',
        'MODUS RETRIEVE': 'If there is one item left in the stack, it cannot be retrieved.',
        'STRIKE': 'On a critical hit, move the target to a location you have access to',
        'EQUIPPED': 'You get 1 Charge at the end of your turn',
        'SORT NAME': 'LOCK',
        'RETRIEVE NAME': 'ENGINE',
        'PASSIVE': 'RIDE - When you move from a location and can target this item, you can choose for it to move with you.'
    },
    'SERIOUS': {
        'INTERACTION': 'SERIOUS BUSINESS - 2: Until the end of your next turn, creatures in this location can only use Strife Actions',
        'MODUS SORT': 'This modus starts with 11 cards, but no more can be added. When CAPTCHALOGUING an item, roll 2d6. The result is the slot the item goes into. If there is already an item in that slot, that item is ejected in favor of the new one. If you roll snake eyes 3 times, all items are ejected.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, you may retrieve any item at a cost of BOONDOLLARS, cost is equal to the item\'s GRIST COST.',
        'STRIKE': 'On hit, deal 1d4 DMG',
        'EQUIPPED': 'Whenever you would take DMG, take 1d4 less',
        'SORT NAME': 'MONOPOLY',
        'RETRIEVE NAME': 'BUSINESS',
        'PASSIVE': 'Pranksters Gambit cannot effect rolls made using this Item or rolls made as a result of the use of this item'
    },
    'RAD': {
        'INTERACTION': 'Add +1 to the next die you roll',
        'MODUS SORT': 'Items are sorted into different stacks based on their GRIST TYPE.',
        'MODUS RETRIEVE': 'In each STACK, only items with the highest grist type can be retrieved.',
        'STRIKE': 'Add +1 to Damage Dice',
        'EQUIPPED': 'Damage dice rolled against you get -1',
        'SORT NAME': 'TECH',
        'RETRIEVE NAME': 'HOP',
        'PASSIVE': 'This Item is fucking awesome'
    },
    'MUSICAL': {
        'INTERACTION': 'SERENADE - 3: All hostile creatures in this location that have not taken damage since the beginning of your last turn make a WIT Save against 1dX, on a failure they are no longer hostile.',
        'MODUS SORT': 'In addition to basic STACK rules, items which name start with a MUSICAL NOTE (A,B,C,D,E,F,G) are sorted into a separate STACK.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, items which name start with a MUSICAL NOTE (A,B,C,D,E,F,G) is retrievable.',
        'STRIKE': 'Add +1 to Strike Check',
        'EQUIPPED': 'Add +1 to Defense Check',
        'SORT NAME': 'MUSIC',
        'RETRIEVE NAME': 'NOTE',
        'PASSIVE': 'When you roll this Item Die, if your Charm Die is the same size or larger add +1 to the result'
    },
    'CHARLATAN': {
        'INTERACTION': 'Reset your Pranksters Gambit',
        'MODUS SORT': 'In addition to basic STACK rules,, split the deck, and put the bottom half on top every interaction.',
        'MODUS RETRIEVE': 'Only the middle card in a stack is retrievable.',
        'STRIKE': 'On hit, you get 1 Pranksters Gambit',
        'EQUIPPED': 'When hit, attacker loses 1 Pranksters Gambit',
        'SORT NAME': 'HEE HEE',
        'RETRIEVE NAME': 'HOO HOO',
        'PASSIVE': 'Pranksters Gambit is added to every Roll made using this Item'
    },
    'COMFY': {
        'INTERACTION': 'The CST of this Interaction is equal to your STM and can be 0. Fall Asleep. While asleep this way, add 1dX to healing rolls from sleeping.',
        'MODUS SORT': 'In addition to basic STACK rules, when a broken item is CAPTCHALOGUED, roll STRESS for it. On a 1, it is fixed.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, launched items do not deal damage, and do not roll STRESS.',
        'STRIKE': 'On a Crit, Target falls asleep',
        'EQUIPPED': 'Add 1dX to healing rolls from sleeping',
        'SORT NAME': 'MEND',
        'RETRIEVE NAME': 'SOFT',
        'PASSIVE': 'Any time a creature would recieve Fall Damage in this location, it doesn\'t'
    },
    'HARLEQUIN': {
        'INTERACTION': 'Add a CHR die to your next check, exhaust, stress',
        'MODUS SORT': 'In addition to basic STACK rules, Two items must be captchalogued at a time instead of just one.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, another random item is launched as well.',
        'STRIKE': 'The Stat Die used for this Strike Check is CHR',
        'EQUIPPED': 'CHR die gets +1',
        'SORT NAME': 'HOO HOO',
        'RETRIEVE NAME': 'MANIA',
        'PASSIVE': 'Whenever you would roll this Item Die, you instead roll CHR'
    },
    'WIZARD': {
        'INTERACTION': 'Add a WIT die to your next check, exhaust, stress',
        'MODUS SORT': 'In addition to basic STACK rules, only one of each Itemkind can be captchalogued at a time.',
        'MODUS RETRIEVE': 'A random item can be retrieved instead of the item on top of the stack.',
        'STRIKE': 'The Stat Die used for this Strike Check is WIT',
        'EQUIPPED': 'WIT die gets +1',
        'SORT NAME': 'TAROT',
        'RETRIEVE NAME': 'DRAW',
        'PASSIVE': 'Whenever you would roll this Item Die, you instead roll WIT'
    },
    'FURRY': {
        'INTERACTION': 'Add an AGL die to your next check, exhaust, stress',
        'MODUS SORT': 'Instead of items going on TOP of the stack, they go under the TOP card instead, if there is a top card.',
        'MODUS RETRIEVE': 'The item below the TOP CARD is retrievable.',
        'STRIKE': 'The Stat Die used for this Strike Check is AGL',
        'EQUIPPED': 'AGL die gets +1',
        'SORT NAME': 'UNDE',
        'RETRIEVE NAME': 'COAT',
        'PASSIVE': 'Whenever you would roll this Item Die, you instead roll AGL'
    },
    'FIRE': {
        'INTERACTION': 'Choose target creature or item. Target creature makes a AGILITY Save against 1dX, on a failiure inflict Burn. Target Item is Ignited. Exhaust, Stress',
        'MODUS SORT': 'In addition to basic STACK rules, sort items with the FIRE trait in a different stack and put that stack on top of the basic stack every interaction.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, treat all launched items as if they had the FIRE trait. This ends when the launch is resolved.',
        'STRIKE': 'On a crit, inflict BURN',
        'EQUIPPED': 'When a creature rolls a DMG die against you, they take 1 damage',
        'SORT NAME': 'HIGH',
        'RETRIEVE NAME': 'FLAME',
        'PASSIVE': 'When consumed, inflict Fire'
    },
    'ICE': {
        'INTERACTION': 'Choose target creature or item. Target creature makes a AGILITY Save against 1dX, on a failiure inflict Frostbite. Target Item is Frozen. Exhaust, Stress',
        'MODUS SORT': 'In addition to basic STACK rules, sort items with the ICE trait in a different stack and put that stack below the basic stack every interaction.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, treat all launched items as if they had the ICE trait. This ends when the launch is resolved.',
        'STRIKE': 'On a crit, inflict FROSTBITE',
        'EQUIPPED': 'Targetting you costs 1 Stamina',
        'SORT NAME': 'LOW',
        'RETRIEVE NAME': 'FREEZE',
        'PASSIVE': 'When consumed, inflict Freeze'
    },
    'SPOOKY': {
        'INTERACTION': 'Target creature makes a CHR Save or inflict Curse. Exhaust',
        'MODUS SORT': 'Whenever an item is CAPTCHALOGUED, it goes into a random position in the deck.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, whenever an item is launched, a GHOST AGGRIEVEs a random character in the room.',
        'STRIKE': 'On a crit, inflict CURSE',
        'EQUIPPED': 'Whenever you take the Taunt Action, add 1dX to the Diplomacy Check',
        'SORT NAME': 'SPOOKY',
        'RETRIEVE NAME': 'POLTERGEIST',
        'PASSIVE': 'This Item Die ignores the effects of Curse'
    },
    'FELINE': {
        'INTERACTION': 'The result of your next Check is 9, exhaust',
        'MODUS SORT': 'CAPTCHALOGUED items to to the bottom of the STACK.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, launched items inflict BLEED on hit target.',
        'STRIKE': 'SCRATCH - On a hit, inflict Bleed',
        'EQUIPPED': 'You do not take fall damage',
        'SORT NAME': 'STEALTH',
        'RETRIEVE NAME': 'CLAW',
        'PASSIVE': 'CATS must Captchalogue this Item when able'
    },
    'ELECTRIC': {
        'INTERACTION': 'Target gets 1dX Charge, Stress',
        'MODUS SORT': 'In addition to basic STACK rules, When an item is captchalogued, roll a d20 for each item in the sylladex. On 1, launch item being rolled for.',
        'MODUS RETRIEVE': 'All ejected items are treated as if they have the ELECTRIC trait.',
        'STRIKE': 'On a hit, you get Target''s Charge, Target''s Charge becomes 0',
        'EQUIPPED': 'Add +1 to Stamina Rolls',
        'SORT NAME': 'CIRCUIT',
        'RETRIEVE NAME': 'CHARGE',
        'PASSIVE': 'Whenever you roll this Item Die, you can spend 1 charge to reroll that die and take the new result.'
    },
    'BOUNCY': {
        'INTERACTION': 'Launch target Item',
        'MODUS SORT': 'In addition to basic STACK rules, an item with the BOUNCY trait is captchalogued, a different item with the BOUNCY trait is ejected, if there is one.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, ejected items are treated as if they have the BOUNCY trait.',
        'STRIKE': 'On a Critical Hit, launch this item.',
        'EQUIPPED': 'When a Luanched item hits you, Launch it',
        'SORT NAME': 'POGO',
        'RETRIEVE NAME': 'SPRING',
        'PASSIVE': 'When this item die rolls a 1, reroll it. You must keep the new result.'
    },
    'CANINE': {
        'INTERACTION': 'FETCH - 1: Target Creature captchalogues this item',
        'MODUS SORT': 'In addition to basic STACK rules, when a launched item hits you, captchalogue it instead of taking damage. STRESS is still rolled.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, launched items are re-captchalogued after the launch is resolved.',
        'STRIKE': 'BITE - On a hit, inflict Stuck',
        'EQUIPPED': 'Your Stamina Die is one size larger',
        'SORT NAME': 'CATCH',
        'RETRIEVE NAME': 'FETCH',
        'PASSIVE': 'DOGS must Captchalouge this Item when able'
    },
    'PLUSH': {
        'INTERACTION': 'Add a VIM die to your next check, exhaust, stress',
        'MODUS SORT': 'Instead of the TOP of the stack, items go to the MIDDLE.',
        'MODUS RETRIEVE': 'The second card from the bottom is retrievable.',
        'STRIKE': 'The Stat Die used for this Strike Check is VIM',
        'EQUIPPED': 'VIM die gets +1',
        'SORT NAME': 'PLUS',
        'RETRIEVE NAME': 'CUSHION',
        'PASSIVE': 'Whenever you would roll this Item Die, you instead roll VIM'
    },
    'NOIR': {
        'INTERACTION': 'Reroll all 1s on your next Damage roll, exhaust',
        'MODUS SORT': 'Items are sorted alphabetically in the stack.',
        'MODUS RETRIEVE': 'Only items of the first letter there is can be captchalogued. (ie. If there\'s no A items, only the B items can be retrieved and so on.)',
        'STRIKE': 'On hit, deal 1d6 DMG',
        'EQUIPPED': 'Whenever you would take Damage, take 1d6 less',
        'SORT NAME': 'ORGANIZE',
        'RETRIEVE NAME': 'FOLDER',
        'PASSIVE': 'When you would Stress this item, do so favorably'
    },
    'ANIME': {
        'INTERACTION': 'Add +2 to the next die you roll, exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, you may CAPTCHALOGUE items for free equal to the amount of hostile creatures in the area toward you.',
        'MODUS RETRIEVE': 'You may retrieve any item at any time for no cost, equal to the amount of times you have been inspired before this turn.',
        'STRIKE': 'Add +2 to Damage Dice',
        'EQUIPPED': 'Damage Dice rolled against you get -2',
        'SORT NAME': 'MCGUFFIN',
        'RETRIEVE NAME': 'SPIRIT',
        'PASSIVE': 'Whenever you roll the maximum result on this item die when making a check, add 1dX to the result'
    },
    'VAMPIRIC': {
        'INTERACTION': 'You lose 1dX Vitality, add this item die to your next Damage Roll, exhaust',
        'MODUS SORT': 'Every time you captchalogue an item, roll it\'s die and gain TEMP VIT equal to the result. If the item is consumable, consume it immediately for no cost.',
        'MODUS RETRIEVE': 'Every time an item is launched, take X damage and and add X to damage the item deals (X = 1d6).',
        'STRIKE': 'Whenever you roll a DMG die, you get 1 VIT. If Target is bleeding, you instead get 2 VIT.',
        'EQUIPPED': 'You have +X GV',
        'SORT NAME': 'ABSORB',
        'RETRIEVE NAME': 'DRAIN',
        'PASSIVE': 'Any time an Angel or Fairy interacts with or targets this item, they take 1dX damage'
    },
    'DERSE': {
        'INTERACTION': 'Target Dersite joins your party',
        'MODUS SORT': 'In addition to basic STACK rules, Only one NON WEAPONKIND may be captchalogued at any time.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, all WEAPONKINDs are retrievable at all times.',
        'STRIKE': 'Reroll 1s on Damage rolls',
        'EQUIPPED': 'Dersites see you as an ally',
        'SORT NAME': 'WAR',
        'RETRIEVE NAME': 'CHEST',
        'PASSIVE': 'Prospitians cannot interact with or target this item'
    },
    'ANGELIC': {
        'INTERACTION': 'Target is healed 1dX, exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, when an item with the ANGELIC trait is captchalogued, you may put it in any position in the sylladex instead of on top.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, treat all launched items as if they had the ANGELIC trait. This ends when the launch is resolved.',
        'STRIKE': 'Add +2 to Strike Check',
        'EQUIPPED': 'Add +2 to Defense Rolls',
        'SORT NAME': 'DIVINE',
        'RETRIEVE NAME': 'SMITE',
        'PASSIVE': 'Any time a Ghost or Vampire interacts with or targets this Item, they take 1dX damage'
    },
    'CAPRINE': {
        'INTERACTION': 'COUNT SHEEP - 3: Target creature makes a WIT Save or Falls Asleep. Exhaust.',
        'MODUS SORT': 'When an item is CAPTCHALOGUED, the modus screams, ending stealth and making neutral NPCs hostile toward you.',
        'MODUS RETRIEVE': 'When an item is EJECTED, the modus screams, ending STEALTH and making neutral NPCs hostile toward you.',
        'STRIKE': 'Strike Checks are favorable against Sleeping Targets',
        'EQUIPPED': 'Double healing from Sleep',
        'SORT NAME': 'BLEAT',
        'RETRIEVE NAME': 'SCREAM',
        'PASSIVE': 'This Item Die is added to the healing rolls from sleep of every creature in this location'
    },
    'EQUINE': {
        'INTERACTION': 'HOW IRONIC THAT YOUR VERY DEMISE WOULD BE WITHIN THE PROXIMITY OF SOME HORSES - 3: When target creature dies this turn, they drop double Grist, XP, and Vitality Gel. It is a JUST death. Exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, items with the EQUINE trait are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is lauched, all of them are.',
        'STRIKE': 'On a hit, you may move target to a location you have access to',
        'EQUIPPED': 'VIM and AGL get +1',
        'SORT NAME': 'STABLES',
        'RETRIEVE NAME': 'STAMPEDE',
        'PASSIVE': 'RIDE - When you move from a location and can target this item, you can choose for it to move with you.'
    },
    'PROSPIT': {
        'INTERACTION': 'Target Prospitian joins your party',
        'MODUS SORT': 'In addition to basic STACK rules, Only one WEAPONKIND may be captchalogued at any time.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, all NON-WEAPONKINDs are retrievable at all times.',
        'STRIKE': 'Reroll 1s on Strike Check',
        'EQUIPPED': 'Prospitians see you as an ally',
        'SORT NAME': 'PEACE',
        'RETRIEVE NAME': 'POCKETS',
        'PASSIVE': 'Dersites cannot interact with or target this item'
    },
    'DRACONIC': {
        'INTERACTION': 'Target Creature makes a WIT Save or Inflict BLIND, Exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, sort WEAPONKINDS into a different stack and put that stack on top of the basic stack every interaction.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, items of your current specibi are always retrievable.',
        'STRIKE': 'On a Crit, inflict Blind',
        'EQUIPPED': 'Whenever you would be inflicted with a Status Effect, call a coin flip. If you win, you are not inflicted with the Status Effect.',
        'SORT NAME': 'TOOL',
        'RETRIEVE NAME': 'BELT',
        'PASSIVE': 'Add 1d2 to Checks made using this item'
    },
    'ARACHNID': {
        'INTERACTION': 'Target Creature makes an AGL Save or Inflict PARALYZE, Exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, items are contained in MAGIC 8-BALLS. Items must be broken first in order to interact with them. When an item breaks while it\'s in a MAGIC 8-BALL, it isn\'t considered broken.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, after an item is launched and it rolls 8 on STRESS, launch another item.',
        'STRIKE': 'On a Crit, inflict Paralyze',
        'EQUIPPED': 'When hit, attacker becomes stuck',
        'SORT NAME': '8-BALL',
        'RETRIEVE NAME': 'BR8K',
        'PASSIVE': 'Whenever a Check made using this item die would result in 8, add 1dX to the result'
    },
    'NAUTICAL': {
        'INTERACTION': 'Target makes an AGL save or inflict WET',
        'MODUS SORT': 'In addition to basic STACK rules, sort items with the NAUTICAL trait into a different stack and put that stack below the basic stack every interaction.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is EJECTED, the target it hits becomes MOIST.',
        'STRIKE': 'On a crit, inflict Wet',
        'EQUIPPED': 'You can breath underwater',
        'SORT NAME': 'MARINE',
        'RETRIEVE NAME': 'WAVE',
        'PASSIVE': 'Checks made using this item ignore the effects of Wet'
    },
    'AVIAN': {
        'INTERACTION': 'GLIDE - 1: Fall damage taken until your next turn is reduced to 0',
        'MODUS SORT': 'In addition to basic STACK rules, when an item is CAPTCHALOGUED, you may put any other item in the sylladex on top of that item.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, you may instead launch the most recently captchalogued item.',
        'STRIKE': 'Add +1 to Strike Check and +1 to Damage Dice',
        'EQUIPPED': 'You can Fly',
        'SORT NAME': 'AVIAN',
        'RETRIEVE NAME': 'BREEZE',
        'PASSIVE': 'RIDE - When you move from a location and can target this item, you can choose for it to move with you.'
    },
    'NUCLEAR': {
        'INTERACTION': 'Target makes a VIM save or inflict DECAY',
        'MODUS SORT': 'When you roll STAMINA, you may add 1 for each item with the NUCLEAR trait in the sylladex. For each stamina you add in this way, take 1d4 Damage.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, it targets all creatures in the room.',
        'STRIKE': 'On a crit, inflict Decay',
        'EQUIPPED': 'Add 2 to your Stamina Roll',
        'SORT NAME': 'GENERATOR',
        'RETRIEVE NAME': 'BLAST',
        'PASSIVE': 'When consumed, inflict Decay'
    },
    'FROG': {
        'INTERACTION': 'The next time you would roll a 1 on a die until your next turn, reroll it',
        'MODUS SORT': 'In addition to basic STACK rules, when CAPTCHALOGUING an item, you may pay double its GRIST COST to instead CAPTCHALOGUE a copy of that item.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, you may pay double its GRIST COST to instead launch a copy of that item.',
        'STRIKE': 'On a crit, perform the action again. You may choose new targets.',
        'EQUIPPED': 'Reroll 1s on Stamina Rolls',
        'SORT NAME': 'GENESIS',
        'RETRIEVE NAME': 'ALCHEMY',
        'PASSIVE': 'CONTRABAND - Dersites will confiscate this Item when able'
    },
    'FAIRY': {
        'INTERACTION': 'Target Creature can FLY until your next turn',
        'MODUS SORT': 'In addition to basic STACK rules, items with the FAIRY trait are sorted into a separate STACK',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, launched items CHARM hit target.',
        'STRIKE': 'On a hit, inflict Charm',
        'EQUIPPED': 'CHR and WIT get +1',
        'SORT NAME': 'PIXIE',
        'RETRIEVE NAME': 'DUST',
        'PASSIVE': 'If you roll an odd number on this die, reroll it and keep the new result'
    },
    'ROCKET': {
        'INTERACTION': 'Move to a location you have access to as if you could Fly.',
        'MODUS SORT': 'In addition to basic STACK rules, sort items with the ROCKET trait into a different stack and put that stack on top of the basic stack every interaction.',
        'MODUS RETRIEVE': 'If the sylladex is full, launch all items in the sylladex.',
        'STRIKE': 'On a hit, inflict Burn',
        'EQUIPPED': 'Add 1d4 charge at the end of your turn',
        'SORT NAME': 'ROCKET',
        'RETRIEVE NAME': 'BLASTOFF',
        'PASSIVE': 'RIDE - When you move from a location and can target this item, you can choose for it to move with you.'
    },
    'SPACE': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'This modus has maximum 15 points to work with instead of captchalogue cards. DROP type items take up 1 point, BLOCK 2, GUSHER 3, and DIAMOND 4. Adding a CAPTCHALOGUE CARD to this modus adds 1 more maximum point.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is retrieved, it goes to a random adjacent area instead of the current area.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'PUZZLE',
        'RETRIEVE NAME': 'WARP',
        'PASSIVE': 'Not yet implemented'
    },
    'HEART': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'CAPTCHALOGUED items from other selves can be placed in this modus.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, any other self can retrieve items from this sylladex.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'SOUL',
        'RETRIEVE NAME': 'LINK',
        'PASSIVE': 'Not yet implemented'
    },
    'LIFE': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, when you CAPTCHALOGUE a broken item, that item is fixed.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when a launched item hits a target, instead of dealing damage, give TEMP VIT.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'LIFE',
        'RETRIEVE NAME': 'CURE',
        'PASSIVE': 'Not yet implemented'
    },
    'GRIMDARK': {
        'INTERACTION': 'Enter GRIMDARK MODE',
        'MODUS SORT': 'In addition to basic STACK rules, when you roll damage, you may add 1 damage die for each item with the GRIMDARK trait in this sylladex. Each time you add damage this way, take damage equal to the added damage die.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, add +3 to STRIKE CHECK with launched items.',
        'STRIKE': 'Add +3 to Damage Dice',
        'EQUIPPED': '/',
        'SORT NAME': 'GRIM',
        'RETRIEVE NAME': 'DARK',
        'PASSIVE': 'If you are not in GRIMDARK MODE, interacting with or targetting this item deals 1 damage to you'
    },
    'BREATH': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'CAPTCHALOGUED items can be put into any slot in the sylladex.',
        'MODUS RETRIEVE': 'Any item in the sylladex can be retrieved with no penalty.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'FREE',
        'RETRIEVE NAME': 'ARRAY',
        'PASSIVE': 'Not yet implemented'
    },
    'VOID': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'The first two cards become the TOP and BOTTOM cards. When you captchalogue an item, stack it in between the top and bottom cards.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, ignore the TOP and BOTTOM card of the stack, unless they are the last two items in the sylladex.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'CONCEAL',
        'RETRIEVE NAME': 'REVEAL',
        'PASSIVE': 'Not yet implemented'
    },
    'LIGHT': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, when using an item from this sylladex, roll its die FAVORABLY.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, launched items roll STRIKE CHECK and DAMAGE favorably.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'LUCKY',
        'RETRIEVE NAME': 'SNIPE',
        'PASSIVE': 'Not yet implemented'
    },
    'WELSH': {
        'INTERACTION': 'Remove target item from the game, exhaust',
        'MODUS SORT': 'In addition to basic STACK rules, CAPTCHALOGUED items are treated as if they have no traits.',
        'MODUS RETRIEVE': 'In addition to basic STACK effects, launched items deal double the damage to targets with items of DIAMOND or ZILLIUM grist type equipped.',
        'STRIKE': 'If Damage from this weapon would Kill a target, it ignores any conditional or unconditional immortality effects',
        'EQUIPPED': 'Ignore the STRIKE trait effects of Items targetting you',
        'SORT NAME': 'HOLLOW',
        'RETRIEVE NAME': 'WELSH',
        'PASSIVE': 'Any time an effect from this item would be able to target a creature, that creature\'s equipped and active items are also valid targets'
    },
    'DOOM': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, while a broken item is in this sylladex, it is not considered broken.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, DECAY hit target.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'NECROMANCY',
        'RETRIEVE NAME': 'DOOM',
        'PASSIVE': 'Not yet implemented'
    },
    'BLOOD': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, other creatures in the area may add items to this sylladex.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, chums in this area may retrieve items from this sylladex.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'CHUM',
        'RETRIEVE NAME': 'BORROW',
        'PASSIVE': 'Not yet implemented'
    },
    'RAGE': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': '"Whenever this sylladex is interacted with, Roll a D4: 1 - This modus is split into 4 even stacks. 2 - All items are launched from this modus. 3 - This modus behaves like a basic STACK modus. 4 - This modus is sorted into four stacks, each holding a different grist type."',
        'MODUS RETRIEVE': '"Whenever this sylladex is interacted with, Roll a D4: 1 - One random item is retrievable. 2 - All items are launched from this modus. 3 - A retrievable item is launched. 4 - No items can be retrieved from this modus."',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'MIRACLE',
        'RETRIEVE NAME': 'MIRACLE',
        'PASSIVE': 'Not yet implemented'
    },
    'TRICKSTER': {
        'INTERACTION': 'Enter TRICKSTER MODE',
        'MODUS SORT': 'Whenever an item is CAPTCHALOGUED, it gains a random STATUS EFFECT.',
        'MODUS RETRIEVE': 'Whenever an item is EJECTED, it gains a random STATUS EFFECT.',
        'STRIKE': 'You just fucking hit',
        'EQUIPPED': 'Add 1d4 to your Stamina roll',
        'SORT NAME': 'ZILLY',
        'RETRIEVE NAME': 'HOO',
        'PASSIVE': 'This Item\'s grist type is Zillium, it has a d20 Item Die, and ignores stress'
    },
    'TIME': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, when an item is CAPTCHALOGUED, roll STRESS.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, when an item is launched, it returns to where it was in the sylladex when the launch is resolved.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': '4D',
        'RETRIEVE NAME': 'REVERSE',
        'PASSIVE': 'Not yet implemented'
    },
    'HOPE': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, you may create a GHOST ITEM with any code. This ghost item counts as an item but cannot be retrieved or launched. You can see the name, info, and any other notes the DM may give it.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, GHOST ITEMS can be launched. The ghost item disappears once the launch is resolved.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'PICTIONARY',
        'RETRIEVE NAME': 'DREAM',
        'PASSIVE': 'Not yet implemented'
    },
    'MIND': {
        'INTERACTION': 'Not yet implemented',
        'MODUS SORT': 'In addition to basic STACK rules, you may use any action from any item in this sylladex.',
        'MODUS RETRIEVE': 'In addition to basic STACK rules, you may equip any retrievable item for 0 stamina.',
        'STRIKE': 'Not yet implemented',
        'EQUIPPED': 'Not yet implemented',
        'SORT NAME': 'OBSERVE',
        'RETRIEVE NAME': 'EQUIP',
        'PASSIVE': 'Not yet implemented'
    },
    'META': {
        'INTERACTION': 'The next time you would make a roll, instead take the average of all dice that would have been rolled',
        'MODUS SORT': 'This item is a STRIFE SPECIBUS if paired with the META trait. If not, this item is a STRIFE CARD.',
        'MODUS RETRIEVE': 'This item is a STRIFE SPECIBUS if paired with the META trait. If not, this item is a STRIFE CARD.',
        'STRIKE': 'Add +3 to Strike Check',
        'EQUIPPED': 'Alchemize any time',
        'SORT NAME': 'META',
        'RETRIEVE NAME': 'GAME',
        'PASSIVE': 'This Item die always rolls the average'
    }
}

interaction_cost = {
    'GENERIC': '/',
    'HEAVYWEIGHT': '1',
    'LIGHTWEIGHT': '1',
    'SHARP': '1',
    'BLUNT': '1',
    'BOUNCY': '1',
    'STICKY': '1',
    'CANDY': '1',
    'MEAT': '1',
    'FOOD': '1',
    'MAGNETIC': '2',
    'COMPUTER': '1',
    'STORAGE': '1',
    'JPEG': '2',
    'PLANT': '0',
    'VEHICLE': '2',
    'FIRE': '2',
    'ICE': '2',
    'CUTE': '2',
    'SPOOKY': '2',
    'CANINE': '1',
    'FELINE': '2',
    'COMFY': '?',
    'SERIOUS': '2',
    'CHARLATAN': '2',
    'RAD': '1',
    'MUSICAL': '2',
    'PLUSH': '1',
    'HARLEQUIN': '1',
    'WIZARD': '1',
    'FURRY': '1',
    'ELECTRIC': '2',
    'DERSE': '3',
    'PROSPIT': '3',
    'ANGELIC': '1',
    'VAMPIRIC': '1',
    'CAPRINE': '3',
    'EQUINE': '3',
    'DRACONIC': '3',
    'ARACHNID': '3',
    'NOIR': '1',
    'ANIME': '1',
    'FAIRY': '1',
    'ROCKET': '2',
    'FROG': '1',
    'NUCLEAR': '3',
    'NAUTICAL': '3',
    'AVIAN': '1',
    'GRIMDARK': '6',
    'WELSH': '6',
    'TRICKSTER': '6',
    'META': '1',
    'SPACE': '1',
    'TIME': '3',
    'HEART': '2',
    'MIND': '2',
    'LIFE': '3',
    'DOOM': '5',
    'LIGHT': '5',
    'VOID': '5',
    'BREATH': '0',
    'BLOOD': '6',
    'HOPE': '5',
    'RAGE': '5',
}

# Grist Data

grist_dice = {
    'ARTIFACT': '1d2',
    'DROP': '1d4',
    'BLOCK': '1d6',
    'GUSHER': '1d8',
    'DIAMOND': '1d10',
    'ZILLIUM': '1d20'
}

grist_image = {
    'BUILD': 'sylladex/uiElements/asset/GRISTS/Build.png',
    'ARTIFACT': 'sylladex/uiElements/asset/GRISTS/Artifact.png',
    'ZILLIUM': 'sylladex/uiElements/asset/GRISTS/Zillium.png',
    'DROP': 'sylladex/uiElements/asset/GRISTS/Drop.png',
    'BLOCK': 'sylladex/uiElements/asset/GRISTS/Block.png',
    'GUSHER': 'sylladex/uiElements/asset/GRISTS/Gusher.png',
    'DIAMOND': 'sylladex/uiElements/asset/GRISTS/Diamond.png',
}

# Action Data

action_data = {
    #  NAME       CST DMG DESC
    'NO ACTION': ['/', '/', '/'],

    # BASIC ATTACKS
    'AGGRIVE': ['2', '1dx', '/'],

    # MELEE ATTACKS
    'ASSAIL': ['3', '1dX', 'Make this attack twice against random targets'],
    'ASTONISH': ['2', '1dX', 'FAV, exhaust'],
    'ASTRICT': ['2', '/', 'DAZE Target, exhaust'],
    'ASS': ['1', '1dX', '-2 on DMG roll, exhaust'],
    'ASSERT': ['3', '1dX', 'Make this attack 1d4 times against random targets'],
    'ASTOUND': ['3', '2dX', 'Double damage on CRIT'],
    'ASPHIXIATE': ['2', '1dX', 'PARALYZE on crit'],
    'ASTUN': ['1', '2dX', 'UNFAV, exhaust'],
    'ASSAULT': ['3', '/', 'Deal 1dX to all non-allies, exhaust'],
    'ASTRINGE': ['4', '3dX', 'Change rolled number of both STRIKE CHECK dice, as long as final result adds up to the original total, exhaust'],
    'ASSECURE': ['2', '2dX', 'Heal equal to DMG, exhaust'],
    'ASSESS': ['3', '2dX', 'If attack hits, refund STM, exhaust'],
    'ASSUBJUGATE': ['3', '2dX', 'Make this attack against all non-allies'],
    'ASSURE': ['6', '4dX', 'On hit, Crit, exhaust'],
    'ASSASINATE': ['X', 'XdX', 'Exhaust'],
    'ASSEVERATE': ['0', '1dX', 'Exhaust'],

    # RANGED ATTACKS
    'ARRIVE': ['2', '/', 'Next action costs half STM, exhaust'],
    'ARGUFY': ['2', '/', 'Target gets -1 to next STRIKE CHECK, exhaust'],
    'ARSONATE': ['2', '/', 'Target gets -1 to all dice on their next DMG roll, exhaust'],
    'ARTILLERATE': ['1', '1dX', 'Exhaust'],
    'ARRANGE': ['2', '/', 'Use random action, exhaust action if used action has exhausts.'],
    'ARREST': ['2', '/', 'Target gets -2 to next STRIKE CHECK, exhaust.'],
    'AROMATIZE': ['2', '/', 'Target gets -2 to all dice on their next DMG roll, exhaust.'],
    'ARBITERATE': ['2', '1dX', 'Add 1d4 DMG, exhaust.'],
    'ARCHIVE': ['4', '2', 'Use action until it misses (Only pay stamina for first use), exhaust.'],
    'ARROGATE': ['3', '1dX', 'Target gets -2 to all STRIKE CHECKS on their next turn, exhaust'],
    'ARBORIZE': ['3', '1dX', 'Target gets -1 to all DMG rolls on their next turn, exhaust'],
    'ARMAMENTIFY': ['3', '2dX', 'Add 1d4 DMG, exhaust'],
    'ARITHMETIZE': ['5', '1d4', 'Use action until it misses (Only pay stamina for first use)'],
    'ARTICULATE': ['3', '1dX', 'Target gets -3 to all STRIKE CHECKS on their next turn, exhaust'],
    'ARISE': ['4', '2dX', 'Target gets -2 to all DMG rolls on their next turn, exhaust.'],
    'ARSENALIZE': ['3', '2dX', 'Add 1d4 DMG'],

    # MAGIC ATTACKS
    'ACCEDE': ['1', '/', 'Replace this action with a random action until next turn, exhaust.'],
    'ACCUSE': ['1', '/', 'Do 1 DMG to next attacker, exhaust.'],
    'ACCOST': ['1', '/', 'Add 1dX to next DEFENSE CHECK, exhaust.'],
    'ACCRUE': ['2', '/', 'Next turn, STM roll is FAV, exhaust.'],
    'ACQUIRE': ['1', '/', 'Refresh used actions, exhaust.'],
    'ACCOY': ['2', '/', 'Next time you are hit, deal 1dX DMG to attacker, exhaust.'],
    'ACQUIT': ['2', '/', 'Add 1dX to all DEFENSE CHECKS until next turn, exhaust.'],
    'ACCOUNT': ['2', '/', 'Gain 1d4 STM, exhaust.'],
    'ACCESSORIZE': ['3', '/', 'Next action hits, exhaust.'],
    'ACTUALIZE': ['2', '/', 'Next time you are hit, deflect damage, exhaust.'],
    'ACCUMULATE': ['2', '/', 'STRIKE CHECKs against you are unfavorable until next turn, exhaust.'],
    'ACCELERATE': ['2', '/', 'Actions cost 1 less stamina this turn (Min 1), exhaust.'],
    'ACCLIMATE': ['4', '/', 'Next action crits, exhaust.'],
    'ACERBATE': ['2', '/', 'Remove all STATUS EFFECTS'],
    'ACCLAIM': ['2', '/', 'Add 2dX to all DEFENSE CHECKs until next turn, exhaust.'],
    'ACHIEVE': ['0', '/', 'Lose half of your VIT, roll STM, exhaust.'],

    # BUFFS
    'ABASH': ['2', '2dX', 'Exhaust'],
    'ABSIST': ['3', '1dX', 'Add remaining STM to STRIKE CHECK (After paying this action\'s cost), exhaust'],
    'ABSTAIN': ['4', '/', 'Heal 1dX, exhaust'],
    'ABJUDGE': ['3', 'YdX', 'Y = Allies in area, exhaust'],
    'ABERRATE': ['2', '2dX', 'Add prankster\'s gambit to DMG roll, exhaust'],
    'ABDUCT': ['3', '/', 'Switch your prankster\'s gambit with target\'s, exhaust'],
    'ABJURE': ['4', '/', 'Heal YdX at the start of your next turn, Y = Amount of times Strike Checks missed against you, exhaust.'],
    'ABOLISH': ['2', 'YdX', 'Allies add your prankster\'s gambit to STRIKE CHECK instead of their own until your next turn, exhaust.'],
    'ABSORB': ['5', '/', 'Add amount of DMG DICE rolled against you (from now until next turn) to first STRIKE CHECK next turn, exhaust.'],
    'ABBREVIATE': ['3', '1dX', 'Add 1dX to STRIKE CHECK, exhaust.'],
    'ABATE': ['3', '/', 'Target heals 1dX VIT, exhaust.'],
    'ABORT': ['4', '2dX', 'Move an ally to an adjacent room, if able.'],
    'ABUSE': ['1', '1dX', '/'],
    'ABIDE': ['3', '2dX', 'Add remaining AP to STRIKE CHECK (AP is used up)'],
    'ABHOR': ['5', '2dX', 'Heal DMG dealt, exhaust.'],
    'ABIRRITATE': ['4', '4dX', 'All allies (including you) add +2 to all DMG Rolls until next turn, exhaust.']

}


# Code Functions

def get_code_value(symbol: str, position: str):
    if code_cypher.get(symbol):
        if code_cypher.get(symbol).get(position):

            return code_cypher.get(symbol).get(position)
        else:
            raise Exception(f'Could not find position {position} in {symbol}')
    else:
        raise Exception(f'Could not find {symbol}')


def read_code(name: str, code_num: str, obj: object):
    if len(code_num) >= 9:
        raise Exception('Codes can not be longer than 8 characters')
    elif len(code_num) <= 7:
        raise Exception('Codes must be 8 characters long')
    _code_array = list(code_num)

    _kind = get_code_value(_code_array[0], '1')
    _grist = get_code_value(_code_array[1], '2')
    _trait1 = get_code_value(_code_array[2], '3')
    _trait2 = get_code_value(_code_array[3], '4')
    if _trait1 == 'TRICKSTER' or _trait2 == 'TRICKSTER':
        _grist = 'ZILLIUM'

    _action1 = get_action_name(_code_array[4], '5')
    _action2 = get_action_name(_code_array[5], '6')
    _action3 = get_action_name(_code_array[6], '7')
    _action4 = get_action_name(_code_array[7], '8')

    obj.code_data = CodeData(
        name, code_num, _kind, _grist, _trait1, _trait2, _action1, _action2, _action3, _action4)

# Kind Functions


def get_weapon_type(weaponkind: str):

    if weaponkind_type.get(weaponkind):
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if weaponkind == 'KIND1':
            return _custom_data['KIND1']['TYPE']
        elif weaponkind == 'KIND2':
            return _custom_data['KIND2']['TYPE']
        else:
            return weaponkind_type.get(weaponkind)
    else:
        raise Exception(f'Could not find type for {weaponkind}')


def find_kind_image(kind_name: str):
    if kind_image.get(kind_name):
        return kind_image.get(kind_name)
    else:
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if kind_name == 'KIND1':
            return kind_image.get(_custom_data['KIND1']['ICON'])
        elif kind_name == 'KIND2':
            return kind_image.get(_custom_data['KIND2']['ICON'])
        else:
            raise Exception(f'Could not find image for {kind_name}')


def find_kind_image_small(kind_name: str):
    if kind_image_small.get(kind_name):
        return kind_image_small.get(kind_name)
    else:
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if kind_name == 'KIND1':
            return kind_image_small.get(_custom_data['KIND1']['ICON'])
        elif kind_name == 'KIND2':
            return kind_image_small.get(_custom_data['KIND2']['ICON'])
        else:
            raise Exception(f'Could not find image for {kind_name}')

# Trait Functions


def get_trait_info(trait_name: str, inspect_type: str):
    if trait_data.get(trait_name):
        if trait_data.get(trait_name).get(inspect_type):
            return trait_data.get(trait_name).get(inspect_type)
        else:
            raise Exception(
                f'Could not find inspect type {inspect_type} in {trait_name}')
    else:
        raise Exception(f'Could not find trait {trait_name}')

# Grist Functions


def get_grist_dice(grist_name: str):
    if grist_dice.get(grist_name):
        return grist_dice.get(grist_name)
    else:
        raise Exception(f'Could not find dice for {grist_name}')


def find_grist_image(grist_name: str):
    if grist_image.get(grist_name):
        return grist_image.get(grist_name)
    else:
        raise Exception(f'Could not find image for {grist_name}')


# Action Functions

def get_action_name(symbol: str, position: str):
    if code_cypher.get(symbol):
        if code_cypher.get(symbol).get(position):
            return code_cypher.get(symbol).get(position)
        else:
            raise Exception(f'Couldn\'t find {position} in {symbol}')
    else:
        raise Exception(f'Couldn\'t find {symbol}')


def get_action_info(action_name: str, w_type: str):
    if action_data.get(action_name):
        return action_data.get(action_name)
    else:
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if w_type == 'MELEE':
            return [_custom_data[action_name]['AS']['COST'], _custom_data[action_name]['AS']['DAMAGE'], _custom_data[action_name]['AS']['DESCRIPTION']]

        elif w_type == 'RANGED':
            return [_custom_data[action_name]['AR']['COST'], _custom_data[action_name]['AR']['DAMAGE'], _custom_data[action_name]['AR']['DESCRIPTION']]

        elif w_type == 'MAGIC':
            return [_custom_data[action_name]['AC']['COST'], _custom_data[action_name]['AC']['DAMAGE'], _custom_data[action_name]['AC']['DESCRIPTION']]

        raise Exception(f'Cant find data for action_name {action_name}')


def get_action_icon(action_name: str, _x: int, _y: int):
    with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
        _custom_data = json.load(_custom_data_file)

    if action_data.get(action_name):
        _action = UIElement.get_ui_elem('ActionIcon')(
            _x, _y, 'CardInspectorAction', False, 1000)

        _action.setup_icon(action_name)

        return _action

    _action = UIElement.get_ui_elem('ActionIcon')(
        _x, _y, 'CardInspectorCustomAction', False, 1000)

    _action.setup_icon(action_name)

    return _action
