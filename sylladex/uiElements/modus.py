import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class Modus(UIBase):
    def __init__(self, x, y, size, image, modus):
        super().__init__(x, y, size, image)
        self.modus = modus
        
        if UIBase.get_modus() == self.modus:
            self.current = True
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png").convert_alpha()
            self.rect.y = 898
        else:
            self.current = False

    def on_click(self):
        pass