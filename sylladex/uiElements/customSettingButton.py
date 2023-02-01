import pygame as pg

from baseUI import UIBase, Apperance


class CustomSettingButton(UIBase):
    def __init__(self):
        super().__init__(0, 50, 'CustomSettingButton')

        self.apperance = Apperance(
            self,
            (70,70),
            [[64, 64], '#666666', [0, 6]], 
            [[64, 64], '#1155CC', [6, 0]], 
            colorKey = True, 
            image = ['sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png', [18, 12]]
            )

        self.toolTipText = 'Open custom card code settings'
        self.hovering = False
    
    def hover(self):
        self.apperance.change_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO_HOVER.png', [18, 12])
        self.hovering = True

    def no_hover(self):
        self.apperance.change_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png', [18, 12])
        self.hovering = False

    def update(self):
        if UIBase.check_forUI('SideBar') and self.rect != 326:
            self.rect.x = 326
        elif not UIBase.check_forUI('SideBar') and self.rect.x != 0:
            self.rect.x = 0

    def on_click(self):
        if self.toolTipText == 'Open custom card code settings':
            self.rect.x = 342
            self.toolTipText = 'Close custom card code settings'
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('SideBar')):
                    UIBase.get_uiElem('CustomSettingMenu')(326)
                    self.rect.x = 668
                    return
            UIBase.get_uiElem('CustomSettingMenu')(0)

        elif self.toolTipText == 'Close custom card code settings':

            self.rect.x = 0
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('CustomSettingMenu')):
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                    for child in elem.children:
                        UIBase.remove_fromGroup(child)
                        child.kill()
                        if hasattr(child, 'children'):
                            for child in child.children:
                                UIBase.remove_fromGroup(child)
                                child.kill()
                elif isinstance(elem, UIBase.get_uiElem('SideBar')):
                    self.rect.x = 326        
            
            self.toolTipText = 'Open custom card code settings'
