import pygame as pg

from baseUI import UIBase, Apperance


class ModusCard(UIBase):
    def __init__(self, x, y, modus):

        self.modus = modus
        self.toolTipText = f'Changes the modus to {self.modus} MODUS'

        super().__init__(x, y, f'ModusCard ({self.modus})')

        self.apperance = Apperance(
            self,
            [78, 102],
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS.png', [6,6]]
            )

        self.hovering = False
        
        if UIBase.get_modus() == self.modus:
            self.current = True
            self.apperance.change_image(f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png', [0,0])
            self.rect.y -= 3
            self.rect.x -= 3
        else:
            self.current = False

    def on_click(self):
        UIBase.set_modus(self.modus)
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.get_uiElem('ModusCard')):
                if elem == self:
                    elem.apperance.options = {
                    'colorKey': True, 
                    'image': [f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png', [0,0]]
                    }
                else:
                    elem.apperance.options = {
                        'colorKey': True, 
                        'image': [f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS.png', [6,6]]
                        }
            
            elem.apperance.reload_apperance()  
            if hasattr(elem, 'reload_image'):
                elem.reload_image()

    def hover(self):
        self.rect.y = 898
        self.hovering = True

    def no_hover(self):
        self.rect.y = 910
        self.hovering = False