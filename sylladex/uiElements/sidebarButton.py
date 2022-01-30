import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.textField import TextField
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.modus import Modus
from sylladex.uiElements.addCardButton import AddCardButton
from sylladex.uiElements.removeCardButton import RemoveCardButton

class SidebarButton(UIBase):
    def __init__(self, x, y, size, image, state):
        super().__init__(x, y, size, image)

        self.state = state
        if self.state == "":
            self.toolTipText = "Opens Side Bar"
        else:
            self.toolTipText = "Closes Side Bar"

        self.hovering = False

    def hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON{self.state}_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON{self.state}.png").convert_alpha()
        self.hovering = False

    def on_click(self):
        if self.state == "":
            SidebarButton.kill(self)

            SideBar()

            AddCardButton()
            RemoveCardButton()

            SidebarButton(320, 505, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png","_REVERESED")
            TextField(242, 142, 53, 48, 3, "numOfCards", "The Number of Cards in you Sylladex", "0")
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
            SidebarButton(0, 537, (70, 70),f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png","")

            for elem in UIBase.get_group("ui"):

                if isinstance(elem, SideBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, GristCacheButton):
                    elem.rect.x = 0
                if isinstance(elem, TextField):
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
                if isinstance(elem, AddCardButton):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, RemoveCardButton):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

