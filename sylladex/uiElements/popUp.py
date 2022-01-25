import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class PopUp(UIBase):
    def __init__(self, text):
        super().__init__(560, 380, (800, 320), "sylladex/uiElements/asset/MISC/POPUP.png")

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.txt_surface = self.font.render(text, True, (0,0,0))
        self.image.blit(self.txt_surface, [self.rect.w/2-self.txt_surface.get_width()/2, self.rect.h/2-self.txt_surface.get_height()/2])
        self.last = pg.time.get_ticks()
        self.timer = 1200  
        self.negate = False

    def remove(self):
        if self.negate == False:
            UIBase.get_group().remove(self)
            PopUp.kill(self)