import pygame as pg

from uiElement import UIElement, Apperance


class ToolTip(UIElement):
    def __init__(self, pos: tuple, text: str):
        self.text = text

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.txt_surface = self.font.render(text, True, (0,0,0))

        width = self.txt_surface.get_width() + 6
        height = self.txt_surface.get_height() + 6

        super().__init__(pos[0]+12, pos[1]+15, 'ToolTip', 99)

        self.apperance = Apperance(
            self, 
            (width, height), 
            [[width, height], '#D2D2D2', [0,0]]
            )

        self.image.blit(self.txt_surface, [3, 3])
    