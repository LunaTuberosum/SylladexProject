import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, (70,70), "GRIST_CACHE_BUTTON.png", True)

        self.toolTipText = "Comming Soon" 

        self.hovering = False

    def hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png").convert_alpha()
        self.hovering = False
        
    def on_click(self):
        UIBase.PopUp('Grsit cahce is comming very soon')