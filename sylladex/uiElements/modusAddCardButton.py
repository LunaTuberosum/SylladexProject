import json
import pygame as pg

from uiElement import UIElement, Apperance


class ModusAddCardButton(UIElement):
    def __init__(self):
        super().__init__(
            302,
            169,
            f'ModusAddCardButton',
            7
        )

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], '#666666', [0, 6]],
            [[64, 64], '#7C7C7C', [6, 0]],
            [[10, 40], '#666666', [33, 12]],
            [[40, 10], '#666666', [18, 27]],
            colorKey=True,
        )

        self.to_be_rect = 698

    def update(self):
        if UIElement.get_parent(self).to_be_rect == -116:
            return
        if self.to_be_rect != self.rect.x:
            UIElement.move_element(self, [UIElement.lerp(
                self.rect.x, self.to_be_rect, 0.2), self.rect.y])
        elif self.rect.x <= 628:
            UIElement.remove_from_group(self)

    def on_click(self):
        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem('ModusCard')) and _elem.modus_add_card == UIElement.get_parent(self):
                _elem.initate_new_modus()

    def hover(self):
        self.hovering = True
        self.apperance.size_color_pos = [
            [[64, 64], '#666666', [0, 6]],
            [[64, 64], '#7C7C7C', [6, 0]],
            [[10, 40], '#999999', [33, 12]],
            [[40, 10], '#999999', [18, 27]],
        ]
        self.apperance.reload_apperance()

    def no_hover(self):
        super().no_hover()
        self.hovering = False
        self.apperance.size_color_pos = [
            [[64, 64], '#666666', [0, 6]],
            [[64, 64], '#7C7C7C', [6, 0]],
            [[10, 40], '#666666', [33, 12]],
            [[40, 10], '#666666', [18, 27]],
        ]
        self.apperance.reload_apperance()
