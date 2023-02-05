import pygame as pg

from uiElement import UIElement, Apperance


class RemoveCardButton(UIElement):

    __eject = False

    def __init__(self, x, y):

        super().__init__(
            x, 
            y, 
            'RemoveCardButton', 
            4
            )

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], 'ModusBackground', [0, 6]], 
            [[64, 64], 'ModusAccent', [6, 0]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [6, 0]])
 
        self.tool_tip_text = "Eject a Card from your Sylladex" 
        self.hovering = False
        
    def reload_image(self):
        if self.hovering == False:
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [6, 0],)
        else: 
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [6, 0])

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()
        
    @classmethod
    def get_eject(cls):
        return cls.__eject
    # def on_click(self):
    #     if UIElement.get_uiElem('RemoveCardButton').__eject == False:
    #         UIElement.get_uiElem('RemoveCardButton').__eject = True
            
    #     else:
    #         UIElement.get_uiElem('RemoveCardButton').__eject = False
                
                        

        