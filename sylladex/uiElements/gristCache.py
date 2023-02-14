from sqlite3 import DatabaseError
import pygame as pg
import pickle

from uiElement import UIElement, Apperance
from sylladex.uiElements.sideBar import SideBar


class GristCache(UIElement):
    def __init__(self):

        super().__init__(
            -392 if UIElement.find_current_ui('SideBar') else -719, 
            626, 
            'GristCache', 
            1
            )

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.apperance = Apperance(
            self, 
            (719,452),
            [[719,452], '#999999', [0,0]],
            [[713, 446], '#CCCCCC', [0, 6]], 
            texts = [['GRIST CACHE', [525, 25], 'left', '#FFFFFF']]
            )

        self.add_child(UIElement.get_ui_elem('GristCacheLimit')(212, 16))

        for _index, grist in enumerate(
            ['Build', 'Shale', 'Ruby', 'Cobalt', 
            'Chalk', 'Marble', 'Iron', 'Amber', 
            'Caulk', 'Tar', 'Uranium', 'Amethyst', 
            'Garnet', 'Artifact', 'Zillium', 'Diamond']):

            if _index < 4: 
                self.add_child(
                    UIElement.get_ui_elem('GristInfoBox')(
                        (9)+(174*_index), 
                        66, 
                        grist))
            elif _index < 8: 
                self.add_child(
                    UIElement.get_ui_elem('GristInfoBox')(
                        (9)+(174*(_index-4)), 
                        163, 
                        grist))
            elif _index < 12: 
                self.add_child(
                    UIElement.get_ui_elem('GristInfoBox')(
                        (9)+(174*(_index-8)), 
                        259, 
                        grist))
            elif _index < 16: 
                self.add_child(
                    UIElement.get_ui_elem('GristInfoBox')(
                        (9)+(174*(_index-12)), 
                        356, 
                        grist))

        self.load_cache()

        if UIElement.check_for_ui('SideBar'):
            self.to_be_rect = 326
        else:
            self.to_be_rect = 0

    def update(self):
        
        if self.to_be_rect != self.rect.x:
            UIElement.move_element(self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 626])
            UIElement.find_current_ui('GristCacheButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -719 or self.to_be_rect == -392:
                UIElement.remove_from_group(self)

    def save_cache(self):
        _data = []
        UIElement.get_ui_elem('ConsoleMessage')('Saved Cache')

        for _index, _child in enumerate(self.children):
            if _index > 0:
                _data.append(_child.children[0].text)

        with open('sylladex/uiElements/data/uiCache.plk', 'wb') as _save_cache:
            pickle.dump(_data, _save_cache, -1)

    def load_cache(self):

        with open('sylladex/uiElements/data/uiCache.plk', 'rb') as _save_cache:
            _data = pickle.load(_save_cache)

        
        for _index, _data in enumerate(_data):
            self.children[_index+1].children[0].text = _data

            self.children[_index+1].children[0].apperance.kargs = {'texts': [[
                self.children[_index+1].children[0].text, 
                self.children[_index+1].children[0].text_postion, 
                self.children[_index+1].children[0].alginment, 
                self.children[_index+1].children[0].text_color]]
                }
            
            self.children[_index+1].children[0].apperance.reload_apperance()
                