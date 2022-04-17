### 9 items can fit before scroll
import pygame as pg
import pickle

from sylladex.uiElements.baseUI import UIBase


class CardList(UIBase):
    listObj = []

    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, image, True)
        self.uiLayers.change_layer(self, -1)
        
    def add_toList(self):
        self.listObj.append(UIBase.ListObject())
        card = self.listObj[len(self.listObj)-1]
        UIBase.add_toGroup(card)
        UIBase.uiLayers.change_layer(card, -1)
        self.place_list()

    def remove_fromList(self, TextField):
        if self.listObj[len(self.listObj)-1].empty == True:
            self.listObj[len(self.listObj)-1].kill()
            self.listObj.remove(self.listObj[len(self.listObj)-1])
        else:
            UIBase.PopUp("You can only remove empty cards. Eject cards first")
            UIBase.TextField.text = str(len(self.listObj))
            UIBase.TextField.draw()
            return
        
    def save_list(self):
        tempList = []
        for card in self.listObj:
            tempList.append([card.name, card.code, card.tier, card.empty])

        with open('sylladex/uiElements/data/uiData.plk', 'wb') as saveList:
            pickle.dump(tempList, saveList, -1)

    def load_list(self):
        with open('sylladex/uiElements/data/uiData.plk', 'rb') as saveList:
            tempList = pickle.load(saveList)

        self.listObj.clear()

        for card in tempList:
            obj = UIBase.ListObject()
            obj.name = card[0]
            obj.code = card[1]
            obj.tier = card[2]
            obj.empty = card[3]
            self.listObj.append(obj)
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.TextField):
                elem.text = str(len(self.listObj))
                elem.draw()
                elem.no_hover()

    def start_list(self):
        self.load_list()
        for card in self.listObj:
            UIBase.add_toGroup(card)
            UIBase.uiLayers.change_layer(card, -1)
        self.place_list()

    def place_list(self):
        offset = 70
        for card in self.listObj:
            
            card.rect.y = 127 + offset
            offset += 70
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, UIBase.ScrollBar):
                UIBase.uiElements.remove(elem)
                UIBase.uiLayers.remove(elem)
                elem.kill()
        UIBase.ScrollBar()