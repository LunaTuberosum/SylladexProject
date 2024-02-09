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
                    6, 0], 'ModusBackground']
            ]
        )

        self.tool_tip_text = "Opens Side Bar"

        self.hovering = False

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        super().no_hover()
        self.hovering = False
        self.reload_image()

    def reload_image(self):
        if self.hovering == False:
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [
                            6, 0], 'ModusBackground']
                    ])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [
                            6, 0], 'ModusBackground']
                    ])
        else:
            if self.tool_tip_text == 'Opens Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_HOVER.png', [
                            6, 0], 'ModusForeground']
                    ])
            elif self.tool_tip_text == 'Closes Side Bar':
                self.apperance.change_images(
                    [
                        [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_HOVER_REVERESED.png', [
                            6, 0], 'ModusForeground']
                    ])

    def on_click(self):
        if self.tool_tip_text == 'Opens Side Bar':
            self.tool_tip_text = 'Closes Side Bar'
            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_REVERESED.png', [
                        6, 0], 'ModusBackground']
                ])
            self.rect.x = 319

            _side_bar = UIElement.find_current_ui('SideBar')
            if _side_bar:
                _side_bar.to_be_rect = 0
                return
            UIElement.get_ui_elem('SideBar')()

        elif self.tool_tip_text == 'Closes Side Bar':
            self.tool_tip_text = 'Opens Side Bar'
            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [
                        6, 0], 'ModusBackground']
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
