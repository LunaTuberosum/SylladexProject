import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.popUp import PopUp

class AddCardButton(UIBase):
    def __init__(self):
        super().__init__(30, 50, (70, 70), "sylladex/uiElements/asset/STACK/ADD_CARD.png")

        self.toolTipText = "Captchalogue a Card to your Sylladex" 
        
    def on_click(self):
        for item in CardList.listObj:
            if item.empty == True:
                item.empty = False
                item.start_card()
                return
        PopUp("You have no empty cards")
        