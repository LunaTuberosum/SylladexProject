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

        self.tool_tip_text = "Opens Side Bar"

        self.hovering = False
        self.inactive = False

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()

    def update(self):
        if UIBase.check_for_ui('CustomSettingMenu'):
            self.inactive = True
            return
        self.inactive = False

    def reload_image(self):
        if self.hovering == False:
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0])
        else: 
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER.png', [6, 0])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER_REVERESED.png', [6, 0])

    def on_click(self):
        if self.inactive == False:
            if self.tool_tip_text == 'Opens Side Bar':
                self.tool_tip_text = 'Closes Side Bar'
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [6, 0])
                self.rect.x = 319

                UIBase.get_ui_elem('SideBar')()

                # UIBase.get_ui_elem('AddCardButton')()
                # UIBase.get_ui_elem('RemoveCardButton')()


                # UIBase.get_ui_elem('CardList')(24, 196, (249, 649))

            #     for elem in UIBase.get_group("ui"):
            #         if isinstance(elem, UIBase.get_ui_elem('GristCacheButton')):
            #             elem.rect.x = 326
            #             for elem2 in UIBase.get_group('ui'):
            #                 if isinstance(elem2, UIBase.get_ui_elem('GristCache')):
            #                     elem.rect.x = 1038
            #                     elem2.rect.x = 326
            #                     elem2.repositionChildren()
            #         if isinstance(elem, UIBase.get_ui_elem('CardList')):
            #             elem.start_list()

            #         if isinstance(elem, UIBase.get_ui_elem('ScrollBar')):
            #             UIBase.uiElements.remove(elem)
            #             UIBase.uiLayers.remove(elem)
            #             elem.kill()

            #         if isinstance(elem, UIBase.get_ui_elem('CustomSettingButton')):
            #             elem.rect.x = 326

            elif self.tool_tip_text == 'Closes Side Bar':
                self.tool_tip_text = 'Opens Side Bar'
                self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
                self.rect.x = 0

                UIBase.find_cur_ui('SideBar').to_be_rect = -326

                if UIBase.check_for_ui('GristCache'): 
                    if UIBase.find_cur_ui('GristCache').to_be_rect != -392:
                        UIBase.find_cur_ui('GristCache').to_be_rect = 0
                    else:
                        UIBase.find_cur_ui('GristCache').to_be_rect = -719

