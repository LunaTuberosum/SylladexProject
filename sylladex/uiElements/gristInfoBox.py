import pygame as pg

from uiElement import UIElement, Apperance


class GristInfoBox(UIElement):
    def __init__(self, x: int, y: int, grist: str):
        super().__init__(x, y, 'GristInfoBox', 1)

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.grist = grist

        self.apperance = Apperance(
            self,
            [170, 90],
            [[164, 84], '#999999', [6, 6]],
            [[164, 84], '#C4C4C4', [0, 0]],
            [[52, 84], '#D9D9D9', [0, 0]],
            [[111, 23], '#D9D9D9', [53, 0]],
            [[111, 23], '#D9D9D9', [53, 24]],
            [[111, 36], '#EFEFEF', [53, 48]],
            colorKey=True,
            image=[
                f'sylladex/uiElements/asset/GRIST/{self.grist}.png', [6, 22]],
            texts=[[self.grist, [111, 11], 'center', '#000000']]
        )

        self.add_child(
            UIElement.get_ui_elem('TextField')(
                53,
                48,
                [111, 36],
                f'{self.grist}NumBox',
                f'Let\'s you alter how much {self.grist} grist you have',
                5,
                startLayer=1,
                textColor=(67, 178, 222),
                textType='Num',
                baseColors=[(239, 239, 239), (199, 199, 199), (179, 179, 179)],
                align='center',
                exitCommand=UIElement.find_current_ui('GristCache').save_cache
            )
        )
        self.add_child(
            UIElement.get_ui_elem('GristProgressBar')(self)
        )
