import pygame as pg

from baseUI import UIBase
import settings

class CardInspector(UIBase):
    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 439), 'CardInspector', (0,0,0))

        self.create_appearance(colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]])