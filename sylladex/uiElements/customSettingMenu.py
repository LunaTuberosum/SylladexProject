import pygame as pg

from uiElement import UIElement


class CustomSettingMenu(UIElement):
    def __init__(self, x):
        super().__init__(x, 38, (348,768), 'CustomSettingMenu', '#666666')

        self.create_appearance([[326, 732], '#434343', [10, 24]], [[326, 732], '#1155CC', [0, 12]])

        self.children = [
            UIElement.get_ui_elem('CustomSettingSectionName')(self, 36, 'WEAPONKINDS'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "WEAPONKIND", 'kind1', 66),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "WEAPONKIND", 'kind2', 96),
            UIElement.get_ui_elem('CustomSettingSectionName')(self, 126, 'ACTIONS'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+210, self.rect.y+126, 'meleeToggle', 'ME'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+240, self.rect.y+126, 'rangedToggle', 'RA'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+270, self.rect.y+126, 'magicToggle', 'MA'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "ACTION", 'action1', 156),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "ACTION", 'action2', 258),
            UIElement.get_ui_elem('CustomSettingSectionName')(self, 360, 'TRAIT'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+182, self.rect.y+390, 't1Toggle', '1'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+212, self.rect.y+390, 't2Toggle', '2'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+242, self.rect.y+390, 't3Toggle', '3'),
            UIElement.get_ui_elem('ToggleButton')(self.rect.x+272, self.rect.y+390, 't4Toggle', '4'),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'name', 390),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier1-4', 420),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier5-8', 498),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier9-12', 576),
            UIElement.get_ui_elem('CustomSettingAreaBox')(self, "TRAIT", 'tier13-16', 654),
            ]
        self.children[4].on_click()

        self.children[10].on_click()
        