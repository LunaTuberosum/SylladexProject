import json
import pygame as pg

from uiElement import UIElement, Apperance


class GristCache(UIElement):
    def __init__(self):

        super().__init__(
            -392 if UIElement.find_current_ui('SideBar') else -732,
            803,
            'GristCache',
            2
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 36)

        self.apperance = Apperance(
            self,
            [744, 277],
            [[744, 277], '#666666', [0, 0]],
            [[732, 242], '#999999', [0, 24]],
            [[174, 42], '#666666', [558, 24]],
            [[114, 42], '#666666', [618, 66]],
            [[546, 48], '#CCCCCC', [0, 12]],
            [[606, 199], '#CCCCCC', [0, 54]],
            [[114, 157], '#CCCCCC', [606, 96]],
            [[174, 42], '#D8DDFF', [570, 0]],
            [[114, 42], '#D8DDFF', [630, 42]],
            colorKey=True,
            texts=[
                ['GRIST CACHE', [38, 34], 'left', '#000000']
            ]
        )

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            12,
            54,
            'Build'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            190,
            54,
            'Artifact'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            364,
            54,
            'Zillium'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            12,
            151,
            'Drop'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            190,
            151,
            'Block'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            364,
            151,
            'Gusher'
        ))

        self.add_child(UIElement.get_ui_elem('GristInfoBox')(
            538,
            151,
            'Diamond'
        ))

        self.load_cache()

        self.to_be_rect = UIElement.find_current_ui(
            'SideBar').rect.right if UIElement.check_for_ui('SideBar') else 0

    def update(self):

        if self.to_be_rect != self.rect.x:
            UIElement.move_element(self, [UIElement.lerp(
                self.rect.x, self.to_be_rect, 0.2), self.rect.y])
            UIElement.find_current_ui(
                'GristCacheButton').rect.x = self.rect.right

        else:
            if self.to_be_rect < 0 and self.rect.x - self.to_be_rect:
                UIElement.remove_from_group(self)

    def save_cache(self):
        with open('sylladex/uiElements/data/gristData.json', 'r') as _grist_data_file:
            _grist_data = json.load(_grist_data_file)

        for _child in self.children:
            _grist_data['Grist'][_child.grist] = _child.children[0].text

        _new_grist_data = json.dumps(_grist_data, indent=4)

        with open('sylladex/uiElements/data/gristData.json', 'w') as _grist_data_file:
            _grist_data_file.write(_new_grist_data)

        UIElement.get_ui_elem('ConsoleMessage')('Saved Cache')

    def load_cache(self):

        with open('sylladex/uiElements/data/gristData.json', 'r') as _grist_data_file:
            _grist_data = json.load(_grist_data_file)

        for _child in self.children:
            _child.children[0].text = _grist_data['Grist'][_child.grist]

            _child.children[0].reload_text()
