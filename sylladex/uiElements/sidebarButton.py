import pygame as pg

from sylladex.uiElements.baseUI import UIBase


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
            UIBase.SidebarButton.kill(self)

            UIBase.SideBar()

            UIBase.AddCardButton()
            UIBase.RemoveCardButton()

            UIBase.SidebarButton(320, 505, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png","_REVERESED")
            UIBase.TextField(242, 142, 53, 48, 3, "numOfCards", "The Number of Cards in you Sylladex", "0")
            UIBase.CardList(24, 196, (249, 649),"sylladex/uiElements/asset/MISC/LIST_BACK.png")

            UIBase.ModusCard(33, 910, (72, 96), "sylladex/uiElements/asset/MISC/STACK_MODUS.png", "STACK")
            UIBase.ModusCard(121, 910, (72, 96), "sylladex/uiElements/asset/MISC/QUEUE_MODUS.png", "QUEUE")
            UIBase.ModusCard(209, 910, (72, 96), "sylladex/uiElements/asset/MISC/TREE_MODUS.png", "TREE")

            for elem in UIBase.get_group("ui"):
                if isinstance(elem, UIBase.GristCacheButton):
                    elem.rect.x = 326
                if isinstance(elem, UIBase.CardList):
                    elem.start_list()

                if isinstance(elem, UIBase.ScrollBar):
                    UIBase.uiElements.remove(elem)
                    UIBase.uiLayers.remove(elem)
                    elem.kill()
            UIBase.ScrollBar()
            
        else:
            UIBase.SidebarButton.kill(self)
            UIBase.SidebarButton(0, 537, (70, 70),f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png","")

            for elem in UIBase.get_group("ui"):

                if isinstance(elem, UIBase.SideBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.GristCacheButton):
                    elem.rect.x = 0
                if isinstance(elem, UIBase.TextField):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.CardList):
                    for card in elem.listObj:
                        UIBase.remove_fromGroup(card)
                    UIBase.CardList.kill(elem)
                if isinstance(elem, UIBase.ScrollBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.ModusCard):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.AddCardButton):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.RemoveCardButton):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

