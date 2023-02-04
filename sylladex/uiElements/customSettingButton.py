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

        self.tool_tip_text = 'Open custom card code settings'
        self.hovering = False
    
    def hover(self):
        self.apperance.change_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO_HOVER.png', [18, 12])
        self.hovering = True

    def no_hover(self):
        self.apperance.change_image('sylladex/uiElements/asset/MISC/CUSTOM_SETTING_LOGO.png', [18, 12])
        self.hovering = False

    def on_click(self):
        if self.tool_tip_text == 'Open custom card code settings':
            self.rect.x = 342
            self.tool_tip_text = 'Close custom card code settings'
            for _elem in UIBase.get_group('ui'):
                if isinstance(_elem, UIBase.get_ui_elem('SideBar')):
                    UIBase.get_ui_elem('CustomSettingMenu')(326)
                    self.rect.x = 668
                    return
            UIBase.get_ui_elem('CustomSettingMenu')(0)

        elif self.tool_tip_text == 'Close custom card code settings':

            self.rect.x = 0
            for _elem in UIBase.get_group('ui'):
                if isinstance(_elem, UIBase.get_ui_elem('CustomSettingMenu')):
                    UIBase.remove_from_group(_elem)
                    for _child in _elem.children:
                        UIBase.remove_from_group(_child)
                        if hasattr(_child, 'children'):
                            for _child in _child.children:
                                UIBase.remove_from_group(_child)
                elif isinstance(_elem, UIBase.get_ui_elem('SideBar')):
                    self.rect.x = 326        
            
            self.tool_tip_text = 'Open custom card code settings'
