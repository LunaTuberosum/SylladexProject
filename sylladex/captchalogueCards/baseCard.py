import pygame as pg

from sylladex.captchalogueCards.stackManager import StackManager


class BaseCard(pg.sprite.Sprite):
    cards = pg.sprite.Group()

    def __init__(self):
        super().__init__()
        StackManager.stack.append(self)
        BaseCard.cards.add(self)
        self.cardID = StackManager.get_length()

    def get_cardGroup():
        return BaseCard.cards

    def add_cardToGroup(card):
        BaseCard.get_cardGroup().add(card)
