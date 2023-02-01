import pygame as pg

from baseUI import UIBase, Apperance


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, 'GristCacheButton')

        self.apperance = Apperance(
            self,
            (70,70),
            [[64, 64], '#999999', [0, 6]], 
            [[64, 64], '#D9D9D9', [6, 0]], 
            colorKey = True, 
            image = ['sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0]]
            )

        self.toolTipText = "Opens Grist Cache" 

        self.hovering = False

    def hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        else:
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        else:
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        self.hovering = False

    def update(self):
        if UIBase.check_forUI('SideBar'):
            if UIBase.check_forUI('GristCache') and self.rect.x != 1039:
                self.rect.x = 1039
            elif not UIBase.check_forUI('GristCache') and self.rect.x != 326:
                self.rect.x = 326
        else:
            if UIBase.check_forUI('GristCache') and self.rect.x != 713:
                self.rect.x = 713
            elif not UIBase.check_forUI('GristCache') and self.rect.x != 0:
                self.rect.x = 0
        
    def on_click(self):
        if self.toolTipText == 'Opens Grist Cache':

            self.toolTipText = 'Closes Grist Cache'
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])

            UIBase.get_uiElem('GristCache')()
            
        elif self.toolTipText == 'Closes Grist Cache':

            self.toolTipText = 'Opens Grist Cache'
            self.apperance.change_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])

            UIBase.remove_fromGroup(UIBase.find_curUI('GristCache'))
            
