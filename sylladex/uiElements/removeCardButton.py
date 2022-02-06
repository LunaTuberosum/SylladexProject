import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class RemoveCardButton(UIBase):

    eject = False

    def __init__(self):
        super().__init__(112, 50, (70, 70), "sylladex/uiElements/asset/STACK/REMOVE_CARD.png")

        self.toolTipText = "Eject a Card from your Sylladex" 
        
    def on_click(self):
        if UIBase.RemoveCardButton.eject == False:
            UIBase.RemoveCardButton.eject = True
            
        else:
            UIBase.RemoveCardButton.eject = False
                
                        

        