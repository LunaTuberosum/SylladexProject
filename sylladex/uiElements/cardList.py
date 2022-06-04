### 9 items can fit before scroll
import pygame as pg
import pickle

from sylladex.uiElements.baseUI import UIBase


class CardList(UIBase):
    children = []

    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, image, 'CardList', True)
        self.uiLayers.change_layer(self, -1)
        
    def add_toList(self):
        self.children.append(UIBase.ListObject())
        card = self.children[len(self.children)-1]
        UIBase.add_toGroup(card)
        UIBase.uiLayers.change_layer(card, -1)
        self.place_list()

    def remove_fromList(self, TextField):
        if self.children[len(self.children)-1].empty == True:
            self.children[len(self.children)-1].kill()
            self.children.remove(self.children[len(self.children)-1])
        else:
            UIBase.PopUp("You can only remove empty cards. Eject cards first")
            UIBase.TextField.text = str(len(self.children))
            UIBase.TextField.draw()
            return
        
    def save_list(self):
        UIBase.ConsoleMessage('Saved List')
        tempList = []
        for card in self.children:
            tempList.append([card.name, card.code, card.tier, card.empty])

        with open('sylladex/uiElements/data/uiList.plk', 'wb') as saveList:
            pickle.dump(tempList, saveList, -1)

    def load_list(self):
        with open('sylladex/uiElements/data/uiList.plk', 'rb') as saveList:
            tempList = pickle.load(saveList)

        self.children.clear()

        for card in tempList:
            obj = UIBase.ListObject()
            obj.name = card[0]
            obj.code = card[1]
            obj.tier = card[2]
            obj.empty = card[3]
            self.children.append(obj)
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.TextField) and elem.job == 'numOfCards':
                elem.text = str(len(self.children))
                elem.draw()
                elem.no_hover()

    def start_list(self):
        self.load_list()
        for card in self.children:
            UIBase.add_toGroup(card)
            UIBase.uiLayers.change_layer(card, -1)
        self.place_list()

    def place_list(self):
        offset = 70
        for card in self.children:
            
            card.rect.y = 127 + offset
            offset += 70
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.ScrollBar):
                UIBase.remove_fromGroup(elem)
                elem.kill()
        UIBase.ScrollBar()