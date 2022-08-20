import pygame as pg

from baseUI import UIBase
import settings
from ..captchalogueCards.baseCard import BaseCard

class CenterObj(UIBase):
    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2, (1,1), 'CenterObj', '#FFFFFF')

        self.create_appearance(colorKey = True)

    def move_self(self, rel):
        self.rect.move_ip(rel)

    def recenter(self):
        offSetX = settings.SCREEN_WIDTH/2 - self.rect.x
        offSetY = settings.SCREEN_HEIGHT/2 - self.rect.y

        if offSetX == 0 and offSetY == 0:
            return

        self.rect.x = settings.SCREEN_WIDTH/2
        self.rect.y = settings.SCREEN_HEIGHT/2

        for card in BaseCard.get_cardGroup():
            card.rect.x += offSetX
            card.rect.y += offSetY

        UIBase.get_uiElem('ConsoleMessage')('Centered stacking area')
