import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp


class GristCacheButton(UIBase):
    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, image)
        
    def on_click(self):
        PopUp('Grsit cahce is comming very soon')