import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.numTextField import NumTextField
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.modus import Modus


class SidebarButton(UIBase):
    def __init__(self, x, y, size, image, state):
        super().__init__(x, y, size, image)

        self.state = state
        self.hovering = False

    def hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON{self.state}HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON{self.state}.png").convert_alpha()
        self.hovering = False

    def on_click(self):
        if self.state == "_":
            SidebarButton.kill(self)

            SideBar()
            SidebarButton(320, 505, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED_.png","_REVERESED_")
            NumTextField(242, 142, (54, 48),"sylladex/uiElements/asset/MISC/NUM_CARD_FIELD.png",3)
            CardList(24, 196, (249, 649),"sylladex/uiElements/asset/MISC/LIST_BACK.png")

            Modus(33, 910, (72, 96), "sylladex/uiElements/asset/MISC/STACK_MODUS.png", "STACK")
            Modus(121, 910, (72, 96), "sylladex/uiElements/asset/MISC/QUEUE_MODUS.png", "QUEUE")
            Modus(209, 910, (72, 96), "sylladex/uiElements/asset/MISC/TREE_MODUS.png", "TREE")

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
            SidebarButton(0, 537, (70, 70),f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_.png","_")

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
                if isinstance(elem, Modus):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

