import pygame as pg

from baseUI import UIBase


class SideBar(UIBase):
    def __init__(self):
        super().__init__(0, 0, (326, 1080), 'SideBar', '#999999')

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self._create_appearance([[326, 1080], UIBase.modusBackground, [0, 0]], [[320, 1080], UIBase.modusForground, [0, 0]], [[284, 691], UIBase.modusBackground, [18, 136]], [[284, 60], UIBase.modusBackground, [18, 136]], [[218, 48], '#B7B7B7', [24, 142]], [[54, 48], '#999999', [242, 142]], [[249, 625], '#999999', [24, 196]], [[23, 625], '#B7B7B7', [273, 196]], [[278, 199], UIBase.modusBackground, [24, 857]], [[278, 199], '#A4A4A4', [18, 851]], colorKey = True, texts = [['SYLLADEX', [24, 20], 'left', '#FFFFFF'], ['NUM OF CARDS', [133, 170], 'center'], ['FETCH MODUS', [21, 871], 'left', '#FFFFFF']])