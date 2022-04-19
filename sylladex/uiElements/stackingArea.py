import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class StackingArea(UIBase):
    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, image, 'StackingArea')
