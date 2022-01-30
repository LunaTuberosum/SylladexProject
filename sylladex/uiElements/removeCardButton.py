import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.cardList import CardList


class RemoveCardButton(UIBase):
    def __init__(self):
        super().__init__(112, 50, (70, 70), "sylladex/uiElements/asset/STACK/REMOVE_CARD.png")

        self.toolTipText = "Eject a Card from your Sylladex" 
        
    def on_click(self):
        if len(CardList.listObj) == 0:
            PopUp("You have no cards to remove")
        else:
            PopUp('COMMING SOON')

        