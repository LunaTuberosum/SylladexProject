import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase


class CustomSettingMenu(UIBase):
    def __init__(self, x):
        super().__init__(x, 38, (348,768), "surfaceRect", 'CustomSettingMenu', True, '#666666')

        self.backgroundColor = pg.Surface((326,732))
        self.backgroundColor.fill('#434343')
        self.image.blit(self.backgroundColor, [10, 24])
        
        self.foregroundColor = pg.Surface((326,732))
        self.foregroundColor.fill('#1155CC')
        self.image.blit(self.foregroundColor, [0, 12])

        self.children = [
            UIBase.CustomSettingSectionName(self, 36, 'WEAPONKINDS'),
            UIBase.CustomSettingAreaBox(self, "WEAPONKIND", 'kind1', 66),
            UIBase.CustomSettingAreaBox(self, "WEAPONKIND", 'kind2', 96),
            UIBase.CustomSettingSectionName(self, 126, 'ACTIONS'),
            UIBase.ToggleButton(self.rect.x+210, self.rect.y+126, 'meleeToggle', 'ME'),
            UIBase.ToggleButton(self.rect.x+240, self.rect.y+126, 'rangedToggle', 'RA'),
            UIBase.ToggleButton(self.rect.x+270, self.rect.y+126, 'magicToggle', 'MA'),
            UIBase.CustomSettingAreaBox(self, "ACTION", 'action1', 156),
            UIBase.CustomSettingAreaBox(self, "ACTION", 'action2', 258),
            UIBase.CustomSettingSectionName(self, 360, 'TRAIT'),
            UIBase.ToggleButton(self.rect.x+182, self.rect.y+390, 't1Toggle', '1'),
            UIBase.ToggleButton(self.rect.x+212, self.rect.y+390, 't2Toggle', '2'),
            UIBase.ToggleButton(self.rect.x+242, self.rect.y+390, 't3Toggle', '3'),
            UIBase.ToggleButton(self.rect.x+272, self.rect.y+390, 't4Toggle', '4'),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'name', 390),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier1-4', 420),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier5-8', 498),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier9-12', 576),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier13-16', 654),
            ]
        self.children[4].on_click()

        self.children[10].on_click()
        