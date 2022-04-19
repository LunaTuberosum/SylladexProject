import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class RemoveCardButton(UIBase):

    eject = False

    def __init__(self):
        super().__init__(112, 50, (70, 70), "REMOVE_CARD.png", 'RemoveCardButton')

        self.toolTipText = "Eject a Card from your Sylladex" 
        self.hovering = False
        
    def hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD.png").convert_alpha()
        self.hovering = False  
        
    def on_click(self):
        if UIBase.RemoveCardButton.eject == False:
            UIBase.RemoveCardButton.eject = True
            
        else:
            UIBase.RemoveCardButton.eject = False
                
                        

        