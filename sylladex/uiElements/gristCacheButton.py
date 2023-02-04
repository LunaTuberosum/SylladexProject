import pygame as pg

from baseUI import UIBase, Apperance


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, 'GristCacheButton', 1)

        self.apperance = Apperance(
            self,
            (70,70),
            [[64, 64], '#999999', [0, 6]], 
            [[64, 64], '#D9D9D9', [6, 0]], 
            colorKey = True, 
            image = ['sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0]]
            )

        self.tool_tip_text = "Opens Grist Cache" 

        self.hovering = False

    def hover(self):
        if self.tool_tip_text == 'Closes Grist Cache':
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        else:
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        if self.tool_tip_text == 'Closes Grist Cache':
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        else:
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        self.hovering = False

    def on_click(self):
        if self.tool_tip_text == 'Opens Grist Cache':

            self.tool_tip_text = 'Closes Grist Cache'
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])

            if UIBase.check_for_ui('SideBar'):
                UIBase.get_ui_elem('GristCache')(-392)
            else:
                UIBase.get_ui_elem('GristCache')(-719)
            
        elif self.tool_tip_text == 'Closes Grist Cache':

            self.tool_tip_text = 'Opens Grist Cache'
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])

            if UIBase.check_for_ui('SideBar'):
                UIBase.find_cur_ui('GristCache').to_be_rect = -392
            else:
                UIBase.find_cur_ui('GristCache').to_be_rect = -719
