import pygame as pg

from baseUI import UIBase
import settings
from sylladex.captchalogueCards import codeDatabase

class CardInspector(UIBase):
    def __init__(self, codeData):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 439), 'CardInspector', (209,158,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.codeData = codeData
        UIBase.get_group('layer').change_layer(self, 3)

        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 48], "center"],
                [self.codeData.name, [65, 48], "left"], 
                [codeDatabase.get_weaponType(self.codeData.kind), [278, 84], "center"], 
                ["TRAIT 1", [46, 84], "center"], 
                [self.codeData.trait1, [110, 84], 'left'],
                ["TRAIT 2", [46, 109], "center"], 
                [self.codeData.trait2, [110, 109], 'left'],
                ["ITEMKIND", [52, 134], "center"], 
                [self.codeData.kind, [121, 134], 'left'],
                ['GRIST TYPE', [64, 159], 'center'], 
                [self.codeData.grist, [146, 159], 'left'],
                ['EFFECTIVE', [68, 184], 'center'], 
                ['INEFFECTIVE', [68, 209], 'center'], 
                ['INSPECT INFORMATION', [159, 305], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '1'), [283, 121], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '2'), [283, 146], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '3'), [283, 171], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, 'BD'), [283, 196], 'center'], 
                ['CST', [30, 330], 'center'], 
                ['DMG', [30, 355], 'center'], 
                ['CODE', [79, 391], 'center'], 
                [self.codeData.code, [151, 391], "center"],
                ['TIER', [223, 391], 'center'], 
                [self.codeData.tier, [265, 391], "center"],
                ['1', [247, 121], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 171], 'center'], 
                ['BD', [247, 196], 'center'],
                ['/', [60, 330], 'center'],
                ['/', [60, 355], 'center'],
                ['/', [190, 342], 'center'] #Max Char is 28
                ]
            )

        self.children = [
            UIBase.get_uiElem('CardInspectorButton')(self),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+81, self.rect.y+72, 'Trait1'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+81, self.rect.y+97, 'Trait2'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+27, self.rect.y+233, 'Action1'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+27, self.rect.y+258, 'Action2'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+159, self.rect.y+233, 'Action3'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+159, self.rect.y+258, 'Action4'),
        ]

        codeDatabase.get_actionImage(self.codeData.action1, self, [51, 233])
        codeDatabase.get_actionImage(self.codeData.action2, self, [51, 258])
        codeDatabase.get_actionImage(self.codeData.action3, self, [183, 233])
        codeDatabase.get_actionImage(self.codeData.action4, self, [183, 258])

        kindIcon = pg.image.load(codeDatabase.find_kindImage(self.codeData.kind)).convert_alpha()
        kindIcon = pg.transform.scale(kindIcon, [24, 24])
        self.image.blit(kindIcon, [92, 122])

        gristIcon = pg.image.load(codeDatabase.find_gristImage(self.codeData.grist)).convert_alpha()
        gristIcon = pg.transform.scale(gristIcon, [24, 24])
        self.image.blit(gristIcon, [116, 147])

        for index, eff in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Effective')):
            effIcon = pg.image.load(codeDatabase.find_gristImage(eff)).convert_alpha()
            effIcon = pg.transform.scale(effIcon, [24, 24])
            self.image.blit(effIcon, [124+(25*index), 172])

        for index, dis in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Diseffective')):
            disIcon = pg.image.load(codeDatabase.find_gristImage(dis)).convert_alpha()
            disIcon = pg.transform.scale(disIcon, [24, 24])
            self.image.blit(disIcon, [124+(25*index), 197])

    def update(self):
        for check in UIBase.get_uiElem('CardInspectorCheck').checks:
            if check.selected == True:
                self.change_desc(check.job)
                return
        self.change_desc('/')

    def change_desc(self, new_desc):
        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 48], "center"],
                [self.codeData.name, [65, 48], "left"], 
                [codeDatabase.get_weaponType(self.codeData.kind), [278, 84], "center"], 
                ["TRAIT 1", [46, 84], "center"], 
                [self.codeData.trait1, [110, 84], 'left'],
                ["TRAIT 2", [46, 109], "center"], 
                [self.codeData.trait2, [110, 109], 'left'],
                ["ITEMKIND", [52, 134], "center"], 
                [self.codeData.kind, [121, 134], 'left'],
                ['GRIST TYPE', [64, 159], 'center'], 
                [self.codeData.grist, [146, 159], 'left'],
                ['EFFECTIVE', [68, 184], 'center'], 
                ['INEFFECTIVE', [68, 209], 'center'], 
                ['INSPECT INFORMATION', [159, 305], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '1'), [283, 121], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '2'), [283, 146], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '3'), [283, 171], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, 'BD'), [283, 196], 'center'], 
                ['CST', [30, 330], 'center'], 
                ['DMG', [30, 355], 'center'], 
                ['CODE', [79, 391], 'center'], 
                [self.codeData.code, [151, 391], "center"],
                ['TIER', [223, 391], 'center'], 
                [self.codeData.tier, [265, 391], "center"],
                ['1', [247, 121], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 171], 'center'], 
                ['BD', [247, 196], 'center'],
                ['/', [60, 330], 'center'],
                ['/', [60, 355], 'center'],
                [new_desc, [190, 342], 'center'] #Max Char is 28
                ]
            )

        for child in self.children:
            if isinstance(child, UIBase.get_uiElem('ActionIcon')):
                noAction = True
                break
            else:
                noAction = False

        if noAction == False:
            codeDatabase.get_actionImage(self.codeData.action1, self, [51, 233])
            codeDatabase.get_actionImage(self.codeData.action2, self, [51, 258])
            codeDatabase.get_actionImage(self.codeData.action3, self, [183, 233])
            codeDatabase.get_actionImage(self.codeData.action4, self, [183, 258])

        kindIcon = pg.image.load(codeDatabase.find_kindImage(self.codeData.kind)).convert_alpha()
        kindIcon = pg.transform.scale(kindIcon, [24, 24])
        self.image.blit(kindIcon, [92, 122])

        gristIcon = pg.image.load(codeDatabase.find_gristImage(self.codeData.grist)).convert_alpha()
        gristIcon = pg.transform.scale(gristIcon, [24, 24])
        self.image.blit(gristIcon, [116, 147])

        for index, eff in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Effective')):
            effIcon = pg.image.load(codeDatabase.find_gristImage(eff)).convert_alpha()
            effIcon = pg.transform.scale(effIcon, [24, 24])
            self.image.blit(effIcon, [124+(25*index), 172])

        for index, dis in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Diseffective')):
            disIcon = pg.image.load(codeDatabase.find_gristImage(dis)).convert_alpha()
            disIcon = pg.transform.scale(disIcon, [24, 24])
            self.image.blit(disIcon, [124+(25*index), 197])
