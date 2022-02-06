import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, (70,70), "sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png")

        self.toolTipText = "Comming Soon" 
        
    def on_click(self):
        UIBase.PopUp('Grsit cahce is comming very soon')