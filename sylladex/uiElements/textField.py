import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp


class TextField(UIBase):
    def __init__(self, x, y, size, image, maxChar):
        super().__init__(x, y, size, image)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.text = ""
        self.txt_surface = self.font.render("", True, (0,0,0))

        self.maxChar = maxChar
        self.active = False
        
    def draw(self):
        self.image = pg.image.load("sylladex/uiElements/asset/MISC/NUM_CARD_FIELD.png").convert_alpha()
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2))

    def on_click(self):
        self.active = True