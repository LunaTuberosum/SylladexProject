import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.cardList import CardList


class NumTextField(UIBase):
    text = "0"

    def __init__(self, x, y, size, image, maxChar):
        super().__init__(x, y, size, image)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.text = NumTextField.text 
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

        self.maxChar = maxChar
        self.active = False

        self.toolTipText = "The Number of Cards in you Sylladex" 

    def exit_field(self):
        self.active = False
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, CardList):
                amount = int(NumTextField.text) - len(elem.listObj)
                if amount < 0:
                    for removeCard in range(0, amount*-1):
                        elem.remove_fromList(self)
                    elem.place_list()
                else:
                    for newCard in range(0, amount):
                        elem.add_toList()
        
    def draw(self):
        self.image = pg.image.load("sylladex/uiElements/asset/MISC/NUM_CARD_FIELD.png").convert_alpha()
        NumTextField.text = self.text
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