import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class StackingArea(UIBase):
    def __init__(self):
        super().__init__(0, 0, (1920, 36), 'StackingArea', (0,0,0))

        self._create_appearance([[1920, 36], UIBase.modusBackground, [0,0]], [[1920, 24], UIBase.modusForground, [0,0]])
