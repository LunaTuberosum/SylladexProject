import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase


class TextField(UIBase):

    def __init__(self, x, y, width, height, maxChar, job, toolTipText, textType, textColor=(0,0,0)):
        super().__init__(x, y, (width, height), 'surfaceRect', f'TextField ({job})', True, (255,255,255))

        self.textColor = textColor
        self.textType = textType
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        if self.textType == 'Num':
            self.defultText = '0'
            self.text = self.defultText
        if self.textType == 'Txt':
            self.defultText = ''
            self.text = self.defultText
        self.txt_surface = self.font.render(self.text, True, self.textColor)
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

        self.maxChar = maxChar
        self.job = job
        self.active = False
        self.hovering = False

        self.toolTipText = toolTipText

        self.baseColor = (255,255,255)
        self.hoverColor = (230,230,230)
        self.selectedColor = (170,170,170)

    def changeColors(self, base, hover, selected):
        self.baseColor = base
        self.hoverColor = hover
        self.selectedColor = selected

        self.no_hover()

    def exit_field(self):
        self.active = False
        
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.CardList) and self.job == "numOfCards":
                amount = int(self.text) - len(elem.children)
                if amount < 0:
                    for removeCard in range(0, amount*-1):
                        elem.remove_fromList(self)
                    elem.place_list()
                else:
                    for newCard in range(0, amount):
                        elem.add_toList()

            elif isinstance(elem, UIBase.ToggleButton):
                if elem.job == 'meleeToggle':
                    if elem.on == True:
                        if self.job == 'action1Cost':
                            codeDatabase.change_codeValue('Melee 1 Cost', self.text)
                        elif self.job == 'action1Dmg':
                            codeDatabase.change_codeValue('Melee 1 Dmg', self.text)
                        elif self.job == 'action2Cost':
                            codeDatabase.change_codeValue('Melee 2 Cost', self.text)
                        elif self.job == 'action2Dmg':
                            codeDatabase.change_codeValue('Melee 2 Dmg', self.text)
                elif elem.job == 'rangedToggle':
                    if elem.on == True:
                        if self.job == 'action1Cost':
                            codeDatabase.change_codeValue('Ranged 1 Cost', self.text)
                        elif self.job == 'action1Dmg':
                            codeDatabase.change_codeValue('Ranged 1 Dmg', self.text)
                        elif self.job == 'action2Cost':
                            codeDatabase.change_codeValue('Ranged 2 Cost', self.text)
                        elif self.job == 'action2Dmg':
                            codeDatabase.change_codeValue('Ranged 2 Dmg', self.text)
                elif elem.job == 'magicToggle':
                    if elem.on == True:
                        if self.job == 'action1Cost':
                            codeDatabase.change_codeValue('Magic 1 Cost', self.text)
                        elif self.job == 'action1Dmg':
                            codeDatabase.change_codeValue('Magic 1 Dmg', self.text)
                        elif self.job == 'action2Cost':
                            codeDatabase.change_codeValue('Magic 2 Cost', self.text)
                        elif self.job == 'action2Dmg':
                            codeDatabase.change_codeValue('Magic 2 Dmg', self.text)

        if self.job == 'kind1Name':
            codeDatabase.change_codeValue('Customkind 1', self.text)
            self.job = f'{self.text}Name'
            self.objName = f'TextField ({self.job})'
            self.toolTipText = f'Changes the name of {self.text}'
        elif self.job == 'kind2Name':
            codeDatabase.change_codeValue('Customkind 2', self.text)
            self.job = f'{self.text}Name'
            self.objName = f'TextField ({self.job})'
            self.toolTipText = f'Changes the name of {self.text}'
                    
        
    def draw(self):
        self.image.fill(self.selectedColor)
        
        self.txt_surface = self.font.render(self.text, True, self.textColor)
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

    def typeing(self, event):
        
        if self.active == True:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
                self.draw()

            elif event.key == pg.K_RETURN:
                
                if len(self.text) > 1:
                    if self.text[0] == '0':
                        self.text = self.text[1:]

                if len(self.job) > 6 and self.job[-6:] == 'NumBox':
                    for elem in UIBase.get_group('ui'):
                        if isinstance(elem, UIBase.GristCacheLimit):
                            if self.text > elem.limitNum:
                                self.text = elem.limitNum
                        if isinstance(elem, UIBase.GristCache):
                            elem.save_cache()
                            
                if self.text == "":
                    if self.textType == 'Num':
                        self.text = self.defultText
                    elif self.textType == 'Txt':
                        self.text = self.defultText
                self.exit_field()
                return

            elif event.key == pg.K_TAB:
                if pg.time.get_ticks() - UIBase.prevTick >= 1:
                    if self.job == 'nameOverlay':
                        nextText = 'codeOverlay'
                    elif self.job == 'codeOverlay':
                        nextText = 'tierOverlay'
                    elif self.job == 'tierOverlay':
                        nextText = 'nameOverlay'

                    for elem in UIBase.get_group('ui'):
                        if isinstance(elem, UIBase.TextField):
                            if elem.job == nextText:
                                elem.on_click()
                                elem.draw()
                                self.exit_field()
                                self.no_hover()
                                UIBase.prevTick = pg.time.get_ticks()

            else:
                if event.key != pg.K_RETURN and len(self.text) < self.maxChar:
                    
                    self.text += event.unicode

                    if len(self.job) > 6 and self.job[-6:] == 'NumBox':
                        isNum = False
                        for num in range(0,10):
                            if len(self.text) > 0 and self.text[-1] == str(num):
                                isNum = True
                        if isNum == False:
                            if len(self.text) > 0:
                                self.text = self.text[:-1]

                    self.draw()

    def hover(self):
        if self.active == False:
            self.image.fill(self.hoverColor)
            self.txt_surface = self.font.render(self.text, True, self.textColor)
            self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.image.fill(self.baseColor)
            self.txt_surface = self.font.render(self.text, True, self.textColor)
            self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
            self.hovering = False

    def on_click(self):
        self.active = True
        self.image.fill(self.selectedColor)
        self.txt_surface = self.font.render(self.text, True, self.textColor)
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
        
        