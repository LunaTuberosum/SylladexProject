import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristInfoBox(UIBase):
    def __init__(self, x, y, grist):
        super().__init__(x, y, (170,90), "GRIST_INFO_BOX.png", True)

        self.grist = grist

        self.gristImage = pg.image.load(f'sylladex/uiElements/asset/GRIST/{self.grist}.png').convert_alpha()
        self.gristImage = pg.transform.scale(self.gristImage, (40,40))
        self.image.blit(self.gristImage, (6, 22))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24, bold=True)

        self.gristName = self.font.render(self.grist, False, 'black')
        self.image.blit(self.gristName, (55.5-(self.gristName.get_width()/2)+52, 11.5-(self.gristName.get_height()/2)))

    def update(self):
        self.image.blit(self.gristImage, (6, 22))