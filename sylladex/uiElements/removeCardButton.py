import pygame as pg

from baseUI import UIBase


class RemoveCardButton(UIBase):

    eject = False

    def __init__(self):
        super().__init__(110, 48, (74, 74), 'RemoveCardButton', (0,0,0))

        self.create_appearance(
            [[64, 64], UIBase.modusBackground, [2, 8]], 
            [[64, 64], UIBase.modusAccent, [8, 2]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [8, 2]]
            )
 
        self.toolTipText = "Eject a Card from your Sylladex" 
        self.hovering = False
        
    def reloadSelf(self):
        self.create_appearance(
            [[64, 64], UIBase.modusBackground, [2, 8]], 
            [[64, 64], UIBase.modusAccent, [8, 2]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [8, 2]]
            )

    def hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [8, 2])
        self.hovering = True

    def no_hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [8, 2])
        self.hovering = False
        
    def on_click(self):
        if UIBase.get_uiElem('RemoveCardButton').eject == False:
            UIBase.get_uiElem('RemoveCardButton').eject = True
            self.toolTipText = "Stop ejecting Cards from your Sylladex" 
            self.create_appearance(
                [[68, 68], '#FFFFFF', [0, 6]],
                [[68, 68], '#FFFFFF', [6, 0]],
                [[64, 64], UIBase.modusBackground, [2, 8]], 
                [[64, 64], UIBase.modusAccent, [8, 2]], 
                colorKey = True, 
                image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [8, 2]]
                )
        else:
            UIBase.get_uiElem('RemoveCardButton').eject = False
            self.toolTipText = "Eject a Card from your Sylladex"
            self.image.fill((0,0,0))
            self.create_appearance(
                [[64, 64], UIBase.modusBackground, [2, 8]], 
                [[64, 64], UIBase.modusAccent, [8, 2]], 
                colorKey = True, 
                image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [8, 2]]
                )
            