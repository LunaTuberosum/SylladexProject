### 9 items can fit before scroll
import pygame as pg
import pickle

from uiElement import UIElement, Apperance
from ..captchalogueCards.baseCard import BaseCard


class CardList(UIElement):
    __list = []

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            'CardList', 
            3)

        self.apperance = Apperance(
            self,
            [249, 649],
            [[249, 649], '#A4A4A4', [0, 0]], 
        )

        self.start_list()

    @classmethod
    def get_list(cls):
        return cls.__list
        
    @classmethod
    def add_to_list(cls):
        cls.get_list().append(UIElement.get_ui_elem('ListObject')())
        _card = cls.get_list()[len(cls.get_list())-1]
        UIElement.add_to_group(_card)
        cls.save_list()
        UIElement.find_current_ui('CardList').place_list()

    @classmethod
    def remove_from_list(cls):
        if cls.get_list()[len(cls.get_list())-1].empty == True:
            cls.get_list()[len(cls.get_list())-1].kill()
            cls.get_list().remove(cls.get_list()[len(cls.get_list())-1])
            cls.save_list()
        else:
            UIElement.get_ui_elem('PopUp')("You can only remove empty cards. Eject cards first")
            for _elem in UIElement.get_group('ui'):
                if isinstance(_elem, UIElement.get_ui_elem('TextField')) and _elem.job == 'numOfCards':
                    _elem.text = str(len(cls.get_list()))
                    _elem.exit_field()
            return

    @classmethod        
    def save_list(cls):
        UIElement.get_ui_elem('ConsoleMessage')('Saved List')
        _tempList = []
        for _card in cls.get_list():
            _tempList.append([_card.code_data, _card.empty])

        with open('sylladex/uiElements/data/uiList.plk', 'wb') as _save_list:
            pickle.dump(_tempList, _save_list, -1)

    @classmethod
    def load_list(cls):
        with open('sylladex/uiElements/data/uiList.plk', 'rb') as _save_list:
            _tempList = pickle.load(_save_list)

        cls.get_list().clear()

        for _card in _tempList:
            obj = UIElement.get_ui_elem('ListObject')()

            
            if _card[0]:
                obj.code_data = _card[0]
                obj.redraw_card()

            obj.empty = _card[1]
            cls.get_list().append(obj)

        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem('TextField')) and _elem.job == 'numOfCards':
                _elem.text = str(len(cls.get_list()))
                _elem.exit_field()
 
    @classmethod
    def start_list(cls):
        cls.load_list()
        UIElement.find_current_ui('CardList').place_list()

    def place_list(self):
        _offset = 70
        for _card in self.get_list():
            
            _card.rect.x = self.rect.x
            _card.rect.y = 127 + _offset
            _offset += 70