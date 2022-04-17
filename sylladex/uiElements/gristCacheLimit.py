from tkinter.font import BOLD
import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCacheLimit(UIBase):
    def __init__(self, x):
        super().__init__(x+212, 642, (290,42), "GRIST_CACHE_LIMIT.png", True)

        self.toolTipText = 'The amount of each grist you can hold based on your Rung'

        self.limitNum = '20480'
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 32, bold=True)
        self.txt_surface = self.font.render(self.limitNum, False, '#42B2DE')
        x = (51 - (self.txt_surface.get_width()/2)) + 182
        y = 18 - (self.txt_surface.get_height()/2)
        self.image.blit(self.txt_surface, [x, y])