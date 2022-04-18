import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCache(UIBase):
    def __init__(self, x):
        super().__init__(x, 626, (719,452), "GRIST_CACHE.png", True)

        self.children = []

        self.children.append(UIBase.GristCacheLimit(x))

        for index, grist in enumerate(['Build', 'Shale', 'Ruby', 'Cobalt', 'Chalk', 'Marble', 'Iron', 'Amber', 'Caulk', 'Tar', 'Uranium', 'Amethyst', 'Garnet', 'Artifact', 'Zillium', 'Diamond']):
            if index < 4: self.children.append(UIBase.GristInfoBox((self.rect.x+9)+(174*index), 692, grist))
            elif index < 8: self.children.append(UIBase.GristInfoBox((self.rect.x+9)+(174*(index-4)), 789, grist))
            elif index < 12: self.children.append(UIBase.GristInfoBox((self.rect.x+9)+(174*(index-8)), 885, grist))
            elif index < 16: self.children.append(UIBase.GristInfoBox((self.rect.x+9)+(174*(index-12)), 982, grist))

    def repositionChildren(self):

        for index, child in enumerate(self.children):
            if index == 0: child.rect.x = self.rect.x+212
            elif index < 5: child.rect.x = (self.rect.x+9) + (174*(index - 1))
            elif index < 9: child.rect.x = (self.rect.x+9) + (174*(index - 5))
            elif index < 13: child.rect.x = (self.rect.x+9) + (174*(index - 9))
            elif index < 17: child.rect.x = (self.rect.x+9) + (174*(index - 13))

            if index > 0:
                child.children[0].rect.x = child.rect.x+53