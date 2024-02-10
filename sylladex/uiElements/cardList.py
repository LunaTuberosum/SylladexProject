# 9 items can fit before scroll
import json
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
            11
        )

        self.apperance = Apperance(
            self,
            [249, 625],
            [[249, 625], '#A4A4A4', [0, 0]],
        )

        self.start_list()

    def remove_self(self):
        for _card in CardList.get_list():
            UIElement.remove_from_group(_card)

    @classmethod
    def get_list(cls):
        return cls.__list

    @classmethod
    def add_multi_to_list(cls):
        _num = int(UIElement.find_current_ui(
            'TextField', 'TextField (numOfCards)').text)
        _dif = _num - len(cls.get_list())

        if _dif < 0:
            for i in range(abs(_dif)):
                cls.remove_from_list()
        else:
            for i in range(_dif):
                cls._add_to_list()

        cls.save_list()
        UIElement.find_current_ui('CardList').place_list()
        UIElement.find_current_ui('ScrollBar').update_size()
        UIElement.find_current_ui('ScrollBar').rect.y = 196

    @classmethod
    def _add_to_list(cls):
        cls.get_list().append(UIElement.get_ui_elem('ListObject')())

    @classmethod
    def remove_from_list(cls):
        if cls.get_list()[len(cls.get_list())-1].empty == True:
            cls.get_list()[len(cls.get_list())-1].kill()
            cls.get_list().remove(cls.get_list()[len(cls.get_list())-1])
        else:
            UIElement.get_ui_elem('PopUp')(
                "You can only remove empty cards. Eject cards first")
            for _elem in UIElement.get_group('ui'):
                if isinstance(_elem, UIElement.get_ui_elem('TextField')) and _elem.job == 'numOfCards':
                    _elem.text = str(len(cls.get_list()))
                    _elem.reload_text()
            return

    @classmethod
    def save_list(cls):
        _card_list = {}

        for _index, _card in enumerate(cls.get_list()):
            _card_list[_index + 1] = {'name': '-', 'code': ''}
            _card_data = _card_list[_index + 1]

            _card_data['name'] = _card.name
            _card_data['code'] = _card.code

        _new_card_list = json.dumps(_card_list, indent=4)

        with open('sylladex/uiElements/data/cardList.json', 'w') as _card_list_file:
            _card_list_file.write(_new_card_list)

        UIElement.get_ui_elem('ConsoleMessage')('Saved List')

    @classmethod
    def load_list(cls):
        with open('sylladex/uiElements/data/cardList.json', 'r') as _card_list_file:
            _card_list = json.load(_card_list_file)

        cls.get_list().clear()

        for _card_num in _card_list:
            _card = _card_list[_card_num]
            _obj = UIElement.get_ui_elem('ListObject')()

            _obj.code = _card['code']
            _obj.name = _card['name']

            for _c in UIElement.base_card.get_cards():
                if _c.code_data.code == _obj.code:
                    _obj.capta_card = _c

            _obj.redraw_card()
            cls.get_list().append(_obj)

        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem('TextField')) and _elem.job == 'numOfCards':
                _elem.text = str(len(cls.get_list()))
                _elem.reload_text()
                break

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
