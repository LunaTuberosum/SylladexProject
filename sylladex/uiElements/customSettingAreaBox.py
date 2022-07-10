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

            if self.inputDetail == customData[0].split(',')[0]:
                curImage = customData[1].split(',')[0]
            elif self.inputDetail == customData[0].split(',')[2]:
                curImage = customData[1].split(',')[1]

            self.children = [
                UIBase.OptionToggle(self.rect.x, self.rect.y, 24, 24, f'{self.inputDetail}WeaponIcon' ,'#C9DAF8', list(codeDatabase.kind.keys()), curImage, self.inputDetail, 'Image'),
                UIBase.TextField(self.rect.x+72, self.rect.y, 106, 24, 13, f'{self.inputDetail}Name', f'Changes the name of {self.inputDetail}', 'Txt'),
                UIBase.OptionToggle(self.rect.x+226, self.rect.y, 48, 24, f'{self.inputDetail}WeaponType' ,'#C9DAF8', ['NA','MELEE','RANGED','MAGIC'], codeDatabase.get_weaponType(self.inputDetail), self.inputDetail, 'Text')
            ]

            self.children[1].text = self.inputDetail
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