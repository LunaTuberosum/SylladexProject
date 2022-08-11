import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class FinishButton(UIBase):
    def __init__(self, card):
        super().__init__(78, card.rect.y+64, (140, 36), 'FinishButton', UIBase.modusBackground)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self._create_appearance([[128, 30], UIBase.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIBase.modusBackground]])

        self.card = card
        UIBase.get_group('layer').change_layer(self, 1)
        self.toolTipText = "Finish Captchalogueing a Card to your Deck" 

        self.hovering = False
        
    def hover(self):
        self._create_appearance([[128, 30], UIBase.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIBase.modusForground]])
        self.hovering = True

    def no_hover(self):
        self._create_appearance([[128, 30], UIBase.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIBase.modusBackground]])
        self.hovering = False
        
    def on_click(self):
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.TextField):
                if elem.job == "nameOverlay":
                    if len(elem.text) == 0:
                        UIBase.PopUp('The card must have a name')
                        return
                    self.card.name = elem.text

                elif elem.job == "codeOverlay":
                    if len(elem.text) < 8:
                        UIBase.PopUp('Codes must be a 8 characters long')
                        return
                    self.card.code = elem.text
                elif elem.job == "tierOverlay":
                    if len(elem.text) == 0:
                        UIBase.PopUp('Cards must have a tier')
                        return

                    isNum = True
                    for char in elem.text:
                        for num in range(0,10):
                            if char == str(num):
                                isNum = True
                                break
                            else:
                                isNum = False
                        if isNum == False:
                            UIBase.PopUp("Tier must only be numbers")
                            return

                    if int(elem.text) > 16:
                        UIBase.PopUp("Tier can be no higher than 16")
                        return
                    elif int(elem.text) == 0:
                        UIBase.PopUp("Tier must be at least 1")
                        return
                    
                    self.card.tier = elem.text
                        
        self.card.writing = False   
        self.card.redraw_card((255,255,255))
        self.card.empty = False
        for child in self.card.children:
            child.kill()
        self.card.children.clear()
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.CardList):
                elem.save_list()