import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class CustomSettingSectionName(UIBase):
    def __init__(self, parent, y, section):
        self.parent = parent
        self.section = section
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        super().__init__(self.parent.rect.x+12, self.parent.rect.y+y, (186,30), "surfaceRect", f'CustomSettingSectionName ({self.section})', True, (255,255,255))
        self.image.set_colorkey((255,255,255))

        self.backgroundColor = pg.Surface((180,24))
        self.backgroundColor.fill('#1C4587')
        self.image.blit(self.backgroundColor, [6, 6])
        
        self.foregroundColor = pg.Surface((180,24))
        self.foregroundColor.fill('#3C78D8')
        self.image.blit(self.foregroundColor, [0, 0])

        self.sectionText = self.font.render('CUSTOM '+self.section, True, (0,0,0))
        self.image.blit(self.sectionText, [90-(self.sectionText.get_width()/2), 12-(self.sectionText.get_height()/2)])