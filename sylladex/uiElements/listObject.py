import pygame as pg
from dataclasses import dataclass, asdict

from uiElement import UIElement, Apperance
from sylladex.captchalogueCards import codeDatabase


@dataclass
class CodeData():
    name: str = "-"
    code: str = "-"
    tier: str = "-"

    kind: str = ''
    grist: str = ''
    trait_1: str = ''
    trait_2: str = ''
    action_1: str = ''
    action_2: str = ''
    action_3: str = ''
    action_4: str = ''

    cardID: int = 0


class ListObject(UIElement):
    def __init__(self):

        super().__init__(
            24,
            127,
            'CardListObject',
            3
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.apperance = Apperance(
            self,
            [249, 64],
            [[249, 64], '#FFFFFF', [0, 0]],
            image=["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]],
            imageAlpha=125,
            texts=[
                ['-', [6, 15], 'left', '#000000'],
                ['-', [6, 49], 'left', '#000000'],
                ['-', [190, 49], 'left', '#000000']]
        )

        self.interactable = True
        self.prev_pos = None
        self.grabbed = False
        self.hovering = False
        self.writing = False

        self.empty = True
        self.capta_card = None

        self.code_data = CodeData()

        self.prev_tick = 0

    def create_code_data(self, inputs: dict):
        self.code_data.name = inputs['name']
        self.code_data.code = inputs['code']
        self.code_data.tier = inputs['tier']
        self.code_data.kind = inputs['kind']
        self.code_data.grist = inputs['grist']
        self.code_data.trait_1 = inputs['trait_1']
        self.code_data.trait_2 = inputs['trait_2']
        self.code_data.action_1 = inputs['action_1']
        self.code_data.action_2 = inputs['action_2']
        self.code_data.action_3 = inputs['action_3']
        self.code_data.action_4 = inputs['action_4']
        self.code_data.cardID = inputs['cardID']

        self.redraw_card()

    # def update(self):
    #     if self.prev_tick > 0:
    #         if pg.time.get_ticks() - self.prev_tick >= 500:
    #             if self.capta_card.shaking == False:
    #                 self.capta_card.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_HIGHLIGHT.png').convert_alpha()
    #                 self.capta_card.kind_image()

    #     if self.grabbed == True:
    #         self.rect.left = pg.mouse.get_pos()[0] - 32
    #         self.rect.top = pg.mouse.get_pos()[1] - 32
    #         self.redraw_card((255,255,255))

    #         self.hovering = False

    #     if self.rect.y >= 196 and self.rect.y <= 757:
    #         self.interactable = True
    #         if self.children:
    #             for child in self.children:
    #                 UIElement.get_group('layer').change_layer(child, -1)
    #             UIElement.get_group('layer').change_layer(self.children[3], 1)
    #     else:
    #         self.interactable = False
    #         if self.children:
    #             for child in self.children:
    #                 UIElement.get_group('layer').change_layer(child, -1)

    def redraw_card(self):
        if self.writing == False:
            if self.capta_card:
                self.apperance.size_color_pos = [
                    [[249, 64], '#FFFFFF', [0, 0]],  [[10, 64], 'ModusForground', [239, 0]]]

                self.apperance.kwargs = {
                    'image': [UIElement.CodeDatabase.find_kind_image(self.code_data.kind), [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                        [self.code_data.name, [6, 15], 'left', '#000000'],
                        [self.code_data.code, [6, 49], 'left', '#000000'],
                        [self.code_data.tier, [150, 49], 'left', '#000000']]}

            elif self.code_data.code == "-":

                self.apperance.kwargs = {
                    'image': ["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                        ['-', [6, 15], 'left', '#000000'],
                        ['-', [6, 49], 'left', '#000000'],
                        ['-', [150, 49], 'left', '#000000']]}

            elif self.code_data:

                self.apperance.kwargs = {
                    'image': [UIElement.CodeDatabase.find_kind_image(self.code_data.kind), [185, 3]],
                    'imageAlpha': 125,
                    'texts': [
                        [self.code_data.name, [6, 15], 'left', '#000000'],
                        [self.code_data.code, [6, 49], 'left', '#000000'],
                        [self.code_data.tier, [150, 49], 'left', '#000000']]}

            self.apperance.reload_apperance()

    def place_children(self):
        self.children[0].rect.topleft = (self.rect.x+3, self.rect.y+3)
        self.children[1].rect.topleft = (self.rect.x+3, self.rect.y+35)
        self.children[2].rect.topleft = (self.rect.x+129, self.rect.y+35)
        self.children[3].rect.topleft = (78, self.rect.y+64)

    # def start_card(self):

    #     self.image.fill((255,255,255))
    #     self.writing = True
    #     self.children.append(UIElement.get_uiElem('TextField')(self.rect.x+3, self.rect.y+3, 243, 28, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", "Txt"))
    #     self.children.append(UIElement.get_uiElem('TextField')(self.rect.x+3, self.rect.y+35, 105, 28, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", "Txt"))
    #     self.children.append(UIElement.get_uiElem('TextField')(self.rect.x+129, self.rect.y+35, 33, 28, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", "Txt"))

    #     for child in self.children:
    #         UIElement.get_group('layer').change_layer(child, -1)
    #         child.changeColors((230,230,230), (200,200,200), (170,170,170))

    #     self.children.append(UIElement.get_uiElem('FinishButton')(self))

    #     self.children[0].active = True
    #     self.children[0].image.fill((170,170,170))

    #     for elem in UIElement.get_group("ui"):
    #         if hasattr(elem, "job"):
    #             if elem.job == "nameOverlay" or elem.job == "codeOverlay" or elem.job == "tierOverlay":
    #                 elem.color = (235,235,235)
    #                 elem.no_hover()

    def hover(self):
        # if self.capta_card:
        #     if self.prev_tick == 0:
        #         self.prev_tick = pg.time.get_ticks()

        if self.writing == False:
            self.apperance.size_color_pos = [[[249, 64], '#D1D1D1', [0, 0]]]
            self.apperance.reload_apperance()
            self.hovering = True

    def no_hover(self):
        if self.writing == False:
            self.apperance.size_color_pos = [[[249, 64], '#FFFFFF', [0, 0]]]
            self.apperance.reload_apperance()
            self.hovering = False

        # if self.capta_card:
        #     self.prev_tick = 0
        #     self.capta_card.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
        #     self.capta_card.kind_image()

    # def alt_no_hover(self):
    #     self.redraw_card((230,230,230))
    #     self.hovering = False

    # def alt_hover(self):
    #     self.redraw_card((255,255,255))
    #     self.hovering = True

    # def on_click(self):
    #     if UIElement.get_uiElem('RemoveCardButton').eject == True and self.interactable == True:
    #         if self.empty == False:
    #             self.empty = True
    #             self.code_data = CodeData()

    #             UIElement.get_uiElem('RemoveCardButton').eject = False
    #             for elem in UIElement.get_group("ui"):
    #                 if isinstance(elem, UIElement.get_uiElem('ListObject')):
    #                     elem.redraw_card((255,255,255))
    #                 elif isinstance(elem, UIElement.get_uiElem('CardList')):
    #                     elem.save_list()
    #         else:
    #             UIElement.get_uiElem('PopUp')("You can\'t eject an empty card")

    #     elif self.interactable == True:
    #         if self.empty == False:
    #             self.grabbed = True
    #             self.prev_pos = self.rect.topleft
    #             UIElement.get_group('layer').change_layer(self, len(UIElement.get_group('ui')))
