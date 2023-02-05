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
            UIElement.get_ui_elem('CustomSettingSectionName')(self.rect.x + 12, self.rect.y + 36, 'WEAPONKINDS'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self.rect.x + 12, self.rect.y + 66, "WEAPONKIND", 'kind1'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self.rect.x + 12, self.rect.y + 96, "WEAPONKIND", 'kind2'),
            UIElement.get_ui_elem('CustomSettingSectionName')(self.rect.x + 12, self.rect.y + 126, 'ACTIONS'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+210, self.rect.y+126, 'meleeToggle', 'ME'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+240, self.rect.y+126, 'rangedToggle', 'RA'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+270, self.rect.y+126, 'magicToggle', 'MA'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self.rect.x + 12, self.rect.y + 156, "ACTION", 'action1'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self.rect.x + 12, self.rect.y + 258, "ACTION", 'action2'),
            UIElement.get_ui_elem('CustomSettingSectionName')(self.rect.x + 12, self.rect.y + 360, 'TRAIT'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+182, self.rect.y+390, 't1Toggle', '1'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+212, self.rect.y+390, 't2Toggle', '2'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+242, self.rect.y+390, 't3Toggle', '3'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+272, self.rect.y+390, 't4Toggle', '4'),
            # UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'name', 390),
        #     UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier1-4', 420),
        #     UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier5-8', 498),
        #     UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier9-12', 576),
        #     UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier13-16', 654),
            ]

        # self.children[4].on_click()

        # self.children[10].on_click()

        if UIElement.find_current_ui('SideBar'):
            self.to_be_rect = 326
        else:
            self.to_be_rect = 0

    def update(self):
        if self.rect.x != self.to_be_rect:
            UIElement.move_element(self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 0])
            UIElement.find_current_ui('CustomSettingButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -348 or self.to_be_rect == -22:
                UIElement.remove_from_group(self)
        