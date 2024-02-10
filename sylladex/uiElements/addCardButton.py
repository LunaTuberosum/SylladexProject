import pygame as pg

from uiElement import UIElement, Apperance


class AddCardButton(UIElement):
    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            'AddCard',
            11
        )

        self.apperance = Apperance(
            self,
            [74, 74],
            [[64, 64], 'ModusBackground', [2, 8]],
            [[64, 64], 'ModusAccent', [8, 2]],
            colorKey=True,
            image=[
                [f'sylladex/uiElements/asset/{UIElement.get_modus()}/ADD_CARD_ICON.png', [
                    6, 0], 'ModusBackground']
            ]
        )

        self.tool_tip_text = "Captchalogue a Card to your Sylladex"
        self.hovering = False
        self.writing = False

    def reload_image(self):
        if self.writing:
            self.apperance.size_color_pos = [
                [[68, 68], '#FFFFFF', [0, 6]],
                [[68, 68], '#FFFFFF', [6, 0]],
                [[64, 64], 'ModusBackground', [2, 8]],
                [[64, 64], 'ModusAccent', [8, 2]],
            ]

        else:
            self.apperance.size_color_pos = [
                [[64, 64], 'ModusBackground', [2, 8]],
                [[64, 64], 'ModusAccent', [8, 2]],
            ]

        if not self.hovering:

            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/ADD_CARD_ICON.png', [
                        8, 2], 'ModusBackground']
                ])

        else:

            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/ADD_CARD_ICON_HOVER.png', [
                        8, 2], 'ModusForeground']
                ])

    def hover(self):
        if self.writing == True:
            return
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        super().no_hover()
        if self.writing == True:
            return
        self.hovering = False
        self.reload_image()

    def on_click(self):
        for _card in UIElement.get_ui_elem('CardList').get_list():
            if _card.writing == True:
                self.writing = False
                _card.writing = False
                self.reload_image()
                _card.empty = True
                _card.redraw_card()
                self.tool_tip_text = "Captchalogue a Card to your Sylladex"

                for child in _card.children:
                    child.kill()
                _card.children.clear()
                return
            if _card.code == '-':
                if _card.interactable == True:
                    self.writing = True
                    self.reload_image()
                    _card.start_card()
                    self.tool_tip_text = "Stop adding a Card to your Sylladex"

                    return
                else:
                    UIElement.get_ui_elem('PopUp')('Empty card not in view')

                    return
        UIElement.get_ui_elem('PopUp')("You have no empty cards")
