import pygame as pg

from uiElement import UIElement, Apperance


class ModusCard(UIElement):
    def __init__(self, x, modus):

        self.modus = modus
        self.tool_tip_text = f'Changes the modus to {self.modus} MODUS'

        super().__init__(x, 910, f'ModusCard ({self.modus})')

        self.apperance = Apperance(
            self,
            [78, 102],
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS.png', [6,6]]
            )

        self.hovering = False
        
        if UIElement.get_modus() == self.modus:
            self.current = True
            self.apperance.change_image(f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png', [0,0])
            self.rect.y = 907
        else:
            self.current = False

    def on_click(self):
        UIElement.set_modus(self.modus)
        for elem in UIElement.get_group("ui"):
            if isinstance(elem, UIElement.get_ui_elem('ModusCard')):
                if elem == self:
                    elem.apperance.options = {
                    'colorKey': True, 
                    'image': [f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png', [0,0]]
                    }
                    self.rect.y = 907
                else:
                    elem.apperance.options = {
                        'colorKey': True, 
                        'image': [f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS.png', [6,6]]
                        }
                    self.rect.y = 910
            
            elem.apperance.reload_apperance()  
            if hasattr(elem, 'reload_image'):
                elem.reload_image()

    def hover(self):
        self.rect.y = 900
        self.hovering = True

    def no_hover(self):
        self.rect.y = 910
        self.hovering = False