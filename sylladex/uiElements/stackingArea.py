import pygame as pg

from uiElement import UIElement, Apperance


class StackingArea(UIElement):
    def __init__(self):

        super().__init__(
            0, 
            0, 
            'StackingArea', 
            1
            )

        self.apperance = Apperance(
            self,
            [1920, 36],
            [[1920, 36], 'ModusBackground', [0,0]],
            [[1920, 24], 'ModusForeground', [0,0]]
            )
