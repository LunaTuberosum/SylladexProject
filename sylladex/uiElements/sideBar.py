import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class SideBar(UIBase):
    def __init__(self):
        super().__init__(0, 0, (326, 1080), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR.png")