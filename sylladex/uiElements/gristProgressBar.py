import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristProgressBar(UIBase):
    def __init__(self, parent):
        self.parent = parent
        self.prevAmount = self.parent.children[0].text

        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.GristCacheLimit):
                self.progress = int(self.parent.children[0].text) / int(elem.limitNum)
                break

        super().__init__(self.parent.rect.x+59, self.parent.rect.y+30, (99*self.progress,12), "surfaceRect", True, (67,178,222))

    def update(self):
        if self.parent.children[0].text != self.prevAmount:
            self.prevAmount = self.parent.children[0].text
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.GristCacheLimit):
                    if self.parent.children[0].text == '':
                        self.progress = 0
                        break
                    elif int(self.parent.children[0].text) > int(elem.limitNum):
                        self.parent.children[0].text = elem.limitNum
                        self.progress = int(self.parent.children[0].text) / int(elem.limitNum)
                        break

                    else:
                        self.progress = int(self.parent.children[0].text) / int(elem.limitNum)
                        break

            self.image = pg.Surface((99*self.progress, 12))
            self.image.fill((76,178,222))
        
