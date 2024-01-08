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
            colorKey=True,
            image=[f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [6, 0]])

        self.tool_tip_text = 'Eject a Card from your Sylladex'
        self.hovering = False

    def reload_image(self):
        if self.hovering == False and UIElement.get_ui_elem('RemoveCardButton').get_eject() == False:
            self.apperance.change_image(
                f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [6, 0],)
        else:
            self.apperance.change_image(
                f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [6, 0])

    def hover(self):
        self.hovering = True
        self.reload_image()

    def no_hover(self):
        self.hovering = False
        self.reload_image()

    @classmethod
    def get_eject(cls):
        return cls.__eject

    @classmethod
    def change_eject(cls, eject):
        cls.__eject = eject

    def on_click(self):
        if UIElement.get_ui_elem('RemoveCardButton').get_eject() == False:
            self.tool_tip_text = 'Stop ejecting a Card from your Sylladex'
            UIElement.get_ui_elem('RemoveCardButton').change_eject(True)

        else:
            self.tool_tip_text = 'Eject a Card from your Sylladex'
            UIElement.get_ui_elem('RemoveCardButton').change_eject(False)
