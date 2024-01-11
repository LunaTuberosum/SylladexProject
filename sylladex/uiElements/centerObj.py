import pygame as pg

from uiElement import UIElement, Apperance
import settings
from ..captchalogueCards.baseCard import BaseCard


class CenterObj(UIElement):
    def __init__(self):
        super().__init__(
            settings.SCREEN_WIDTH/2,
            settings.SCREEN_HEIGHT/2,
            'CenterObj',
            -999
        )

        self.apperance = Apperance(self, (0, 0), colorKey=True)

    def move_self(self, rel):
        self.rect.move_ip(rel)

    def only_center_self(self):
        self.rect.x = settings.SCREEN_WIDTH/2
        self.rect.y = settings.SCREEN_HEIGHT/2

    def recenter(self):
        _off_set_x = settings.SCREEN_WIDTH/2 - self.rect.x
        _off_set_y = settings.SCREEN_HEIGHT/2 - self.rect.y

        if _off_set_x == 0 and _off_set_y == 0:
            return

        self.rect.x = settings.SCREEN_WIDTH/2
        self.rect.y = settings.SCREEN_HEIGHT/2

        for card in BaseCard.get_cards():
            card.rect.x += _off_set_x
            card.rect.y += _off_set_y

        UIElement.get_ui_elem('ConsoleMessage')('Centered stacking area')
