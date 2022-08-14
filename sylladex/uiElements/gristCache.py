import pygame as pg
import pickle

from baseUI import UIBase


class GristCache(UIBase):
    def __init__(self, x):
        super().__init__(x, 626, (719,452), 'GristCache', '#999999')

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.create_appearance([[713, 446], '#CCCCCC', [0, 6]], texts = [['GRIST CACHE', [525, 25], 'left', '#FFFFFF']])

        self.children = []

        self.children.append(UIBase.get_uiElem('GristCacheLimit')(x))

        for index, grist in enumerate(['Build', 'Shale', 'Ruby', 'Cobalt', 'Chalk', 'Marble', 'Iron', 'Amber', 'Caulk', 'Tar', 'Uranium', 'Amethyst', 'Garnet', 'Artifact', 'Zillium', 'Diamond']):
            if index < 4: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*index), 692, grist))
            elif index < 8: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-4)), 789, grist))
            elif index < 12: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-8)), 885, grist))
            elif index < 16: self.children.append(UIBase.get_uiElem('GristInfoBox')((self.rect.x+9)+(174*(index-12)), 982, grist))

        self.load_list()

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
            self.children[index+1].children[0].draw()
            self.children[index+1].children[0].no_hover()
    
    def repositionChildren(self):

        for index, child in enumerate(self.children):
            if index == 0: child.rect.x = self.rect.x+212
            elif index < 5: child.rect.x = (self.rect.x+9) + (174*(index - 1))
            elif index < 9: child.rect.x = (self.rect.x+9) + (174*(index - 5))
            elif index < 13: child.rect.x = (self.rect.x+9) + (174*(index - 9))
            elif index < 17: child.rect.x = (self.rect.x+9) + (174*(index - 13))

            if index > 0:
                child.children[0].rect.x = child.rect.x+53
                