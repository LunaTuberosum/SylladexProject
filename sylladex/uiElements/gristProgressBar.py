import pygame as pg

from baseUI import UIBase, Apperance


class GristProgressBar(UIBase):
    def __init__(self, parent: object):
        self.parent = parent
        self.prevAmount = self.parent.children[0].text

        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('GristCacheLimit')):
                self.progress = int(self.parent.children[0].text) / int(elem.limitNum)
                break

        super().__init__(self.parent.rect.x+59, self.parent.rect.y+30, f'GristProgressBar ({self.parent.grist})', 0)

        self.apperance = Apperance(
            self,
            (99, 12),
            [[99*self.progress, 12], (67,178,222), [0,0]],
            colorKey=True
        )

    def update(self):
        if self.parent.children[0].text != self.prevAmount:

            if self.parent.children[0].text == '':
                self.prevAmount = 0
                
                self.progress = 0

            else: 
                self.prevAmount = self.parent.children[0].text

                print(int(self.parent.children[0].text) / int(UIBase.find_curUI('GristCacheLimit').limitNum))
                
                self.progress = int(self.parent.children[0].text) / int(UIBase.find_curUI('GristCacheLimit').limitNum)

            self.apperance.sizeColorPos = [
                [[99*self.progress, 12], (67,178,222), [0,0]]
                ]

            self.apperance.reload_apperance()
        
