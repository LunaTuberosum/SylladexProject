import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ListObject(UIBase):
    def __init__(self, x, y, size, image, length):
        super().__init__(x, y, size, image)
        self.uiLayers.change_layer(self, 0)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.text = length
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.image.blit(self.txt_surface, (10,10))