import sys
import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class EscapeMenuOption(UIBase):
    def __init__(self, x, y, text):

        
        self.text = text
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.color= '#1118ee'
        self.hoverColor = '#551a8b'

        self.prefix = self.font.render('> ', True, self.color)
        self.bigPrefix = self.font.render('==> ', True, self.color)
        self.bigPrefixAlt = self.font.render('==> ', True, self.hoverColor)

        self.font.set_underline(True)

        self.txt_surf = self.font.render(self.text, False, self.color)
        self.txt_surfAlt = self.font.render(self.text, False, self.hoverColor)

        self.x = x
        super().__init__(x+(102.5-(self.prefix.get_width()/2+self.txt_surf.get_width()/2)), y, (self.prefix.get_width()+self.txt_surf.get_width(), 51), "surfaceRect" ,f'EscapeOption ({self.text})', True, (239, 239, 239))

        self.image.blit(self.prefix, [0,0])
        self.image.blit(self.txt_surf, [self.prefix.get_width(),0])

        self.hovering = False

    def hover(self):
        self.image = pg.Surface((self.bigPrefix.get_width()+self.txt_surf.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.bigPrefix, [0,0])
        self.image.blit(self.txt_surf, [self.bigPrefix.get_width(),0])

        self.rect.x =  self.x+(102.5-(self.bigPrefix.get_width()/2+self.txt_surf.get_width()/2))

        self.hovering = True
    
    def no_hover(self):
        self.image = pg.Surface((self.prefix.get_width()+self.txt_surf.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.prefix, [0,0])
        self.image.blit(self.txt_surf, [self.prefix.get_width(),0])
        self.hovering = False

        self.rect.x =  self.x+(102.5-(self.prefix.get_width()/2+self.txt_surf.get_width()/2))\

    def on_click(self):
        self.image = pg.Surface((self.bigPrefixAlt.get_width()+self.txt_surfAlt.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.bigPrefixAlt, [0,0])
        self.image.blit(self.txt_surfAlt, [self.bigPrefixAlt.get_width(),0])

        if self.text == 'To Desktop':
            pg.quit()
            sys.exit()
