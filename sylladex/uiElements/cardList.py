### 9 items can fit before scroll
import pygame as pg
import pickle

from baseUI import UIBase
from ..captchalogueCards.baseCard import BaseCard


class CardList(UIBase):
    children = []

    def __init__(self, x, y, size):
        super().__init__(x, y, size, 'CardList', '#A4A4A4')
        self.uiLayers.change_layer(self, -1)
    
    @classmethod
    def add_toList(cls):
        cls.children.append(UIBase.get_uiElem('ListObject')())
        card = cls.children[len(cls.children)-1]
        UIBase.add_toGroup(card)
        UIBase.uiLayers.change_layer(card, -1)
        cls.place_list()
        cls.save_list()

    @classmethod
    def remove_fromList(cls, TextField):
        if cls.children[len(cls.children)-1].empty == True:
            cls.children[len(cls.children)-1].kill()
            cls.children.remove(cls.children[len(cls.children)-1])
            cls.save_list()
        else:
            UIBase.get_uiElem('PopUp')("You can only remove empty cards. Eject cards first")
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('TextField')) and elem.job == 'numOfCards':
                    elem.text = str(len(cls.children))
                    elem.draw()
                    elem.no_hover()
            return
    
    @classmethod
    def save_list(cls):
        UIBase.get_uiElem('ConsoleMessage')('Saved List')
        tempList = []
        for card in cls.children:
            tempList.append([card.codeData, card.empty])

        with open('sylladex/uiElements/data/uiList.plk', 'wb') as saveList:
            pickle.dump(tempList, saveList, -1)

    @classmethod
    def load_list(cls):
        with open('sylladex/uiElements/data/uiList.plk', 'rb') as saveList:
            tempList = pickle.load(saveList)

        cls.children.clear()

        for card in tempList:
            obj = UIBase.get_uiElem('ListObject')()

            
            if card[0]:
                obj.codeData = card[0]

                for _card in BaseCard.get_cardGroup():
                    if _card.codeData == obj.codeData:
                        obj.captaCard = _card
                        break
                obj.redraw_card('#FFFFFF')

            obj.empty = card[1]
            cls.children.append(obj)

        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('TextField')) and elem.job == 'numOfCards':
                elem.text = str(len(cls.children))
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
            if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                UIBase.remove_fromGroup(elem)
                elem.kill()
        UIBase.get_uiElem('ScrollBar')()