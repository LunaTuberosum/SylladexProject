import pygame as pg
import random

from uiElement import Apperance, UIElement


class FinishButton(UIElement):
    def __init__(self, y, card):
        super().__init__(
            54,
            y,
            'FinishButton',
            13
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/fontstuck.ttf", 36)

        self.apperance = Apperance(
            self,
            [140, 36],
            [[140, 36], 'ModusBackground', [0, 0]],
            [[128, 30], 'ModusAccent', [6, 0]],
            texts=[
                ['FINISH', [70, 18], 'center', 'ModusBackground']
            ]
        )

        self.card = card
        self.tool_tip_text = "Finish Captchalogueing a Card to your Deck"

        self.hovering = False

    def hover(self):
        self.apperance.kwargs['texts'] = [
            ['FINISH', [70, 18], 'center', 'ModusForeground']
        ]
        self.apperance.reload_apperance()
        self.hovering = True

    def no_hover(self):
        self.apperance.kwargs['texts'] = [
            ['FINISH', [70, 18], 'center', 'ModusBackground']
        ]
        self.apperance.reload_apperance()
        self.hovering = False

    def on_click(self):
        if len(self.card.children[0].text) == 0:
            UIElement.get_ui_elem('PopUp')(
                'The card must have a name')
            return

        elif len(self.card.children[1].text) < 8:
            UIElement.get_ui_elem('PopUp')(
                'Codes must be a 8 characters long')
            return

        self.card.writing = False
        self.card.name = self.card.children[0].text
        self.card.code = self.card.children[1].text

        self.card.redraw_card()
        for child in self.card.children:
            child.kill()
        self.card.children.clear()

        UIElement.get_ui_elem('CardList').save_list()
        _add = UIElement.find_current_ui('AddCardButton')
        _add.writing = False
        _add.reload_image()

        if self.card.capta_card:
            self.card.capta_card.create_code_data(
                self.card.name, self.card.code)
            self.card.capta_card.redraw_card()

            UIElement.base_card.save_cards()
            return

        # if UIElement.base_card.get_length() == 0:
        self.card.capta_card = UIElement.base_card([random.randrange(400, 1500), random.randrange(
            0, 800)], self.card.name, self.card.code)

        UIElement.base_card.save_cards()
