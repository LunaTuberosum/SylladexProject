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
    def add_multi_to_list(cls):
        _num = int(UIElement.find_current_ui(
            'TextField', 'TextField (numOfCards)').text)
        _dif = _num - len(cls.get_list())

        if _dif < 0:
            for i in range(abs(_dif)):
                cls.remove_from_list()
            cls.save_list()
            return

        for i in range(_dif):
            cls._add_to_list()

        cls.save_list()
        UIElement.find_current_ui('CardList').place_list()
        UIElement.find_current_ui('ScrollBar').update_size()

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
                    _elem.exit_field()
            return

    @classmethod
    def save_list(cls):
        _card_list = {}

        for _index, _card in enumerate(cls.get_list()):
            _card_list[_index + 1] = {'CodeData': {}, 'Empty': True}
            _card_data = _card_list[_index + 1]

            _card_data['CodeData']['name'] = _card.code_data.name
            _card_data['CodeData']['code'] = _card.code_data.code
            _card_data['CodeData']['tier'] = _card.code_data.tier

            _card_data['CodeData']['kind'] = _card.code_data.kind
            _card_data['CodeData']['grist'] = _card.code_data.grist
            _card_data['CodeData']['trait_1'] = _card.code_data.trait_1
            _card_data['CodeData']['trait_2'] = _card.code_data.trait_2
            _card_data['CodeData']['action_1'] = _card.code_data.action_1
            _card_data['CodeData']['action_2'] = _card.code_data.action_2
            _card_data['CodeData']['action_3'] = _card.code_data.action_3
            _card_data['CodeData']['action_4'] = _card.code_data.action_4

            _card_data['CodeData']['cardID'] = _card.code_data.cardID

            _card_data['Empty'] = _card.empty

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

            _obj.create_code_data(_card['CodeData'])

            _obj.empty = _card['Empty']
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
