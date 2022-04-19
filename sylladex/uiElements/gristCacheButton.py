import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCacheButton(UIBase):
    def __init__(self):
        super().__init__(0, 928, (70,70), "GRIST_CACHE_BUTTON.png", 'GristCacheButton', True)

        self.toolTipText = "Opens Grist Cache" 

        self.hovering = False

    def hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png").convert_alpha()
        else:
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        if self.toolTipText == 'Closes Grist Cache':
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON_HOVER.png").convert_alpha()
        else:
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png").convert_alpha()
        self.hovering = False
        
    def on_click(self):
        if self.toolTipText == 'Opens Grist Cache':
            self.toolTipText = 'Closes Grist Cache'
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON_HOVER.png").convert_alpha()
            
            self.rect.x = 713
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.SideBar):
                    self.rect.x = 1038
                    UIBase.GristCache(325)
                    return
                    
            UIBase.GristCache(0)

        elif self.toolTipText == 'Closes Grist Cache':
            self.toolTipText = 'Opens Grist Cache'
            self.image = pg.image.load(f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png").convert_alpha()

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
                    elem.save_cache()
                    UIBase.remove_fromGroup(elem)
                    elem.kill()

                if isinstance(elem, UIBase.SideBar):
                    self.rect.x = 326

             
            
