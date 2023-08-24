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

        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 36, 'WEAPONKINDS'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 66, "WEAPONKINDS", 'KIND1'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 96, "WEAPONKINDS", 'KIND2'))
        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 126, 'ACTIONS'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            210, 126, 'melee', 'ME', 'Changes view to custom MELEE actions'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            240, 126, 'ranged', 'RA', 'Changes view to custom RANGED actions'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            270, 126, 'magic', 'MA', 'Changes view to custom MAGIC actions'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 156, "ACTIONS", 'ACTION1'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 258, "ACTIONS", 'ACTION2'))
        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 360, 'TRAITS'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            182, 390, 'TRAIT1', '1',  'Changes view to custom TRAIT 1'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            212, 390, 'TRAIT2', '2',  'Changes view to custom TRAIT 2'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            242, 390, 'TRAIT3', '3',  'Changes view to custom TRAIT 3'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            272, 390, 'TRAIT4', '4',  'Changes view to custom TRAIT 4'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 390, "TRAITS", 'name'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 420, "TRAITS", 'tier 1-4'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 498, "TRAITS", 'tier 5-8'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 576, "TRAITS", 'tier 9-12'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 654, "TRAITS", 'tier 13-16'))

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
