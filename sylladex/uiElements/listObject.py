import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ListObject(UIBase):
    def __init__(self, x, y, size, image, length):
        super().__init__(x, y, size, image)
        self.uiLayers.change_layer(self, 0)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.txt_surface = self.font.render("-", True, (0,0,0))
        self.image.blit(self.txt_surface, (3,3))
        self.image.blit(self.txt_surface, (3,37))
        self.image.blit(self.txt_surface, (129,37))

        self.interactable = True
    
    def update(self):
        if self.rect.y >= 196 and self.rect.y <= 757:
            self.interactable = True
        else:
            self.interactable = False