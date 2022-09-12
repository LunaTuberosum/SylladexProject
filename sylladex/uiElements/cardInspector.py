import pygame as pg

from baseUI import UIBase
import settings

class CardInspector(UIBase):
    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 439), 'CardInspector', (255,255,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.create_appearance(colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]], texts = [["NAME", [36, 48], "center"], ["TRAIT 1", [50, 84], "center"], ["TRAIT 2", [50, 110], "center"], ["ITEMKIND", [52, 134], "center"], ['GRIST TYPE', [64, 158], 'center']])