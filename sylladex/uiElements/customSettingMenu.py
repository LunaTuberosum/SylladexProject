import pygame as pg

from uiElement import UIElement, Apperance


class CustomSettingMenu(UIElement):
    def __init__(self):

        super().__init__(
            -22 if UIElement.find_current_ui('SideBar') else -348,
            38,
            'CustomSettingMenu',
            2
        )

        self.apperance = Apperance(
            self,
            [348, 768],
            [[326, 732], '#434343', [10, 24]],
            [[326, 732], '#1155CC', [0, 12]]
        )

        self.children = [
            UIElement.get_ui_elem('CustomSettingSectionName')(
                self.rect.x + 12, self.rect.y + 36, 'WEAPONKINDS'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x + 12, self.rect.y + 66, "WEAPONKINDS", 'kind1'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x + 12, self.rect.y + 96, "WEAPONKINDS", 'kind2'),
            UIElement.get_ui_elem('CustomSettingSectionName')(
                self.rect.x + 12, self.rect.y + 126, 'ACTIONS'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+210, self.rect.y+126, 'melee', 'ME'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+240, self.rect.y+126, 'ranged', 'RA'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+270, self.rect.y+126, 'magic', 'MA'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x + 12, self.rect.y + 156, "ACTIONS", 'action1'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x + 12, self.rect.y + 258, "ACTIONS", 'action2'),
            UIElement.get_ui_elem('CustomSettingSectionName')(
                self.rect.x + 12, self.rect.y + 360, 'TRAITS'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+182, self.rect.y+390, 't1', '1'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+212, self.rect.y+390, 't2', '2'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+242, self.rect.y+390, 't3', '3'),
            UIElement.get_ui_elem('ToggleButton')(
                self.rect.x+272, self.rect.y+390, 't4', '4'),
            # UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'name', 390),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x+12, self.rect.y+420, "TRAITS", 'tier 1-4'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x+12, self.rect.y+498, "TRAITS", 'tier 5-8'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x+12, self.rect.y+576, "TRAITS", 'tier 9-12'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(
                self.rect.x+12, self.rect.y+654, "TRAITS", 'tier 13-16'),
        ]

        if UIElement.find_current_ui('SideBar'):
            self.to_be_rect = 326
        else:
            self.to_be_rect = 0

    def update(self):
        if self.rect.x != self.to_be_rect:
            UIElement.move_element(
                self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 0])
            UIElement.find_current_ui(
                'CustomSettingButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -348 or self.to_be_rect == -22:
                UIElement.remove_from_group(self)
