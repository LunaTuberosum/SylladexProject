import json
import pygame as pg
import pickle

from uiElement import UIElement


class StackManager():
    stack = pg.sprite.LayeredUpdates()

    @classmethod
    def get_stack(cls) -> pg.sprite.LayeredUpdates:
        return cls.stack

    @classmethod
    def get_length(cls) -> int:
        return len(cls.stack)

    @classmethod
    def get_top_card(cls, situation: str) -> object:
        if situation == 'distance':
            for index, card in enumerate(cls.stack):
                if index == cls.get_length()-2:
                    return card

        elif situation == 'remove':
            for index, card in enumerate(cls.stack):
                if index == cls.get_length()-1:
                    return card

    @classmethod
    def add_to_stack(cls, card: object):
        cls.stack.add(card)
        cls.get_stack().change_layer(card, cls.get_length())

    @classmethod
    def remove_from_stack(cls, card: object):
        cls.stack.remove(card)
        for index, card in enumerate(cls.get_stack()):
            print(index, card.codeData.code)

    @classmethod
    def save_stack(cls):

        with open('sylladex/captchalogueCards/data/stackData.json', 'r') as _stack_data_file:
            _code_data = json.load(_stack_data_file)

        _code_list = {}

        for _index, _card in enumerate(StackManager.get_stack()):
            _code_list[_index + 1] = {'CodeData': {}}
            _code_data = _code_list[_index + 1]

            _code_data['CodeData']['name'] = _card.code_data.name
            _code_data['CodeData']['code'] = _card.code_data.code
            _code_data['CodeData']['tier'] = _card.code_data.tier

            _code_data['CodeData']['kind'] = _card.code_data.kind
            _code_data['CodeData']['grist'] = _card.code_data.grist
            _code_data['CodeData']['trait_1'] = _card.code_data.trait_1
            _code_data['CodeData']['trait_2'] = _card.code_data.trait_2
            _code_data['CodeData']['action_1'] = _card.code_data.action_1
            _code_data['CodeData']['action_2'] = _card.code_data.action_2
            _code_data['CodeData']['action_3'] = _card.code_data.action_3
            _code_data['CodeData']['action_4'] = _card.code_data.action_4

            _code_data['CodeData']['cardID'] = _card.code_data.cardID

        _new_stack_list = json.dumps(_code_list, indent=4)

        with open('sylladex/captchalogueCards/data/stackData.json', 'w') as _stack_list_file:
            _stack_list_file.write(_new_stack_list)

        UIElement.get_ui_elem('ConsoleMessage')('Saved Stack')

    @classmethod
    def load_stack(cls, all_cards: list):
        with open('sylladex/captchalogueCards/data/stackData.json', 'r') as _stack_data_file:
            _stack_data = json.load(_stack_data_file)

        for _code_num in _stack_data:
            _code = _stack_data[_code_num]['CodeData']
            _code_data = UIElement.CodeData(
                _code['name'], _code['code'], _code['tier'], _code['kind'], _code['grist'], _code['trait_1'], _code['trait_2'], _code['action_1'], _code['action_2'], _code['action_3'], _code['action_4'], _code['cardID'])

            for card in all_cards:
                if _code_data == card.code_data:
                    StackManager.add_to_stack(card)
                    break
        UIElement.get_ui_elem('ConsoleMessage')('Loaded Stack')
