import pygame as pg

from baseUI import UIBase


class RemoveCardButton(UIBase):

    eject = False

    def __init__(self):
        super().__init__(112, 50, (70, 70), 'RemoveCardButton', (0,0,0))

        self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [6, 0]])
 
        self.toolTipText = "Eject a Card from your Sylladex" 
        self.hovering = False
        
    def reloadSelf(self):
        self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [6, 0]])

    def hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [6, 0])
        self.hovering = False
        
    def on_click(self):
        if UIBase.get_uiElem('RemoveCardButton').eject == False:
            UIBase.get_uiElem('RemoveCardButton').eject = True
            
        else:
            UIBase.get_uiElem('RemoveCardButton').eject = False
                
                        

        