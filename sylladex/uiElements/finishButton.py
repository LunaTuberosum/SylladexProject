import pygame as pg

from uiElement import UIElement

class FinishButton(UIElement):
    def __init__(self, card):
        super().__init__(78, card.rect.y+64, (140, 36), 'FinishButton', UIElement.modusBackground)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.create_appearance([[128, 30], UIElement.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIElement.modusBackground]])

        self.card = card
        UIElement.get_group('layer').change_layer(self, 1)
        self.tool_tip_text = "Finish Captchalogueing a Card to your Deck" 

        self.hovering = False

    def reloadSelf(self):
        self.create_appearance([[140, 36], UIElement.modusBackground, [0, 0]],[[128, 30], UIElement.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIElement.modusBackground]])
        
    def hover(self):
        self.create_appearance([[128, 30], UIElement.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIElement.modusForground]])
        self.hovering = True

    def no_hover(self):
        self.create_appearance([[128, 30], UIElement.modusAccent, [6, 0]], texts = [['FINISH', [70, 18], 'center', UIElement.modusBackground]])
        self.hovering = False
        
    def on_click(self):
        for _elem in UIElement.get_group("ui"):
            if isinstance(_elem, UIElement.get_ui_elem('TextField')):
                if _elem.job == "nameOverlay":
                    if len(_elem.text) == 0:
                        UIElement.get_ui_elem('PopUp')('The card must have a name')
                        return
                    _name = _elem.text

                elif _elem.job == "codeOverlay":
                    if len(_elem.text) < 8:
                        UIElement.get_ui_elem('PopUp')('Codes must be a 8 characters long')
                        return
                    _code = _elem.text

                elif _elem.job == "tierOverlay":
                    if len(_elem.text) == 0:
                        UIElement.get_ui_elem('PopUp')('Cards must have a tier')
                        return

                    _is_num = True
                    for _char in _elem.text:
                        for _num in range(0,10):
                            if _char == str(_num):
                                _is_num = True
                                break
                            else:
                                _is_num = False
                        if _is_num == False:
                            UIElement.get_ui_elem('PopUp')("Tier must only be numbers")
                            return

                    if int(_elem.text) > 16:
                        UIElement.get_ui_elem('PopUp')("Tier can be no higher than 16")
                        return
                    elif int(_elem.text) == 0:
                        UIElement.get_ui_elem('PopUp')("Tier must be at least 1")
                        return
                    
                    _tier = _elem.text
                        
        self.card.writing = False   
        UIElement.CodeDatabase.read_code(_name, _code, _tier, self.card)
        self.card.redraw_card((255,255,255))
        self.card.empty = False
        for child in self.card.children:
            child.kill()
        self.card.children.clear()
        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem('CardList')):
                _elem.save_list()