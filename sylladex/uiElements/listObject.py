import pygame as pg
from dataclasses import dataclass

from baseUI import UIBase, Apperance
from sylladex.captchalogueCards import codeDatabase

@dataclass
class CodeData():
    name: str = "-"
    code: str = "-"
    tier: str = "-"
    
    kind: str = ''
    grist: str = ''
    trait1: str = ''
    trait2: str = ''
    action1: str = ''
    action2: str = ''
    action3: str = ''
    action4: str = ''

    cardID: int = 0
    
class ListObject(UIBase):
    def __init__(self):
        super().__init__(24, 127, 'CardListObject', 1)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf",24)

        self.apperance = Apperance(
            self,
            [249, 64],
            [[249, 64], '#FFFFFF', [0,0]],
            image=["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]],
            imageAlpha=125,
            texts=[
                ['-', [6, 15], 'left', '#000000'],
                ['-', [6, 49], 'left', '#000000'],
                ['-', [190, 49], 'left', '#000000']]
        )
        
        self.children = []

        self.interactable = True
        self.prevPos = None
        self.grabbed = False
        self.hovering = False
        self.writing = False

        self.empty = True
        self.captaCard = None

        self.codeData = CodeData()

        self.prevTick = 0
    

    # def update(self):
    #     if self.prevTick > 0:
    #         if pg.time.get_ticks() - self.prevTick >= 500:
    #             if self.captaCard.shaking == False:
    #                 self.captaCard.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA_HIGHLIGHT.png').convert_alpha()
    #                 self.captaCard.kind_image()

    #     if self.grabbed == True:
    #         self.rect.left = pg.mouse.get_pos()[0] - 32
    #         self.rect.top = pg.mouse.get_pos()[1] - 32
    #         self.redraw_card((255,255,255))

    #         self.hovering = False

    #     if self.rect.y >= 196 and self.rect.y <= 757:
    #         self.interactable = True
    #         if self.children:
    #             for child in self.children:
    #                 UIBase.get_group('layer').change_layer(child, -1)
    #             UIBase.get_group('layer').change_layer(self.children[3], 1)
    #     else:
    #         self.interactable = False
    #         if self.children:
    #             for child in self.children:
    #                 UIBase.get_group('layer').change_layer(child, -1)

    def redraw_card(self):
        if self.writing == False:
            if self.captaCard:
                self.apperance.sizeColorPos = [[[249, 64], '#FFFFFF', [0, 0]],  [[10, 64], 'ModusForground', [239, 0]]]

                self.apperance.options = {
                    'image': [UIBase.CodeDatabase.find_kindImage(self.codeData.kind), [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                    [self.codeData.name, [6, 15], 'left', '#000000'],
                    [self.codeData.code, [6, 49], 'left', '#000000'],
                    [self.codeData.tier, [150, 49], 'left', '#000000']]}

            elif self.codeData.code == "-":

                self.apperance.options = {
                    'image': ["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                    ['-', [6, 15], 'left', '#000000'],
                    ['-', [6, 49], 'left', '#000000'],
                    ['-', [150, 49], 'left', '#000000']]}

            elif self.codeData:

                self.apperance.options = {
                    'image': [UIBase.CodeDatabase.find_kindImage(self.codeData.kind), [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                    [self.codeData.name, [6, 15], 'left', '#000000'],
                    [self.codeData.code, [6, 49], 'left', '#000000'],
                    [self.codeData.tier, [150, 49], 'left', '#000000']]}

            self.apperance.reload_apperance()

    def place_children(self):
        self.children[0].rect.topleft = (self.rect.x+3, self.rect.y+3)
        self.children[1].rect.topleft = (self.rect.x+3, self.rect.y+35)
        self.children[2].rect.topleft = (self.rect.x+129, self.rect.y+35)
        self.children[3].rect.topleft = (78, self.rect.y+64)

    # def start_card(self):

    #     self.image.fill((255,255,255))
    #     self.writing = True
    #     self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+3, self.rect.y+3, 243, 28, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", "Txt"))
    #     self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+3, self.rect.y+35, 105, 28, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", "Txt"))
    #     self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+129, self.rect.y+35, 33, 28, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", "Txt"))
        

    #     for child in self.children:
    #         UIBase.get_group('layer').change_layer(child, -1)
    #         child.changeColors((230,230,230), (200,200,200), (170,170,170))

    #     self.children.append(UIBase.get_uiElem('FinishButton')(self))

    #     self.children[0].active = True
    #     self.children[0].image.fill((170,170,170))


    #     for elem in UIBase.get_group("ui"):
    #         if hasattr(elem, "job"):
    #             if elem.job == "nameOverlay" or elem.job == "codeOverlay" or elem.job == "tierOverlay":
    #                 elem.color = (235,235,235)
    #                 elem.no_hover()

    def hover(self):
        # if self.captaCard:
        #     if self.prevTick == 0:
        #         self.prevTick = pg.time.get_ticks()

        if self.writing == False:
            self.apperance.sizeColorPos = [[[249, 64], '#D1D1D1', [0,0]]]
            self.apperance.reload_apperance()
            self.hovering = True

    def no_hover(self):
        if self.writing == False:
            self.apperance.sizeColorPos = [[[249, 64], '#FFFFFF', [0,0]]]
            self.apperance.reload_apperance()
            self.hovering = False

        # if self.captaCard:
        #     self.prevTick = 0
        #     self.captaCard.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        #     self.captaCard.kind_image()

    # def alt_no_hover(self):
    #     self.redraw_card((230,230,230))
    #     self.hovering = False

    # def alt_hover(self):
    #     self.redraw_card((255,255,255))
    #     self.hovering = True

    # def on_click(self):
    #     if UIBase.get_uiElem('RemoveCardButton').eject == True and self.interactable == True:
    #         if self.empty == False:
    #             self.empty = True
    #             self.codeData = CodeData()

    #             UIBase.get_uiElem('RemoveCardButton').eject = False
    #             for elem in UIBase.get_group("ui"):
    #                 if isinstance(elem, UIBase.get_uiElem('ListObject')):
    #                     elem.redraw_card((255,255,255))
    #                 elif isinstance(elem, UIBase.get_uiElem('CardList')):
    #                     elem.save_list()
    #         else: 
    #             UIBase.get_uiElem('PopUp')("You can\'t eject an empty card")

    #     elif self.interactable == True:
    #         if self.empty == False:
    #             self.grabbed = True
    #             self.prevPos = self.rect.topleft
    #             UIBase.get_group('layer').change_layer(self, len(UIBase.get_group('ui')))