import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class TextField(UIBase):

    def __init__(self, x, y, width, height, maxChar, job, toolTipText, defaultValue):
        super().__init__(x, y, (width, height), 'surfaceRect', True, (255,255,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.text = defaultValue
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

        self.maxChar = maxChar
        self.job = job
        self.active = False
        self.hovering = False

        self.toolTipText = toolTipText

    def exit_field(self):
        self.active = False
        self.image.fill((255,255,255))
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.CardList) and self.job == "numOfCards":
                amount = int(self.text) - len(elem.listObj)
                if amount < 0:
                    for removeCard in range(0, amount*-1):
                        elem.remove_fromList(self)
                    elem.place_list()
                else:
                    for newCard in range(0, amount):
                        elem.add_toList()
        
    def draw(self):
        self.image.fill((160,160,160))
        
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
     
           

    def typeing(self, event):
        
        if self.active == True:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
                self.draw()

            elif event.key == pg.K_RETURN:
                if self.text == "":
                    self.text = "0"
                self.draw()
                self.exit_field()

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
                                self.draw()
                                self.exit_field()
                                UIBase.prevTick = pg.time.get_ticks()
                                return

            else:
                if event.key != pg.K_RETURN and len(self.text) < self.maxChar:
                    self.text += event.unicode
                    self.draw()

    def hover(self):
        if self.active == False:
            self.image.fill((230,230,230))
            self.txt_surface = self.font.render(self.text, True, (0,0,0))
            self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.image.fill((255,255,255))
            self.txt_surface = self.font.render(self.text, True, (0,0,0))
            self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
            self.hovering = False

    def on_click(self):
        self.active = True
        self.image.fill((170,170,170))
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
        
        