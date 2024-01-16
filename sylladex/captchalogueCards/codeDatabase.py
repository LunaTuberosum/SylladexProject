import json
from random import *
from math import *

from uiElement import UIElement

code_cypher = {

    # SPEACIAL CHARACTERS
    '!': {
        '1': 'KIND1',
        '2': 'ARTIFACT',
        '3': 'TRAIT1',
        '4': 'TRAIT3',
        '5': {
            'MELEE': 'ACTION1',
            'RANGED': 'ACTION1',
            'MAGIC': 'ACTION1',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ACTION1',
            'RANGED': 'ACTION1',
            'MAGIC': 'ACTION1',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ACTION1',
            'RANGED': 'ACTION1',
            'MAGIC': 'ACTION1',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ACTION1',
            'RANGED': 'ACTION1',
            'MAGIC': 'ACTION1',
            'NA': 'No Action'
        },
    },
    '?': {
        '1': 'KIND2',
        '2': 'ARTIFACT',
        '3': 'TRAIT2',
        '4': 'TRAIT4',
        '5': {
            'MELEE': 'ACTION2',
            'RANGED': 'ACTION2',
            'MAGIC': 'ACTION2',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ACTION2',
            'RANGED': 'ACTION2',
            'MAGIC': 'ACTION2',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ACTION2',
            'RANGED': 'ACTION2',
            'MAGIC': 'ACTION2',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ACTION2',
            'RANGED': 'ACTION2',
            'MAGIC': 'ACTION2',
            'NA': 'No Action'
        },
    },

    # NUMBERED CHARCTERS
    '0': {
        '1': 'Artifactkind',
        '2': 'ARTIFACT',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
    },
    '1': {
        '1': 'Moduskind',
        '2': 'ARTIFACT',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'No Action',
            'RANGED': 'No Action',
            'MAGIC': 'No Action',
            'NA': 'No Action'
        },
    },
    '2': {
        '1': 'Hammerkind',
        '2': 'URANIUM',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCMILATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
    },
    '3': {
        '1': 'Needlekind',
        '2': 'AMETHYST',
        '3': 'FOOD',
        '4': 'LIGHT',
        '5': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
    },
    '4': {
        '1': 'Bladekind',
        '2': 'GARNET',
        '3': 'CANDY',
        '4': 'GRIMDARK',
        '5': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARESENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
    },
    '5': {
        '1': 'Riflekind',
        '2': 'IRON',
        '3': 'MEAT',
        '4': 'COMPUTER',
        '5': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCMILATE',
            'NA': 'No Action'
        },
    },
    '6': {
        '1': 'Utensilkind',
        '2': 'MARBLE',
        '3': 'BOUNCY',
        '4': 'SENTIENT',
        '5': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
    },
    '7': {
        '1': 'Fistkind',
        '2': 'CHALK',
        '3': 'STICKY',
        '4': 'MAGICAL',
        '5': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
    },
    '8': {
        '1': 'Puppetkind',
        '2': 'SHALE',
        '3': 'HOT',
        '4': 'EXQUISITE',
        '5': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
    },
    '9': {
        '1': 'Pistolkind',
        '2': 'COBALT',
        '3': 'COLD',
        '4': 'ROCKET',
        '5': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
    },

    # UPPERCASE CHARACTERS
    'A': {
        '1': 'Lancekind',
        '2': 'RUBY',
        '3': 'ELECTRIC',
        '4': 'SPIRITUAL',
        '5': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSOTIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCMILATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
    },
    'B': {
        '1': 'Thrwstarkind',
        '2': 'CAULK',
        '3': 'IRRADAITED',
        '4': 'SHITTY',
        '5': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
    },
    'C': {
        '1': 'Sicklekind',
        '2': 'TAR',
        '3': 'SHARP',
        '4': 'TRICKSTER',
        '5': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
    },
    'D': {
        '1': 'Clawkind',
        '2': 'AMBER',
        '3': 'ROCKET',
        '4': 'SCIENTIFIC',
        '5': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
    },
    'E': {
        '1': 'Chainsawkind',
        '2': 'URANIUM',
        '3': 'COMPUTER',
        '4': 'STORAGE',
        '5': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
    },
    'F': {
        '1': 'Canekind',
        '2': 'AMETHYST',
        '3': 'LIGHT SOURCE',
        '4': 'HEAVY',
        '5': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
    },
    'G': {
        '1': 'Dicekind',
        '2': 'GARNET',
        '3': 'STORAGE',
        '4': 'LIGHT SOURCE',
        '5': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
    },
    'H': {
        '1': 'Bowkind',
        '2': 'IRON',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
    },
    'I': {
        '1': 'Clubkind',
        '2': 'MARBLE',
        '3': 'FOOD',
        '4': 'LIGHT',
        '5': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
    },
    'J': {
        '1': 'Wandkind',
        '2': 'CHALK',
        '3': 'CANDY',
        '4': 'GRIMDARK',
        '5': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
    },
    'K': {
        '1': 'Spearkind',
        '2': 'SHALE',
        '3': 'MEAT',
        '4': 'COMPUTER',
        '5': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
    },
    'L': {
        '1': 'Bunnykind',
        '2': 'COBALT',
        '3': 'BOUNCY',
        '4': 'SENTIENT',
        '5': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
    },
    'M': {
        '1': 'Paperkind',
        '2': 'RUBY',
        '3': 'STICKY',
        '4': 'MAGICAL',
        '5': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
    },
    'N': {
        '1': 'Fncysntakind',
        '2': 'CAULK',
        '3': 'HOT',
        '4': 'EXQUISITE',
        '5': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
    },
    'O': {
        '1': 'Umbrellakind',
        '2': 'TAR',
        '3': 'COLD',
        '4': 'ROCKET',
        '5': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
    },
    'P': {
        '1': 'Broomkind',
        '2': 'AMBER',
        '3': 'ELECTRIC',
        '4': 'SPIRTITUAL',
        '5': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
    },
    'Q': {
        '1': 'Flshlghtkind',
        '2': 'URANIUM',
        '3': 'SHARP',
        '4': 'TRICKSTER',
        '5': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
    },
    'R': {
        '1': 'Sawkind',
        '2': 'AMETHYST',
        '3': 'ROCKET',
        '4': 'SCIENTIFIC',
        '5': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
    },
    'S': {
        '1': 'Wrenchkind',
        '2': 'GARNET',
        '3': 'COMPUTER',
        '4': 'STORAGE',
        '5': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
    },
    'T': {
        '1': 'Scrwdrvrkind',
        '2': 'IRON',
        '3': 'LIGHT SOURCE',
        '4': 'HEAVY',
        '5': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
    },
    'U': {
        '1': 'Plierkind',
        '2': 'MARBLE',
        '3': 'STORAGE',
        '4': 'LIGHT SOURCE',
        '5': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
    },
    'V': {
        '1': 'Nailkind',
        '2': 'CHALK',
        '3': 'STORAGE',
        '4': 'LIGHT SOURCE',
        '5': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
    },
    'W': {
        '1': 'Crowbarkind',
        '2': 'SHALE',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
    },
    'X': {
        '1': 'Bookkind',
        '2': 'COBALT',
        '3': 'FOOD',
        '4': 'LIGHT',
        '5': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
    },
    'Y': {
        '1': 'Yoyokind',
        '2': 'RUBY',
        '3': 'CANDY',
        '4': 'GRIMDARK',
        '5': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
    },
    'Z': {
        '1': 'Staplerkind',
        '2': 'CAULK',
        '3': 'MEAT',
        '4': 'COMPUTER',
        '5': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
    },

    # LOWERCASE CHARACTERS
    'a': {
        '1': 'Shotgunkind',
        '2': 'TAR',
        '3': 'BOUNCY',
        '4': 'SENTIENT',
        '5': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
    },
    'b': {
        '1': 'Pencilkind',
        '2': 'AMBER',
        '3': 'HOT',
        '4': 'MAGICAL',
        '5': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
    },
    'c': {
        '1': 'Brushkind',
        '2': 'URANIUM',
        '3': 'HOT',
        '4': 'EXQUISITE',
        '5': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
    },
    'd': {
        '1': 'Scythekind',
        '2': 'AMETHYST',
        '3': 'COLD',
        '4': 'ROCKET',
        '5': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
    },
    'e': {
        '1': 'Scissorkind',
        '2': 'GARNET',
        '3': 'ELECTRIC',
        '4': 'SPIRITUAL',
        '5': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
    },
    'f': {
        '1': 'Knifekind',
        '2': 'IRON',
        '3': 'IRRADAITED',
        '4': 'SHITTY',
        '5': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
    },
    'g': {
        '1': 'Shovelkind',
        '2': 'MARBLE',
        '3': 'SHARP',
        '4': 'TRICKSTER',
        '5': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
    },
    'h': {
        '1': 'Cordkind',
        '2': 'CHALK',
        '3': 'ROCKET',
        '4': 'SCIENTIFIC',
        '5': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
    },
    'i': {
        '1': 'Axekind',
        '2': 'SHALE',
        '3': 'COMPUTER',
        '4': 'STORAGE',
        '5': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
    },
    'j': {
        '1': 'Dartkind',
        '2': 'COBALT',
        '3': 'LIGHT SOURCE',
        '4': 'HEAVY',
        '5': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
    },
    'k': {
        '1': 'Chainkind',
        '2': 'RUBY',
        '3': 'STORAGE',
        '4': 'LIGHT SOURCE',
        '5': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
    },
    'l': {
        '1': 'Ballkind',
        '2': 'CAULK',
        '3': 'NONE',
        '4': 'NONE',
        '5': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
    },
    'm': {
        '1': 'Rockkind',
        '2': 'TAR',
        '3': 'FOOD',
        '4': 'LIGHT',
        '5': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASS',
            'RANGED': 'ARCHIVE',
            'MAGIC': 'ACCESSORIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
    },
    'n': {
        '1': 'Hckystckkind',
        '2': 'AMBER',
        '3': 'CANDY',
        '4': 'GRIMDARK',
        '5': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
    },
    'o': {
        '1': 'Tridentkind',
        '2': 'URANIUM',
        '3': 'MEAT',
        '4': 'COMPUTER',
        '5': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
    },
    'p': {
        '1': 'Razorkind',
        '2': 'AMETHYST',
        '3': 'BOUNCY',
        '4': 'SENTIENT',
        '5': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
    },
    'q': {
        '1': 'Fankind',
        '2': 'GARNET',
        '3': 'HOT',
        '4': 'MAGICAL',
        '5': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
    },
    'r': {
        '1': 'Cardkind',
        '2': 'IRON',
        '3': 'HOT',
        '4': 'EXQUISITE',
        '5': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
    },
    's': {
        '1': 'Armorkind',
        '2': 'MARBLE',
        '3': 'COLD',
        '4': 'ROCKET',
        '5': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
    },
    't': {
        '1': 'Shoekind',
        '2': 'CHALK',
        '3': 'ELECTRIC',
        '4': 'SPIRITUAL',
        '5': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEVERATE',
            'RANGED': 'ARRAIGN',
            'MAGIC': 'ACERBATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
    },
    'u': {
        '1': 'Hatkind',
        '2': 'SHALE',
        '3': 'IRRADAITED',
        '4': 'SHITTY',
        '5': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSEMBLE',
            'RANGED': 'ARISE',
            'MAGIC': 'ACCOUNT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASPHIXIATE',
            'RANGED': 'ARBITRATE',
            'MAGIC': 'ACCEDE',
            'NA': 'No Action'
        },
    },
    'v': {
        '1': 'Glasseskind',
        '2': 'COBALT',
        '3': 'SHARP',
        '4': 'TRICKSTER',
        '5': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSIGN',
            'RANGED': 'ARRANGE',
            'MAGIC': 'ACKNOWLEDGE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSURE',
            'RANGED': 'ARROGATE',
            'MAGIC': 'ACTUALIZE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTRICT',
            'RANGED': 'ARTILLERATE',
            'MAGIC': 'ACUPRESSURE',
            'NA': 'No Action'
        },
    },
    'w': {
        '1': 'Picturekind',
        '2': 'RUBY',
        '3': 'ROCKET',
        '4': 'SCIENTIFIC',
        '5': {
            'MELEE': 'AGGRAVATE',
            'RANGED': 'AGGRAVATE',
            'MAGIC': 'AGGRAVATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASPIRE',
            'RANGED': 'ARBORIZE',
            'MAGIC': 'ACCELERATE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGREGATE',
            'RANGED': 'AGGREGATE',
            'MAGIC': 'AGGREGATE',
            'NA': 'No Action'
        },
    },
    'x': {
        '1': 'Bustkind',
        '2': 'CAULK',
        '3': 'COMPUTER',
        '4': 'STORAGE',
        '5': {
            'MELEE': 'ASSIST',
            'RANGED': 'ARRIVE',
            'MAGIC': 'ACQUIRE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSERT',
            'RANGED': 'ARITHMETIZE',
            'MAGIC': 'ACCUMULATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'AGGRESS',
            'RANGED': 'AGGRESS',
            'MAGIC': 'AGGRESS',
            'NA': 'No Action'
        },
    },
    'y': {
        '1': 'Furniturekind',
        '2': 'TAR',
        '3': 'LIGHT SOURCE',
        '4': 'HEAVY',
        '5': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASTONISH',
            'RANGED': 'ARSENALIZE',
            'MAGIC': 'ACTUATE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSAIL',
            'RANGED': 'ARDOR',
            'MAGIC': 'ACCLAIM',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASSAULT',
            'RANGED': 'ARGUFY',
            'MAGIC': 'ACCOMPLISH',
            'NA': 'No Action'
        },
    },
    'z': {
        '1': 'Vehiclekind',
        '2': 'AMBER',
        '3': 'STORAGE',
        '4': 'LIGHT SOURCE',
        '5': {
            'MELEE': 'ASSASSINATE',
            'RANGED': 'ARF',
            'MAGIC': 'ACCLIMATE',
            'NA': 'No Action'
        },
        '6': {
            'MELEE': 'ASSESS',
            'RANGED': 'ARMAMENTIFY',
            'MAGIC': 'ACCUSE',
            'NA': 'No Action'
        },
        '7': {
            'MELEE': 'ASSIMILATE',
            'RANGED': 'ARREST',
            'MAGIC': 'ACQUAINT',
            'NA': 'No Action'
        },
        '8': {
            'MELEE': 'ASTOUND',
            'RANGED': 'ARTICULATE',
            'MAGIC': 'ACUERE',
            'NA': 'No Action'
        },
    },
}

weaponkind_type = {
    'KIND1': 'NA',
    'KIND2': 'NA',
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
    'Shoekind': 'NA',
    'Hatkind': 'NA',
    'Glasseskind': 'NA',
    'Picturekind': 'NA',
    'Bustkind': 'NA',
    'Furniturekind': 'NA',
    'Vehiclekind': 'NA'
}

trait_1_desc = {
    'NONE': {
        'WEAPON': {
            '1': '/',
            '2': '/',
            '3': '/',
            '4': '/'
        },
        'ITEM': {
            '1': '/',
            '2': '/',
            '3': '/',
            '4': '/'
        },
    },
    'FOOD': {
        'WEAPON': {
            '1': 'CONSUME TO REPLENISH 1d10 VITALITY',
            '2': 'CONSUME TO REPLENISH 2d10 VITALITY',
            '3': 'CONSUME TO REPLENISH 4d10 VITALITY',
            '4': 'CONSUME TO REPLENISH 8d10 VITALITY'
        },
        'ITEM': {
            '1': 'CONSUME TO REPLENISH 1d10 VITALITY',
            '2': 'CONSUME TO REPLENISH 2d10 VITALITY',
            '3': 'CONSUME TO REPLENISH 4d10 VITALITY',
            '4': 'CONSUME TO REPLENISH 8d10 VITALITY'
        },
    },
    'CANDY': {
        'WEAPON': {
            '1': 'CONSUME TO GAIN 1 STAMINA',
            '2': 'CONSUME TO GAIN 2 STAMINA',
            '3': 'CONSUME TO GAIN 4 STAMINA',
            '4': 'CONSUME TO GAIN 8 STAMINA'
        },
        'ITEM': {
            '1': 'CONSUME TO GAIN 1 STAMINA',
            '2': 'CONSUME TO GAIN 2 STAMINA',
            '3': 'CONSUME TO GAIN 4 STAMINA',
            '4': 'CONSUME TO GAIN 8 STAMINA'
        },
    },
    'MEAT': {
        'WEAPON': {
            '1': 'CONSUME TO GAIN +1 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '2': 'CONSUME TO GAIN +2 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '3': 'CONSUME TO GAIN +4 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '4': 'CONSUME TO GAIN +8 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN'
        },
        'ITEM': {
            '1': 'CONSUME TO GAIN +1 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '2': 'CONSUME TO GAIN +2 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '3': 'CONSUME TO GAIN +4 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN',
            '4': 'CONSUME TO GAIN +8 ON EVERY STRIKE CHECK YOU MAKE UNTIL NEXT TURN'
        },
    },
    'BOUNCY': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO ATTACK A SECOND TARGET WITH LEVEL 1 DAMAGE',
            '2': 'ON HIT, 1d10 CHANCE TO ATTACK A SECOND TARGET WITH LEVEL 1 DAMAGE',
            '3': 'ON HIT, 1d8 CHANCE TO ATTACK A SECOND TARGET WITH LEVEL 1 DAMAGE',
            '4': 'ON HIT, 1d6 CHANCE TO ATTACK A SECOND TARGET WITH LEVEL 1 DAMAGE'
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AGL + 1, FOR - 1',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AGL + 2, FOR - 2',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AGL + 3, FOR - 3'
        },
    },
    'STICKY': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO GRAPPLE TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO GRAPPLE TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO GRAPPLE TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO GRAPPLE TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO GRAPPLE TARGET',
            '2': 'WHEN HIT, 1d10 CHANCE TO GRAPPLE TARGET',
            '3': 'WHEN HIT, 1d8 CHANCE TO GRAPPLE TARGET',
            '4': 'WHEN HIT, 1d6 CHANCE TO GRAPPLE TARGET'
        },
    },
    'HOT': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO INFLICT BURN ON TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO INFLICT BURN ON TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO INFLICT BURN ON TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO INFLICT BURN ON TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO INFLICT BURN TO ATTACKER',
            '2': 'WHEN HIT, 1d10 CHANCE TO INFLICT BURN TO ATTACKER',
            '3': 'WHEN HIT, 1d8 CHANCE TO INFLICT BURN TO ATTACKER',
            '4': 'WHEN HIT, 1d6 CHANCE TO INFLICT BURN TO ATTACKER'
        },
    },
    'COLD': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO INFLICT FROSTBITE ON TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO INFLICT FROSTBITE ON TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO INFLICT FROSTBITE ON TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO INFLICT FROSTBITE ON TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO INFLICT FROSTBITE TO ATTACKER',
            '2': 'WHEN HIT, 1d10 CHANCE TO INFLICT FROSTBITE TO ATTACKER',
            '3': 'WHEN HIT, 1d8 CHANCE TO INFLICT FROSTBITE TO ATTACKER',
            '4': 'WHEN HIT, 1d6 CHANCE TO INFLICT FROSTBITE TO ATTACKER'
        },
    },
    'ELECTRIC': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO INFLICT STUN ON TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO INFLICT STUN ON TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO INFLICT STUN ON TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO INFLICT STUN ON TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO INFLICT STUN ON ATTACKER',
            '2': 'WHEN HIT, 1d10 CHANCE TO INFLICT STUN ON ATTACKER',
            '3': 'WHEN HIT, 1d8 CHANCE TO INFLICT STUN ON ATTACKER',
            '4': 'WHEN HIT, 1d6 CHANCE TO INFLICT STUN ON ATTACKER'
        },
    },
    'IRRADAITED': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO INFLICT POISON ON TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO INFLICT POISON ON TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO INFLICT POISON ON TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO INFLICT POISON ON TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO INFLICT POISON',
            '2': 'WHEN HIT, 1d10 CHANCE TO INFLICT POISON',
            '3': 'WHEN HIT, 1d8 CHANCE TO INFLICT POISON',
            '4': 'WHEN HIT, 1d6 CHANCE TO INFLICT POISON'
        },
    },
    'SHARP': {
        'WEAPON': {
            '1': 'ON HIT, 1d12 CHANCE TO INFLICT BLEED ON TARGET',
            '2': 'ON HIT, 1d10 CHANCE TO INFLICT BLEED ON TARGET',
            '3': 'ON HIT, 1d8 CHANCE TO INFLICT BLEED ON TARGET',
            '4': 'ON HIT, 1d6 CHANCE TO INFLICT BLEED ON TARGET'
        },
        'ITEM': {
            '1': 'WHEN HIT, 1d12 CHANCE TO INFLICT BLEED TO ATTACKER',
            '2': 'WHEN HIT, 1d10 CHANCE TO INFLICT BLEED TO ATTACKER',
            '3': 'WHEN HIT, 1d8 CHANCE TO INFLICT BLEED TO ATTACKER',
            '4': 'WHEN HIT, 1d6 CHANCE TO INFLICT BLEED TO ATTACKER'
        },
    },
    'ROCKET': {
        'WEAPON': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY'
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY'
        },
    },
    'COMPUTER': {
        'WEAPON': {
            '1': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '2': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '3': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '4': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
        'ITEM': {
            '1': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '2': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '3': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '4': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
    },
    'LIGHT SOURCE': {
        'WEAPON': {
            '1': 'LIGHTS UP ROOM OR AREA',
            '2': 'LIGHTS UP ROOM OR AREA',
            '3': 'LIGHTS UP ROOM OR AREA',
            '4': 'LIGHTS UP ROOM OR AREA'
        },
        'ITEM': {
            '1': 'LIGHTS UP ROOM OR AREA',
            '2': 'LIGHTS UP ROOM OR AREA',
            '3': 'LIGHTS UP ROOM OR AREA',
            '4': 'LIGHTS UP ROOM OR AREA'
        },
    },
    'STORAGE': {
        'WEAPON': {
            '1': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '2': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '3': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '4': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
        'ITEM': {
            '1': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '2': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '3': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '4': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
    }
}

trait_2_desc = {
    'NONE': {
        '1': {
            'MELEE': '/',
            'RANGED': '/',
            'MAGIC': '/',
            'NA': '/'
        },
        '2': {
            'MELEE': '/',
            'RANGED': '/',
            'MAGIC': '/',
            'NA': '/'
        },
        '3': {
            'MELEE': '/',
            'RANGED': '/',
            'MAGIC': '/',
            'NA': '/'
        },
        '4': {
            'MELEE': '/',
            'RANGED': '/',
            'MAGIC': '/',
            'NA': '/'
        }
    },
    'LIGHT': {
        '1': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS'
        },
        '2': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +1 USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +1 USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +1 USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +1'
        },
        '3': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +2, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +2, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +2, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +1'
        },
        '4': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +3, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +3, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +3, USE AGL ON STRIKE CHECK INSTEAD OF STR',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AG1 +3'
        }
    },
    'GRIMDARK': {
        '1': {
            'MELEE': 'REQUIRES +1 IMG TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'REQUIRES +1 IMG TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'REQUIRES +1 IMG TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'REQUIRES +1 IMG TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT'
        },
        '2': {
            'MELEE': 'REQUIRES +2 IMG TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'REQUIRES +2 IMG TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'REQUIRES +2 IMG TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'REQUIRES +2 IMG TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT'
        },
        '3': {
            'MELEE': 'REQUIRES +3 IMG TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'REQUIRES +3 IMG TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'REQUIRES +3 IMG TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'REQUIRES +3 IMG TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT'
        },
        '4': {
            'MELEE': 'REQUIRES +4 IMG TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'REQUIRES +4 IMG TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'REQUIRES +4 IMG TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'REQUIRES +4 IMG TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT'
        }
    },
    'COMPUTER': {
        '1': {
            'MELEE': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'RANGED': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'MAGIC': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'NA': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
        '2': {
            'MELEE': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'RANGED': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'MAGIC': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'NA': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
        '3': {
            'MELEE': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'RANGED': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'MAGIC': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'NA': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
        '4': {
            'MELEE': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'RANGED': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'MAGIC': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            'NA': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB'
        },
    },
    'SENTIENT': {
        '1': {
            'MELEE': 'ARTIFACT CAN THINK, FEEL EMOTIONS, AND HAS THE INTELLIGENCE OF AN ANIMAL',
            'RANGED': 'ARTIFACT CAN THINK, FEEL EMOTIONS, AND HAS THE INTELLIGENCE OF AN ANIMAL',
            'MAGIC': 'ARTIFACT CAN THINK, FEEL EMOTIONS, AND HAS THE INTELLIGENCE OF AN ANIMAL',
            'NA': 'ARTIFACT CAN THINK, FEEL EMOTIONS, AND HAS THE INTELLIGENCE OF AN ANIMAL'
        },
        '2': {
            'MELEE': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A CONSORT',
            'RANGED': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A CONSORT',
            'MAGIC': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A CONSORT',
            'NA': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A CONSORT'
        },
        '3': {
            'MELEE': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A PERSON',
            'RANGED': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A PERSON',
            'MAGIC': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A PERSON',
            'NA': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A PERSON'
        },
        '4': {
            'MELEE': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, HAS A HIGHER INTELLIGENCE THAN A PERSON AND THINKS ITS BETTER THAN YOU',
            'RANGED': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, HAS A HIGHER INTELLIGENCE THAN A PERSON AND THINKS ITS BETTER THAN YOU',
            'MAGIC': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, HAS A HIGHER INTELLIGENCE THAN A PERSON AND THINKS ITS BETTER THAN YOU',
            'NA': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, HAS A HIGHER INTELLIGENCE THAN A PERSON AND THINKS ITS BETTER THAN YOU'
        }
    },
    'MAGICAL': {
        '1': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS'
        },
        '2': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +1, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +1, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +1, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +1'
        },
        '3': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +2, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +2, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +2, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +2'
        },
        '4': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +3, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +3, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +3, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +3'
        }
    },
    'EXQUISITE': {
        '1': {
            'MELEE': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'RANGED': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'MAGIC': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'NA': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED'
        },
        '2': {
            'MELEE': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'RANGED': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'MAGIC': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'NA': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED'
        },
        '3': {
            'MELEE': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'RANGED': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'MAGIC': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'NA': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED'
        },
        '4': {
            'MELEE': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'RANGED': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'MAGIC': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            'NA': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED'
        }
    },
    'ROCKET': {
        '1': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS'
        },
        '2': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS'
        },
        '3': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY'
        },
        '4': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY'
        }
    },
    'SPIRITUAL': {
        '1': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, USE CHA ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS'
        },
        '2': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 1',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 1',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 1, USE CHA ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 1'
        },
        '3': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 2',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 2',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 2, USE CHA ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 2'
        },
        '4': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 3',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 3',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 3, USE CHA ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 3'
        },
    },
    'SHITTY': {
        '1': {
            'MELEE': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'RANGED': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'MAGIC': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'NA': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1'
        },
        '2': {
            'MELEE': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'RANGED': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'MAGIC': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'NA': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1'
        },
        '3': {
            'MELEE': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'RANGED': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'MAGIC': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'NA': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1'
        },
        '4': {
            'MELEE': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'RANGED': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'MAGIC': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            'NA': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1'
        }
    },
    'TRICKSTER': {
        '1': {
            'MELEE': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST'
        },
        '2': {
            'MELEE': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST'
        },
        '3': {
            'MELEE': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST'
        },
        '4': {
            'MELEE': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'RANGED': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'MAGIC': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST, WEAPON IS CONSIDERED A MAGIC WEAPON',
            'NA': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST'
        }
    },
    'SCIENTIFIC': {
        '1': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, USE INT ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, USE INT ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS'
        },
        '2': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1, USE INT ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1, USE INT ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1'
        },
        '3': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 2, USE INT ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 2',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 2, USE INT ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 2'
        },
        '4': {
            'MELEE': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 3, USE INT ON STRIKE CHECK INSTEAD OF STR',
            'RANGED': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 3',
            'MAGIC': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 3, USE INT ON STRIKE CHECK INSTEAD OF IMG',
            'NA': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 3'
        }
    },
    'STORAGE': {
        '1': {
            'MELEE': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'RANGED': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'MAGIC': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'NA': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
        '2': {
            'MELEE': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'RANGED': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'MAGIC': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'NA': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
        '3': {
            'MELEE': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'RANGED': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'MAGIC': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'NA': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
        '4': {
            'MELEE': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'RANGED': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'MAGIC': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            'NA': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        }
    },
    'HEAVY': {
        '1': {
            'MELEE': 'REQUIRES +1 STR TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT',
            'RANGED': 'REQUIRES +1 STR TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT',
            'MAGIC': 'REQUIRES +1 STR TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT',
            'NA': 'REQUIRES +1 STR TO EQUIP, 1d12 CHANCE TO DEAL BD ON HIT'
        },
        '2': {
            'MELEE': 'REQUIRES +2 STR TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT',
            'RANGED': 'REQUIRES +2 STR TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT',
            'MAGIC': 'REQUIRES +2 STR TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT',
            'NA': 'REQUIRES +2 STR TO EQUIP, 1d10 CHANCE TO DEAL BD ON HIT'
        },
        '3': {
            'MELEE': 'REQUIRES +3 STR TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT',
            'RANGED': 'REQUIRES +3 STR TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT',
            'MAGIC': 'REQUIRES +3 STR TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT',
            'NA': 'REQUIRES +3 STR TO EQUIP, 1d8 CHANCE TO DEAL BD ON HIT'
        },
        '4': {
            'MELEE': 'REQUIRES +4 STR TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT',
            'RANGED': 'REQUIRES +4 STR TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT',
            'MAGIC': 'REQUIRES +4 STR TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT',
            'NA': 'REQUIRES +4 STR TO EQUIP, 1d6 CHANCE TO DEAL BD ON HIT'
        }
    },
    'LIGHT SOURCE': {
        '1': {
            'MELEE': 'LIGHTS UP ROOM OR AREA',
            'RANGED': 'LIGHTS UP ROOM OR AREA',
            'MAGIC': 'LIGHTS UP ROOM OR AREA',
            'NA': 'LIGHTS UP ROOM OR AREA'
        },
        '2': {
            'MELEE': 'LIGHTS UP ROOM OR AREA',
            'RANGED': 'LIGHTS UP ROOM OR AREA',
            'MAGIC': 'LIGHTS UP ROOM OR AREA',
            'NA': 'LIGHTS UP ROOM OR AREA'
        },
        '3': {
            'MELEE': 'LIGHTS UP ROOM OR AREA',
            'RANGED': 'LIGHTS UP ROOM OR AREA',
            'MAGIC': 'LIGHTS UP ROOM OR AREA',
            'NA': 'LIGHTS UP ROOM OR AREA'
        },
        '4': {
            'MELEE': 'LIGHTS UP ROOM OR AREA',
            'RANGED': 'LIGHTS UP ROOM OR AREA',
            'MAGIC': 'LIGHTS UP ROOM OR AREA',
            'NA': 'LIGHTS UP ROOM OR AREA'
        }
    }
}

grist_data = {

    # SPECIAL GRISTS
    'ARTIFACT': {
        'Effective': ['ZILLIUM', 'ZILLIUM', 'ZILLIUM', 'ZILLIUM'],
        'Diseffective': ['ALL', 'ALL', 'ALL', 'ALL']
    },
    'BUILD': {
        'Effective': ['NONE', 'NONE', 'NONE', 'NONE'],
        'Diseffective': ['NONE', 'NONE', 'NONE', 'NONE']
    },

    # GUSHER GRISTS
    'URANIUM': {
        'Effective': ['AMETHYST', 'IRON', 'COBALT', 'AMBER'],
        'Diseffective': ['GARNET', 'CHALK', 'SHALE', 'TAR']
    },
    'AMETHYST': {
        'Effective': ['GARNET', 'MARBLE', 'RUBY', 'TAR'],
        'Diseffective': ['URANIUM', 'IRON', 'COBALT', 'CAULK']
    },
    'GARNET': {
        'Effective': ['URANIUM', 'CHALK', 'SHALE', 'CAULK'],
        'Diseffective': ['AMETHYST', 'MARBLE', 'RUBY', 'TAR']
    },

    # MATERIAL GRISTS
    'IRON': {
        'Effective': ['AMETHYST', 'MARBLE', 'COBALT', 'AMBER'],
        'Diseffective': ['URANIUM', 'CHALK', 'RUBY', 'TAR']
    },
    'MARBLE': {
        'Effective': ['GARNET', 'CHALK', 'SHALE', 'CAULK'],
        'Diseffective': ['AMETHYST', 'IRON', 'COBALT', 'AMBER']
    },
    'CHALK': {
        'Effective': ['URANIUM', 'IRON', 'RUBY', 'TAR'],
        'Diseffective': ['GARNET', 'MARBLE', 'SHALE', 'CAULK']
    },

    # GEM GUSHER GRISTs
    'SHALE': {
        'Effective': ['URANIUM', 'CHALK', 'COBALT', 'CAULK'],
        'Diseffective': ['GARNET', 'MARBLE', 'RUBY', 'AMBER']
    },
    'COBALT': {
        'Effective': ['AMETHYST', 'MARBLE', 'RUBY', 'TAR'],
        'Diseffective': ['URANIUM', 'IRON', 'SHALE', 'CAULK']
    },
    'RUBY': {
        'Effective': ['GARNET', 'IRON', 'SHALE', 'AMBER'],
        'Diseffective': ['AMETHYST', 'CHALK', 'COBALT', 'TAR']
    },

    # COMPONENT GRISTS
    'CAULK': {
        'Effective': ['AMETHYST', 'CHALK', 'COBALT', 'AMBER'],
        'Diseffective': ['GARNET', 'MARBLE', 'SHALE', 'TAR']
    },
    'TAR': {
        'Effective': ['URANIUM', 'IRON', 'RUBY', 'CAULK'],
        'Diseffective': ['AMETHYST', 'CHALK', 'COBALT', 'AMBER']
    },
    'AMBER': {
        'Effective': ['GARNET', 'MARBLE', 'SHALE', 'TAR'],
        'Diseffective': ['URANIUM', 'IRON', 'RUBY', 'CAULK']
    },

    # EX SPECIAL GRISTS
    'DIAMOND': {
        'Effective': ['NONE', 'NONE', 'NONE', 'NONE'],
        'Diseffective': ['NONE', 'NONE', 'NONE', 'NONE']
    },
    'ZILLIUM': {
        'Effective': ['ALL', 'ALL', 'ALL', 'ALL'],
        'Diseffective': ['ARTIFACT', 'ARTIFACT', 'ARTIFACT', 'ARTIFACT']
    }
}

action_data = {
    #  NAME       CST DMG DESC
    'No Action': ['/', '/', '/'],

    # BASIC ATTACKS
    'AGGREGATE': ['0', '/', 'Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'AGGRESS': ['3', '2', 'Reuse'],
    'AGGRAVATE': ['4', '3', 'Reuse'],

    # MELEE ATTACKS
    'ASPHIXIATE': ['5', '3', 'Grapple'],
    'ASPIRE': ['2', '/', 'Next stamina roll is favorablE'],
    'ASS': ['1', '/', 'Unfavorable, BD'],
    'ASSAIL': ['2', '2', 'Unfavorable, reuse'],
    'ASSASSINATE': ['5', '3', 'favorable, BD'],
    'ASSAULT': ['3', '3', 'Unfavorable, reuse'],
    'ASSEMBLE': ['2', '/', 'Instant, Gain 1d4 stamina'],
    'ASSERT': ['4', '3', 'Favorable'],
    'ASSESS': ['2', '/', 'Actions are Favorable this turn'],
    'ASSEVERATE': ['0', '/', 'Instant, an action targetting another character targets you instead'],
    'ASSIGN': ['1', '/', 'Actions made against target are Favorable until next turn.'],
    'ASSIMILATE': ['0', '/', 'Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ASSIST': ['1', '/', 'Instant, Reuse, give an action Favorable'],
    'ASSURE': ['3', '2', 'Favorable, reuse'],
    'ASTONISH': ['2', '1', 'Instant'],
    'ASTOUND': ['3', '2', 'Instant'],
    'ASTRICT': ['2', '/', 'Grapple'],

    # RANGED ATTACKS
    'ARBITRATE': ['1', '1', 'Unfavorable, reuse'],
    'ARBORIZE': ['1', '/', 'BD, Reuse'],
    'ARCHIVE': ['0', '/', 'Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ARDOR': ['2', '/', 'Instant, gain 1d4 stamina'],
    'ARF': ['1', '/', 'Unfavorable, BD'],
    'ARGUFY': ['3', '3', 'Unfavorable, reuse'],
    'ARISE': ['2', '/', 'Next stamina roll is favorable'],
    'ARITHMETIZE': ['5', '3', 'Favorable, BD'],
    'ARMAMENTIFY': ['1', '/', 'Actions targetting you are unfavorable until next turn'],
    'ARRAIGN': ['1', '1', 'Unfavorable, reuse'],
    'ARRANGE': ['3', '1', 'Favorable'],
    'ARREST': ['2', '/', 'Grapple'],
    'ARRIVE': ['1', '1', 'Action must be first action used on your turn'],
    'ARROGATE': ['2', '2', 'Unfavorable, reuse'],
    'ARSENALIZE': ['2', '/', 'All actions are favorable this turn'],
    'ARTICULATE': ['4', '2', 'Favorable'],
    'ARTILLERATE': ['2', '/', 'All actions deal BD this turn'],

    # MAGIC ATTACKS
    'ACCEDE': ['2', '1', 'BD'],
    'ACCELERATE': ['2', '/', 'Until start of next turn, all actions cost 1 less stamina to use (cannot be lower than 1)'],
    'ACCESSORIZE': ['4', '/', 'Change armor'],
    'ACCLAIM': ['0', '/', 'Instant, an action targetting another character targets you instead'],
    'ACCLIMATE': ['3', '1', 'Instant, Cancel an action targetting you'],
    'ACCOMPLISH': ['2', '/', 'All actions are favorable this turn'],
    'ACCOUNT': ['0', '/', 'Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ACCUMULATE': ['2', '/', 'Next stamina roll is favorable'],
    'ACCUSE': ['3', '3', 'Unfavorable, Instant'],
    'ACERBATE': ['2', '2', 'Unfavorable, Instant'],
    'ACKNOWLEDGE': ['2', '/', 'Instant, cancel an action'],
    'ACQUAINT': ['1', '/', 'Actions against target are favorable until next turn'],
    'ACQUIRE': ['2', '/', 'Gain 1d4 stamina'],
    'ACTUALIZE': ['1', '/', 'All actions deal BD this turn'],
    'ACTUATE': ['1', '/', 'Actions targetting you are unfavorable until next turn'],
    'ACUERE': ['1', '1', 'Unfavorable, Instant'],
    'ACUPRESSURE': ['1', '/', 'BD, reuse, instant'],

}

tier_damage_num = {
    '1': {
        '1': '5',
        '2': '10',
        '3': '15',
        'BD': '1d4',
        'DF': '3',
        'BR': '1d4'
    },
    '2': {
        '1': '7',
        '2': '14',
        '3': '21',
        'BD': '1d6',
        'DF': '5',
        'BR': '1d6'
    },
    '3': {
        '1': '10',
        '2': '20',
        '3': '30',
        'BD': '1d8',
        'DF': '5',
        'BR': '1d8'
    },
    '4': {
        '1': '14',
        '2': '28',
        '3': '42',
        'BD': '1d10',
        'DF': '6',
        'BR': '1d10'
    },
    '5': {
        '1': '19',
        '2': '38',
        '3': '57',
        'BD': '1d12',
        'DF': '7',
        'BR': '1d12'
    },
    '6': {
        '1': '25',
        '2': '50',
        '3': '75',
        'BD': '2d8',
        'DF': '8',
        'BR': '2d8'
    },
    '7': {
        '1': '32',
        '2': '64',
        '3': '1596',
        'BD': '2d10',
        'DF': '9',
        'BR': '2d10'
    },
    '8': {
        '1': '40',
        '2': '80',
        '3': '120',
        'BD': '2d12',
        'DF': '10',
        'BR': '2d12'
    },
    '9': {
        '1': '49',
        '2': '98',
        '3': '147',
        'BD': '3d10',
        'DF': '11',
        'BR': '3d10'
    },
    '10': {
        '1': '59',
        '2': '118',
        '3': '177',
        'BD': '3d12',
        'DF': '12',
        'BR': '3d12'
    },
    '11': {
        '1': '70',
        '2': '140',
        '3': '210',
        'BD': '4d10',
        'DF': '13',
        'BR': '4d10'
    },
    '12': {
        '1': '82',
        '2': '164',
        '3': '246',
        'BD': '5d10',
        'DF': '14',
        'BR': '5d10'
    },
    '13': {
        '1': '95',
        '2': '190',
        '3': '285',
        'BD': '6d10',
        'DF': '15',
        'BR': '6d10'
    },
    '14': {
        '1': '109',
        '2': '218',
        '3': '327',
        'BD': '7d10',
        'DF': '16',
        'BR': '7d10'
    },
    '15': {
        '1': '114',
        '2': '124',
        '3': '248',
        'BD': '8d10',
        'DF': '17',
        'BR': '8d10'
    },
    '16': {
        '1': '140',
        '2': '280',
        '3': '420',
        'BD': '10d10',
        'DF': '18',
        'BR': '10d10'
    }
}

# IMAGE DATABSES

grist_image = {
    'ALL': 'sylladex/uiElements/asset/GRISTS/All.png',
    'AMBER': 'sylladex/uiElements/asset/GRISTS/Amber.png',
    'AMETHYST': 'sylladex/uiElements/asset/GRISTS/Amethyst.png',
    'ARTIFACT': 'sylladex/uiElements/asset/GRISTS/Artifact.png',
    'BUILD': 'sylladex/uiElements/asset/GRISTS/Build.png',
    'CAULK': 'sylladex/uiElements/asset/GRISTS/Caulk.png',
    'CHALK': 'sylladex/uiElements/asset/GRISTS/Chalk.png',
    'COBALT': 'sylladex/uiElements/asset/GRISTS/Cobalt.png',
    'DIAMOND': 'sylladex/uiElements/asset/GRISTS/Diamond.png',
    'GARNET': 'sylladex/uiElements/asset/GRISTS/Garnet.png',
    'IRON': 'sylladex/uiElements/asset/GRISTS/Iron.png',
    'MARBLE': 'sylladex/uiElements/asset/GRISTS/Marble.png',
    'RUBY': 'sylladex/uiElements/asset/GRISTS/Ruby.png',
    'SHALE': 'sylladex/uiElements/asset/GRISTS/Shale.png',
    'TAR': 'sylladex/uiElements/asset/GRISTS/Tar.png',
    'URANIUM': 'sylladex/uiElements/asset/GRISTS/Uranium.png',
    'ZILLIUM': 'sylladex/uiElements/asset/GRISTS/Zillium.png',
    'NONE': 'sylladex/uiElements/asset/GRISTS/NONE.png'
}

grist_image_small = {
    'ALL': 'sylladex/uiElements/asset/GRISTS/SMALL/All.png',
    'AMBER': 'sylladex/uiElements/asset/GRISTS/SMALL/Amber.png',
    'AMETHYST': 'sylladex/uiElements/asset/GRISTS/SMALL/Amethyst.png',
    'ARTIFACT': 'sylladex/uiElements/asset/GRISTS/SMALL/Artifact.png',
    'BUILD': 'sylladex/uiElements/asset/GRISTS/SMALL/Build.png',
    'CAULK': 'sylladex/uiElements/asset/GRISTS/SMALL/Caulk.png',
    'CHALK': 'sylladex/uiElements/asset/GRISTS/SMALL/Chalk.png',
    'COBALT': 'sylladex/uiElements/asset/GRISTS/SMALL/Cobalt.png',
    'DIAMOND': 'sylladex/uiElements/asset/GRISTS/SMALL/Diamond.png',
    'GARNET': 'sylladex/uiElements/asset/GRISTS/SMALL/Garnet.png',
    'IRON': 'sylladex/uiElements/asset/GRISTS/SMALL/Iron.png',
    'MARBLE': 'sylladex/uiElements/asset/GRISTS/SMALL/Marble.png',
    'RUBY': 'sylladex/uiElements/asset/GRISTS/SMALL/Ruby.png',
    'SHALE': 'sylladex/uiElements/asset/GRISTS/SMALL/Shale.png',
    'TAR': 'sylladex/uiElements/asset/GRISTS/SMALL/Tar.png',
    'URANIUM': 'sylladex/uiElements/asset/GRISTS/SMALL/Uranium.png',
    'ZILLIUM': 'sylladex/uiElements/asset/GRISTS/SMALL/Zillium.png',
    'NONE': 'sylladex/uiElements/asset/GRISTS/SMALL/NONE.png'
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
    'Bustkind': 'sylladex/uiElements/asset/KINDS/BustKind.png',
    'Canekind': 'sylladex/uiElements/asset/KINDS/CaneKind.png',
    'Cardkind': 'sylladex/uiElements/asset/KINDS/CardKind.png',
    'Chainkind': 'sylladex/uiElements/asset/KINDS/ChainKind.png',
    'Chainsawkind': 'sylladex/uiElements/asset/KINDS/ChainsawKind.png',
    'Clawkind': 'sylladex/uiElements/asset/KINDS/ClawKind.png',
    'Clubkind': 'sylladex/uiElements/asset/KINDS/ClubKind.png',
    'Cordkind': 'sylladex/uiElements/asset/KINDS/CordKind.png',
    'Crowbarkind': 'sylladex/uiElements/asset/KINDS/CrowbarKind.png',
    'Customkind': 'sylladex/uiElements/asset/KINDS/CustomKind.png',
    'Dartkind': 'sylladex/uiElements/asset/KINDS/DartKind.png',
    'Dicekind': 'sylladex/uiElements/asset/KINDS/DiceKind.png',
    'Fankind': 'sylladex/uiElements/asset/KINDS/FanKind.png',
    'Fistkind': 'sylladex/uiElements/asset/KINDS/FistKind.png',
    'Flshlghtkind': 'sylladex/uiElements/asset/KINDS/FlshlghtKind.png',
    'Fncysntakind': 'sylladex/uiElements/asset/KINDS/FncysntaKind.png',
    'Furniturekind': 'sylladex/uiElements/asset/KINDS/FurnitureKind.png',
    'Glasseskind': 'sylladex/uiElements/asset/KINDS/GlassesKind.png',
    'Hammerkind': 'sylladex/uiElements/asset/KINDS/HammerKind.png',
    'Hatkind': 'sylladex/uiElements/asset/KINDS/HatKind.png',
    'Hckystckkind': 'sylladex/uiElements/asset/KINDS/HckystckKind.png',
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
    'Umbrellakind': 'sylladex/uiElements/asset/KINDS/UmbrellaKind.png',
    'Utensilkind': 'sylladex/uiElements/asset/KINDS/UtensilKind.png',
    'Vehiclekind': 'sylladex/uiElements/asset/KINDS/VehicleKind.png',
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

action_image = {
    'No Action': 'sylladex/uiElements/asset/ACTION/NO ACTION.png',
    'ACCEDE': 'sylladex/uiElements/asset/ACTION/ACCEDE.png',
    'ACCELERATE': 'sylladex/uiElements/asset/ACTION/ACCELERATE.png',
    'ACCESSORIZE': 'sylladex/uiElements/asset/ACTION/ACCESSORIZE.png',
    'ACCLAIM': 'sylladex/uiElements/asset/ACTION/ACCLAIM.png',
    'ACCLIMATE': 'sylladex/uiElements/asset/ACTION/ACCLIMATE.png',
    'ACCOMPLISH': 'sylladex/uiElements/asset/ACTION/ACCOMPLISH.png',
    'ACCOUNT': 'sylladex/uiElements/asset/ACTION/ACCOUNT.png',
    'ACCUMULATE': 'sylladex/uiElements/asset/ACTION/ACCUMULATE.png',
    'ACCUSE': 'sylladex/uiElements/asset/ACTION/ACCUSE.png',
    'ACERBATE': 'sylladex/uiElements/asset/ACTION/ACERBATE.png',
    'ACKNOWLEDGE': 'sylladex/uiElements/asset/ACTION/ACKNOWLEDGE.png',
    'ACQUAINT': 'sylladex/uiElements/asset/ACTION/ACQUAINT.png',
    'ACQUIANT': 'sylladex/uiElements/asset/ACTION/ACQUIANT.png',
    'ACQUIRE': 'sylladex/uiElements/asset/ACTION/ACQUIRE.png',
    'ACTUALIZE': 'sylladex/uiElements/asset/ACTION/ACTUALIZE.png',
    'ACTUATE': 'sylladex/uiElements/asset/ACTION/ACTUATE.png',
    'ACUERE': 'sylladex/uiElements/asset/ACTION/ACUERE.png',
    'ACUPRESSURE': 'sylladex/uiElements/asset/ACTION/ACUPRESSURE.png',

    'AGGRAVATE': 'sylladex/uiElements/asset/ACTION/AGGRAVATE.png',
    'AGGREGATE': 'sylladex/uiElements/asset/ACTION/AGGREGATE.png',
    'AGGRESS': 'sylladex/uiElements/asset/ACTION/AGGRESS.png',

    'ARBITRATE': 'sylladex/uiElements/asset/ACTION/ARBITRATE.png',
    'ARBORIZE': 'sylladex/uiElements/asset/ACTION/ARBORIZE.png',
    'ARCHIVE': 'sylladex/uiElements/asset/ACTION/ARCHIVE.png',
    'ARDOR': 'sylladex/uiElements/asset/ACTION/ARDOR.png',
    'ARF': 'sylladex/uiElements/asset/ACTION/ARF.png',
    'ARGUFY': 'sylladex/uiElements/asset/ACTION/ARGUFY.png',
    'ARISE': 'sylladex/uiElements/asset/ACTION/ARISE.png',
    'ARITHMETIZE': 'sylladex/uiElements/asset/ACTION/ARITHMETIZE.png',
    'ARMAMENTIFY': 'sylladex/uiElements/asset/ACTION/ARMAMENTIFY.png',
    'ARRAIGN': 'sylladex/uiElements/asset/ACTION/ARRAIGN.png',
    'ARRANGE': 'sylladex/uiElements/asset/ACTION/ARRANGE.png',
    'ARREST': 'sylladex/uiElements/asset/ACTION/ARREST.png',
    'ARRIVE': 'sylladex/uiElements/asset/ACTION/ARRIVE.png',
    'ARROGATE': 'sylladex/uiElements/asset/ACTION/ARROGATE.png',
    'ARSENALIZE': 'sylladex/uiElements/asset/ACTION/ARSENALIZE.png',
    'ARTICULATE': 'sylladex/uiElements/asset/ACTION/ARTICULATE.png',
    'ARTILLERATE': 'sylladex/uiElements/asset/ACTION/ARTILLERATE.png',

    'ASPHIXIATE': 'sylladex/uiElements/asset/ACTION/ASPHIXIATE.png',
    'ASPIRE': 'sylladex/uiElements/asset/ACTION/ASPIRE.png',
    'ASS': 'sylladex/uiElements/asset/ACTION/ASS.png',
    'ASSAIL': 'sylladex/uiElements/asset/ACTION/ASSAIL.png',
    'ASSASSINATE': 'sylladex/uiElements/asset/ACTION/ASSASSINATE.png',
    'ASSAULT': 'sylladex/uiElements/asset/ACTION/ASSAULT.png',
    'ASSEMBLE': 'sylladex/uiElements/asset/ACTION/ASSEMBLE.png',
    'ASSERT': 'sylladex/uiElements/asset/ACTION/ASSERT.png',
    'ASSESS': 'sylladex/uiElements/asset/ACTION/ASSESS.png',
    'ASSEVERATE': 'sylladex/uiElements/asset/ACTION/ASSEVERATE.png',
    'ASSIGN': 'sylladex/uiElements/asset/ACTION/ASSIGN.png',
    'ASSIMILATE': 'sylladex/uiElements/asset/ACTION/ASSIMILATE.png',
    'ASSIST': 'sylladex/uiElements/asset/ACTION/ASSIST.png',
    'ASSURE': 'sylladex/uiElements/asset/ACTION/ASSURE.png',
    'ASTONISH': 'sylladex/uiElements/asset/ACTION/ASTONISH.png',
    'ASTOUND': 'sylladex/uiElements/asset/ACTION/ASTOUND.png',
    'ASTRICT': 'sylladex/uiElements/asset/ACTION/ASTRICT.png',

}


def read_code(name: str, code_num: str, tier: str, list_obj: object):
    if len(code_num) >= 9:
        raise Exception('Codes can not be longer than 8 characters')
    elif len(code_num) <= 7:
        raise Exception('Codes must be 8 characters long')
    _code_array = list(code_num)

    _kind = get_code_value(_code_array[0], '1')
    _grist = get_code_value(_code_array[1], '2')
    _trait1 = get_code_value(_code_array[2], '3')
    _trait2 = get_code_value(_code_array[3], '4')
    if _trait2 == 'TRICKSTER':
        _grist = 'ZILLIUM'

    elif _trait2 == 'EXQUISITE':
        _grist = 'DIAMOND'

    elif _trait2 == 'SHITTY':
        _grist = 'ARTIFACT'
        tier = '1'

    _wType = get_weapon_type(_kind, _trait2)
    _action1 = get_action_name(_code_array[4], '5', _wType)
    _action2 = get_action_name(_code_array[5], '6', _wType)
    _action3 = get_action_name(_code_array[6], '7', _wType)
    _action4 = get_action_name(_code_array[7], '8', _wType)

    list_obj.code_data = UIElement.code_data(
        name, code_num, tier, _kind, _grist, _trait1, _trait2, _action1, _action2, _action3, _action4)


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


def get_action_name(symbol: str, position: str, wType: str):
    if code_cypher.get(symbol):
        if code_cypher.get(symbol).get(position):
            if code_cypher.get(symbol).get(position).get(wType):
                return code_cypher.get(symbol).get(position).get(wType)
            else:
                raise Exception(
                    f'Couldn\'t find {wType} action_image at {position} in {symbol}')
        else:
            raise Exception(f'Couldn\'t find {position} in {symbol}')
    else:
        raise Exception(f'Couldn\'t find {symbol}')


def get_action_image(action_name: str, _x: int, _y: int):
    with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
        _custom_data = json.load(_custom_data_file)

    if action_name == 'No Action':
        return action_image.get('No Action')

    elif action_name[:6] == 'ACTION':

        _action = UIElement.get_ui_elem('ActionIcon')(
            _x, _y, 'CardInspectorCustomAction', False, 1000)

        _action.setup_icon('melee', _custom_data[action_name])

        UIElement.find_current_ui(
            'CardInspector').actions_values.append(_action)

        return action_image.get('No Action')

    else:
        return action_image.get(action_name)


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


def find_grist_image(grist_name: str):
    if grist_image.get(grist_name):
        return grist_image.get(grist_name)
    else:
        raise Exception(f'Could not find image for {grist_name}')


def find_grist_image_small(grist_name: str):
    if grist_image_small.get(grist_name):
        return grist_image_small.get(grist_name)
    else:
        raise Exception(f'Could not find image for {grist_name}')


def get_code_value(symbol: str, position: str):
    if code_cypher.get(symbol):
        if code_cypher.get(symbol).get(position):

            return code_cypher.get(symbol).get(position)
        else:
            raise Exception(f'Could not find position {position} in {symbol}')
    else:
        raise Exception(f'Could not find {symbol}')


def get_trait_1_data(code_data: object):
    _wType = get_weapon_type(code_data.kind, code_data.trait_2)
    _tier_level = str((int(code_data.tier)//4)+1)
    if _tier_level == '5':
        _tier_level = '4'

    if trait_1_desc.get(code_data.trait_1):
        if _wType != 'NA':
            if trait_1_desc.get(code_data.trait_1).get('WEAPON'):
                if trait_1_desc.get(code_data.trait_1).get('WEAPON').get(_tier_level):
                    return trait_1_desc.get(code_data.trait_1).get('WEAPON').get(_tier_level)
                else:
                    raise Exception('Invalid tier level')
            else:
                raise Exception(
                    f'Could not find weapon kind name for {code_data.kind}')
        else:
            if trait_1_desc.get(code_data.trait_1).get('ITEM'):
                if trait_1_desc.get(code_data.trait_1).get('ITEM').get(_tier_level):
                    return trait_1_desc.get(code_data.trait_1).get('ITEM').get(_tier_level)
                else:
                    raise Exception('Invalid tier level')
            else:
                raise Exception(
                    f'Could not find weapon kind name for {code_data.kind}')
    else:
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if _tier_level == '1':
            return _custom_data[code_data.trait_1]['1-4']
        elif _tier_level == '2':
            return _custom_data[code_data.trait_1]['5-8']
        elif _tier_level == '3':
            return _custom_data[code_data.trait_1]['9-12']
        elif _tier_level == '4':
            return _custom_data[code_data.trait_1]['13-16']


def get_trait_2_data(code_data: object):
    _wType = get_weapon_type(code_data.kind, code_data.trait_2)
    _tier_level = str((int(code_data.tier)//4)+1)
    if _tier_level == '5':
        _tier_level = '4'

    if trait_2_desc.get(code_data.trait_2):
        if trait_2_desc.get(code_data.trait_2).get(_tier_level):
            if trait_2_desc.get(code_data.trait_2).get(_tier_level).get(_wType):

                return trait_2_desc.get(code_data.trait_2).get(_tier_level).get(_wType)
            else:
                raise Exception(
                    f'Could not find weapon kind_name for {code_data.kind}')
        else:
            raise Exception('Invalid tier level')
    else:
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if _tier_level == '1':
            return _custom_data[code_data.trait_2]['1-4']
        elif _tier_level == '2':
            return _custom_data[code_data.trait_2]['5-8']
        elif _tier_level == '3':
            return _custom_data[code_data.trait_2]['9-12']
        elif _tier_level == '4':
            return _custom_data[code_data.trait_2]['13-16']


def get_weapon_type(weaponkind: str, trait_2: str):
    if trait_2 == 'TRICKSTER':
        return 'MAGIC'
    elif trait_2 == 'MAGICAL':
        return 'MAGIC'
    elif trait_2 == 'GRIMDARK':
        return 'MAGIC'

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


def get_tier_damage_num(tier: str, value: str):
    if tier_damage_num.get(tier):
        if tier_damage_num.get(tier).get(value):
            return tier_damage_num.get(tier).get(value)
        else:
            raise Exception(f'Could not find value {value} in {tier}')
    else:
        raise Exception(f'Could not find tier {tier}')
