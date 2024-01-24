import json
import pygame as pg

from uiElement import Apperance, UIElement
import settings


class CardInspector(UIElement):
    def __init__(self, code_data):
        super().__init__(
            settings.SCREEN_WIDTH,
            settings.SCREEN_HEIGHT / 2 - 219.5,
            'CardInspector',
            999
        )

        self.font = pg.font.Font(
            'sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf', 19)

        self.code_data = code_data
        self.to_be_rect = settings.SCREEN_WIDTH-346

        self.apperance = Apperance(
            self,
            [343, 537],
            colorKey=True,
            images=[
                [f'sylladex/uiElements/asset/{UIElement.get_modus()}/CARD_INSPECTOR.png', [
                    0, 0]],
                [UIElement.code_database.find_kind_image_small(
                    self.code_data.kind), [92, 164]],
                [UIElement.code_database.find_grist_image(
                    self.code_data.grist), [134, 212]],
            ],
            texts=[
                ['NAME', [36, 51], 'center', '#000000'],
                [self.code_data.name, [
                    65, 51], 'left', '#000000'],

                [UIElement.code_database.get_weapon_type(self.code_data.kind), [
                    275, 98], 'center', '#000000'],

                ['TRAIT 1', [46, 99], 'center', '#000000'],
                [self.code_data.trait_1, [
                    172, 99], 'center', '#000000'],

                ['TRAIT 2', [46, 132], 'center', '#000000'],
                [self.code_data.trait_2, [
                    172, 132], 'center', '#000000'],

                ['ITEMKIND', [52, 180], 'center', '#000000'],
                [self.check_for_custom(self.code_data.kind), [
                    178, 180], 'center', '#000000'],

                ['GRIST TYPE', [56, 228], 'center', '#000000'],
                [UIElement.code_database.get_grist_dice(self.code_data.grist), [
                    117, 228], 'center', '#000000'],
                [self.code_data.grist, [199, 228], 'center', '#000000'],

                ['INSPECT INFORMATION', [97, 365], 'center', '#000000'],

                ['CST', [28, 398], 'center', '#000000'],
                ['DMG', [28, 432], 'center', '#000000'],

                ['CODE', [117, 480], 'center', '#000000'],
                [self.code_data.code, [189, 480], 'center', '#000000'],

                ['/', [60, 398], 'center', '#000000'],
                ['/', [60, 432], 'center', '#000000'],
                ['/', [193, 414], 'center', '#000000']  # Max Char is 28
            ]
        )

        self.add_child(
            UIElement.get_ui_elem('CardInspectorButton')(self)
        )
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(85, 87, 'Trait1', self.trait_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(85, 120, 'Trait2', self.trait_desc))

        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(12, 276, 'Action1', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(12, 312, 'Action2', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(144, 276, 'Action3', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(144, 312, 'Action4', self.action_desc))

        self.add_child(UIElement.code_database.get_action_icon(
            self.code_data.action_1, 36, 276))
        self.add_child(UIElement.code_database.get_action_icon(
            self.code_data.action_2, 36, 312))
        self.add_child(UIElement.code_database.get_action_icon(
            self.code_data.action_3, 168, 276))
        self.add_child(UIElement.code_database.get_action_icon(
            self.code_data.action_4, 168, 312))

        self.add_child(UIElement.get_ui_elem('DropDown')(
            183,
            348,
            [120, 32],
            'Inspection',
            'Change the inspection type',
            [
                'PASSIVE',
                'INTERACTION',
                'STRIKE',
                'EQUIPPED',
                'MODUS SORT',
                'MODUS RETRIEVE',
            ],
            'PASSIVE',
            'Text',
            startLayer=1000,
            baseColors=[
                '#B7B7B7',
                '#D9D9D9',
                '#A3A3A3'
            ],
            exitCommand=self.change_inspect
        ))

    def reloadSelf(self):
        self.update()
        self.prevDescType = 'Reload'

    def update(self):
        if self.rect.x != self.to_be_rect:

            UIElement.move_element(
                self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), settings.SCREEN_HEIGHT / 2 - 219.5])
            self.children[0].rect.right = self.rect.left

        else:
            if self.to_be_rect == settings.SCREEN_WIDTH:
                UIElement.remove_from_group(self)

    def uncheck_all(self):
        for _i in range(1, 7):
            self.children[_i].selected = False
            self.children[_i].apperance.size_color_pos = [
                [[16, 16], '#434343', [4, 4]],
                [[12, 12], '#D8DDFF', [6, 6]]
            ]
            self.children[_i].apperance.reload_apperance()

        self._clear_desc()

    def _clear_desc(self):
        _text = self.apperance.kwargs['texts']

        while len(_text) > 17:
            _text.pop()

        _text.append(['/', [60, 398], 'center', '#000000'])
        _text.append(['/', [60, 432], 'center', '#000000'])
        _text.append(['/', [193, 414], 'center', '#000000'])

        self.apperance.kwargs['texts'] = _text
        self.apperance.reload_apperance()

    def check_for_custom(self, item: str):
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if item[:len(item) - 1] == 'KIND' or item[:len(item) - 1] == 'TRAIT':
            return _custom_data[item]['NAME']

        else:
            return item

    def line_positions(self, text: str) -> list:
        _words = text.split(' ')

        _lines = ['']

        _count = 0
        for _word in _words:
            if _count + len(_word) > 27:
                _count = len(_word) + 1
                _lines.append(_word + ' ')
            else:
                _count += len(_word) + 1
                _lines[len(_lines) - 1] += _word + ' '

        _section = 66 // len(_lines)

        _positions = []
        for _sec in range(_section):
            _positions.append([193, 381 + (_section // 2) + (_section * _sec)])

        return [_lines, _positions]

    def trait_desc(self, check: object):
        if check.job == 'Trait1':
            _lines_and_pos = self.line_positions(
                UIElement.code_database.get_trait_info(self.code_data.trait_1, self.children[11].current_option))
        elif check.job == 'Trait2':
            _lines_and_pos = self.line_positions(
                UIElement.code_database.get_trait_info(self.code_data.trait_2, self.children[11].current_option))

        _text = self.apperance.kwargs['texts']

        _text.pop()

        for _i in range(len(_lines_and_pos[0])):
            _text.append([_lines_and_pos[0][_i], _lines_and_pos[1]
                         [_i], 'center', '#000000'])

        self.apperance.kwargs['texts'] = _text
        self.apperance.reload_apperance()

    def change_inspect(self):
        if self.children[1].selected:
            self._clear_desc()
            self.trait_desc(self.children[1])
        elif self.children[2].selected:
            self._clear_desc()
            self.trait_desc(self.children[2])

    def action_desc(self, check: object):
        if check.job == 'Action1':
            _action_info = UIElement.code_database.get_action_info(
                self.code_data.action_1, UIElement.code_database.get_weapon_type(self.code_data.kind))

        elif check.job == 'Action2':
            _action_info = UIElement.code_database.get_action_info(
                self.code_data.action_2, UIElement.code_database.get_weapon_type(self.code_data.kind))

        elif check.job == 'Action3':
            _action_info = UIElement.code_database.get_action_info(
                self.code_data.action_3, UIElement.code_database.get_weapon_type(self.code_data.kind))

        elif check.job == 'Action4':
            _action_info = UIElement.code_database.get_action_info(
                self.code_data.action_4, UIElement.code_database.get_weapon_type(self.code_data.kind))

        _lines_and_pos = self.line_positions(_action_info[2])

        _text = self.apperance.kwargs['texts']

        _text[17] = [_action_info[0], [60, 398], 'center', '#000000']
        _text[18] = [_action_info[1], [60, 432], 'center', '#000000']

        _text.pop()

        for _i in range(len(_lines_and_pos[0])):
            _text.append([_lines_and_pos[0][_i], _lines_and_pos[1]
                         [_i], 'center', '#000000'])

        self.apperance.kwargs['texts'] = _text
        self.apperance.reload_apperance()
