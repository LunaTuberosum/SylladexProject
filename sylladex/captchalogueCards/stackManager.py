import pygame as pg
import pickle

from uiElement import UIElement

class StackManager():
    stack = pg.sprite.LayeredUpdates()

    @classmethod
    def get_stack(cls) -> pg.sprite.LayeredUpdates:
        return cls.stack

    @classmethod
    def get_length(cls):
        return len(cls.stack)

    @classmethod
    def get_top_card(cls, situation):
        if situation == 'distance':
            for index, card in enumerate(cls.stack):
                if index == cls.get_length()-2:
                    return card

        elif situation == 'remove':
            for index, card in enumerate(cls.stack):
                if index == cls.get_length()-1:
                    return card

    @classmethod
    def add_toStack(cls, card):
        cls.stack.add(card)
        cls.get_stack().change_layer(card, cls.get_length())

    @classmethod
    def remove_fromStack(cls, card):
        cls.stack.remove(card)
        for index, card in enumerate(cls.get_stack()):
            print(index, card.codeData.code)

    @classmethod
    def save_stack(cls):
        tempArray = []
        for card in StackManager.get_stack():
            tempArray.append(card.codeData)

        with open("sylladex/captchalogueCards/data/stackData.plk", "wb") as saveStack:
            pickle.dump(tempArray, saveStack, -1)

    @classmethod
    def load_stack(cls, allCards):
        with open("sylladex/captchalogueCards/data/stackData.plk", "rb") as loadStack:
            tempArray = pickle.load(loadStack)

        for codeData in tempArray:
            for card in allCards:
                if codeData == card.codeData:
                    StackManager.add_toStack(card)
                    break
        for card in StackManager.get_stack(): UIElement.get_group('layer').change_layer(card, -2)
        UIElement.get_uiElem('ConsoleMessage')('Loaded Stack')
        