import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class AddCardButton(UIBase):
    def __init__(self):
        super().__init__(30, 50, (70, 70), "sylladex/uiElements/asset/STACK/ADD_CARD.png")

        self.toolTipText = "Captchalogue a Card to your Sylladex" 
        
    def on_click(self):
        for item in UIBase.CardList.listObj:
            if item.writing == True:
                item.writing = False
                item.redraw_card((255,255,255))
                self.toolTipText = "Captchalogue a Card to your Sylladex" 
                
                for child in item.children:
                    child.kill()
                return
            if item.empty == True:
                item.start_card()
                self.toolTipText = "Stop adding a Card to your Sylladex" 

                return
        UIBase.PopUp("You have no empty cards")
        