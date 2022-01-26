import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ScrollBar(pg.sprite.Sprite):
    selected = False

    def __init__(self, cardList):
        super().__init__()

        UIBase.add_toGroup(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.itemList = cardList

        if len(self.itemList) == 0:
            sections = 0
        else:
        
            sections = 631 / len(self.itemList)
        size = sections * 9
        self.image = pg.Surface((23, size))
        self.image.fill((255, 0, 220))
        self.rect = pg.Rect(273, 196, 23, size)

        self.rectTemp = self.rect.y

    def on_click(self):
        self.selected = True 

    def move_bar(self, mousePos):
        checkNum = 631 / len(self.itemList)
        # checkNum = startNum * (len(self.itemList)- 9 )
        # self.rectTemp += rel[1]
        if mousePos[1] >= self.rect.y + checkNum:
            self.rect.y += checkNum

            for item in self.itemList:
                item.rect.y -= 70

        elif mousePos[1] <= self.rect.y - checkNum:
            self.rect.y -= checkNum

            for item in self.itemList:
                item.rect.y += 70