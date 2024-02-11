import json
import pygame as pg

from uiElement import UIElement, Apperance


class ModusAddCard(UIElement):
    def __init__(self):

        super().__init__(
            -46,
            672,
            f'ModusAddCard',
            8
        )

        self.main_color = '#CCCCCC'
        self.side_color = '#7C7C7C'

        self.code_in = False
        self.color_selected = False

        self.font = pg.font.Font(
            'sylladex/uiElements/asset/FONTS/DisposableDroidBB.ttf', 19)

        self.apperance = Apperance(
            self,
            [372, 408],
            colorKey=True,
            texts=[
                ['NAME', [48, 60], 'center', '#000000'],
                ['MODUS SORT', [174, 132], 'center', '#000000'],
                ['MODUS RETRIEVE', [174, 240], 'center', '#000000'],
                ['CODE', [48, 348], 'center', '#000000'],
                ['COLOR', [207, 348], 'center', '#000000']
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
            7,
            startLayer=9,
            fontSize=19,
            baseColors=[
                '#EFEFEF',
                '#FFFFFF',
                '#D9D9D9'
            ],
            align='center',
            exitCommand=self.check_code
        ))

        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        self.add_child(UIElement.get_ui_elem('DropDown')(
            234,
            336,
            [90, 24],
            f'modusColor',
            f'The color for a new modus',
            [
                (k if k != 'NULL' else '') for k in _modus_colors.keys()
            ],
            '',
            'Text',
            startLayer=9,
            baseColors=[
                '#EFEFEF',
                '#FFFFFF',
                '#B7B7B7'
            ],
            exitCommand=self.change_color
        ))

        self.to_be_rect = 326

    def update(self):
        if self.to_be_rect != self.rect.x:
            UIElement.move_element(self, [UIElement.lerp(
                self.rect.x, self.to_be_rect, 0.2), self.rect.y])
        elif self.rect.x <= -46:
            UIElement.remove_from_group(self)

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
            [[116, 24], self.side_color, [36, 96]],

            # Trait 1
            [[116, 24], '#D9D9D9', [24, 84]],

            # Trait 2 Shadow
            [[116, 24], self.side_color, [164, 96]],

            # Trait 2s
            [[116, 24], '#D9D9D9', [152, 84]],

            # Modus sort Shadow
            [[300, 96], self.side_color, [36, 132]],

            # Modus sort
            [[300, 24], '#B7B7B7', [24, 120]],
            [[300, 72], '#D9D9D9', [24, 144]],

            # Modus retrieve Shadow
            [[300, 96], self.side_color, [36, 240]],

            # Modus retrieve
            [[300, 24], '#B7B7B7', [24, 228]],
            [[300, 72], '#D9D9D9', [24, 252]],

            # Code Shadow
            [[144, 24], self.side_color, [36, 348]],

            # Code
            [[48, 24], '#B7B7B7', [24, 336]],
            [[96, 24], '#D9D9D9', [72, 336]],

            # Color Shadow
            [[144, 24], self.side_color, [192, 348]],

            # Color
            [[54, 24], '#B7B7B7', [180, 336]],
            [[90, 24], '#D9D9D9', [234, 336]],
        ]

    def create_confirm_button(self):
        if self.color_selected and self.code_in:
            if UIElement.find_current_ui('ModusAddCardButton'):
                UIElement.find_current_ui(
                    'ModusAddCardButton').to_be_rect = 698
            else:
                self.add_child(UIElement.get_ui_elem('ModusAddCardButton')())
        else:
            if UIElement.find_current_ui('ModusAddCardButton'):
                UIElement.find_current_ui(
                    'ModusAddCardButton').to_be_rect = 628

    def change_color(self):
        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        _color = self.children[1].current_option

        self.main_color = _modus_colors[_color]['foreground']
        self.side_color = _modus_colors[_color]['background']

        self.apperance.size_color_pos = self.size_color_pos()
        self.apperance.reload_apperance()

        self.color_selected = True
        self.create_confirm_button()

    def line_positions(self, text: str, y: int) -> list:
        _words = text.split(' ')

        _lines = ['']

        _count = 0
        for _word in _words:
            if _count + len(_word) > 34:
                _count = len(_word) + 1
                _lines.append(_word + ' ')
            else:
                _count += len(_word) + 1
                _lines[len(_lines) - 1] += _word + ' '

        _section = 72 // len(_lines)

        _positions = []
        for _sec in range(len(_lines)):
            _positions.append([175, y + (_section // 2) + (_section * _sec)])

        return [_lines, _positions]

    def check_code(self):
        _code = self.children[0].text

        if len(_code) < 8:
            UIElement.get_ui_elem('PopUp')(
                'Codes must be a 8 characters long')
            self.code_in = False
            self.create_confirm_button()
            return

        self.apperance.kwargs['texts'] = [
            ['NAME', [48, 60], 'center', '#000000'],
            ['MODUS SORT', [174, 132], 'center', '#000000'],
            ['MODUS RETRIEVE', [174, 240], 'center', '#000000'],
            ['CODE', [48, 348], 'center', '#000000'],
            ['COLOR', [207, 348], 'center', '#000000'],
            [f'{UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(_code[2], "3"), "SORT NAME")}-{UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(_code[3], "4"), "RETRIEVE NAME")}', [
                173, 60], 'center', '#000000'],
            [f'{UIElement.code_database.get_code_value(_code[2], "3")}', [
                82, 96], 'center', '#000000'],
            [f'{UIElement.code_database.get_code_value(_code[3], "4")}', [
                210, 96], 'center', '#000000'],
        ]

        _lines_and_pos = self.line_positions(
            UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(_code[2], "3"), 'MODUS SORT'), 144)

        for _i in range(len(_lines_and_pos[0])):
            self.apperance.kwargs['texts'].append([_lines_and_pos[0][_i], _lines_and_pos[1]
                                                   [_i], 'center', '#000000'])

        _lines_and_pos = self.line_positions(
            UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(_code[3], "4"), 'MODUS RETRIEVE'), 252)

        for _i in range(len(_lines_and_pos[0])):
            self.apperance.kwargs['texts'].append(
                [_lines_and_pos[0][_i], _lines_and_pos[1][_i], 'center', '#000000'])

        self.apperance.reload_apperance()
        self.code_in = True
        self.create_confirm_button()
