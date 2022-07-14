from os import curdir
import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase


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
        

        super().__init__(self.parent.rect.x+12, self.parent.rect.y+y, (width,height), "surfaceRect", f'CustomSettingAreaBox ({self.typeInput})', True, (255,255,255))
        self.image.set_colorkey((255,255,255))

        if self.typeInput == 'WEAPONKIND':
            self.backgroundColor = pg.Surface((274,24))
            self.backgroundColor.fill('#1C4587')
            self.image.blit(self.backgroundColor, [6, 6])
            
            self.foregroundColor = pg.Surface((274,24))
            self.foregroundColor.fill('#3C78D8')
            self.image.blit(self.foregroundColor, [0, 0])

            self.nameTxt = self.font.render('NAME', True, (0,0,0))
            self.image.blit(self.nameTxt, [24+(24-(self.nameTxt.get_width()/2)), 12-(self.nameTxt.get_height()/2)])

            self.nameTxt = self.font.render('TYPE', True, (0,0,0))
            self.image.blit(self.nameTxt, [178+(24-(self.nameTxt.get_width()/2)), 12-(self.nameTxt.get_height()/2)])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

            if self.inputDetail == 'kind1':
                curImage = customData[1].split(',')[0]
                curKind = customData[0].split(',')[0]
            elif self.inputDetail == 'kind2':
                curImage = customData[1].split(',')[1]
                curKind = customData[0].split(',')[2]

            self.children = [
                UIBase.OptionToggle(self.rect.x, self.rect.y, 24, 24, f'{self.inputDetail}Icon' ,'#C9DAF8', list(codeDatabase.kind.keys()), curImage, curKind, 'Image'),
                UIBase.TextField(self.rect.x+72, self.rect.y, 106, 24, 13, f'{self.inputDetail}Name', f'Changes the name of {curKind}', 'Txt'),
                UIBase.OptionToggle(self.rect.x+226, self.rect.y, 48, 24, f'{self.inputDetail}Type' ,'#C9DAF8', ['NA','MELEE','RANGED','MAGIC'], codeDatabase.get_weaponType(curKind), curKind, 'Text')
            ]

            self.children[1].text = curKind
            self.children[1].font = self.font
            self.children[1].baseColor = '#C9DAF8'
            self.children[1].no_hover()
            self.children[1].hoverColor = '#D9E2F1'
            self.children[1].selectedColor = '#9CB0D5'

        elif self.typeInput == 'ACTION':
            self.backgroundColor = pg.Surface((300,96))
            self.backgroundColor.fill('#1C4587')
            self.image.blit(self.backgroundColor, [6, 6])
            
            self.foregroundColor = pg.Surface((300,96))
            self.foregroundColor.fill('#3C78D8')
            self.image.blit(self.foregroundColor, [0, 0])

            self.nameTxt = self.font.render('COST', True, (0,0,0))
            self.image.blit(self.nameTxt, [108+(24-(self.nameTxt.get_width()/2)), 12-(self.nameTxt.get_height()/2)])

            self.nameTxt = self.font.render('DMG', True, (0,0,0))
            self.image.blit(self.nameTxt, [204+(24-(self.nameTxt.get_width()/2)), 12-(self.nameTxt.get_height()/2)])

            self.nameTxt = self.font.render('ACTION DESCRIPTION', True, (0,0,0))
            self.image.blit(self.nameTxt, [150-(self.nameTxt.get_width()/2), 24+(12-(self.nameTxt.get_height()/2))])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

            if self.inputDetail == 'action1':
                curAction = customData[2].split(',')[0]
            elif self.inputDetail == 'action2':
                curAction = customData[2].split(',')[4]

            self.children = [
                UIBase.ActionIcon(self.rect.x, self.rect.y, f'{self.inputDetail}Icon'),
                UIBase.TextField(self.rect.x+156, self.rect.y, 48, 24, 1, f'{self.inputDetail}Cost', f'Change {curAction}\'s cost', 'Num'),
                UIBase.TextField(self.rect.x+252, self.rect.y, 48, 24, 1, f'{self.inputDetail}Dmg', f'Change {curAction}\'s damage', 'Num'),
                UIBase.LongTextField(self.rect.x, self.rect.y+48, 300, 48, 30, 3, f'{self.inputDetail}Desc', f'Change {curAction}\'s description')
            ]

            if self.inputDetail == 'action1':
                curAction = customData[2].split(',')[0]
            elif self.inputDetail == 'action2':
                curAction = customData[2].split(',')[4]

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
            if self.inputDetail[:4] == 'name':
                self.backgroundColor = pg.Surface((156,24))
                self.backgroundColor.fill('#1C4587')
                self.image.blit(self.backgroundColor, [6, 6])
                
                self.foregroundColor = pg.Surface((156,24))
                self.foregroundColor.fill('#3C78D8')
                self.image.blit(self.foregroundColor, [0, 0])

            elif self.inputDetail[:4] == 'tier':
                self.backgroundColor = pg.Surface((300,72))
                self.backgroundColor.fill('#1C4587')
                self.image.blit(self.backgroundColor, [6, 6])
                
                self.foregroundColor = pg.Surface((300,72))
                self.foregroundColor.fill('#3C78D8')
                self.image.blit(self.foregroundColor, [0, 0])
    
    def update(self):

        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
                customData = database.readlines()

        if self.typeInput == 'ACTION':
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.ToggleButton):
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
                    