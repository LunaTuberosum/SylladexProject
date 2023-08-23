import pygame as pg

from uiElement import UIElement, Apperance


class ToggleButton(UIElement):
    def __init__(self, x: int, y: int, job: str, text: str):

        self.job = job
        self.text = text

        super().__init__(
            x,
            y,
            f'ToggleButton ({job}Toggle)',
            2
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.apperance = Apperance(
            self,
            [30, 30],
            [[24, 24], '#1C4587', [6, 6]],
            [[24, 24], '#3C78D8', [0, 0]],
            colorKey=True,
            texts=[[self.text, [12, 12], 'center', '#000000']],
        )

        self.on = False
        self.hovering = False

    def check_if_toggle(self, section):
        for _elem in UIElement.get_group("ui"):
            if isinstance(_elem, UIElement.get_ui_elem("CustomSettingSectionName")) and _elem.section == section:
                if _elem.cur_toggle == self.text:
                    if self.on == True:
                        return
                    self.on = True
                    self.apperance.size_color_pos = [
                        [[24, 24], '#1C4587', [6, 6]],
                        [[24, 24], '#C9DAF8', [0, 0]],
                    ]
                else:
                    if self.on == False:
                        return
                    self.on = False
                    self.apperance.size_color_pos = [
                        [[24, 24], '#1C4587', [6, 6]],
                        [[24, 24], '#3C78D8', [0, 0]],
                    ]
                self.apperance.reload_apperance()

    def update(self):
        if self.job == "melee" or self.job == "ranged" or self.job == "magic":
            self.check_if_toggle("ACTIONS")
        elif self.job == "t1" or self.job == "t2" or self.job == "t3" or self.job == "t4":
            self.check_if_toggle("TRAITS")

    def on_click(self):
        if self.job == "melee" or self.job == "ranged" or self.job == "magic":
            for _elem in UIElement.get_group("ui"):
                if isinstance(_elem, UIElement.get_ui_elem("CustomSettingSectionName")) and _elem.section == "ACTIONS":
                    _elem.cur_toggle = self.text
                    _elem.apperance.kargs['texts'] = [[f"CUSTOM {(self.job).upper()} ACTIONS", [
                        90, 12], 'center', '#000000']]
                    _elem.apperance.reload_apperance()

        elif self.job == "t1" or self.job == "t2" or self.job == "t3" or self.job == "t4":
            for _elem in UIElement.get_group("ui"):
                if isinstance(_elem, UIElement.get_ui_elem("CustomSettingSectionName")) and _elem.section == "TRAITS":
                    _elem.cur_toggle = self.text

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
