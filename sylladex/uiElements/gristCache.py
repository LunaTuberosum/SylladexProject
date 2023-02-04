from sqlite3 import DatabaseError
import pygame as pg
import pickle

from baseUI import UIBase, Apperance
from sylladex.uiElements.sideBar import SideBar


class GristCache(UIBase):
    def __init__(self, x):
        super().__init__(x, 626, 'GristCache', 0)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.apperance = Apperance(
            self, 
            (719,452),
            [[719,452], '#999999', [0,0]],
            [[713, 446], '#CCCCCC', [0, 6]], 
            texts = [['GRIST CACHE', [525, 25], 'left', '#FFFFFF']]
            )

        self.children = []

        self.children.append(UIBase.get_ui_elem('GristCacheLimit')())

        for _index, grist in enumerate(['Build', 'Shale', 'Ruby', 'Cobalt', 'Chalk', 'Marble', 'Iron', 'Amber', 'Caulk', 'Tar', 'Uranium', 'Amethyst', 'Garnet', 'Artifact', 'Zillium', 'Diamond']):
            if _index < 4: self.children.append(UIBase.get_ui_elem('GristInfoBox')((self.rect.x+9)+(174*_index), 692, grist))
            elif _index < 8: self.children.append(UIBase.get_ui_elem('GristInfoBox')((self.rect.x+9)+(174*(_index-4)), 789, grist))
            elif _index < 12: self.children.append(UIBase.get_ui_elem('GristInfoBox')((self.rect.x+9)+(174*(_index-8)), 885, grist))
            elif _index < 16: self.children.append(UIBase.get_ui_elem('GristInfoBox')((self.rect.x+9)+(174*(_index-12)), 982, grist))

        self.load_list()

        if UIBase.check_for_ui('SideBar'):
            self.to_be_rect = 326
        else:
            self.to_be_rect = 0

    def update(self):
        
        if self.to_be_rect != self.rect.x:
            self.rect.x = UIBase.lerp(self.rect.x, self.to_be_rect, 0.2)
            self.reposition_children()
            UIBase.find_cur_ui('GristCacheButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -719 or self.to_be_rect == -392:
                UIBase.remove_from_group(self)

    def save_cache(self):
        _data = []
        UIBase.get_ui_elem('ConsoleMessage')('Saved Cache')

        for _index, _child in enumerate(self.children):
            if _index > 0:
                _data.append(_child.children[0].text)

        with open('sylladex/uiElements/data/uiCache.plk', 'wb') as _save_cache:
            pickle.dump(_data, _save_cache, -1)

    def load_list(self):

        with open('sylladex/uiElements/data/uiCache.plk', 'rb') as _save_cache:
            _data = pickle.load(_save_cache)

        
        for _index, _data in enumerate(_data):
            self.children[_index+1].children[0].text = _data

            self.children[_index+1].children[0].apperance.options = {'texts': [[
                self.children[_index+1].children[0].text, 
                self.children[_index+1].children[0].text_postion, 
                self.children[_index+1].children[0].alginment, 
                self.children[_index+1].children[0].text_color]]
                }
            
            self.children[_index+1].children[0].apperance.reload_apperance()

    def reposition_children(self):

        for _index, _child in enumerate(self.children):
            if _index == 0: _child.rect.x = self.rect.x+212
            elif _index < 5: _child.rect.x = (self.rect.x+9) + (174*(_index - 1))
            elif _index < 9: _child.rect.x = (self.rect.x+9) + (174*(_index - 5))
            elif _index < 13: _child.rect.x = (self.rect.x+9) + (174*(_index - 9))
            elif _index < 17: _child.rect.x = (self.rect.x+9) + (174*(_index - 13))

            if _index > 0:
                _child.children[0].rect.x = _child.rect.x+53
                _child.children[1].rect.x = _child.rect.x+59
                