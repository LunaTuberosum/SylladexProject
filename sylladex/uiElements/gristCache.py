import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristCache(UIBase):
    def __init__(self, x):
        super().__init__(x, 626, (719,452), "GRIST_CACHE.png", True)

        self.children = []

        self.children.append(UIBase.GristCacheLimit(x))
        self.children.append(UIBase.GristInfoBox(334, 692, 'Build'))
        self.children.append(UIBase.GristInfoBox(510, 692, 'Shale'))
        self.children.append(UIBase.GristInfoBox(686, 692, 'Ruby'))
        self.children.append(UIBase.GristInfoBox(862, 692, 'Cobalt'))

        # self.children.append(UIBase.GristInfoBox(334, 789))
        # self.children.append(UIBase.GristInfoBox(510, 789))
        # self.children.append(UIBase.GristInfoBox(686, 789))
        # self.children.append(UIBase.GristInfoBox(862, 789))

        # self.children.append(UIBase.GristInfoBox(334, 885))
        # self.children.append(UIBase.GristInfoBox(510, 885))
        # self.children.append(UIBase.GristInfoBox(686, 885))
        # self.children.append(UIBase.GristInfoBox(862, 885))

        # self.children.append(UIBase.GristInfoBox(334, 982))
        # self.children.append(UIBase.GristInfoBox(510, 982))
        # self.children.append(UIBase.GristInfoBox(686, 982))
        # self.children.append(UIBase.GristInfoBox(862, 982))

    def repositionChildren(self):

        self.children[0].rect.x = self.rect.x+212