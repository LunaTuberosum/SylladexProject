import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class Modus(UIBase):
    def __init__(self, x, y, size, image, modus):
        super().__init__(x, y, size, image)
        self.modus = modus
        self.hovering = False
        
        if UIBase.get_modus() == self.modus:
            self.current = True
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png").convert_alpha()
            self.rect.y -= 3
            self.rect.x -= 3
        else:
            self.current = False

    def on_click(self):
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, Modus):
                if elem == self:
                    elem.image = pg.image.load(f"sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png").convert_alpha()
                    UIBase.set_modus(self.modus)
                else:
                    elem.image = pg.image.load(f"sylladex/uiElements/asset/MISC/{elem.modus}_MODUS.png").convert_alpha()

    def hover(self):
        self.rect.y = 898
        self.hovering = True

    def no_hover(self):
        self.rect.y = 910
        self.hovering = False