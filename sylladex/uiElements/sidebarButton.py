import pygame as pg

from uiElement import UIElement, Apperance


class SideBarButton(UIElement):
    def __init__(self):
        super().__init__(0, 536,  'SideBarButton', 1)

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], 'ModusBackground', [0, 6]],
            [[64, 64], 'ModusAccent', [6, 0]],
            colorKey=True,
            images=[
                [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [
                    6, 0]]
            ]
        )

        self.tool_tip_text = "Opens Side Bar"

        self.hovering = False

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()

    def reload_image(self):
        if self.hovering == False:
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [
                            6, 0]]
                    ])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [
                            6, 0]]
                    ])
        else:
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_HOVER.png', [
                            6, 0]]
                    ])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_HOVER_REVERESED.png', [
                            6, 0]]
                    ])

    def on_click(self):
        if self.tool_tip_text == 'Opens Side Bar':
            self.tool_tip_text = 'Closes Side Bar'
            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [
                        6, 0]]
                ])
            self.rect.x = 319

            UIElement.get_ui_elem('SideBar')()

            # UIElement.get_ui_elem('AddCardButton')()
            # UIElement.get_ui_elem('RemoveCardButton')()

            # UIElement.get_ui_elem('CardList')(24, 196, (249, 649))

        #     for elem in UIElement.get_group("ui"):
        #         if isinstance(elem, UIElement.get_ui_elem('GristCacheButton')):
        #             elem.rect.x = 326
        #             for elem2 in UIElement.get_group('ui'):
        #                 if isinstance(elem2, UIElement.get_ui_elem('GristCache')):
        #                     elem.rect.x = 1038
        #                     elem2.rect.x = 326
        #                     elem2.repositionChildren()
        #         if isinstance(elem, UIElement.get_ui_elem('CardList')):
        #             elem.start_list()

        #         if isinstance(elem, UIElement.get_ui_elem('ScrollBar')):
        #             UIElement.uiElements.remove(elem)
        #             UIElement.uiLayers.remove(elem)
        #             elem.kill()

        #         if isinstance(elem, UIElement.get_ui_elem('CustomSettingButton')):
        #             elem.rect.x = 326

        elif self.tool_tip_text == 'Closes Side Bar':
            self.tool_tip_text = 'Opens Side Bar'
            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [
                        6, 0]]
                ])
            self.rect.x = 0

            UIElement.find_current_ui('SideBar').to_be_rect = -326
            UIElement.get_ui_elem('RemoveCardButton').change_eject(False)
            UIElement.get_ui_elem('EditCardButton').change_edit(False)

            if UIElement.check_for_ui('GristCache'):
                if UIElement.find_current_ui('GristCache').to_be_rect != -392:
                    UIElement.find_current_ui('GristCache').to_be_rect = 0
                else:
                    UIElement.find_current_ui('GristCache').to_be_rect = -719
