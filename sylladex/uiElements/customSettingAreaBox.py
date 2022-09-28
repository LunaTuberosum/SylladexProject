import pygame as pg

from baseUI import UIBase

class CustomSettingAreaBox(UIBase):
    def __init__(self, parent, typeInput, inputDetail, y):
        self.typeInput = typeInput
        self.inputDetail = inputDetail
        self.parent = parent

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        if self.typeInput == 'WEAPONKIND':
            width = 280
            height = 30
        elif self.typeInput == 'ACTION':
            width = 306
            height = 102
        elif self.typeInput == 'TRAIT':
            if self.inputDetail[:4] == 'name':
                width = 162
                height = 30
            elif self.inputDetail[:4] == 'tier':
                width = 306
                height = 78
        

        super().__init__(self.parent.rect.x+12, self.parent.rect.y+y, (width,height), f'CustomSettingAreaBox ({self.typeInput})', (255,255,255))

        if self.typeInput == 'WEAPONKIND':
            self.create_appearance([[274, 24], '#1C4587', [6, 6]], [[274, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['NAME', [48, 12], 'center'], ['TYPE', [202, 12], 'center']])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

            if self.inputDetail == 'kind1':
                curImage = customData[1].split(',')[0]
                curKind = customData[0].split(',')[0]
            elif self.inputDetail == 'kind2':
                curImage = customData[1].split(',')[1]
                curKind = customData[0].split(',')[2]

            self.children = [
                UIBase.get_uiElem('OptionToggle')(self.rect.x, self.rect.y, 24, 24, f'{self.inputDetail}Icon' ,'#C9DAF8', list(UIBase.CodeDatabase.kind.keys()), curImage, curKind, 'Image'),
                UIBase.get_uiElem('TextField')(self.rect.x+72, self.rect.y, 106, 24, 13, f'{self.inputDetail}Name', f'Changes the name of {curKind}', 'Txt'),
                UIBase.get_uiElem('OptionToggle')(self.rect.x+226, self.rect.y, 48, 24, f'{self.inputDetail}Type' ,'#C9DAF8', ['NA','MELEE','RANGED','MAGIC'], UIBase.CodeDatabase.get_weaponType(curKind), curKind, 'Text')
            ]

            self.children[1].text = curKind
            self.children[1].font = self.font
            self.children[1].baseColor = '#C9DAF8'
            self.children[1].no_hover()
            self.children[1].hoverColor = '#D9E2F1'
            self.children[1].selectedColor = '#9CB0D5'

        elif self.typeInput == 'ACTION':
            self.create_appearance([[300, 96], '#1C4587', [6, 6]], [[300, 96], '#3C78D8', [0, 0]], colorKey = True, texts = [['COST', [132, 12], 'center'], ['DMG', [228, 12], 'center'], ['ACTION DESCRPTION', [150, 36], 'center']])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

            if self.inputDetail == 'action1':
                curAction = customData[2].split(',')[0]
            elif self.inputDetail == 'action2':
                curAction = customData[2].split(',')[4]

            self.children = [
                UIBase.get_uiElem('ActionIcon')(self.rect.x, self.rect.y, f'{self.inputDetail}Icon'),
                UIBase.get_uiElem('TextField')(self.rect.x+156, self.rect.y, 48, 24, 1, f'{self.inputDetail}Cost', f'Change {curAction}\'s cost', 'Num'),
                UIBase.get_uiElem('TextField')(self.rect.x+252, self.rect.y, 48, 24, 1, f'{self.inputDetail}Dmg', f'Change {curAction}\'s damage', 'Num'),
                UIBase.get_uiElem('LongTextField')(self.rect.x, self.rect.y+48, 300, 48, 28, 3, f'{self.inputDetail}Desc', f'Change {curAction}\'s description')
            ]

            self.children[1].font = self.font
            self.children[1].baseColor = '#C9DAF8'
            self.children[1].no_hover()
            self.children[1].hoverColor = '#D9E2F1'
            self.children[1].selectedColor = '#9CB0D5'

            self.children[2].defultText = '/'
            self.children[2].font = self.font
            self.children[2].baseColor = '#C9DAF8'
            self.children[2].no_hover()
            self.children[2].hoverColor = '#D9E2F1'
            self.children[2].selectedColor = '#9CB0D5'

            self.children[3].font = self.font
            self.children[3].baseColor = '#C9DAF8'
            self.children[3].no_hover()
            self.children[3].hoverColor = '#D9E2F1'
            self.children[3].selectedColor = '#9CB0D5'


        elif self.typeInput == 'TRAIT':
            if self.inputDetail == 'name':
                self.create_appearance([[156, 24], '#1C4587', [6, 6]], [[156, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['NAME', [24, 12], 'center']])

                with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                    customData = database.readlines()

                self.children = [
                    UIBase.get_uiElem('TextField')(self.rect.x+48, self.rect.y, 108, 24, 13, 'traitName', f'Change the name of the trait', 'Txt')
                ]

                self.children[0].font = self.font
                self.children[0].baseColor = '#C9DAF8'
                self.children[0].no_hover()
                self.children[0].hoverColor = '#D9E2F1'
                self.children[0].selectedColor = '#9CB0D5'

            elif self.inputDetail[:4] == 'tier':
                self.create_appearance([[300, 72], '#1C4587', [6, 6]], [[300, 72], '#3C78D8', [0, 0]], colorKey = True, texts = [['TIER '+self.inputDetail[4:]+' DESCRIPTION', [150, 12], 'center']])

                self.children = [
                    UIBase.get_uiElem('LongTextField')(self.rect.x, self.rect.y+24, 300, 48, 28, 3, f'{self.inputDetail[4:]}Desc', f'Change the description for tiers {self.inputDetail[4:]}')
                ]

                self.children[0].font = self.font
                self.children[0].baseColor = '#C9DAF8'
                self.children[0].no_hover()
                self.children[0].hoverColor = '#D9E2F1'
                self.children[0].selectedColor = '#9CB0D5'
    
    def update(self):

        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

        if self.typeInput == 'ACTION':
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                    if elem.job == 'meleeToggle' and elem.on == True:
                        if self.inputDetail == 'action1':
                            if self.children[1].active == False:
                                self.children[1].text = customData[2].split(',')[1]
                                self.children[1].no_hover()
                            if self.children[2].active == False:
                                self.children[2].text = customData[2].split(',')[2]
                                self.children[2].no_hover()
                            break
                        elif self.inputDetail == 'action2':
                            if self.children[1].active == False:
                                self.children[1].text = customData[2].split(',')[5]
                                self.children[1].no_hover()
                            if self.children[2].active == False:
                                self.children[2].text = customData[2].split(',')[6]
                                self.children[2].no_hover()
                            break
                    