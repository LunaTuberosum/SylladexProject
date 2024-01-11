import pygame as pg

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
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 36)

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

        elif len(self.card.children[2].text) == 0:
            UIElement.get_ui_elem('PopUp')(
                'Codes must be a 8 characters long')
            return

        if int(self.card.children[2].text) > 16:
            UIElement.get_ui_elem('PopUp')(
                "Tier can be no higher than 16")
            return
        elif int(self.card.children[2].text) == 0:
            UIElement.get_ui_elem('PopUp')(
                "Tier must be at least 1")
            return

        self.card.writing = False
        _id = self.card.code_data.cardID
        UIElement.CodeDatabase.read_code(
            self.card.children[0].text, self.card.children[1].text, self.card.children[2].text, self.card)
        self.card.code_data.cardID = _id

        if self.card.capta_card:
            self.card.capta_card.code_data = self.card.code_data

        self.card.redraw_card()
        self.card.empty = False
        for child in self.card.children:
            child.kill()
        self.card.children.clear()

        UIElement.get_ui_elem('CardList').save_list()
        _add = UIElement.find_current_ui('AddCardButton')
        _add.writing = False
        _add.reload_image()
