import pygame as pg

from baseUI import UIBase, Apperance


class GristInfoBox(UIBase):
    def __init__(self, x, y, grist):
        super().__init__(x, y, 'GristInfoBox')

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24, bold=True)
        self.grist = grist

        self.apperance = Apperance(
            self,
            [170, 90],
            [[164, 84], '#999999', [6, 6]], 
            [[164, 84], '#C4C4C4', [0, 0]],
            [[52, 84], '#D9D9D9', [0, 0]], 
            [[111, 23], '#D9D9D9', [53, 0]], 
            [[111, 23], '#D9D9D9', [53, 24]], 
            [[111, 36], '#EFEFEF', [53, 48]], 
            colorKey = True,
            image = [f'sylladex/uiElements/asset/GRIST/{self.grist}.png', [6, 22]],
            texts = [[self.grist, [111, 11], 'center', '#000000']] 
            )


        self.children = []

        # self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+53, self.rect.y+48, 111, 36, 7, f'{self.grist}NumBox', f'Let\'s you alter how much {self.grist} grist you have', 'Num', (67,178,222)))
        # self.children[0].changeColors((239,239,239), (199,199,199), (179,179,179))

        # self.children.append(UIBase.get_uiElem('GristProgressBar')(self))
