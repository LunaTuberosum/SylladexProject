import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.cardList import CardList


class TextField(pg.sprite.Sprite):

    def __init__(self, x, y, width, height, maxChar, job, toolTipText, defaultValue):
        super().__init__()

        UIBase.add_toGroup(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.image = pg.Surface((width, height))
        self.image.fill((255,255,255))
        self.rect = pg.Rect(x, y, width, height)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.text = defaultValue
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

        self.maxChar = maxChar
        self.job = job
        self.active = False

        self.toolTipText = toolTipText

    def exit_field(self):
        self.active = False
        self.image.fill((255,255,255))
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, CardList) and self.job == "numOfCards":
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

            else:
                if event.key != pg.K_RETURN and len(self.text) < self.maxChar:
                    self.text += event.unicode
                    self.draw()

    def on_click(self):
        self.active = True
        self.image.fill((170,170,170))
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))
        
        