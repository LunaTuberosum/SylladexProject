import pygame as pg

from baseUI import UIBase


class SidebarButton(UIBase):
    def __init__(self):
        super().__init__(0, 536, (70,70), 'SideBarButton', (0,0,0))

        self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0]])

        self.toolTipText = "Opens Side Bar"

        self.hovering = False
        self.inactive = False

    def hover(self):
        if self.toolTipText == 'Opens Side Bar':
            self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER.png', [6, 0])
        elif self.toolTipText == 'Closes Side Bar':
            self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER_REVERESED.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        if self.toolTipText == 'Opens Side Bar':
            self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
        elif self.toolTipText == 'Closes Side Bar':
            self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0])
        self.hovering = False

    def update(self):
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('CustomSettingMenu')):
                self.inactive = True
                return
        self.inactive = False

    def on_click(self):
        if self.inactive == False:
            if self.toolTipText == 'Opens Side Bar':
                self.toolTipText = 'Closes Side Bar'
                self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0]])
                self.rect.x = 319

                UIBase.get_uiElem('SideBar')()

                UIBase.get_uiElem('AddCardButton')()
                UIBase.get_uiElem('RemoveCardButton')()

                UIBase.get_uiElem('TextField')(242, 142, 53, 48, 3, "numOfCards", "The Number of Cards in you Sylladex", "Num")
                UIBase.get_uiElem('CardList')(24, 196, (249, 649))

                UIBase.get_uiElem('ModusCard')(33, 910, (72, 96), "STACK_MODUS.png", "STACK")
                UIBase.get_uiElem('ModusCard')(121, 910, (72, 96), "QUEUE_MODUS.png", "QUEUE")
                UIBase.get_uiElem('ModusCard')(209, 910, (72, 96), "TREE_MODUS.png", "TREE")

                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('GristCacheButton')):
                        elem.rect.x = 326
                        for elem2 in UIBase.get_group('ui'):
                            if isinstance(elem2, UIBase.get_uiElem('GristCache')):
                                elem.rect.x = 1038
                                elem2.rect.x = 326
                                elem2.repositionChildren()
                    if isinstance(elem, UIBase.get_uiElem('CardList')):
                        elem.start_list()

                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        UIBase.uiElements.remove(elem)
                        UIBase.uiLayers.remove(elem)
                        elem.kill()

                    if isinstance(elem, UIBase.get_uiElem('CustomSettingButton')):
                        elem.rect.x = 326

            elif self.toolTipText == 'Closes Side Bar':
                self.toolTipText = 'Opens Side Bar'
                self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0]])
                self.rect.x = 0

                for elem in UIBase.get_group("ui"):

                    if isinstance(elem, UIBase.get_uiElem('SideBar')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('GristCacheButton')):
                        elem.rect.x = 0
                        for elem2 in UIBase.get_group('ui'):
                            if isinstance(elem2, UIBase.get_uiElem('GristCache')):
                                elem.rect.x = 713
                                elem2.rect.x = 0
                                elem2.repositionChildren()
                    if isinstance(elem, UIBase.get_uiElem('CustomSettingButton')):
                        elem.rect.x = 0
                                
                    if isinstance(elem, UIBase.get_uiElem('TextField')):
                        if elem.job == 'numOfCards' or elem.job == 'nameOverlay' or elem.job == 'codeOverlay' or elem.job == 'tierOverlay':
                            UIBase.remove_fromGroup(elem)
                            elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('CardList')):
                        for card in elem.children:
                            card.kill()
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('ModusCard')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('AddCardButton')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('RemoveCardButton')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()
                    if isinstance(elem, UIBase.get_uiElem('FinishButton')):
                        UIBase.remove_fromGroup(elem)
                        elem.kill()

    def reloadSelf(self):
        self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0]])

