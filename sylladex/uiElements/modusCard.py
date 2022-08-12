import pygame as pg

from baseUI import UIBase


class ModusCard(UIBase):
    def __init__(self, x, y, size, image, modus):

        self.modus = modus
        self.toolTipText = f'Changes the modus to {self.modus} MODUS'

        super().__init__(x, y, size, f'ModusCard ({self.modus})', (0,0,0))

        self._create_appearance([size, (0,0,0), [0, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/MISC/{image}', [0,0]])

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
            if isinstance(elem, UIBase.get_uiElem('ModusCard')):
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