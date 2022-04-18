import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class SidebarButton(UIBase):
    def __init__(self):
        super().__init__(0, 536, (70,70), "SIDE_BAR_BUTTON.png")

        self.toolTipText = "Opens Side Bar"

        self.hovering = False

    def hover(self):
        if self.toolTipText == 'Opens Side Bar':
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_HOVER.png").convert_alpha()
        elif self.toolTipText == 'Closes Side Bar':
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        if self.toolTipText == 'Opens Side Bar':
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png").convert_alpha()
        elif self.toolTipText == 'Closes Side Bar':            
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png").convert_alpha()
        self.hovering = False

    def on_click(self):
        if self.toolTipText == 'Opens Side Bar':
            self.toolTipText = 'Closes Side Bar'
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON_REVERESED.png").convert_alpha()
            self.rect.x = 319

            UIBase.SideBar()

            UIBase.AddCardButton()
            UIBase.RemoveCardButton()

            UIBase.TextField(242, 142, 53, 48, 3, "numOfCards", "The Number of Cards in you Sylladex", "0")
            UIBase.CardList(24, 196, (249, 649), "LIST_BACK.png")

            UIBase.ModusCard(33, 910, (72, 96), "STACK_MODUS.png", "STACK")
            UIBase.ModusCard(121, 910, (72, 96), "QUEUE_MODUS.png", "QUEUE")
            UIBase.ModusCard(209, 910, (72, 96), "TREE_MODUS.png", "TREE")

            for elem in UIBase.get_group("ui"):
                if isinstance(elem, UIBase.GristCacheButton):
                    elem.rect.x = 326
                    for elem2 in UIBase.get_group('ui'):
                        if isinstance(elem2, UIBase.GristCache):
                            elem.rect.x = 1038
                            elem2.rect.x = 325
                            elem2.repositionChildren()
                if isinstance(elem, UIBase.CardList):
                    elem.start_list()

                if isinstance(elem, UIBase.ScrollBar):
                    UIBase.uiElements.remove(elem)
                    UIBase.uiLayers.remove(elem)
                    elem.kill()
            UIBase.ScrollBar()
            
        elif self.toolTipText == 'Closes Side Bar':
            self.toolTipText = 'Opens Side Bar'
            self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png").convert_alpha()
            self.rect.x = 0

            for elem in UIBase.get_group("ui"):

                if isinstance(elem, UIBase.SideBar):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                if isinstance(elem, UIBase.GristCacheButton):
                    elem.rect.x = 0
                    for elem2 in UIBase.get_group('ui'):
                        if isinstance(elem2, UIBase.GristCache):
                            elem.rect.x = 713
                            elem2.rect.x = 0
                            elem2.repositionChildren()
                            
                if isinstance(elem, UIBase.TextField):
                    if elem.job == 'numOfCards' or elem.job == 'nameOverlay' or elem.job == 'codeOverlay' or elem.job == 'tierOverlay':
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                if isinstance(elem, UIBase.CardList):
                    elem.save_list()
                    for card in elem.listObj:
                        card.kill()
                    elem.kill()
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
                if isinstance(elem, UIBase.FinishButton):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

