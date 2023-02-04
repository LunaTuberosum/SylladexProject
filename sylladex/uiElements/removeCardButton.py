import pygame as pg

from baseUI import UIBase, Apperance


class RemoveCardButton(UIBase):

    __eject = False

    def __init__(self):
        super().__init__(112, 50, 'RemoveCardButton', )

        self.apperance = Apperance(
            self,
            [70, 70],
            [[64, 64], 'ModusBackground', [0, 6]], 
            [[64, 64], 'ModusAccent', [6, 0]], 
            colorKey = True, 
            image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [6, 0]])
 
        self.tool_tip_text = "Eject a Card from your Sylladex" 
        self.hovering = False
        
    def reload_image(self):
        if self.hovering == False:
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON.png', [6, 0],)
        else: 
            self.apperance.change_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [6, 0])

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
    #     if UIBase.get_uiElem('RemoveCardButton').__eject == False:
    #         UIBase.get_uiElem('RemoveCardButton').__eject = True
            
    #     else:
    #         UIBase.get_uiElem('RemoveCardButton').__eject = False
                
                        

        