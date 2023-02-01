import pygame as pg

from baseUI import UIBase, Apperance


class SideBar(UIBase):
    def __init__(self):
        super().__init__(0, 0, 'SideBar')

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.apperance = Apperance(
            self,
            [326, 1080],
            [[326, 1080], 'ModusBackground', [0, 0]], 
            [[320, 1080], 'ModusForeground', [0, 0]], 
            [[284, 691], 'ModusBackground', [18, 136]], 
            [[284, 60], 'ModusBackground', [18, 136]], 
            [[218, 48], '#B7B7B7', [24, 142]], 
            [[54, 48], '#999999', [242, 142]], 
            [[249, 625], '#999999', [24, 196]], 
            [[23, 625], '#B7B7B7', [273, 196]], 
            [[278, 199], 'ModusBackground', [24, 857]], 
            [[278, 199], '#A4A4A4', [18, 851]], 
            colorKey = True, 
            texts = [
                ['SYLLADEX', [24, 20], 'left', '#FFFFFF'], 
                ['NUM OF CARDS', [133, 170], 'center', '#000000'], 
                ['FETCH MODUS', [21, 871], 'left', '#FFFFFF']])

        self.children = [
            UIBase.get_uiElem('TextField')(
                242, 
                142, 
                [53, 48], 
                "numOfCards", 
                "The Number of Cards in you Sylladex", 
                3,
                textType='Num',
                align='center',
                fontSize=24,
                ),

            UIBase.get_uiElem('ModusCard')(33, 910, "STACK"),
            UIBase.get_uiElem('ModusCard')(121, 910, "QUEUE"),
            UIBase.get_uiElem('ModusCard')(209, 910, "TREE"),
        ]

    def reloadSelf(self):
        self.apperance.reload_apperance()