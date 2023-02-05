import pygame as pg

from uiElement import UIElement

class EscapeMenu(UIElement):
    def __init__(self):
        super().__init__(750, 360, (420, 360), 'EscapeMenu', (0,0,0))

        self.create_appearance([[420, 360], '#000000', [0, 0]], image = ['sylladex/uiElements/asset/MISC/ESCAPE_MENU.png', [0, 0]])
        
        UIElement.get_group('layer').change_layer(self, 3)

        self.children = [
            UIElement.get_ui_elem('EscapeMenuOption')(self.rect.x+110,self.rect.y+110,'Settings'),
            UIElement.get_ui_elem('EscapeMenuOption')(self.rect.x+110,self.rect.y+171,'Tutorials'),
            UIElement.get_ui_elem('EscapeMenuOption')(self.rect.x+110,self.rect.y+232,'To Desktop'),
            UIElement.get_ui_elem('EscapeMenuOption')(self.rect.x+110,self.rect.y+293,'Log Out'),]
