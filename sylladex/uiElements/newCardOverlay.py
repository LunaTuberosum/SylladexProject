import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.textField import TextField
from sylladex.captchalogueCards import codeDatabase

import math


class NewCardOverlay(UIBase):
    def __init__(self):
        super().__init__(774, 274, (372,492), f"sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_NEW_OVERLAY.png")

        TextField(794, 286, 240, 24, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", "")
        TextField(848, 718, 102, 24, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", "")
        TextField(1032, 718, 30, 24, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", "")

    def update(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_NEW_OVERLAY.png").convert_alpha()
        for elem in UIBase.get_group("ui"):
            
            if isinstance(elem, TextField) and elem.job == "codeOverlay":
                if elem.text:
                    kindImage = pg.image.load(codeDatabase.find_kindImage(codeDatabase.code.get(elem.text[0])["1"] )).convert_alpha()
                    kindImage = pg.transform.scale(kindImage, (192, 192))
                    self.image.blit(kindImage, (80, 150))

                    if len(elem.text) >= 2:
                        gristImage = pg.image.load(codeDatabase.find_gristImage(codeDatabase.code.get(elem.text[1])["2"] )).convert_alpha()
                        gristImage = pg.transform.scale(gristImage, (32, 32))
                        self.image.blit(gristImage, (30, 440))

            if isinstance(elem, TextField) and elem.job == "tierOverlay":
                if elem.text:
                    tierLevel = math.ceil(int(elem.text)/4)
                    if tierLevel == 1:
                        tierImage = pg.image.load("sylladex/uiElements/asset/MISC/TIER_LEVEL1.png").convert_alpha()
                    elif tierLevel == 2:
                        tierImage = pg.image.load("sylladex/uiElements/asset/MISC/TIER_LEVEL2.png").convert_alpha()
                    elif tierLevel == 3:
                        tierImage = pg.image.load("sylladex/uiElements/asset/MISC/TIER_LEVEL3.png").convert_alpha()
                    elif tierLevel == 4:
                        tierImage = pg.image.load("sylladex/uiElements/asset/MISC/TIER_LEVEL4.png").convert_alpha()

                    self.image.blit(tierImage, (300, 442))
                    