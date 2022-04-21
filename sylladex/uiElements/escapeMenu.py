import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class EscapeMenu(UIBase):
    def __init__(self):
        super().__init__(750, 360, (420, 360), "ESCAPE_MENU.png", 'EscapeMenu', True)

        self.children = [
            UIBase.EscapeMenuOption(self.rect.x+110,self.rect.y+110,'Settings'),
            UIBase.EscapeMenuOption(self.rect.x+110,self.rect.y+171,'Tutorials'),
            UIBase.EscapeMenuOption(self.rect.x+110,self.rect.y+232,'To Desktop'),
            UIBase.EscapeMenuOption(self.rect.x+110,self.rect.y+293,'Log Out'),]
