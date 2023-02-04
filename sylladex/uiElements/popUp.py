import pygame as pg
import textwrap

from baseUI import UIBase


class PopUp(UIBase):
    def __init__(self, _text, question=False):
        super().__init__(660, 380, (600, 320), 'PopUp', '#999999')

        self.create_appearance([[576, 296], '#D9D9D9', [12, 12]])

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 48)
        _text_len = len(_text) // 26
        _new_text = textwrap.wrap(_text, 26)
        for _index, _text in enumerate(_new_text):
            self.txt_surface = self.font.render(_text, True, (0,0,0))
            self.image.blit(self.txt_surface, [self.rect.w/2-self.txt_surface.get_width()/2, (self.rect.h/4-self.txt_surface.get_height()/2)+(_index*self.rect.h/6)])

        UIBase.get_group('layer').change_layer(self, 3)

        self.last = pg.time.get_ticks()
        self.timer = 1200  
        self.negate = False

    def remove(self):
        if self.negate == False:
            UIBase.remove_from_group(self)