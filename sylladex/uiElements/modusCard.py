import json
import pygame as pg

from uiElement import UIElement, Apperance


class ModusCard(UIElement):
    def __init__(self, x: int, code: str, color: str, active: bool, num: str):

        self.code = code
        self.color = color
        self.num = num

        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        self.main_color = _modus_colors[self.color]['foreground']
        self.side_color = _modus_colors[self.color]['background']
        self.text_color = _modus_colors[self.color]['text']

        super().__init__(
            x,
            910,
            f'ModusCard ({self.code})',
            11
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/fontstuck.ttf", 12)

        self.apperance = Apperance(
            self,
            [90, 114],
            [[72, 82], self.side_color, [9, 15]],
            [[54, 89], self.main_color, [6, 5]],
            [[9, 73], self.main_color, [60, 21]],
            [[9, 64], self.main_color, [69, 30]],
            [[10, 40], self.side_color, [31, 30]],
            [[40, 10], self.side_color, [16, 45]],
            colorKey=True,
            images=[
                ['sylladex/uiElements/asset/ICONS/MODUS.png', [0, 0]]
            ]
        )

        self.active = active
        self.modus_add_card = None
        if self.code == '-':
            self.tool_tip_text = 'Create new modus'
        else:
            self.tool_tip_text = f'Changes the modus to {UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(self.code[2], "3"), "SORT NAME")}-{UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(self.code[3], "4"), "RETRIEVE NAME")} MODUS'

        self.hovering = False

        self.to_be_rect = self.rect.y
        self.redraw()

    def redraw(self):
        self.apperance.change_images([
            ['sylladex/uiElements/asset/ICONS/MODUS.png', [0, 0]]
        ])

        self.apperance.size_color_pos = [
            [[72, 82], self.side_color, [9, 15]],
            [[54, 89], self.main_color, [6, 5]],
            [[9, 73], self.main_color, [60, 21]],
            [[9, 64], self.main_color, [69, 30]]
        ]

        if self.modus_add_card:

            self.apperance.kwargs['texts'] = [
                ['CANCEL', [43, 57], 'center', self.text_color]
            ]

        elif self.code != '-':

            self.apperance.kwargs['texts'] = [
                [UIElement.code_database.get_trait_info(
                    UIElement.code_database.get_code_value(self.code[2], '3'), 'SORT NAME'), [43, 52], 'center', self.text_color],
                [UIElement.code_database.get_trait_info(
                    UIElement.code_database.get_code_value(self.code[3], '4'), 'RETRIEVE NAME'), [43, 62], 'center', self.text_color]
            ]
        else:
            self.apperance.size_color_pos.append(
                [[10, 40], self.side_color, [38, 36]])
            self.apperance.size_color_pos.append(
                [[40, 10], self.side_color, [23, 51]])

            self.apperance.kwargs['texts'] = []

        if self.active or self.modus_add_card:

            self.apperance.change_images([
                ['sylladex/uiElements/asset/ICONS/MODUS_ACTIVE.png', [0, 0]]
            ])

        self.apperance.reload_apperance()

    def update(self):

        if self.to_be_rect != self.rect.y:

            UIElement.move_element(self, [self.rect.x, UIElement.lerp(
                self.rect.y, self.to_be_rect, 0.2)])

    def change_color(self):
        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        self.main_color = _modus_colors[self.color]['foreground']
        self.side_color = _modus_colors[self.color]['background']
        self.text_color = _modus_colors[self.color]['text']

    def initate_new_modus(self):
        self.code = self.modus_add_card.children[0].text
        self.color = self.modus_add_card.children[1].current_option

        self.change_color()

        self.modus_add_card.to_be_rect = -116
        self.modus_add_card = None

        with open('sylladex/uiElements/data/modusData.json', 'r') as _modus_data_file:
            _modus_data = json.load(_modus_data_file)

        _modus_data[self.num]['Code'] = self.code
        _modus_data[self.num]['Color'] = self.color
        _modus_data[self.num]['Active'] = self.active

        _new_modus_data = json.dumps(_modus_data, indent=4)

        with open('sylladex/uiElements/data/modusData.json', 'w') as _modus_data_file:
            _modus_data_file.write(_new_modus_data)

        self.redraw()

    def on_click(self):
        if self.code == '-' and not self.modus_add_card:
            for _elem in UIElement.get_group('ui'):
                if isinstance(_elem, UIElement.get_ui_elem('ModusCard')) and _elem.modus_add_card:
                    self.modus_add_card = _elem.modus_add_card
                    _elem.modus_add_card = None
                    _elem.redraw()
                    self.redraw()
                    return
            self.modus_add_card = UIElement.get_ui_elem('ModusAddCard')()
            self.redraw()

        elif self.code == '-' or self.modus_add_card:
            self.modus_add_card.to_be_rect = -116
            self.modus_add_card = None
            self.redraw()
        else:
            with open('sylladex/uiElements/data/modusData.json', 'r') as _modus_data_file:
                _modus_data = json.load(_modus_data_file)

            self.active = True
            for _elem in UIElement.get_group("ui"):
                if isinstance(_elem, UIElement.get_ui_elem('ModusCard')):
                    if _elem != self:
                        _elem.active = False
                    _elem.redraw()
                    _modus_data[_elem.num]['Code'] = _elem.code
                    _modus_data[_elem.num]['Color'] = _elem.color
                    _modus_data[_elem.num]['Active'] = _elem.active

            _new_modus_data = json.dumps(_modus_data, indent=4)

            with open('sylladex/uiElements/data/modusData.json', 'w') as _modus_data_file:
                _modus_data_file.write(_new_modus_data)

            Apperance.change_modus(self.color)

    def on_middle_click(self):
        if self.code == '-':
            return

        if self.modus_add_card:
            UIElement.remove_from_group(self.modus_add_card)
            self.modus_add_card = None
            self.redraw()
        else:
            self.modus_add_card = UIElement.get_ui_elem('ModusAddCard')()

            self.modus_add_card.children[0].text = self.code
            self.modus_add_card.children[0].reload_text()
            self.modus_add_card.children[1].current_option = self.color
            self.modus_add_card.children[1].reload_apperance()

            self.modus_add_card.change_color()
            self.modus_add_card.check_code()

            self.redraw()

    def on_right_click(self):
        if not self.active and not self.modus_add_card and self.code != '-':
            self.color = 'NULL'
            self.code = '-'

            self.change_color()
            self.redraw()

            with open('sylladex/uiElements/data/modusData.json', 'r') as _modus_data_file:
                _modus_data = json.load(_modus_data_file)

            for _elem in UIElement.get_group("ui"):
                if isinstance(_elem, UIElement.get_ui_elem('ModusCard')):
                    _elem.redraw()
                    _modus_data[_elem.num]['Code'] = _elem.code
                    _modus_data[_elem.num]['Color'] = _elem.color
                    _modus_data[_elem.num]['Active'] = _elem.active

            _new_modus_data = json.dumps(_modus_data, indent=4)

            with open('sylladex/uiElements/data/modusData.json', 'w') as _modus_data_file:
                _modus_data_file.write(_new_modus_data)

    def hover(self):
        self.rect.y = 900
        self.to_be_rect = 900
        self.hovering = True

    def no_hover(self):
        super().no_hover()
        self.to_be_rect = 910
        self.hovering = False
