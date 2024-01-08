import pygame as pg

from uiElement import UIElement, Apperance


class ToolTip(UIElement):
    def __init__(self, pos: list, text: str):
        self.text = text

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        _width = self.font.render(self.text, True, (0, 0, 0)).get_width() + 12

        super().__init__(
            pos[0]+12,
            pos[1]+15,
            'ToolTip',
            999)

        self.apperance = Apperance(
            self,
            [_width, 30],
            [[_width, 30], '#D2D2D2', [0, 0]],
            texts=[[self.text, [6, 15],
                    'left', '#000000']]
        )
