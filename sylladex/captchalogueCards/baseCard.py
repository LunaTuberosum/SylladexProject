import json
import pickle
import pygame as pg

import math

from uiElement import UIElement, Apperance
from .cardOutline import CardOutline

from .stackManager import StackManager


class BaseCard(pg.sprite.Sprite):
    __cards = pg.sprite.Group()
    grabbed_card = pg.sprite.GroupSingle()

    def __init__(
            self,
            pos: list,
    ):
        super().__init__(BaseCard.get_cards())

        self.hovering = False
        self.selected = False

        self.code_data = UIElement.code_data()

        self.rect = pos

        self.apperance = Apperance(
            self,
            [90, 122],
            colorKey=True,
            images=[
                [f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png', [
                    5, 6]],
            ]
        )

        self.cardID = BaseCard.get_length()

        self.prevAnimTick = 0

        self.shaking = False
        self.highlight = False
        self.prev_pos = None

    def create_code_data(self, inputs: dict):
        self.code_data.name = inputs['name']
        self.code_data.code = inputs['code']
        self.code_data.tier = inputs['tier']
        self.code_data.kind = inputs['kind']
        self.code_data.grist = inputs['grist']
        self.code_data.trait_1 = inputs['trait_1']
        self.code_data.trait_2 = inputs['trait_2']
        self.code_data.action_1 = inputs['action_1']
        self.code_data.action_2 = inputs['action_2']
        self.code_data.action_3 = inputs['action_3']
        self.code_data.action_4 = inputs['action_4']
        self.code_data.cardID = inputs['cardID']

    def kind_image(self) -> list:
        if self.selected == True:
            return [UIElement.code_database.find_kind_image(
                self.code_data.kind), [15, 25]]
        else:
            return [UIElement.code_database.find_kind_image(
                self.code_data.kind), [10, 31]]

    def hover(self):
        self.hovering = True
        self.redraw_card()

    def no_hover(self):
        self.hovering = False
        self.redraw_card()

    def on_middle_click(self):
        _elem = UIElement.find_current_ui('CardInspector')
        if _elem:
            UIElement.remove_from_group(_elem)
        UIElement.get_ui_elem('CardInspectorCheck').checks = []

        UIElement.get_ui_elem('CardInspector')(self.code_data)

    def on_click(self):
        BaseCard.grabbed_card.add(self)

        if UIElement.get_modus() == 'STACK':
            for card in StackManager.get_stack():
                if card == self and self == StackManager.get_top_card():
                    StackManager.remove_from_stack(self)
                    self.selected = True
                    return

        self.selected = True
        self.redraw_card()

    def on_release(self):
        BaseCard.grabbed_card.empty()

        _elem = UIElement.find_current_ui('CardList')
        if _elem and self.rect.colliderect(_elem):
            for _card in _elem.get_list():
                if _card.code_data == self.code_data:
                    _card.capta_card = None
                    _card.code_data.cardID = 0
                    _card.redraw_card()
                    break
            _elem.save_list()
            BaseCard.remove_card_from_group(self)

            CardOutline.destroy_outline()
            return

        self.selected = False
        self.redraw_card()

        self.combine()

        CardOutline.destroy_outline()

    def redraw_card(self):
        if self.highlight:
            self.apperance.change_images(
                [
                    [f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_HIGHLIGHT.png', [
                        5, 6]],
                    self.kind_image()
                ])

        elif self.selected:
            self.apperance.change_images(
                [
                    [f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png', [
                        0, 0]],
                    self.kind_image()
                ])

        elif self.hovering:
            self.apperance.change_images(
                [
                    [f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_HIGHLIGHT.png', [
                        5, 6]],
                    self.kind_image()
                ])

        else:
            self.apperance.change_images(
                [
                    [f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png', [
                        5, 6]],
                    self.kind_image()
                ])

    def combine(self):
        for outline in CardOutline.current_outline:
            if outline.rect.colliderect(self.rect):
                self.rect.topleft = outline.rect.topleft
                if StackManager.get_length() > 0:
                    StackManager.add_to_stack(self)
                else:
                    StackManager.add_to_stack(outline.focused_card)
                    StackManager.add_to_stack(self)

                BaseCard.save_cards()
                StackManager.save_stack()

    def move(self, velocity):
        if StackManager.get_stack().has(self):
            return
        self.rect.move_ip(velocity)

        self.find_distance()

    def find_distance(self):
        all_dis = []

        for card in BaseCard.get_cards():
            if UIElement.get_modus() == 'STACK':
                if StackManager.get_length() > 0:
                    if card == StackManager.get_top_card():
                        if CardOutline.current_outline:
                            CardOutline.move_outline(card)
                        else:
                            CardOutline(card)
                        return

                x = self.rect.x
                y = self.rect.y
                x2 = card.rect.x
                y2 = card.rect.y
                distance = [int(math.sqrt((x2 - x)**2+(y2 - y)**2)), card]

                if distance[0] != 0:
                    all_dis.append(distance)

        if len(all_dis) == 0:
            return
        for index, d in enumerate(all_dis):
            if index == 0:
                possiable_card = d
            if d[0] < possiable_card[0]:
                possiable_card = d

        if CardOutline.current_outline:
            CardOutline.move_outline(possiable_card[1])
        else:
            CardOutline(possiable_card[1])

    def update(self):
        if self.selected == True:
            _elem = UIElement.find_current_ui('CardList')
            if _elem and self.rect.colliderect(_elem):
                if self.prev_pos:

                    if self.prev_pos == self.rect.topleft:
                        self.shake_anaimation()
                    else:
                        self.prev_pos = self.rect.topleft
                else:
                    self.prev_pos = self.rect.topleft

            else:
                self.prev_pos = None
                self.shaking = False

    def shake_anaimation(self):
        self.shaking = True
        if self.prevAnimTick == 0:
            self.prevAnimTick = pg.time.get_ticks()
            self.prev_pos = self.rect.topleft
            self.rect.x = self.prev_pos[0] - 3
        else:
            if pg.time.get_ticks() - self.prevAnimTick >= 200:
                self.rect.x = self.prev_pos[0] - 3
                self.prevAnimTick = pg.time.get_ticks()
            elif pg.time.get_ticks() - self.prevAnimTick >= 100:
                self.rect.x = self.prev_pos[0] + 2

    @classmethod
    def move_all_cards(cls, rel):
        for card in cls.get_cards():
            card.rect.move_ip(rel)

    @classmethod
    def get_length(cls):
        return len(cls.__cards)

    @classmethod
    def get_cards(cls):
        return cls.__cards

    @classmethod
    def add_card_to_group(cls, card: object):
        if UIElement.get_modus() == 'STACK':
            StackManager.add_to_stack(card)
            StackManager.save_stack()

    @classmethod
    def remove_card_from_group(cls, card: object, temp: bool = False):
        cls.get_cards().remove(card)
        for _card in StackManager.get_stack():
            if _card == card:
                StackManager.get_stack().remove(card)
        card.kill()

        BaseCard.save_cards()

    @classmethod
    def find_highest_card(cls, card_collection: list) -> object:
        if len(card_collection) > 0:
            _highest_card = card_collection[0]
            for _card in card_collection:
                if cls._compare_layer(_card, _highest_card):
                    _highest_card = _card

            return _highest_card
        else:
            return None

    @classmethod
    def _compare_layer(cls, card: object, other_card: object) -> bool:
        return card.rect.y < other_card.rect.y

    @classmethod
    def save_cards(cls):

        with open('sylladex/captchalogueCards/data/cardData.json', 'r') as _card_data_file:
            _card_data = json.load(_card_data_file)

        _card_list = {}

        for _index, _card in enumerate(BaseCard.get_cards()):
            _card_list[_index + 1] = {'CodeData': {}, 'TopLeft': []}
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

            _card_data['TopLeft'] = _card.rect.topleft

        _new_card_list = json.dumps(_card_list, indent=4)

        with open('sylladex/captchalogueCards/data/cardData.json', 'w') as _card_list_file:
            _card_list_file.write(_new_card_list)

        UIElement.get_ui_elem('ConsoleMessage')('Saved Cards')

    @classmethod
    def load_cards(cls):

        with open('sylladex/captchalogueCards/data/cardData.json', 'r') as _card_data_file:
            _card_data = json.load(_card_data_file)

        for _card_num in _card_data:
            _card = _card_data[_card_num]

            _obj = BaseCard(_card['TopLeft'])
            _obj.create_code_data(_card['CodeData'])

        if UIElement.get_modus() == 'STACK':
            StackManager.load_stack(BaseCard.get_cards())

        UIElement.get_ui_elem('ConsoleMessage')('Loaded Cards')
