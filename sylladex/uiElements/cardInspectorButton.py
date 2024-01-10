from turtle import circle
import pygame as pg

from uiElement import UIElement


class CardInspectorButton(UIElement):
    def __init__(self, current_inspect):
        super().__init__(current_inspect.rect.x-70, current_inspect.rect.y+((current_inspect.rect.h/2)-35), (70,70), 'CardInspectorButton', (0,0,0))

        self.create_appearance([[64, 64], UIElement.modusBackground, [0, 6]], [[64, 64], UIElement.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [6, 0]])

        self.tool_tip_text = 'Closes Card Inspector'
        self.hovering = False

        self.current_inspect = current_inspect

    def hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIElement.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
        self.hovering = False

    def on_click(self):
        UIElement.remove_from_group(self.current_inspect)
        self.current_inspect.kill()
        for child in self.current_inspect.children:
            UIElement.remove_from_group(child)
        UIElement.get_ui_elem('CardInspectorCheck').__checks = []