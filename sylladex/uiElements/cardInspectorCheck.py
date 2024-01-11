from uiElement import Apperance, UIElement

import pygame as pg


class CardInspectorCheck(UIElement):

    def __init__(self, x: int, y: int, job: str, exit_command: object):
        super().__init__(
            x,
            y,
            f'CardInspectorCheck({job})',
            1000
        )

        self.apperance = Apperance(
            self,
            [24, 24],
            [[16, 16], '#434343', [4, 4]],
            [[12, 12], '#D8DDFF', [6, 6]],
            colorKey=True
        )

        self.job = job
        self.exit_command = exit_command

        self.selected = False

    def on_click(self):
        if self.selected == False:

            UIElement.find_current_ui('CardInspector').uncheck_all()

            self.selected = True
            self.apperance.size_color_pos = [
                [[16, 16], '#434343', [4, 4]]
            ]
            self.apperance.reload_apperance()
            self.exit_command(self)

        else:
            UIElement.find_current_ui('CardInspector').uncheck_all()
