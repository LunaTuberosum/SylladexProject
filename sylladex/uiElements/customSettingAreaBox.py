import pygame as pg

from uiElement import UIElement, Apperance


class CustomSettingAreaBox(UIElement):
    def __init__(self, x: int, y: int, section: str, job: str):

        self.section = section
        self.job = job

        super().__init__(
            x,
            y,
            f'CustomSettingAreaBox ({self.section})',
            2
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        if self.section == "WEAPONKINDS":
            self.apperance = Apperance(
                self,
                [280, 102],
                [[274, 24], '#1C4587', [6, 6]],
                [[274, 24], '#3C78D8', [0, 0]],
                [[24, 24], '#C9DAF8', [0, 0]],
                [[106, 24], '#C9DAF8', [72, 0]],
                [[48, 24], '#C9DAF8', [226, 0]],
                colorKey=True,
                texts=[
                    ['NAME', [48, 12], 'center', '#000000'],
                    ['TYPE', [202, 12], 'center', '#000000']]
            )

        elif self.section == "ACTIONS":
            self.apperance = Apperance(
                self,
                [306, 102],
                [[300, 96], '#1C4587', [6, 6]],
                [[300, 96], '#3C78D8', [0, 0]],
                [[108, 24], '#C9DAF8', [0, 0]],
                [[48, 24], '#C9DAF8', [156, 0]],
                [[48, 24], '#C9DAF8', [252, 0]],
                [[300, 48], '#C9DAF8', [0, 48]],
                colorKey=True,
                texts=[
                    ['COST', [132, 12], 'center', '#000000'],
                    ['DMG', [228, 12], 'center', '#000000'],
                    ['ACTION DESCRPTION', [150, 36], 'center', '#000000']
                ]
            )

        elif self.section == "TRAITS":
            self.apperance = Apperance(
                self,
                [306, 102],
                [[300, 72], '#1C4587', [6, 6]],
                [[300, 72], '#3C78D8', [0, 0]],
                [[300, 48], '#C9DAF8', [0, 24]],
                colorKey=True,
                texts=[
                    [f'{self.job.upper()} DESCRIPTION', [132, 12],
                     'center', '#000000'],
                ]
            )
