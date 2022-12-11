import pygame as pg

from baseUI import UIBase

class EditCardButton(UIBase):

    edit = False

    def __init__(self):
        super().__init__(218, 48, (74, 74), 'AddCard', (0,0,0))

        self.create_appearance(
            [[64, 64], UIBase.modusBackground, [2, 8]], 
            [[64, 64], UIBase.modusAccent, [8, 2]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/EDIT_CARD_ICON.png', [8, 2]]
            )

        self.toolTipText = "Edit a Card in your Sylladex" 
        self.hovering = False

    def hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/EDIT_CARD_ICON_HOVER.png', [8, 2])
        self.hovering = True

    def no_hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/EDIT_CARD_ICON.png', [8, 2])
        self.hovering = False

    def on_click(self):
        if UIBase.get_uiElem('EditCardButton').edit == False:
            UIBase.get_uiElem('EditCardButton').edit = True
            self.toolTipText = "Stop editing Cards in your Sylladex"
            self.create_appearance(
                [[68, 68], '#FFFFFF', [0, 6]],
                [[68, 68], '#FFFFFF', [6, 0]],
                [[64, 64], UIBase.modusBackground, [2, 8]],  
                [[64, 64], UIBase.modusAccent, [8, 2]], 
                colorKey = True, 
                image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/EDIT_CARD_ICON.png', [8, 2]]
                )
            
        else:
            UIBase.get_uiElem('EditCardButton').edit = False
            self.toolTipText = "Edit a Card in your Sylladex"
            self.image.fill((0,0,0))
            self.create_appearance(
                [[64, 64], UIBase.modusBackground, [2, 8]], 
                [[64, 64], UIBase.modusAccent, [8, 2]], 
                colorKey = True, 
                image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/EDIT_CARD_ICON.png', [8, 2]]
                )
            
    