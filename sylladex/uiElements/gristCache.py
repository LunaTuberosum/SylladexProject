import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCache(UIBase):
    def __init__(self, x):
        super().__init__(x, 626, (719,452), "GRIST_CACHE.png", True)