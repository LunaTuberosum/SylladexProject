from random import *
from math import *

from sylladex.uiElements.baseUI import UIBase

codeCypher = {

    # SPEACIAL CHARACTERS
    '!': {
        '1': 'Customkind 1', 
        '2': 'ARTIFACT', 
        '3': 'CUSTOM TRAIT 1', 
        '4': 'CUSTOM TRAIT 3', 
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
    '?': {
        '1': 'Customkind 2', 
        '2': 'ARTIFACT', 
        '3': 'CUSTOM TRAIT 2', 
        '4': 'CUSTOM TRAIT 4', 
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

weaponType = {
    'Customkind 1': 'NA',
    'Customkind 2': 'NA',
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

trait1Desc = {
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
    },
    'CUSTOM TRAIT 1': {
        'WEAPON': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
        'ITEM': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
    },
    'CUSTOM TRAIT 2': {
        'WEAPON': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
        'ITEM': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
    }
}

trait2Desc = {
    'NONE': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': '/',
            '2': '/',
            '3': '/',
            '4': '/',
        },
    },
    'LIGHT': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AV + 1, FOR - 1',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AV + 2, FOR - 2',           '4': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, AV + 3, FOR - 3',
        },
    },
    'GRIMDARK': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'REQUIRES +1 IMG TO EQUIP, ADVANTAGE ON CHA CHECKS',
            '2': 'REQUIRES +2 IMG TO EQUIP, ADVANTAGE ON CHA CHECKS, CHA +1',
            '3': 'REQUIRES +3 IMG TO EQUIP, ADVANTAGE ON CHA CHECKS, CHA +2',
            '4': 'REQUIRES +4 IMG TO EQUIP, ADVANTAGE ON CHA CHECKS, CHA +3',
        },
    },
    'COMPUTER': {
        'WEAPON' : {
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
        'ITEM' : {
            '1': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '2': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '3': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
            '4': 'CAN BE USED TO MESSAGE WITH PESTERCHUM AND PLAY SBURB',
        },
    },
    'SENTIENT': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'ARTIFACT CAN THINK, FEEL EMOTIONS, AND HAS THE INTELLIGENCE OF AN ANIMAL',
            '2': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A CONSORT',
            '3': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, AND HAS THE INTELLIGENCE OF A PERSON',
            '4': 'ARTIFACT CAN THINK, FEEL EMOTIONS, SPEAK, HAS A HIGHER INTELLIGENCE THAN A PERSON AND THINKS ITS BETTER THAN YOU',
        },
    },
    'MAGICAL': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +1',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +2',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON IMG CHECKS, IMG +3',
        },
    },
    'EXQUISITE': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            '2': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            '3': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED',
            '4': 'PRIMARY GRIST TYPE IS DIAMOND GRIST, GRIST COST IS DOUBLED'
        },
    },
    'ROCKET': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON AGL CHECKS, CHARACTER CAN FLY'
        },
    },
    'SPIRITUAL': {
        'WEAPON': {
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
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 1',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 2',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON CHA CHECKS, CHA + 3',
        },
    },
    'SHITTY': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            '2': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            '3': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1',
            '4': 'PRIMARY GRIST TYPE IS ARTIFACT GRIST AND ITEM TIER IS 1'
        },
    },
    'TRICKSTER': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST',
            '2': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST',
            '3': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST',
            '4': 'PRIMARY GRIST TYPE IS ZILLIUM GRIST'
        },
    },
    'SCIENTIFIC': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1',
            '2': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1',
            '3': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1',
            '4': 'WHILE EQUIPPED, ADVANTAGE ON INT CHECKS, INT + 1'
        },
    },
    'STORAGE': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '2': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '3': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM',
            '4': 'OTHER ITEMS CAN BE STORED WITHIN THIS ITEM'
        },
    },
    'HEAVY': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'REQUIRES +1 STR TO EQUIP, ADVANTAGE ON FOR CHECKS',
            '2': 'REQUIRES +2 STR TO EQUIP, ADVANTAGE ON FOR CHECKS, FOR +1, AGL -1',
            '3': 'REQUIRES +3 STR TO EQUIP, ADVANTAGE ON FOR CHECKS, FOR +2, AGL -2',
            '4': 'REQUIRES +4 STR TO EQUIP, ADVANTAGE ON FOR CHECKS, FOR +3, AGL -3'
        },
    },
    'LIGHT SOURCE': {
        'WEAPON': {
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
            },
        },
        'ITEM': {
            '1': 'LIGHTS UP ROOM OR AREA',
            '2': 'LIGHTS UP ROOM OR AREA',
            '3': 'LIGHTS UP ROOM OR AREA',
            '4': 'LIGHTS UP ROOM OR AREA'
        },
    },
    'CUSTOM TRAIT 3': {
        'WEAPON': {
            '1': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '2': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '3': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '4': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
        },
        'ITEM': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
    },
    'CUSTOM TRAIT 4': {
        'WEAPON': {
            '1': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '2': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '3': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
            '4': {
                'MELEE': 'NA',
                'RANGED': 'NA',
                'MAGIC': 'NA',
                'NA': 'NA'
            },
        },
        'ITEM': {
            '1': 'NA',
            '2': 'NA',
            '3': 'NA',
            '4': 'NA'
        },
    }
}

gristData = {

    # SPECIAL GRISTS
    'ARTIFACT': {
        'Effective': ['ZILLIUM','ZILLIUM','ZILLIUM','ZILLIUM' ],
        'Diseffective': ['ALL','ALL','ALL','ALL' ]
    },
    'BUILD': {
        'Effective': ['NONE','NONE','NONE','NONE' ],
        'Diseffective': ['NONE','NONE','NONE','NONE' ]
    },

    # GUSHER GRISTS
    'URANIUM': {
        'Effective': ['AMETHYST','IRON','COBALT','AMBER'],
        'Diseffective': ['GARNET','CHALK','SHALE','TAR']
    },
    'AMETHYST': {
        'Effective': ['GARNET','MARBLE','RUBY','TAR'],
        'Diseffective': ['URANIUM','IRON','COBALT','CAULK']
    },
    'GARNET': {
        'Effective': ['URANIUM','CHALK','SHALE','CAULK'],
        'Diseffective': ['AMETHYST','MARBLE','RUBY','TAR']
    },

    # MATERIAL GRISTS
    'IRON': {
        'Effective': ['AMETHYST','MARBLE','COBALT','AMBER'],
        'Diseffective': ['URANIUM','CHALK','RUBY','TAR']
    },
    'MARBLE': {
        'Effective': ['GARNET','CHALK','SHALE','CAULK'],
        'Diseffective': ['AMETHYST','IRON','COBALT','AMBER']
    },
    'CHALK': {
        'Effective': ['URANIUM','IRON','RUBY','TAR'],
        'Diseffective': ['GARNET','MARBLE','SHALE','CAULK']
    },

    # GEM GUSHER GRISTs
    'SHALE': {
        'Effective': ['URANIUM','CHALK','COBALT','CAULK'],
        'Diseffective': ['GARNET','MARBLE','RUBY','AMBER']
    },
    'COBALT': {
        'Effective': ['AMETHYST','MARBLE','RUBY','TAR'],
        'Diseffective': ['URANIUM','IRON','SHALE','CAULK']
    },
    'RUBY': {
        'Effective': ['GARNET','IRON','SHALE','AMBER'],
        'Diseffective': ['AMETHYST','CHALK','COBALT','TAR']
    },

    # COMPONENT GRISTS
    'CAULK': {
        'Effective': ['AMETHYST','CHALK','COBALT','AMBER'],
        'Diseffective': ['GARNET','MARBLE','SHALE','TAR']
    },
    'TAR': {
        'Effective': ['URANIUM','IRON','RUBY','CAULK'],
        'Diseffective': ['AMETHYST','CHALK','COBALT','AMBER']
    },
    'AMBER': {
        'Effective': ['GARNET','MARBLE','SHALE','TAR'],
        'Diseffective': ['URANIUM','IRON','RUBY','CAULK']
    },

    # EX SPECIAL GRISTS
    'DIAMOND': {
        'Effective': ['NONE','NONE','NONE','NONE'],
        'Diseffective': ['NONE','NONE','NONE','NONE']
    },
    'ZILLIUM': {
        'Effective': ['ALL','ALL','ALL','ALL' ],
        'Diseffective': ['ARTIFACT','ARTIFACT','ARTIFACT','ARTIFACT' ]
    }
}

actionData = {
    #  NAME       STA DMG DESC
    'No Action': ['/','/','/'],

    # BASIC ATTACKS
    'AGGREGATE': ['0','/','Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'AGGRESS': ['3','2','Reuse'],
    'AGGRAVATE': ['4','3','Reuse'],
    
    # MELEE ATTACKS
    'ASPHIXIATE': ['5','3','Grapple'],
    'ASPIRE': ['2','/','Next stamina roll is favorablE'],
    'ASS': ['1','/','Unfavorable, BD'],
    'ASSAIL': ['2','2','Unfavorable, reuse'],
    'ASSASSINATE': ['5','3','favorable, BD'],
    'ASSAULT': ['3','3','Unfavorable, reuse'],
    'ASSEMBLE': ['2','/','Instant, Gain 1d4 stamina'],
    'ASSERT': ['4','3','Favorable'],
    'ASSESS': ['2','/','Actions are Favorable this turn'],
    'ASSEVERATE': ['0','/','Instant, an action targetting another character targets you instead'],
    'ASSIGN': ['1','/','Actions made against target are Favorable until next turn.'],
    'ASSIMILATE': ['0','/','Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ASSIST': ['1','/','Instant, Reuse, give an action Favorable'],
    'ASSURE': ['3','2','Favorable, reuse'],
    'ASTONISH': ['2','1','Instant'],
    'ASTOUND': ['3','2','Instant'],
    'ASTRICT': ['2','/','Grapple'],

    # CUSTOM ATTACKS
    'CUSTOM ACTION 1 MELEE': ['/','/','/'],
    'CUSTOM ACTION 2 MELEE': ['/','/','/'],

    # RANGED ATTACKS
    'ARBITRATE': ['1','1','Unfavorable, reuse'],
    'ARBORIZE': ['1','/','BD, Reuse'],
    'ARCHIVE': ['0','/','Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ARDOR': ['2','/','Instant, gain 1d4 stamina'],
    'ARF': ['1','/','Unfavorable, BD'],
    'ARGUFY': ['3','3','Unfavorable, reuse'],
    'ARISE': ['2','/','Next stamina roll is favorable'],
    'ARITHMETIZE': ['5','3','Favorable, BD'],
    'ARMAMENTIFY': ['1','/','Actions targetting you are unfavorable until next turn'],
    'ARRAIGN': ['1','1','Unfavorable, reuse'],
    'ARRANGE': ['3','1','Favorable'],
    'ARREST': ['2','/','Grapple'],
    'ARRIVE': ['1','1','Action must be first action used on your turn'],
    'ARROGATE': ['2','2','Unfavorable, reuse'],
    'ARSENALIZE': ['2','/','All actions are favorable this turn'],
    'ARTICULATE': ['4','2','Favorable'],
    'ARTILLERATE': ['2','/','All actions deal BD this turn'],

    # CUSTOM ATTACKS
    'CUSTOM ACTION 1 RANGED': ['/','/','/'],
    'CUSTOM ACTION 2 RANGED': ['/','/','/'],

    # MAGIC ATTACKS
    'ACCEDE': ['2','1','BD'],
    'ACCELERATE': ['2','/','Until start of next turn, all actions cost 1 less stamina to use (cannot be lower than 1)'],
    'ACCESSORIZE': ['4','/','Change armor'],
    'ACCLAIM': ['0','/','Instant, an action targetting another character targets you instead'],
    'ACCLIMATE': ['3','1','Instant, Cancel an action targetting you'],
    'ACCOMPLISH': ['2','/','All actions are favorable this turn'],
    'ACCOUNT': ['0','/','Instant, any unused stamina from this turn is added to your stamina roll on your next turn'],
    'ACCUMULATE': ['2','/','Next stamina roll is favorable'],
    'ACCUSE': ['3','3','Unfavorable, Instant'],
    'ACERBATE': ['2','2','Unfavorable, Instant'],
    'ACKNOWLEDGE': ['2','/','Instant, cancel an action'],
    'ACQUAINT': ['1','/','Actions against target are favorable until next turn'],
    'ACQUIRE': ['2','/','Gain 1d4 stamina'],
    'ACTUALIZE': ['1','/','All actions deal BD this turn'],
    'ACTUATE': ['1','/','Actions targetting you are unfavorable until next turn'],
    'ACUERE': ['1','1','Unfavorable, Instant'],
    'ACUPRESSURE': ['1','/','BD, reuse, instant'],

    # CUSTOM ATTACKS
    'CUSTOM ACTION 1 MAGIC': ['/','/','/'],
    'CUSTOM ACTION 2 MAGIC': ['/','/','/'],

}

damgeNum = {
    1: {
        '1': '5',
        '2': '10',
        '3': '15',
        'BD': '1d4',
        'DF': '3',
        'BR': '1d4'
    },
    2: {
        '1': '7',
        '2': '14',
        '3': '21',
        'BD': '1d6',
        'DF': '5',
        'BR': '1d6'
    },
    3: {
        '1': '10',
        '2': '20',
        '3': '30',
        'BD': '1d8',
        'DF': '5',
        'BR': '1d8'
    },
    4: {
        '1': '14',
        '2': '28',
        '3': '42',
        'BD': '1d10',
        'DF': '6',
        'BR': '1d10'
    },
    5: {
        '1': '19',
        '2': '38',
        '3': '57',
        'BD': '1d12',
        'DF': '7',
        'BR': '1d12'
    },
    6: {
        '1': '25',
        '2': '50',
        '3': '75',
        'BD': '2d8',
        'DF': '8',
        'BR': '2d8'
    },
    7: {
        '1': '32',
        '2': '64',
        '3': '1596',
        'BD': '2d10',
        'DF': '9',
        'BR': '2d10'
    },
    8: {
        '1': '40',
        '2': '80',
        '3': '120',
        'BD': '2d12',
        'DF': '10',
        'BR': '2d12'
    },
    9: {
        '1': '49',
        '2': '98',
        '3': '147',
        'BD': '3d10',
        'DF': '11',
        'BR': '3d10'
    },
    10: {
        '1': '59',
        '2': '118',
        '3': '177',
        'BD': '3d12',
        'DF': '12',
        'BR': '3d12'
    },
    11: {
        '1': '70',
        '2': '140',
        '3': '210',
        'BD': '4d10',
        'DF': '13',
        'BR': '4d10'
    },
    12: {
        '1': '82',
        '2': '164',
        '3': '246',
        'BD': '5d10',
        'DF': '14',
        'BR': '5d10'
    },
    13: {
        '1': '95',
        '2': '190',
        '3': '285',
        'BD': '6d10',
        'DF': '15',
        'BR': '6d10'
    },
    14: {
        '1': '109',
        '2': '218',
        '3': '327',
        'BD': '7d10',
        'DF': '16',
        'BR': '7d10'
    },
    15: {
        '1': '114',
        '2': '124',
        '3': '248',
        'BD': '8d10',
        'DF': '17',
        'BR': '8d10'
    },
    16: {
        '1': '140',
        '2': '280',
        '3': '420',
        'BD': '10d10',
        'DF': '18',
        'BR': '10d10'
    }
}

## IMAGE DATABSES

grist = {
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

kind = {
    'Artifactkind': 'sylladex/uiElements/asset/KINDS/ArtifactKind.png',
    'Moduskind': 'sylladex/uiElements/asset/KINDS/ModusKind.png',
    'Customkind': 'sylladex/uiElements/asset/KINDS/CustomKind.png',
    'Hammerkind': 'sylladex/uiElements/asset/KINDS/HammerKind.png',
    'Needlekind': 'sylladex/uiElements/asset/KINDS/NeedleKind.png',
    'Bladekind': 'sylladex/uiElements/asset/KINDS/BladeKind.png',
    'Riflekind': 'sylladex/uiElements/asset/KINDS/RifleKind.png',
    'Utensilkind': 'sylladex/uiElements/asset/KINDS/UtensilKind.png',
    'Fistkind': 'sylladex/uiElements/asset/KINDS/FistKind.png',
    'Puppetkind': 'sylladex/uiElements/asset/KINDS/PuppetKind.png',
    'Pistolkind': 'sylladex/uiElements/asset/KINDS/PistolKind.png',
    'Lancekind': 'sylladex/uiElements/asset/KINDS/LanceKind.png',
    'Thrwstarkind': 'sylladex/uiElements/asset/KINDS/ThrwstarKind.png',
    'Sicklekind': 'sylladex/uiElements/asset/KINDS/SickleKind.png',
    'Clawkind': 'sylladex/uiElements/asset/KINDS/ClawKind.png',
    'Chainsawkind': 'sylladex/uiElements/asset/KINDS/ChainsawKind.png',
    'Canekind': 'sylladex/uiElements/asset/KINDS/CaneKind.png',
    'Dicekind': 'sylladex/uiElements/asset/KINDS/DiceKind.png',
    'Bowkind': 'sylladex/uiElements/asset/KINDS/BowKind.png',
    'Clubkind': 'sylladex/uiElements/asset/KINDS/ClubKind.png',
    'Wandkind': 'sylladex/uiElements/asset/KINDS/WandKind.png',
    'Spearkind': 'sylladex/uiElements/asset/KINDS/SpearKind.png',
    'Bunnykind': 'sylladex/uiElements/asset/KINDS/BunnyKind.png',
    'Paperkind': 'sylladex/uiElements/asset/KINDS/PaperKind.png',
    'Fncysntakind': 'sylladex/uiElements/asset/KINDS/FncysntaKind.png',
    'Umbrellakind': 'sylladex/uiElements/asset/KINDS/UmbrellaKind.png',
    'Broomkind': 'sylladex/uiElements/asset/KINDS/BroomKind.png',
    'Flshlghtkind': 'sylladex/uiElements/asset/KINDS/FlshlghtKind.png',
    'Sawkind': 'sylladex/uiElements/asset/KINDS/SawKind.png',
    'Wrenchkind': 'sylladex/uiElements/asset/KINDS/WrenchKind.png',
    'Scrwdrvrkind': 'sylladex/uiElements/asset/KINDS/ScrwdrvrKind.png',
    'Plierkind': 'sylladex/uiElements/asset/KINDS/PlierKind.png',
    'Nailkind': 'sylladex/uiElements/asset/KINDS/NailKind.png',
    'Crowbarkind': 'sylladex/uiElements/asset/KINDS/CrowbarKind.png',
    'Bookkind': 'sylladex/uiElements/asset/KINDS/BookKind.png',
    'Yoyokind': 'sylladex/uiElements/asset/KINDS/YoyoKind.png',
    'Staplerkind': 'sylladex/uiElements/asset/KINDS/StaplerKind.png',
    'Shotgunkind': 'sylladex/uiElements/asset/KINDS/ShotgunKind.png',
    'Pencilkind': 'sylladex/uiElements/asset/KINDS/PencilKind.png',
    'Brushkind': 'sylladex/uiElements/asset/KINDS/BrushKind.png',
    'Scythekind': 'sylladex/uiElements/asset/KINDS/ScytheKind.png',
    'Scissorkind': 'sylladex/uiElements/asset/KINDS/ScissorKind.png',
    'Knifekind': 'sylladex/uiElements/asset/KINDS/KnifeKind.png',
    'Shovelkind': 'sylladex/uiElements/asset/KINDS/ShovelKind.png',
    'Cordkind': 'sylladex/uiElements/asset/KINDS/CordKind.png',
    'Axekind': 'sylladex/uiElements/asset/KINDS/AxeKind.png',
    'Dartkind': 'sylladex/uiElements/asset/KINDS/DartKind.png',
    'Chainkind': 'sylladex/uiElements/asset/KINDS/ChainKind.png',
    'Ballkind': 'sylladex/uiElements/asset/KINDS/BallKind.png',
    'Rockkind': 'sylladex/uiElements/asset/KINDS/RockKind.PNG',
    'Hckystckkind': 'sylladex/uiElements/asset/KINDS/HckystckKind.png',
    'Tridentkind': 'sylladex/uiElements/asset/KINDS/TridentKind.png',
    'Razorkind': 'sylladex/uiElements/asset/KINDS/RazorKind.png',
    'Fankind': 'sylladex/uiElements/asset/KINDS/FanKind.png',
    'Cardkind': 'sylladex/uiElements/asset/KINDS/CardKind.png',
    'Armorkind': 'sylladex/uiElements/asset/KINDS/ArmorKind.png',
    'Shoekind': 'sylladex/uiElements/asset/KINDS/ShoeKind.png',
    'Hatkind': 'sylladex/uiElements/asset/KINDS/HatKind.png',
    'Glasseskind': 'sylladex/uiElements/asset/KINDS/GlassesKind.png',
    'Picturekind': 'sylladex/uiElements/asset/KINDS/PictureKind.png',
    'Bustkind': 'sylladex/uiElements/asset/KINDS/BustKind.png',
    'Furniturekind': 'sylladex/uiElements/asset/KINDS/FurnitureKind.png',
    'Vehiclekind': 'sylladex/uiElements/asset/KINDS/VehicleKind.png',
}

action = {
    'No Action': 'GUI/action/NO ACTION.png',
    'ACCEDE': 'GUI/action/ACCEDE.png',
    'ACCELERATE': 'GUI/action/ACCELERATE.png',
    'ACCESSORIZE': 'GUI/action/ACCESSORIZE.png',
    'ACCLAIM': 'GUI/action/ACCLAIM.png',
    'ACCLIMATE': 'GUI/action/ACCLIMATE.png',
    'ACCOMPLISH': 'GUI/action/ACCOMPLISH.png',
    'ACCOUNT': 'GUI/action/ACCOUNT.png',
    'ACCUMULATE': 'GUI/action/ACCUMULATE.png',
    'ACCUSE': 'GUI/action/ACCUSE.png',
    'ACERBATE': 'GUI/action/ACERBATE.png',
    'ACKNOWLEDGE': 'GUI/action/ACKNOWLEDGE.png',
    'ACQUAINT': 'GUI/action/ACQUAINT.png',
    'ACQUIANT': 'GUI/action/ACQUIANT.png',
    'ACQUIRE': 'GUI/action/ACQUIRE.png',
    'ACTUALIZE': 'GUI/action/ACTUALIZE.png',
    'ACTUATE': 'GUI/action/ACTUATE.png',
    'ACUERE': 'GUI/action/ACUERE.png',
    'ACUPRESSURE': 'GUI/action/ACUPRESSURE.png',

    'AGGRAVATE': 'GUI/action/AGGRAVATE.png',
    'AGGREGATE': 'GUI/action/AGGREGATE.png',
    'AGGRESS': 'GUI/action/AGGRESS.png',

    'ARBITRATE': 'GUI/action/ARBITRATE.png',
    'ARBORIZE': 'GUI/action/ARBORIZE.png',
    'ARCHIVE': 'GUI/action/ARCHIVE.png',
    'ARDOR': 'GUI/action/ARDOR.png',
    'ARF': 'GUI/action/ARF.png',
    'ARGUFY': 'GUI/action/ARGUFY.png',
    'ARISE': 'GUI/action/ARISE.png',
    'ARITHMETIZE': 'GUI/action/ARITHMETIZE.png',
    'ARMAMENTIFY': 'GUI/action/ARMAMENTIFY.png',
    'ARRAIGN': 'GUI/action/ARRAIGN.png',
    'ARRANGE': 'GUI/action/ARRANGE.png',
    'ARREST': 'GUI/action/ARREST.png',
    'ARRIVE': 'GUI/action/ARRIVE.png',
    'ARROGATE': 'GUI/action/ARROGATE.png',
    'ARSENALIZE': 'GUI/action/ARSENALIZE.png',
    'ARTICULATE': 'GUI/action/ARTICULATE.png',
    'ARTILLERATE': 'GUI/action/ARTILLERATE.png',

    'ASPHIXIATE': 'GUI/action/ASPHIXIATE.png',
    'ASPIRE': 'GUI/action/ASPIRE.png',
    'ASS': 'GUI/action/ASS.png',
    'ASSAIL': 'GUI/action/ASSAIL.png',
    'ASSASSINATE': 'GUI/action/ASSASSINATE.png',
    'ASSAULT': 'GUI/action/ASSAULT.png',
    'ASSEMBLE': 'GUI/action/ASSEMBLE.png',
    'ASSERT': 'GUI/action/ASSERT.png',
    'ASSESS': 'GUI/action/ASSESS.png',
    'ASSEVERATE': 'GUI/action/ASSEVERATE.png',
    'ASSIGN': 'GUI/action/ASSIGN.png',
    'ASSIMILATE': 'GUI/action/ASSIMILATE.png',
    'ASSIST': 'GUI/action/ASSIST.png',
    'ASSURE': 'GUI/action/ASSURE.png',
    'ASTONISH': 'GUI/action/ASTONISH.png',
    'ASTOUND': 'GUI/action/ASTOUND.png',
    'ASTRICT': 'GUI/action/ASTRICT.png',

}

def read_code(codeNum, card):
    if len(codeNum) >= 9:
        raise Exception('Codes can not be longer than 8 characters')
    elif len(codeNum) <= 7:
        raise Exception('Codes must be 8 characters long')
    codeArray = list(codeNum)

    
    card.kind = get_codeValue(codeArray[0], '1')
    card.grist = get_codeValue(codeArray[1], '2')
    card.trait1 = get_codeValue(codeArray[2], '3')
    card.trait2 = get_codeValue(codeArray[3], '4')

    wType = get_weaponType(card.kind)
    card.action1 = codeCypher.get(codeArray[4]).get('5').get(wType)
    card.action2 = codeCypher.get(codeArray[5]).get('6').get(wType)
    card.action3 = codeCypher.get(codeArray[6]).get('7').get(wType)
    card.action4 = codeCypher.get(codeArray[7]).get('8').get(wType)


def find_kindImage(kindName):
    if kind.get(kindName):
        return kind.get(kindName)
    else:
        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
            customData = database.readlines()

        if kindName == customData[0].split(',')[0]:
            return kind.get(customData[1].split(',')[0])
        elif kindName == customData[0].split(',')[2]:
            return kind.get(customData[1].split(',')[1])
        else:
            raise Exception(f'Could not find image for {kindName}')

def find_gristImage(gristName):
    if grist.get(gristName):
        return grist.get(gristName)
    else:
        raise Exception(f'Could not find image for {gristName}')

def get_codeValue(symbol, position):
    if codeCypher.get(symbol):
        if codeCypher.get(symbol).get(position):
            if codeCypher.get(symbol).get(position) == 'Customkind 1':
                with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                    customData = database.read()

                return customData.split(',')[0]
            elif codeCypher.get(symbol).get(position) == 'Customkind 2':
                with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                    customData = database.read()

                return customData.split(',')[2]
            return codeCypher.get(symbol).get(position)
        else:
            raise Exception(f'Could not find position {position} in {symbol}')
    else:
        raise Exception(f'Could not find {symbol}')

def get_weaponType(weaponKind):
    if weaponType.get(weaponKind):
        return weaponType.get(weaponKind)
    else:
        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
            customData = database.read()

        if weaponKind == customData.split(',')[0]:
            return customData.split(',')[1]
        elif weaponKind == customData.split(',')[2]:
            return customData.split(',')[3]
        else:
            raise Exception(f'Could not find type for {weaponKind}')
        

def change_codeValue(whichCustom, newCodeValue):

    with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
        customData = database.readlines()

    with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'w') as database:
        if whichCustom == 'Customkind 1':
            database.write(f'{newCodeValue},{customData[0].split(",")[1]},{customData[0].split(",")[2]},{customData[0].split(",")[3]},\n')
            database.write(f'{customData[1].split(",")[0]},{customData[1].split(",")[1]}')

        elif whichCustom == 'Customkind 2':
            database.write(f'{customData[0].split(",")[0]},{customData[0].split(",")[1]},{newCodeValue},{customData[0].split(",")[3]},\n')
            database.write(f'{customData[1].split(",")[0]},{customData[1].split(",")[1]}')

        elif whichCustom == f'{customData[0].split(",")[0]} Type':
            database.write(f'{customData[0].split(",")[0]},{newCodeValue},{customData[0].split(",")[2]},{customData[0].split(",")[3]},\n')
            database.write(f'{customData[1].split(",")[0]},{customData[1].split(",")[1]}')
            
        elif whichCustom == f'{customData[0].split(",")[2]} Type':
            database.write(f'{customData[0].split(",")[0]},{customData[0].split(",")[1]},{customData[0].split(",")[2]},{newCodeValue},\n')
            database.write(f'{customData[1].split(",")[0]},{customData[1].split(",")[1]}')

        elif whichCustom == f'{customData[0].split(",")[0]} Icon':
            database.write(f'{customData[0].split(",")[0]},{customData[0].split(",")[1]},{customData[0].split(",")[2]},{customData[0].split(",")[3]},\n')
            database.write(f'{newCodeValue},{customData[1].split(",")[1]}')

        elif whichCustom == f'{customData[0].split(",")[3]} Icon':
            database.write(f'{customData[0].split(",")[0]},{customData[0].split(",")[1]},{customData[0].split(",")[2]},{customData[0].split(",")[3]},\n')
            database.write(f'{customData[1].split(",")[0]},{newCodeValue}')


    for elem in UIBase.get_group('ui'):
        if isinstance(elem, UIBase.CardList):
            for child in elem.children:
                child.redraw_card((255,255,255))

    