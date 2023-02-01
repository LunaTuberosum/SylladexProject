from sqlite3 import DatabaseError
import pygame as pg
import pickle

from baseUI import UIBase, Apperance
from sylladex.uiElements.sideBar import SideBar


class GristCache(UIBase):
    def __init__(self):
        super().__init__(0, 626, 'GristCache')

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.apperance = Apperance(
            self, 
            (719,452),
            [[719,452], '#999999', [0,0]],
            [[713, 446], '#CCCCCC', [0, 6]], 
            texts = [['GRIST CACHE', [525, 25], 'left', '#FFFFFF']]
            )

        self.children = []

        self.children.append(UIBase.get_uiElem('GristCacheLimit')())

        for index, grist in enumerate(['Build', 'Shale', 'Ruby', 'Cobalt', 'Chalk', 'Marble', 'Iron', 'Amber', 'Caulk', 'Tar', 'Uranium', 'Amethyst', 'Garnet', 'Artifact', 'Zillium', 'Diamond']):
            if index < 4: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*index), 692, grist))
            elif index < 8: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-4)), 789, grist))
            elif index < 12: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-8)), 885, grist))
            elif index < 16: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-12)), 982, grist))

        self.load_list()

    def update(self):
        if UIBase.check_forUI('SideBar') and self.rect != 326:
            self.rect.x = 326
            self.repositionChildren()
        elif not UIBase.check_forUI('SideBar') and self.rect.x != 0:
            self.rect.x = 0
            self.repositionChildren()

    def save_cache(self):
        tempData = []
        UIBase.get_uiElem('ConsoleMessage')('Saved Cache')

        for index, child in enumerate(self.children):
            if index > 0:
                tempData.append(child.children[0].text)

        with open('sylladex/uiElements/data/uiCache.plk', 'wb') as saveCache:
            pickle.dump(tempData, saveCache, -1)

    def load_list(self):

        with open('sylladex/uiElements/data/uiCache.plk', 'rb') as saveCache:
            tempData = pickle.load(saveCache)

        
        for index, data in enumerate(tempData):
            self.children[index+1].children[0].text = data

            self.children[index+1].children[0].apperance.options = {'texts': [[
                self.children[index+1].children[0].text, 
                self.children[index+1].children[0].textPostion, 
                self.children[index+1].children[0].alginment, 
                self.children[index+1].children[0].textColor]]
                }
            
            self.children[index+1].children[0].apperance.reload_apperance()

    def repositionChildren(self):

        for index, child in enumerate(self.children):
            if index == 0: child.rect.x = self.rect.x+212
            elif index < 5: child.rect.x = (self.rect.x+9) + (174*(index - 1))
            elif index < 9: child.rect.x = (self.rect.x+9) + (174*(index - 5))
            elif index < 13: child.rect.x = (self.rect.x+9) + (174*(index - 9))
            elif index < 17: child.rect.x = (self.rect.x+9) + (174*(index - 13))

            if index > 0:
                child.children[0].rect.x = child.rect.x+53
                