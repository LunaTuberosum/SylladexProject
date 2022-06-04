import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class GristInfoBox(UIBase):
    def __init__(self, x, y, grist):
        super().__init__(x, y, (170,90), "GRIST_INFO_BOX.png", 'GristInfoBox',True)

        self.grist = grist

        self.gristImage = pg.image.load(f'sylladex/uiElements/asset/GRIST/{self.grist}.png').convert_alpha()
        self.gristImage = pg.transform.scale(self.gristImage, (40,40))
        self.image.blit(self.gristImage, (6, 22))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24, bold=True)

        self.gristName = self.font.render(self.grist, False, 'black')
        self.image.blit(self.gristName, (55.5-(self.gristName.get_width()/2)+52, 11.5-(self.gristName.get_height()/2)))

        self.children = []

        self.children.append(UIBase.TextField(self.rect.x+53, self.rect.y+48, 111, 36, 7, f'{self.grist}NumBox', f'Let\'s you alter how much {self.grist} grist you have', 'Num', (67,178,222)))
        self.children[0].changeColors((239,239,239), (199,199,199), (179,179,179))

        self.children.append(UIBase.GristProgressBar(self))
        

    def update(self):
        self.image.blit(self.gristImage, (6, 22))