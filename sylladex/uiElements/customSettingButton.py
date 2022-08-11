import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class CustomSettingButton(UIBase):
    def __init__(self):
        super().__init__(0, 50, (70,70), 'CustomSettingButton', (0,0,0))

        self._create_appearance([[64, 64], '#666666', [0, 6]], [[64, 64], '#1155CC', [6, 0]], colorKey = True, image = ['sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png', [18, 12]])

        self.toolTipText = 'Open custom card code settings'
        self.hovering = False
    
    def hover(self):
        self._reload_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO_HOVER.png', [18, 12])
        self.hovering = True

    def no_hover(self):
        self._reload_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png', [18, 12])
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
                    for child in elem.children:
                        UIBase.remove_fromGroup(child)
                        child.kill()
                        if hasattr(child, 'children'):
                            for child in child.children:
                                UIBase.remove_fromGroup(child)
                                child.kill()
                elif isinstance(elem, UIBase.SideBar):
                    self.rect.x = 326        
            
            self.toolTipText = 'Open custom card code settings'
