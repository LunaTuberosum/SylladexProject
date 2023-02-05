import sys
import pygame as pg

from uiElement import UIElement

class EscapeMenuOption(UIElement):
    def __init__(self, x, y, text):
        
        self.text = text
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.color= '#1118ee'
        self.hover_color = '#551a8b'

        self.prefix = self.font.render('> ', True, self.color)
        self.big_prefix = self.font.render('==> ', True, self.color)
        self.big_prefix_alt = self.font.render('==> ', True, self.hover_color)

        self.font.set_underline(True)

        self.txt_surf = self.font.render(self.text, False, self.color)
        self.txt_surf_alt = self.font.render(self.text, False, self.hover_color)

        self.x = x
        super().__init__(x+(102.5-(self.prefix.get_width()/2+self.txt_surf.get_width()/2)), y, (self.prefix.get_width()+self.txt_surf.get_width(), 51), f'EscapeOption ({self.text})', (239, 239, 239))

        UIElement.get_group('layer').change_layer(self, 3)

        self.image.blit(self.prefix, [0,0])
        self.image.blit(self.txt_surf, [self.prefix.get_width(),0])

        self.hovering = False

    def hover(self):
        self.image = pg.Surface((self.big_prefix.get_width()+self.txt_surf.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.big_prefix, [0,0])
        self.image.blit(self.txt_surf, [self.big_prefix.get_width(),0])

        self.rect.x =  self.x+(102.5-(self.big_prefix.get_width()/2+self.txt_surf.get_width()/2))

        self.hovering = True
    
    def no_hover(self):
        self.image = pg.Surface((self.prefix.get_width()+self.txt_surf.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.prefix, [0,0])
        self.image.blit(self.txt_surf, [self.prefix.get_width(),0])
        self.hovering = False

        self.rect.x =  self.x+(102.5-(self.prefix.get_width()/2+self.txt_surf.get_width()/2))\

    def on_click(self):
        self.image = pg.Surface((self.big_prefix_alt.get_width()+self.txt_surf_alt.get_width(), 51))
        self.image.fill((239,239,239))
        self.image.blit(self.big_prefix_alt, [0,0])
        self.image.blit(self.txt_surf_alt, [self.big_prefix_alt.get_width(),0])

        if self.text == 'To Desktop':
            pg.quit()
            sys.exit()
