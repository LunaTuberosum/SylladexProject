import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ScrollBar(pg.sprite.Sprite):
    selected = False

    def __init__(self):
        super().__init__()

        UIBase.add_toGroup(self)
        UIBase.uiLayers.change_layer(self, 1)

        if len(UIBase.CardList.listObj) == 0:
            size = 0
        else:
            if len(UIBase.CardList.listObj) > 9:
                sections = 625 / len(UIBase.CardList.listObj) 
                size = sections * 8
            else:
                size = 0
        self.image = pg.Surface((23, size))
        self.image.fill((255, 0, 220))
        self.rect = pg.Rect(273, 196, 23, size)

        self.rectTemp = self.rect.y

    def on_click(self):
        self.selected = True 
        self.image.fill((255, 97, 220))

    def move_bar(self, pos):
        checkNum = 625 / len(UIBase.CardList.listObj)
        self.rect.y = pos[1]
        if self.rect.y < 196:
            self.rect.y = 196
            for cardItem in UIBase.CardList.listObj:
                cardItem.rect.y = 196 + (70 * UIBase.CardList.listObj.index(cardItem))

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for cardItem in UIBase.CardList.listObj:
                cardItem.rect.y = 196 - (70 * ((len(UIBase.CardList.listObj)-9) - UIBase.CardList.listObj.index(cardItem)))

        else:
            tempNum = checkNum
            allChecks = []
            for newCheck in range(0, len(UIBase.CardList.listObj)-9):
                allChecks.append(tempNum + 196)
                tempNum += checkNum

            for check in allChecks:
                if self.rect.y >= check:

                    if UIBase.CardList.listObj[0].rect.y > 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.CardList.listObj:
                            cardItem.rect.y -= 70
                            for child in cardItem.children:
                                child.rect.y -= 70
                
                if self.rect.y <= check:

                    if UIBase.CardList.listObj[0].rect.y < 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.CardList.listObj:
                            cardItem.rect.y += 70
                            for child in cardItem.children:
                                child.rect.y += 70
                

    def move_bar_wheel(self, rel):
        checkNum = 625 / len(UIBase.CardList.listObj)
        self.rect.y += rel * 10
        if self.rect.y < 196:
            self.rect.y = 196
            for cardItem in UIBase.CardList.listObj:
                cardItem.rect.y = 196 + (70 * UIBase.CardList.listObj.index(cardItem))

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for cardItem in UIBase.CardList.listObj:
                cardItem.rect.y = 196 - (70 * ((len(UIBase.CardList.listObj)-9) - UIBase.CardList.listObj.index(cardItem)))

        else:
            tempNum = checkNum
            allChecks = []
            for newCheck in range(0, len(UIBase.CardList.listObj)-9):
                allChecks.append(tempNum + 196)
                tempNum += checkNum

            for check in allChecks:
                if self.rect.y >= check:

                    if UIBase.CardList.listObj[0].rect.y > 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.CardList.listObj:
                            cardItem.rect.y -= 70
                            for child in cardItem.children:
                                child.rect.y -= 70

                if self.rect.y <= check:

                    if UIBase.CardList.listObj[0].rect.y < 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.CardList.listObj:
                            cardItem.rect.y += 70
                            for child in cardItem.children:
                                child.rect.y += 70