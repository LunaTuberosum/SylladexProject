import pygame as pg

from uiElement import UIElement, Apperance


class CustomSettingSectionName(UIElement):
    def __init__(self, x: int, y: int, section: str):
        self.section = section
        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        super().__init__(
            x,
            y,
            f'CustomSettingSectionName ({self.section})',
            7
        )

        if self.section == 'ACTIONS':
            _text_value = 'CUSTOM MELEE ACTIONS'
        else:
            _text_value = 'CUSTOM ' + self.section

        self.apperance = Apperance(
            self,
            [186, 30],
            [[180, 24], '#1C4587', [6, 6]],
            [[180, 24], '#3C78D8', [0, 0]],
            colorKey=True,
            texts=[[_text_value, [90, 12], 'center', '#000000']])

        if self.section == "ACTIONS":
            self.cur_toggle = "ME"
        elif self.section == "TRAITS":
            self.cur_toggle = "1"
