import pygame as pg

from uiElement import Apperance, UIElement


class EscapeMenuOption(UIElement):
    def __init__(self, x: int, y: int, text: str, exit_command: object):

        super().__init__(
            x,
            y,
            f'EscapeMenuOption ({text})',
            1001
        )

        self.text = text
        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/DisposableDroidBB.ttf", 26)

        self.prefix = '> '
        self.big_prefix = '==> '

        self.color = '#1118ee'
        self.hover_color = '#551a8b'

        self.apperance = Apperance(
            self,
            [205, 50],
            colorKey=True,
            texts=[
                [self.prefix + self.text, [102, 25], 'center', self.color]
            ]
        )

        self.hovering = False
        self.exit_command = exit_command

    def hover(self):
        self.apperance.kwargs['texts'] = [
            [self.big_prefix + self.text, [102, 25], 'center', self.color]
        ]
        self.apperance.reload_apperance()

        self.hovering = True

    def no_hover(self):
        self.apperance.kwargs['texts'] = [
            [self.prefix + self.text, [102, 25], 'center', self.color]
        ]
        self.apperance.reload_apperance()

        self.hovering = False

    def on_click(self):
        self.apperance.kwargs['texts'] = [
            [self.big_prefix + self.text, [102, 25], 'center', self.hover_color]
        ]
        self.apperance.reload_apperance()

        self.exit_command()
