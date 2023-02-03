import pygame as pg

from baseUI import UIBase, Apperance


class GristCacheLimit(UIBase):
    def __init__(self):
        super().__init__(212, 642, 'GristCacheLimit', 0)

        self.limitNum = '20480'

        self.apperance = Apperance(
            self, 
            (290, 42),
            [[284, 36], '#999999', [6, 6]], 
            [[182, 36], '#C4C4C4', [0, 0]], 
            [[102, 36], '#EFEFEF', [182, 0]], 
            colorKey = True, 
            texts = [
                ['CACHE LIMIT', [92, 19], 'center', '#000000', ["sylladex/uiElements/asset/MISC/fontstuck.ttf", 16]],
                [self.limitNum, [233, 18], 'center', '#42B2DE', ["sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 32]]
                ]
            )

        self.toolTipText = 'The amount of each grist you can hold based on your Rung'

    def update(self):
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('GristInfoBox')):
                if elem.children[0].active == False and int(elem.children[0].text) > int(self.limitNum):
                    elem.children[0].text = self.limitNum
                    elem.children[0].exit_field()