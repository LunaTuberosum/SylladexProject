import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, (70,70), 'GristCacheButton', (0,0,0))

        self._create_appearance([[64, 64], '#999999', [0, 6]], [[64, 64], '#D9D9D9', [6, 0]], colorKey = True, image = ['sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0]])

        self.toolTipText = "Opens Grist Cache" 

        self.hovering = False

    def hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        else:
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
        else:
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])
        self.hovering = False
        
    def on_click(self):
        if self.toolTipText == 'Opens Grist Cache':
            self.toolTipText = 'Closes Grist Cache'
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON_HOVER.png', [6, 0])
            
            self.rect.x = 713
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.SideBar):
                    self.rect.x = 1038
                    UIBase.GristCache(325)
                    return
                    
            UIBase.GristCache(0)

        elif self.toolTipText == 'Closes Grist Cache':
            self.toolTipText = 'Opens Grist Cache'
            self._reload_image('sylladex/uiElements/asset/MISC/GRIST_CACHE_ICON.png', [6, 0])

            self.rect.x = 0
            for elem in UIBase.get_group('ui'):
                if isinstance(elem ,UIBase.GristCache):
                    for child in elem.children:
                        if hasattr(child, 'children'):
                            for child2 in child.children:
                                UIBase.remove_fromGroup(child2)
                                child2.kill()
                        UIBase.remove_fromGroup(child)
                        child.kill()
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

                if isinstance(elem, UIBase.SideBar):
                    self.rect.x = 326

             
            
