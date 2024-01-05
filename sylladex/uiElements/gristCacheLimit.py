import pygame as pg

from uiElement import UIElement, Apperance


class GristCacheLimit(UIElement):
    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            'GristCacheLimit',
            1
        )

        self.limit_num = '20480'

        self.apperance = Apperance(
            self,
            (290, 42),
            [[284, 36], '#999999', [6, 6]],
            [[182, 36], '#C4C4C4', [0, 0]],
            [[102, 36], '#EFEFEF', [182, 0]],
            colorKey=True,
            texts=[
                ['CACHE LIMIT', [92, 19], 'center', '#000000', [
                    "sylladex/uiElements/asset/MISC/fontstuck.ttf", 32]],
                [self.limit_num, [233, 18], 'center', '#42B2DE', [
                    "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 32]]
            ]
        )

        self.tool_tip_text = 'The amount of each grist you can hold based on your Rung'

    def update(self):
        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem('GristInfoBox')):
                if _elem.children[0].active == False and int(_elem.children[0].text) > int(self.limit_num):
                    _elem.children[0].text = self.limit_num
                    _elem.children[0].exit_field()
