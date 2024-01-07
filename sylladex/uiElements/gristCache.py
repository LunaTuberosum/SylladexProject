import json
import pygame as pg
import pickle

from uiElement import UIElement, Apperance


class GristCache(UIElement):
    def __init__(self):

        super().__init__(
            -392 if UIElement.find_current_ui('SideBar') else -719,
            626,
            'GristCache',
            1
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 36)

        self.apperance = Apperance(
            self,
            (719, 452),
            [[719, 452], '#999999', [0, 0]],
            [[713, 446], '#CCCCCC', [0, 6]],
            texts=[['GRIST CACHE', [525, 25], 'left', '#FFFFFF']]
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
            self.to_be_rect = UIElement.find_current_ui('SideBar').rect.right
        else:
            self.to_be_rect = 0

    def update(self):

        if self.to_be_rect != self.rect.x:
            UIElement.move_element(self, [UIElement.lerp(
                self.rect.x, self.to_be_rect, 0.2), 626])
            UIElement.find_current_ui(
                'GristCacheButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -719 or self.to_be_rect == -392:
                UIElement.remove_from_group(self)

    def save_cache(self):
        with open('sylladex/uiElements/data/gristData.json', 'r') as _grist_data_file:
            _grist_data = json.load(_grist_data_file)

        for _child in self.children:
            if not isinstance(_child, UIElement.get_ui_elem('GristInfoBox')):
                _grist_data['CacheLimit'] = _child.limit_num
                continue

            _grist_data['Grist'][_child.grist] = _child.children[0].text

        _new_grist_data = json.dumps(_grist_data, indent=4)

        with open('sylladex/uiElements/data/gristData.json', 'w') as _grist_data_file:
            _grist_data_file.write(_new_grist_data)

        UIElement.get_ui_elem('ConsoleMessage')('Saved Cache')

    def load_cache(self):

        with open('sylladex/uiElements/data/gristData.json', 'r') as _grist_data_file:
            _grist_data = json.load(_grist_data_file)

        for _child in self.children:
            if not isinstance(_child, UIElement.get_ui_elem('GristInfoBox')):
                _child.change_cache_limit(_grist_data['CacheLimit'])
                continue

            _child.children[0].text = _grist_data['Grist'][_child.grist]

            _child.children[0].reload_text()
