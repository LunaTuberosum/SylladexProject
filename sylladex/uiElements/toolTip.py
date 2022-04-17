import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ToolTip(UIBase):
    def __init__(self, pos, text):
        self.text = text

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.txt_surface = self.font.render(text, True, (0,0,0))

        width = self.txt_surface.get_width() + 6
        height = self.txt_surface.get_height() + 6

        super().__init__(pos[0]+12, pos[1]+15, (width, height), 'surfaceRect', True, (210,210,210))

        self.image.blit(self.txt_surface, [3, 3])
    