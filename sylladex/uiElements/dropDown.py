import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class DropDown(UIBase):
    def __init__(self,x, y, w, h, job, color, options, defultOptionIndex):
        super().__init__(x, y, (w,h), 'surfaceRect', f'DropDown ({self.job})', True, color)