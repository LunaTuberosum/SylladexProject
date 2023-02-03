import pygame as pg

from baseUI import UIBase, Apperance

class AddCardButton(UIBase):
    def __init__(self):
        super().__init__(30, 50, 'AddCard')

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], 'ModusBackground', [0, 6]], 
            [[64, 64], 'ModusAccent', [6, 0]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/ADD_CARD_ICON.png', [6, 0]]
            )

        self.toolTipText = "Captchalogue a Card to your Sylladex" 
        self.hovering = False
        
    def reload_image(self):
        if self.hovering == False:
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/ADD_CARD_ICON.png', [6, 0],)
        else: 
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/ADD_CARD_ICON_HOVER.png', [6, 0])

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()
    
    # def on_click(self):
    #     for item in UIBase.get_uiElem('CardList').children:
    #         if item.writing == True:
    #             item.writing = False
    #             item.empty = True
    #             item.redraw_card((255,255,255))
    #             self.toolTipText = "Captchalogue a Card to your Sylladex" 
                
    #             for child in item.children:
    #                 child.kill()
    #             item.children.clear()
    #             return
    #         if item.empty == True:
    #             if item.interactable == True:
    #                 item.start_card()
    #                 self.toolTipText = "Stop adding a Card to your Sylladex" 

    #                 return
    #             else:
    #                 UIBase.get_uiElem('PopUp')('Empty card not in view')

    #                 return
    #     UIBase.get_uiElem('PopUp')("You have no empty cards")
        