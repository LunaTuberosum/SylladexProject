import pygame as pg

from sylladex.uiElements.baseUI import UIBase


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
            UIBase.CustomSettingAreaBox(self, "WEAPONKIND", 'customkind1', 66),
            UIBase.CustomSettingAreaBox(self, "WEAPONKIND", 'customkind2', 96),
            UIBase.CustomSettingSectionName(self, 126, 'MELEE ACTIONS'),
            UIBase.CustomSettingAreaBox(self, "ACTION", 'melee1', 156),
            UIBase.CustomSettingAreaBox(self, "ACTION", 'melee2', 258),
            UIBase.CustomSettingSectionName(self, 360, 'TRAIT'),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'name1', 390),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier1-4', 420),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier5-8', 498),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier9-12', 576),
            UIBase.CustomSettingAreaBox(self, "TRAIT", 'tier13-16', 654),
            ]