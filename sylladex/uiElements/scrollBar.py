import pygame as pg

from baseUI import UIBase


class ScrollBar(UIBase):
    selected = False

    def __init__(self):
        if len(UIBase.get_uiElem('CardList').children) == 0:
            size = 0
        else:
            if len(UIBase.get_uiElem('CardList').children) > 9:
                sections = 625 / len(UIBase.get_uiElem('CardList').children) 
                size = sections * 8
            else:
                size = 0

        super().__init__(273, 196, (23, size), 'ScrollBar', '#999999')

        self.rectTemp = self.rect.y

        self.hovering = False

    def hover(self):
        self.image.fill('#D9D9D9')
        self.hovering = True

    def no_hover(self):
        self.image.fill('#999999')
        self.hovering = False

    def on_click(self):
        self.selected = True 

    def move_bar(self, pos):
        checkNum = 625 / len(UIBase.get_uiElem('CardList').children)
        self.rect.y = pos[1]
        if self.rect.y < 196:
            self.rect.y = 196
            for cardItem in UIBase.get_uiElem('CardList').children:
                cardItem.rect.y = 196 + (70 * UIBase.get_uiElem('CardList').children.index(cardItem))
                if cardItem.children:
                    cardItem.place_children()

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for cardItem in UIBase.get_uiElem('CardList').children:
                cardItem.rect.y = 196 - (70 * ((len(UIBase.get_uiElem('CardList').children)-9) - UIBase.get_uiElem('CardList').children.index(cardItem)))
                if cardItem.children:
                    cardItem.place_children()

        else:
            tempNum = checkNum
            allChecks = []
            for newCheck in range(0, len(UIBase.get_uiElem('CardList').children)-9):
                allChecks.append(tempNum + 196)
                tempNum += checkNum

            for check in allChecks:
                if self.rect.y >= check:

                    if UIBase.get_uiElem('CardList').children[0].rect.y > 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.get_uiElem('CardList').children:
                            cardItem.rect.y -= 70
                            if cardItem.children:
                                cardItem.place_children()
                
                if self.rect.y <= check:

                    if UIBase.get_uiElem('CardList').children[0].rect.y < 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.get_uiElem('CardList').children:
                            cardItem.rect.y += 70
                            if cardItem.children:
                                cardItem.place_children()
                

    def move_bar_wheel(self, rel):
        checkNum = 625 / len(UIBase.get_uiElem('CardList').children)
        self.rect.y += rel * 10
        if self.rect.y < 196:
            self.rect.y = 196
            for cardItem in UIBase.get_uiElem('CardList').children:
                cardItem.rect.y = 196 + (70 * UIBase.get_uiElem('CardList').children.index(cardItem))
                if cardItem.children:
                    cardItem.place_children()

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for cardItem in UIBase.get_uiElem('CardList').children:
                cardItem.rect.y = 196 - (70 * ((len(UIBase.get_uiElem('CardList').children)-9) - UIBase.get_uiElem('CardList').children.index(cardItem)))
                if cardItem.children:
                    cardItem.place_children()

        else:
            tempNum = checkNum
            allChecks = []
            for newCheck in range(0, len(UIBase.get_uiElem('CardList').children)-9):
                allChecks.append(tempNum + 196)
                tempNum += checkNum

            for check in allChecks:
                if self.rect.y >= check:

                    if UIBase.get_uiElem('CardList').children[0].rect.y > 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.get_uiElem('CardList').children:
                            cardItem.rect.y -= 70
                            if cardItem.children:
                                cardItem.place_children()

                if self.rect.y <= check:

                    if UIBase.get_uiElem('CardList').children[0].rect.y < 196 - (70 * allChecks.index(check)):
                        
                        for cardItem in UIBase.get_uiElem('CardList').children:
                            cardItem.rect.y += 70
                            if cardItem.children:
                                cardItem.place_children()