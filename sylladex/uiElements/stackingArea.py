import pygame as pg

from baseUI import UIBase


class StackingArea(UIBase):
    def __init__(self):
        super().__init__(0, 0, (1920, 36), 'StackingArea', (0,0,0))

        self.create_appearance([[1920, 36], UIBase.modusBackground, [0,0]], [[1920, 24], UIBase.modusForground, [0,0]])
