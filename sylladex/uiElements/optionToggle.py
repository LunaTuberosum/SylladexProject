import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase


class OptionToggle(UIBase):
    def __init__(self,x, y, w, h, job, color, options, defultOption, customObj, showType):
        super().__init__(x, y, (w,h), 'surfaceRect', f'DropDown ({job})', True, color)

        self.job = job
        self.options = options
        self.currentOption = defultOption
        self.customObj = customObj
        self.toolTipText = f'Change weapon type for {self.customObj}'
        self.showType = showType

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 16)

        for index, option in enumerate(self.options):
            if option == self.currentOption:
                self.currentIndex = index

        if self.showType == 'Text':
            self.currentText = self.font.render(f'{self.currentOption}', True, (0,0,0))
            self.image.blit(self.currentText, [(24-(self.currentText.get_width()/2)), 12-(self.currentText.get_height()/2)])
        elif self.showType == 'Image':
            self.currentImage = pg.image.load(codeDatabase.find_kindImage(self.currentOption)).convert_alpha()
            self.currentImage = pg.transform.scale(self.currentImage, (24,24))
            self.image.blit(self.currentImage, [0,0])

            
    def on_click(self):
        self.currentIndex += 1
        if self.currentIndex == len(self.options): self.currentIndex = 0
        self.currentOption = self.options[self.currentIndex]

        self.image.fill('#C9DAF8')

        if self.showType == 'Text':
            self.currentText = self.font.render(f'{self.currentOption}', True, (0,0,0))
            self.image.blit(self.currentText, [(24-(self.currentText.get_width()/2)), 12-(self.currentText.get_height()/2)])

            codeDatabase.change_codeValue(f'{self.customObj} Type', self.currentOption)
        elif self.showType == 'Image':
            self.currentImage = pg.image.load(codeDatabase.find_kindImage(self.currentOption)).convert_alpha()
            self.currentImage = pg.transform.scale(self.currentImage, (24,24))
            self.image.blit(self.currentImage, [0,0])

            codeDatabase.change_codeValue(f'{self.customObj} Icon', self.currentOption)

    def on_altClick(self):
        self.currentIndex -= 1
        if self.currentIndex == -1: self.currentIndex = len(self.options)-1
        self.currentOption = self.options[self.currentIndex]

        self.image.fill('#C9DAF8')

        if self.showType == 'Text':
            self.currentText = self.font.render(f'{self.currentOption}', True, (0,0,0))
            self.image.blit(self.currentText, [(24-(self.currentText.get_width()/2)), 12-(self.currentText.get_height()/2)])

            codeDatabase.change_codeValue(f'{self.customObj} Type', self.currentOption)
        elif self.showType == 'Image':
            self.currentImage = pg.image.load(codeDatabase.find_kindImage(self.currentOption)).convert_alpha()
            self.currentImage = pg.transform.scale(self.currentImage, (24,24))
            self.image.blit(self.currentImage, [0,0])

            codeDatabase.change_codeValue(f'{self.customObj} Icon', self.currentOption)
