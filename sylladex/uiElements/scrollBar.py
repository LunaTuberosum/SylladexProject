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
            size = 0
        else:
            if len(self.itemList) > 9:
                sections = 625 / len(self.itemList) 
                size = sections * 8
            else:
                size = 0
        self.image = pg.Surface((23, size))
        self.image.fill((255, 0, 220))
        self.rect = pg.Rect(273, 196, 23, size)

        self.rectTemp = self.rect.y

    def on_click(self):
        self.selected = True 

    def move_bar(self, rel, pos):
        checkNum = 625 / len(self.itemList)
        self.rect.y = pos[1]
        if self.rect.y < 196:
            self.rect.y = 196
            for cardItem in self.itemList:
                cardItem.rect.y = 196 + (70 * self.itemList.index(cardItem))

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for cardItem in self.itemList:
                cardItem.rect.y = 196 - (70 * ((len(self.itemList)-9) - self.itemList.index(cardItem)))

        else:
            tempNum = checkNum
            allChecks = []
            for newCheck in range(0, len(self.itemList)-9):
                allChecks.append(tempNum + 196)
                tempNum += checkNum

            for check in allChecks:
                if self.rect.y >= check:

                    if self.itemList[0].rect.y > 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in self.itemList:
                            cardItem.rect.y -= 70
                
                if self.rect.y <= check:

                    if self.itemList[0].rect.y < 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in self.itemList:
                            cardItem.rect.y += 70