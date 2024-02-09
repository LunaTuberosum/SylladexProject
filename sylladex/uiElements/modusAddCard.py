import json
import pygame as pg

from uiElement import UIElement, Apperance


class ModusAddCard(UIElement):
    def __init__(self):

        super().__init__(
            326,
            672,
            f'ModusAddCard',
            998
        )

        self.main_color = '#CCCCCC'
        self.side_color = '#7C7C7C'

        self.font = pg.font.Font(
            'sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf', 19)

        self.apperance = Apperance(
            self,
            [372, 408],
            colorKey=True,
            texts=[
                ['NAME', [48, 60], 'center', '#000000'],
                ['MODUS SORT', [174, 156], 'center', '#000000'],
                ['MODUS RETRIVE', [174, 252], 'center', '#000000'],
                ['CODE', [48, 348], 'center', '#000000'],
                ['COLOR', [210, 348], 'center', '#000000']
            ]
        )

        self.apperance.size_color_pos = self.size_color_pos()
        self.apperance.reload_apperance()

        self.add_child(UIElement.get_ui_elem('TextField')(
            72,
            336,
            [96, 24],
            "modusCard",
            "The code for a new modus",
            3,
            startLayer=1000,
            fontSize=19,
            baseColors=[
                '#EFEFEF',
                '#FFFFFF',
                '#D9D9D9'
            ],
            align='center'
        ))

        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        print((k if k != 'NULL' else '') for k in _modus_colors.keys())

        self.add_child(UIElement.get_ui_elem('DropDown')(
            240,
            336,
            [84, 24],
            f'modusColor',
            f'The color for a new modus',
            [
                (k if k != 'NULL' else '') for k in _modus_colors.keys()
            ],
            '',
            'Text',
            startLayer=1000,
            baseColors=[
                '#EFEFEF',
                '#FFFFFF',
                '#B7B7B7'
            ],
            exitCommand=self.change_color
        ))

    def size_color_pos(self) -> list:
        return [
            # Background
            [[372, 408], '#666666', [0, 0]],

            # Background shadow
            [[12, 12], '#434343', [276, 24]],
            [[12, 12], '#434343', [312, 48]],
            [[336, 324], '#434343', [24, 72]],

            # Color Key
            [[72, 24], '#D8DDFF', [300, 0]],
            [[36, 24], '#D8DDFF', [336, 24]],

            # Main Color
            [[263, 370], self.main_color, [12, 12]],
            [[36, 346], self.main_color, [275, 36]],
            [[36, 322], self.main_color, [311, 60]],

            # Name Box Shadow
            [[251, 24], self.side_color, [36, 60]],

            # Name Box
            [[48, 24], '#B7B7B7', [24, 48]],
            [[203, 24], '#D9D9D9', [72, 48]],

            # Trait 1 Shadow
            [[116, 24], self.side_color, [36, 108]],

            # Trait 1
            [[116, 24], '#D9D9D9', [24, 96]],

            # Trait 2 Shadow
            [[116, 24], self.side_color, [164, 108]],

            # Trait 2s
            [[116, 24], '#D9D9D9', [152, 96]],

            # Modus sort Shadow
            [[300, 72], self.side_color, [36, 156]],

            # Modus sort
            [[300, 24], '#B7B7B7', [24, 144]],
            [[300, 48], '#D9D9D9', [24, 168]],

            # Modus retrieve Shadow
            [[300, 72], self.side_color, [36, 252]],

            # Modus retrieve
            [[300, 24], '#B7B7B7', [24, 240]],
            [[300, 48], '#D9D9D9', [24, 264]],

            # Code Shadow
            [[144, 24], self.side_color, [36, 348]],

            # Code
            [[48, 24], '#B7B7B7', [24, 336]],
            [[96, 24], '#D9D9D9', [72, 336]],

            # Color Shadow
            [[144, 24], self.side_color, [192, 348]],

            # Color
            [[60, 24], '#B7B7B7', [180, 336]],
            [[84, 24], '#D9D9D9', [240, 336]],
        ]

    def change_color(self):
        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        _color = self.children[1].current_option

        self.main_color = _modus_colors[_color]['foreground']
        self.side_color = _modus_colors[_color]['background']

        self.apperance.size_color_pos = self.size_color_pos()
        self.apperance.reload_apperance()
