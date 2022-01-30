import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, (70,70), "sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png")

        self.toolTipText = "Comming Soon" 
        
    def on_click(self):
        PopUp('Grsit cahce is comming very soon')