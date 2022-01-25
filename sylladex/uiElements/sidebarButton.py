import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.textField import TextField

class SidebarButton(UIBase):
    def __init__(self, x, y, size, image, state):
        super().__init__(x, y, size, image)

        self.state = state

    def on_click(self):
        if self.state == "open":
            SidebarButton.kill(self)
            SideBar()
            SidebarButton(320, 505, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png", "close")
            TextField(242, 142, (54, 48), "sylladex/uiElements/asset/MISC/NUM_CARD_FIELD.png", 3)
            for elem in UIBase.get_group():
                if isinstance(elem, GristCacheButton):
                    elem.rect.x = 326
        else:
            SidebarButton.kill(self)
            SidebarButton(0, 537, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png", "open")
            for elem in UIBase.get_group():
                if isinstance(elem, SideBar):
                    SideBar.kill(elem)
                if isinstance(elem, GristCacheButton):
                    elem.rect.x = 0
                if isinstance(elem, TextField):
                    TextField.kill(elem)