import pygame as pg

from baseUI import UIBase
import settings

class CardInspector(UIBase):
    def __init__(self):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 439), 'CardInspector', (255,255,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.create_appearance(colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_INSPECTOR.png', [0, 0]], texts = [["NAME", [36, 48], "center"], ["TRAIT 1", [51, 84], "center"], ["TRAIT 2", [51, 109], "center"], ["ITEMKIND", [52, 134], "center"], ['GRIST TYPE', [64, 159], 'center'], ['EFFECTIVE', [68, 184], 'center'], ['INEFFECTIVE', [68, 209], 'center'], ['INSPECT INFORMATION', [159, 305], 'center'], ['CST', [30, 330], 'center'], ['DMG', [30, 355], 'center'], ['CODE', [79, 391], 'center'], ['TIER', [223, 391], 'center'], ['1', [247, 121], 'center'], ['2', [247, 146], 'center'], ['3', [247, 171], 'center'], ['BD', [247, 196], 'center']])