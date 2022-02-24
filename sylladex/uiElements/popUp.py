import pygame as pg
import textwrap

from sylladex.uiElements.baseUI import UIBase


class PopUp(UIBase):
    def __init__(self, text, question=False):
        super().__init__(660, 380, (600, 320), "sylladex/uiElements/asset/MISC/POPUP.png")

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 48)
        text_len = len(text) // 26
        newText = textwrap.wrap(text, 26)
        for index, text in enumerate(newText):
            self.txt_surface = self.font.render(text, True, (0,0,0))
            self.image.blit(self.txt_surface, [self.rect.w/2-self.txt_surface.get_width()/2, (self.rect.h/4-self.txt_surface.get_height()/2)+(index*self.rect.h/6)])

        self.last = pg.time.get_ticks()
        self.timer = 1200  
        self.negate = False

    def remove(self):
        if self.negate == False:
            UIBase.remove_fromGroup(self)
            self.kill()