import pygame as pg

from uiElement import UIElement, Apperance


class CustomSettingButton(UIElement):
    def __init__(self):
        
        super().__init__(
            0, 
            50, 
            'CustomSettingButton', 
            1
            )

        self.apperance = Apperance(
            self,
            [70,70],
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
            self.tool_tip_text = 'Close custom card code settings'
            
            UIElement.get_ui_elem('CustomSettingMenu')()

        elif self.tool_tip_text == 'Close custom card code settings':
            
            if UIElement.find_current_ui('SideBar'):
                UIElement.find_current_ui('CustomSettingMenu').to_be_rect = -22
            else:
                UIElement.find_current_ui('CustomSettingMenu').to_be_rect = -348
            
            self.tool_tip_text = 'Open custom card code settings'
