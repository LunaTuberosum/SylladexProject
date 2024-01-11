import pygame as pg

from uiElement import UIElement, Apperance


class DropDownBackground(UIElement):
    def __init__(self, x: int, y: int, size: list, color: str, start_layer: int):

        super().__init__(
            x,
            y,
            f'DropDownBackground',
            start_layer
        )

        self.apperance = Apperance(
            self,
            size,
            [size, color, [0, 0]]
        )
