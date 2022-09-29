import pygame as pg

from baseUI import UIBase
import settings
from sylladex.captchalogueCards import codeDatabase

class CardInspector(UIBase):
    def __init__(self, codeData):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 447), 'CardInspector', (209,158,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.codeData = codeData
        self.prevDescType = 'None'
        UIBase.get_group('layer').change_layer(self, 3)

        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 47], "center"],
                [self.codeData.name, [65, 47], "left"], 
                [codeDatabase.get_weaponType(self.codeData.kind), [278, 83], "center"], 
                ["TRAIT 1", [46, 83], "center"], 
                [self.codeData.trait1, [110, 83], 'left'],
                ["TRAIT 2", [46, 108], "center"], 
                [self.codeData.trait2, [110, 108], 'left'],
                ["ITEMKIND", [52, 133], "center"], 
                [self.codeData.kind, [121, 133], 'left'],
                ['GRIST TYPE', [64, 158], 'center'], 
                [self.codeData.grist, [146, 158], 'left'],
                ['EFFECTIVE', [68, 183], 'center'], 
                ['INEFFECTIVE', [68, 208], 'center'], 
                ['INSPECT INFORMATION', [159, 304], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '1'), [283, 120], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '2'), [283, 145], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '3'), [283, 170], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, 'BD'), [283, 195], 'center'], 
                ['CST', [30, 331], 'center'], 
                ['DMG', [30, 361], 'center'], 
                ['CODE', [79, 399], 'center'], 
                [self.codeData.code, [151, 399], "center"],
                ['TIER', [223, 399], 'center'], 
                [self.codeData.tier, [265, 399], "center"],
                ['1', [247, 120], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 170], 'center'], 
                ['BD', [247, 195], 'center'],
                ['/', [60, 331], 'center'],
                ['/', [60, 361], 'center'],
                ['/', [192, 346], 'center'] #Max Char is 28
                ]
            )

        self.children = [
            UIBase.get_uiElem('CardInspectorButton')(self),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+81, self.rect.y+71, 'Trait1'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+81, self.rect.y+96, 'Trait2'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+27, self.rect.y+232, 'Action1'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+27, self.rect.y+257, 'Action2'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+159, self.rect.y+232, 'Action3'),
            UIBase.get_uiElem('CardInspectorCheck')(self.rect.x+159, self.rect.y+257, 'Action4'),
        ]

        codeDatabase.get_actionImage(self.codeData.action1, self, [51, 232])
        codeDatabase.get_actionImage(self.codeData.action2, self, [51, 257])
        codeDatabase.get_actionImage(self.codeData.action3, self, [183, 232])
        codeDatabase.get_actionImage(self.codeData.action4, self, [183, 257])

        kindIcon = pg.image.load(codeDatabase.find_kindImage(self.codeData.kind)).convert_alpha()
        kindIcon = pg.transform.scale(kindIcon, [24, 24])
        self.image.blit(kindIcon, [92, 121])

        gristIcon = pg.image.load(codeDatabase.find_gristImage(self.codeData.grist)).convert_alpha()
        gristIcon = pg.transform.scale(gristIcon, [24, 24])
        self.image.blit(gristIcon, [116, 146])

        for index, eff in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Effective')):
            effIcon = pg.image.load(codeDatabase.find_gristImage(eff)).convert_alpha()
            effIcon = pg.transform.scale(effIcon, [24, 24])
            self.image.blit(effIcon, [124+(25*index), 171])

        for index, dis in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Diseffective')):
            disIcon = pg.image.load(codeDatabase.find_gristImage(dis)).convert_alpha()
            disIcon = pg.transform.scale(disIcon, [24, 24])
            self.image.blit(disIcon, [124+(25*index), 197])

    def update(self):
        for check in UIBase.get_uiElem('CardInspectorCheck').checks:
            if check.selected == True:
                if check.job == 'Trait1' and self.prevDescType != 'Trait1':
                    self.prevDescType = 'Trait1'
                    traitDesc = codeDatabase.get_trat1Data(self.codeData.trait1, self.codeData.kind, int(self.codeData.tier)).split(' ')
                    lines = ['']

                    wordMax = 0
                    curLine = 0
                    for word in traitDesc:
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word}')
                            curLine += 1
                    
                    self.change_desc(lines, len(lines))

                elif check.job == 'Trait2' and self.prevDescType != 'Trait2':
                    self.prevDescType = 'Trait2'
                    traitDesc = codeDatabase.get_trat2Data(self.codeData.trait2, self.codeData.kind, int(self.codeData.tier)).split(' ')
                    lines = ['']


                    wordMax = 0
                    curLine = 0
                    for word in traitDesc:
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word} ')
                            curLine += 1

                    self.change_desc(lines, len(lines))

                elif check.job == 'Action1' and self.prevDescType != 'Action1':
                    self.prevDescType = 'Action1'
                    actionInfo = codeDatabase.get_actionInfo(self.codeData.action1)

                    lines = ['']


                    wordMax = 0
                    curLine = 0
                    for word in actionInfo[2].split(' '):
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word} ')
                            curLine += 1

                    self.change_desc(lines, len(lines), True, actionInfo)

                elif check.job == 'Action2' and self.prevDescType != 'Action2':
                    self.prevDescType = 'Action2'
                    actionInfo = codeDatabase.get_actionInfo(self.codeData.action2)

                    lines = ['']


                    wordMax = 0
                    curLine = 0
                    for word in actionInfo[2].split(' '):
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word} ')
                            curLine += 1

                    print(lines)

                    self.change_desc(lines, len(lines), True, actionInfo)

                elif check.job == 'Action3' and self.prevDescType != 'Action3':
                    self.prevDescType = 'Action3'
                    actionInfo = codeDatabase.get_actionInfo(self.codeData.action3)

                    lines = ['']


                    wordMax = 0
                    curLine = 0
                    for word in actionInfo[2].split(' '):
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word} ')
                            curLine += 1

                    self.change_desc(lines, len(lines), True, actionInfo)

                elif check.job == 'Action4' and self.prevDescType != 'Action4':
                    self.prevDescType = 'Action4'
                    actionInfo = codeDatabase.get_actionInfo(self.codeData.action4)

                    lines = ['']


                    wordMax = 0
                    curLine = 0
                    for word in actionInfo[2].split(' '):
                        if wordMax + len(word) < 28:
                            wordMax += len(word) + 1
                            lines[curLine] += f'{word} '
                        else:
                            wordMax = len(word) + 1
                            lines.append(f'{word} ')
                            curLine += 1

                    self.change_desc(lines, len(lines), True, actionInfo)
                return

        if self.prevDescType != 'None':
            self.change_desc('/', 1)
            self.prevDescType = 'None'

    def change_desc(self, new_desc, lineCount, isAction = False, actionData = None):
        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 47], "center"],
                [self.codeData.name, [65, 47], "left"], 
                [codeDatabase.get_weaponType(self.codeData.kind), [278, 83], "center"], 
                ["TRAIT 1", [46, 83], "center"], 
                [self.codeData.trait1, [110, 83], 'left'],
                ["TRAIT 2", [46, 108], "center"], 
                [self.codeData.trait2, [110, 108], 'left'],
                ["ITEMKIND", [52, 133], "center"], 
                [self.codeData.kind, [121, 133], 'left'],
                ['GRIST TYPE', [64, 158], 'center'], 
                [self.codeData.grist, [146, 158], 'left'],
                ['EFFECTIVE', [68, 183], 'center'], 
                ['INEFFECTIVE', [68, 208], 'center'], 
                ['INSPECT INFORMATION', [159, 304], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '1'), [283, 120], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '2'), [283, 145], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, '3'), [283, 170], 'center'], 
                [codeDatabase.get_damageNumValue(self.codeData.tier, 'BD'), [283, 195], 'center'], 
                ['CST', [30, 331], 'center'], 
                ['DMG', [30, 361], 'center'], 
                ['CODE', [79, 399], 'center'], 
                [self.codeData.code, [151, 399], "center"],
                ['TIER', [223, 399], 'center'], 
                [self.codeData.tier, [265, 399], "center"],
                ['1', [247, 120], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 170], 'center'], 
                ['BD', [247, 195], 'center']
                ]
            )

        if isAction == False:
            self.create_appearance(texts = [
                ['/', [60, 331], 'center'],
                ['/', [60, 361], 'center']])
        else:
            self.create_appearance(texts = [
                [actionData[0], [60, 331], 'center'],
                [actionData[1], [60, 361], 'center']])

        
        if lineCount == 1:
            self.create_appearance(texts = [[new_desc[0], [192, 346], 'center']])
        
        elif lineCount == 2:
            self.create_appearance(texts = [[new_desc[0], [192, 337], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 355], 'center']])
        
        elif lineCount == 3:
            self.create_appearance(texts = [[new_desc[0], [192, 328], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 346], 'center']])
            self.create_appearance(texts = [[new_desc[2], [192, 364], 'center']])
        
        elif lineCount == 4:
            self.create_appearance(texts = [[new_desc[0], [192, 326], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 342], 'center']])
            self.create_appearance(texts = [[new_desc[2], [192, 355], 'center']])
            self.create_appearance(texts = [[new_desc[3], [192, 368], 'center']])

        for child in self.children:
            if isinstance(child, UIBase.get_uiElem('ActionIcon')):
                noAction = True
                break
            else:
                noAction = False

        if noAction == False:
            codeDatabase.get_actionImage(self.codeData.action1, self, [51, 232])
            codeDatabase.get_actionImage(self.codeData.action2, self, [51, 257])
            codeDatabase.get_actionImage(self.codeData.action3, self, [183, 232])
            codeDatabase.get_actionImage(self.codeData.action4, self, [183, 257])

        kindIcon = pg.image.load(codeDatabase.find_kindImage(self.codeData.kind)).convert_alpha()
        kindIcon = pg.transform.scale(kindIcon, [24, 24])
        self.image.blit(kindIcon, [92, 121])

        gristIcon = pg.image.load(codeDatabase.find_gristImage(self.codeData.grist)).convert_alpha()
        gristIcon = pg.transform.scale(gristIcon, [24, 24])
        self.image.blit(gristIcon, [116, 146])

        for index, eff in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Effective')):
            effIcon = pg.image.load(codeDatabase.find_gristImage(eff)).convert_alpha()
            effIcon = pg.transform.scale(effIcon, [24, 24])
            self.image.blit(effIcon, [124+(25*index), 171])

        for index, dis in enumerate(codeDatabase.gristData.get(self.codeData.grist).get('Diseffective')):
            disIcon = pg.image.load(codeDatabase.find_gristImage(dis)).convert_alpha()
            disIcon = pg.transform.scale(disIcon, [24, 24])
            self.image.blit(disIcon, [124+(25*index), 196])
