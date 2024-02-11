import json
import pygame as pg

from uiElement import UIElement, Apperance


class ToggleButton(UIElement):
    def __init__(self, x: int, y: int, job: str, text: str, tool_tip_text: str, exit_command: object, start_state: bool = False):

        self.job = job
        self.text = text

        super().__init__(
            x,
            y,
            f'ToggleButton ({job}Toggle)',
            8
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/DisposableDroidBB.ttf", 18)

        self.apperance = Apperance(
            self,
            [30, 30],
            [[24, 24], '#1C4587', [6, 6]],
            [[24, 24], '#3C78D8', [0, 0]],
            colorKey=True,
            texts=[[self.text, [12, 12], 'center', '#000000']],
        )

        self.on = start_state
        self.hovering = False
        self.tool_tip_text = tool_tip_text

        self.exit_command = exit_command

    def update(self):
        if self.on:
            self.apperance.size_color_pos = [
                [[24, 24], '#1C4587', [6, 6]],
                [[24, 24], '#C9DAF8', [0, 0]],
            ]
        elif not self.hovering:
            self.apperance.size_color_pos = [
                [[24, 24], '#1C4587', [6, 6]],
                [[24, 24], '#3C78D8', [0, 0]],
            ]
        self.apperance.reload_apperance()

    def on_click(self):
        self.exit_command(self)

    def hover(self):
        if self.on == False:
            self.apperance.size_color_pos = [
                [[24, 24], '#1C4587', [6, 6]],
                [[24, 24], '#C9DAF8', [0, 0]],
            ]
            self.apperance.reload_apperance()

            self.hovering = True

    def no_hover(self):
        if self.on == False:
            self.apperance.size_color_pos = [
                [[24, 24], '#1C4587', [6, 6]],
                [[24, 24], '#3C78D8', [0, 0]],
            ]
            self.apperance.reload_apperance()

            self.hovering = False
