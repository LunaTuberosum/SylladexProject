import pygame as pg

from uiElement import UIElement, Apperance
import settings


class ToolTip(UIElement):
    def __init__(self, pos: list, text: str):
        self.text = text

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/DisposableDroidBB.ttf", 24)
        _width = self.font.render(self.text, True, (0, 0, 0)).get_width() + 12

        if pos[0] + 12 + _width >= settings.SCREEN_WIDTH:
            _x = pos[0] - _width - 12
        else:
            _x = pos[0] + 12

        super().__init__(
            _x,
            pos[1] + 15,
            'ToolTip',
            1010
        )

        self.apperance = Apperance(
            self,
            [_width, 30],
            [[_width, 30], '#CCCCCC', [0, 0]],
            texts=[[self.text, [6, 15],
                    'left', '#000000']]
        )
