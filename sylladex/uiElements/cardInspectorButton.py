import settings
import pygame as pg

from uiElement import Apperance, UIElement


class CardInspectorButton(UIElement):
    def __init__(self, current_inspect):
        super().__init__(
            -70,
            227,
            'CardInspectorButton',
            999
        )

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], 'ModusBackground', [0, 6]],
            [[64, 64], 'ModusAccent', [6, 0]],
            colorKey=True,
            images=[
                [f'sylladex/uiElements/asset/ICONS/SIDE_BAR_ICON.png', [
                    6, 0], 'ModusBackground']
            ]
        )

        self.tool_tip_text = 'Closes Card Inspector'
        self.hovering = False

        self.current_inspect = current_inspect

    def hover(self):
        self.apperance.change_images(
            [
                [f'sylladex/uiElements/asset/ICONS/SIDE_BAR_ICON_HOVER.png', [
                    6, 0], 'ModusForeground']
            ])
        self.hovering = True

    def no_hover(self):
        self.apperance.change_images(
            [
                [f'sylladex/uiElements/asset/ICONS/SIDE_BAR_ICON.png', [
                    6, 0], 'ModusBackground']
            ])
        self.hovering = False

    def on_click(self):
        self.current_inspect.to_be_rect = settings.SCREEN_WIDTH + 70
        # UIElement.remove_from_group(self.current_inspect)
        # for child in self.current_inspect.children:
        #     UIElement.remove_from_group(child)
        # UIElement.get_ui_elem('CardInspectorCheck').__checks = []
