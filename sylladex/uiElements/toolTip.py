import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ToolTip(pg.sprite.Sprite):
    def __init__(self, pos, text):
        super().__init__()

        UIBase.add_toGroup(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.text = text

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.txt_surface = self.font.render(text, True, (0,0,0))

        width = self.txt_surface.get_width() + 6
        height = self.txt_surface.get_height() + 6

        self.image = pg.Surface((width, height))
        self.image.fill((210, 210, 210))
        self.rect = pg.Rect(pos[0]+12, pos[1]+15, width, height)

        self.image.blit(self.txt_surface, [3, 3])
    