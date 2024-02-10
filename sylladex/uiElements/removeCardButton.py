import pygame as pg

from uiElement import UIElement, Apperance


class RemoveCardButton(UIElement):

    __eject = False

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            'RemoveCardButton',
            11
        )

        self.apperance = Apperance(
            self,
            [74, 74],
            [[64, 64], 'ModusBackground', [2, 8]],
            [[64, 64], 'ModusAccent', [8, 2]],
            colorKey=True,
            images=[
                [f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [
                    8, 2], 'ModusBackground']
            ])

        self.tool_tip_text = 'Eject a Card from your Sylladex'
        self.hovering = False

    def reload_image(self):
        if UIElement.get_ui_elem('RemoveCardButton').get_eject():
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
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON.png', [
                        8, 2], 'ModusBackground']
                ])

        else:

            self.apperance.change_images(
                [
                    [f'sylladex/uiElements/asset/{UIElement.get_modus()}/REMOVE_CARD_ICON_HOVER.png', [
                        8, 2], 'ModusForeground']
                ])

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
