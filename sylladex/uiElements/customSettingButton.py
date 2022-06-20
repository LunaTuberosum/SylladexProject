import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class CustomSettingButton(UIBase):
    def __init__(self):
        super().__init__(0, 50, (70,70), "surfaceRect", 'CustomSettingButton', True)
        self.image.set_colorkey((0,0,0))

        self.backgroundColor = pg.Surface((64,64))
        self.backgroundColor.fill('#666666')
        self.image.blit(self.backgroundColor, [0, 6])
        
        self.foregroundColor = pg.Surface((64,64))
        self.foregroundColor.fill('#1155CC')
        self.image.blit(self.foregroundColor, [6, 0])

        self.logoImage = pg.image.load('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png').convert_alpha()
        self.image.blit(self.logoImage, [18, 12])

        self.toolTipText = 'Change custom card code settings'
        self.hovering = False
    
    def hover(self):
        self.logoImage = pg.image.load('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO_HOVER.png').convert_alpha()
        self.image.blit(self.logoImage, [18, 12])
        self.hovering = True

    def no_hover(self):
        self.logoImage = pg.image.load('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png').convert_alpha()
        self.image.blit(self.logoImage, [18, 12])
        self.hovering = False
