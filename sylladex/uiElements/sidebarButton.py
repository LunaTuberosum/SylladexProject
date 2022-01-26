import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.numTextField import NumTextField
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.scrollBar import ScrollBar


class SidebarButton(UIBase):
    def __init__(self, x, y, size, image, state):
        super().__init__(x, y, size, image)

        self.state = state

    def on_click(self):
        if self.state == "open":
            SidebarButton.kill(self)

            SideBar()
            SidebarButton(
                320, 505, (70, 70),
                f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png",
                "close")
            NumTextField(242, 142, (54, 48),
                         "sylladex/uiElements/asset/MISC/NUM_CARD_FIELD.png",
                         3)
            CardList(24, 196, (249, 649),
                     "sylladex/uiElements/asset/MISC/LIST_BACK.png")

            for elem in UIBase.get_group("ui"):
                if isinstance(elem, GristCacheButton):
                    elem.rect.x = 326
                if isinstance(elem, CardList):
                    elem.start_list()

                if isinstance(elem, ScrollBar):
                    UIBase.uiElements.remove(elem)
                    UIBase.uiLayers.remove(elem)
                    elem.kill()
            ScrollBar(CardList.listObj)
            
        else:
            SidebarButton.kill(self)
            SidebarButton(
                0, 537, (70, 70),
                f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png",
                "open")

            for elem in UIBase.get_group("ui"):

                if isinstance(elem, SideBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, GristCacheButton):
                    elem.rect.x = 0
                if isinstance(elem, NumTextField):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, CardList):
                    for card in elem.listObj:
                        UIBase.remove_fromGroup(card)
                    CardList.kill(elem)
                if isinstance(elem, ScrollBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

