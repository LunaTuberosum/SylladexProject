import pygame as pg

from baseUI import UIBase, Apperance


class StackingArea(UIBase):
    def __init__(self):
        super().__init__(0, 0, 'StackingArea')

        self.apperance = Apperance(
            self,
            [1920, 36],
            [[1920, 36], 'ModusBackground', [0,0]],
            [[1920, 24], 'ModusForeground', [0,0]]
            )
