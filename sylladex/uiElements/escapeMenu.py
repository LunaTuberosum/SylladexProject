import pygame as pg

from baseUI import UIBase

class EscapeMenu(UIBase):
    def __init__(self):
        super().__init__(750, 360, (420, 360), 'EscapeMenu', (0,0,0))

        self.create_appearance([[420, 360], '#000000', [0, 0]], image = ['sylladex/uiElements/asset/MISC/ESCAPE_MENU.png', [0, 0]])
        
        UIBase.get_group('layer').change_layer(self, 3)

        self.children = [
            UIBase.get_uiElem('EscapeMenuOption')(self.rect.x+110,self.rect.y+110,'Settings'),
            UIBase.get_uiElem('EscapeMenuOption')(self.rect.x+110,self.rect.y+171,'Tutorials'),
            UIBase.get_uiElem('EscapeMenuOption')(self.rect.x+110,self.rect.y+232,'To Desktop'),
            UIBase.get_uiElem('EscapeMenuOption')(self.rect.x+110,self.rect.y+293,'Log Out'),]
