import pygame as pg

from baseUI import UIBase


class CustomSettingMenu(UIBase):
    def __init__(self, x):
        super().__init__(x, 38, (348,768), 'CustomSettingMenu', '#666666')

        self.create_appearance([[326, 732], '#434343', [10, 24]], [[326, 732], '#1155CC', [0, 12]])

        self.children = [
            UIBase.get_uiElem('CustomSettingSectionName')(self, 36, 'WEAPONKINDS'),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "WEAPONKIND", 'kind1', 66),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "WEAPONKIND", 'kind2', 96),
            UIBase.get_uiElem('CustomSettingSectionName')(self, 126, 'ACTIONS'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+210, self.rect.y+126, 'meleeToggle', 'ME'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+240, self.rect.y+126, 'rangedToggle', 'RA'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+270, self.rect.y+126, 'magicToggle', 'MA'),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "ACTION", 'action1', 156),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "ACTION", 'action2', 258),
            UIBase.get_uiElem('CustomSettingSectionName')(self, 360, 'TRAIT'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+182, self.rect.y+390, 't1Toggle', '1'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+212, self.rect.y+390, 't2Toggle', '2'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+242, self.rect.y+390, 't3Toggle', '3'),
            UIBase.get_uiElem('ToggleButton')(self.rect.x+272, self.rect.y+390, 't4Toggle', '4'),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "TRAIT", 'name', 390),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "TRAIT", 'tier1-4', 420),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "TRAIT", 'tier5-8', 498),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "TRAIT", 'tier9-12', 576),
            UIBase.get_uiElem('CustomSettingAreaBox')(self, "TRAIT", 'tier13-16', 654),
            ]
        self.children[4].on_click()

        self.children[10].on_click()
        