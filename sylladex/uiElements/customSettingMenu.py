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