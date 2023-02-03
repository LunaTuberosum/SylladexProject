import pygame as pg

from baseUI import UIBase,Apperance


class SideBarButton(UIBase):
    def __init__(self):
        super().__init__(0, 536,  'SideBarButton')

        self.apperance = Apperance(
            self,
            [70,70],
            [[64, 64], 'ModusBackground', [0, 6]], 
            [[64, 64], 'ModusAccent', [6, 0]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0]]
            )

        self.toolTipText = "Opens Side Bar"

        self.hovering = False
        self.inactive = False

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()

    def update(self):
        if UIBase.check_forUI('CustomSettingMenu'):
            self.inactive = True
            return
        self.inactive = False

    def reload_image(self):
        if self.hovering == False:
            if self.toolTipText == 'Opens Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
            elif self.toolTipText == 'Closes Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0])
        else: 
            if self.toolTipText == 'Opens Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER.png', [6, 0])
            elif self.toolTipText == 'Closes Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER_REVERESED.png', [6, 0])

    def on_click(self):
        if self.inactive == False:
            if self.toolTipText == 'Opens Side Bar':
                self.toolTipText = 'Closes Side Bar'
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0])
                self.rect.x = 319

                UIBase.get_uiElem('SideBar')()

                # UIBase.get_uiElem('AddCardButton')()
                # UIBase.get_uiElem('RemoveCardButton')()


                # UIBase.get_uiElem('CardList')(24, 196, (249, 649))

            #     for elem in UIBase.get_group("ui"):
            #         if isinstance(elem, UIBase.get_uiElem('GristCacheButton')):
            #             elem.rect.x = 326
            #             for elem2 in UIBase.get_group('ui'):
            #                 if isinstance(elem2, UIBase.get_uiElem('GristCache')):
            #                     elem.rect.x = 1038
            #                     elem2.rect.x = 326
            #                     elem2.repositionChildren()
            #         if isinstance(elem, UIBase.get_uiElem('CardList')):
            #             elem.start_list()

            #         if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
            #             UIBase.uiElements.remove(elem)
            #             UIBase.uiLayers.remove(elem)
            #             elem.kill()

            #         if isinstance(elem, UIBase.get_uiElem('CustomSettingButton')):
            #             elem.rect.x = 326

            elif self.toolTipText == 'Closes Side Bar':
                self.toolTipText = 'Opens Side Bar'
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
                self.rect.x = 0

                UIBase.find_curUI('SideBar').toBeRect = -326

                if UIBase.check_forUI('GristCache'): UIBase.find_curUI('GristCache').toBeRect = 0
