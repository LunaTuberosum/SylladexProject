import pygame as pg
from sylladex.captchalogueCards.baseCard import BaseCard

from uiElement import UIElement, Apperance


class ListObject(UIElement):
    def __init__(self):

        super().__init__(
            24,
            127,
            'CardListObject',
            12
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/DisposableDroidBB.ttf", 24)

        self.apperance = Apperance(
            self,
            [249, 64],
            [[249, 64], '#FFFFFF', [0, 0]],
            images=[
                ["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]]
            ],
            imageAlpha=125,
            texts=[
                ['-', [6, 15], 'left', '#000000'],
                ['-', [6, 49], 'left', '#000000'],
            ]
        )

        self.prev_pos = None
        self.grabbed = False
        self.hovering = False
        self.writing = False

        self.capta_card = None

        self.name = '-'
        self.code = '-'

        self.prev_tick = 0

    def update(self):
        if self.prev_tick > 0:
            if pg.time.get_ticks() - self.prev_tick >= 500:
                if self.capta_card:
                    self.capta_card.highlight = True

        if self.rect.y >= 196 and self.rect.y <= 757:
            self.interactable = True
            UIElement.change_layer(self, 12)
        else:
            self.interactable = False
            UIElement.change_layer(self, 9)

    def move(self, rel):
        if not self.grabbed:
            return
        self.rect.move_ip(rel)
        self.hovering = False

    def redraw_card(self):
        if not self.hovering:
            _color = '#FFFFFF'
        else:
            _color = '#D1D1D1'

        if self.writing == False:

            if self.code == "-":
                self.apperance.size_color_pos = [
                    [[249, 64], _color, [0, 0]],
                ]

                self.apperance.change_images([
                    ["sylladex/uiElements/asset/KINDS/CustomKind.png", [185, 3]]
                ])
                self.apperance.kwargs['imageAlpha'] = 125

                self.apperance.kwargs['texts'] = [
                    ['-', [6, 15], 'left', '#000000'],
                    ['-', [6, 49], 'left', '#000000'],
                ]

            else:
                self.apperance.size_color_pos = [
                    [[249, 64], _color, [0, 0]],
                ]

                self.apperance.change_images([
                    [UIElement.code_database.find_kind_image(
                        UIElement.code_database.get_code_value(self.code[0], '1')), [185, 3]]
                ])
                self.apperance.kwargs['imageAlpha'] = 125

                self.apperance.kwargs['texts'] = [
                    [self.name, [6, 15], 'left', '#000000'],
                    [self.code, [6, 49], 'left', '#000000'],
                ]

            self.apperance.reload_apperance()

    def start_card(self):

        self.apperance.kwargs['texts'] = []
        self.apperance.kwargs['imageAlpha'] = 0
        self.apperance.reload_apperance()
        self.writing = True

        self.add_child(
            UIElement.get_ui_elem('TextField')(
                6,
                3,
                [237, 28],
                "nameOverlay",
                "Input the name of the Captchalogue Card (A-Z, a-z)",
                21,
                startLayer=13,
                baseColors=[(230, 230, 230), (200, 200, 200), (170, 170, 170)]
            ))
        self.add_child(
            UIElement.get_ui_elem('TextField')(
                6,
                35,
                [116, 28],
                "codeOverlay",
                "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)",
                7,
                startLayer=13,
                baseColors=[(230, 230, 230), (200, 200, 200), (170, 170, 170)]
            ))

        self.add_child(
            UIElement.get_ui_elem('FinishButton')(
                64,
                self)
        )

    def hover(self):
        if self.capta_card:
            if self.prev_tick == 0:
                self.prev_tick = pg.time.get_ticks()

        if self.writing == False:
            self.hovering = True
            self.redraw_card()

    def no_hover(self):
        if self.writing == False:
            if self.hovering == False and self.capta_card:
                self.capta_card.highlight = False
                self.prev_tick = 0
            self.hovering = False
            self.redraw_card()

    def on_click(self):
        if self.writing:
            return

        if UIElement.get_ui_elem('RemoveCardButton').get_eject() and self.interactable:
            if self.code == '-':
                UIElement.get_ui_elem('PopUp')(
                    "You can\'t eject an empty card")
                return

            if self.capta_card:
                UIElement.get_ui_elem('PopUp')(
                    "Remove card from stacking area before clearing data")
                return

            UIElement.get_ui_elem('RemoveCardButton').change_eject(False)
            self.empty = True
            self.code = '-'
            self.name = ''
            self.redraw_card()

            UIElement.find_current_ui('RemoveCardButton').reload_image()
            UIElement.find_current_ui('CardList').save_list()

        elif UIElement.get_ui_elem('EditCardButton').get_edit() and self.interactable:
            if self.code == '-':
                UIElement.get_ui_elem('PopUp')(
                    "You can\'t edit an empty card")
                return

            UIElement.get_ui_elem('EditCardButton').change_edit(False)

            self.hovering = False
            self.start_card()
            self.children[0].text = self.name
            self.children[0].reload_text()
            self.children[1].text = self.code
            self.children[1].reload_text()

        elif self.interactable == True:
            if self.code != '-':
                self.grabbed = True
                self.prev_pos = self.rect.topleft
                UIElement.get_group('layer').change_layer(self, 999)

    def on_release(self, pos: list):
        if pos[0] > UIElement.find_current_ui('CardList').rect.right:
            if self.capta_card == None:
                self.capta_card = BaseCard(pos)
                UIElement.code_database.read_code(
                    self.name, self.code, self.capta_card)
                self.capta_card.code_data.cardID = self.capta_card.cardID

                BaseCard.save_cards()
                UIElement.find_current_ui('CardList').save_list()

            else:
                UIElement.get_ui_elem('PopUp')(
                    'This card is already deployed')
        else:
            UIElement.get_ui_elem('PopUp')(
                'Drag the card into the stacking area')

        self.rect.topleft = self.prev_pos
        UIElement.get_group('layer').change_layer(self, 12)
        self.redraw_card()
        self.grabbed = False
