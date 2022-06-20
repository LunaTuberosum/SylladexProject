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

        self.toolTipText = 'Open custom card code settings'
        self.hovering = False
    
    def hover(self):
        self.logoImage = pg.image.load('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO_HOVER.png').convert_alpha()
        self.image.blit(self.logoImage, [18, 12])
        self.hovering = True

    def no_hover(self):
        self.logoImage = pg.image.load('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png').convert_alpha()
        self.image.blit(self.logoImage, [18, 12])
        self.hovering = False

    def on_click(self):
        if self.toolTipText == 'Open custom card code settings':
            self.rect.x = 342
            self.toolTipText = 'Close custom card code settings'
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.SideBar):
                    UIBase.CustomSettingMenu(326)
                    self.rect.x = 668
                    return
            UIBase.CustomSettingMenu(0)

        elif self.toolTipText == 'Close custom card code settings':

            self.rect.x = 0
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.CustomSettingMenu):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                elif isinstance(elem, UIBase.SideBar):
                    self.rect.x = 326        
            
            self.toolTipText = 'Open custom card code settings'
