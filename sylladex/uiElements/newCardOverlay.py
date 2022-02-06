import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.textField import TextField
from sylladex.captchalogueCards import codeDatabase

import math


class NewCardOverlay(UIBase):
    def __init__(self):
        super().__init__(664, 274, (372,492), f"sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_NEW_OVERLAY.png")

        TextField(664, 440, 243, 28, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", "")
        TextField(664, 516, 105, 28, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", "")
        TextField(664, 592, 33, 28, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", "")

    def update(self):
        self.image = pg.image.load(f"sylladex/uiElements/asset/{UIBase.get_modus()}/CARD_NEW_OVERLAY.png").convert_alpha()
        for elem in UIBase.get_group("ui"):
            
            if isinstance(elem, TextField) and elem.job == "codeOverlay":
                if elem.text:
                    kindImage = pg.image.load(codeDatabase.find_kindImage(codeDatabase.code.get(elem.text[0])["1"] )).convert_alpha()
                    kindImage = pg.transform.scale(kindImage, (192, 192))
                    self.image.blit(kindImage, (340, 150))
                    