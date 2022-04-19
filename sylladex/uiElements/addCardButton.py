import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class AddCardButton(UIBase):
    def __init__(self):
        super().__init__(30, 50, (70, 70), f"ADD_CARD.png", 'AddCard')

        self.toolTipText = "Captchalogue a Card to your Sylladex" 
        self.hovering = False
        
    def hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/ADD_CARD_HOVER.png").convert_alpha()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/ADD_CARD.png").convert_alpha()
        self.hovering = False
    
    def on_click(self):
        for item in UIBase.CardList.children:
            if item.writing == True:
                item.writing = False
                item.redraw_card((255,255,255))
                self.toolTipText = "Captchalogue a Card to your Sylladex" 
                
                for child in item.children:
                    child.kill()
                return
            if item.empty == True:
                if item.interactable == True:
                    item.start_card()
                    self.toolTipText = "Stop adding a Card to your Sylladex" 

                    return
                else:
                    UIBase.PopUp('Empty card not in view')

                    return
        UIBase.PopUp("You have no empty cards")
        