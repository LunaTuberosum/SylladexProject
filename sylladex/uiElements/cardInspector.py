import json
import pygame as pg

from uiElement import Apperance, UIElement
import settings
from sylladex.captchalogueCards import codeDatabase


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

        self.actions_values = []

        self.apperance = Apperance(
            self,
            [346, 447],
            colorKey=True,
            images=[
                [f'sylladex/uiElements/asset/{UIElement.get_modus()}/CARD_INSPECTOR.png', [
                    0, 0]],
                [codeDatabase.find_kind_image_small(
                    self.code_data.kind), [92, 121]],
                [codeDatabase.find_grist_image_small(
                    self.code_data.grist), [116, 146]],
                [codeDatabase.get_action_image(
                    self.code_data.action_1, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2), 51, 232), [51, 232]],
                [codeDatabase.get_action_image(
                    self.code_data.action_2, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2), 51, 256), [51, 256]],
                [codeDatabase.get_action_image(
                    self.code_data.action_3, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2), 183, 232), [183, 232]],
                [codeDatabase.get_action_image(
                    self.code_data.action_4, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2), 183, 256), [183, 256]]
            ],
            texts=[
                ['NAME', [36, 48], 'center', '#000000'],
                [self.code_data.name, [
                    65, 48], 'left', '#000000'],
                [codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2), [
                    281, 84], 'center', '#000000'],
                ['TRAIT 1', [46, 84], 'center', '#000000'],
                [self.check_for_custom(self.code_data.trait_1), [
                    108, 83], 'left', '#000000'],
                ['TRAIT 2', [46, 109], 'center', '#000000'],
                [self.check_for_custom(self.code_data.trait_2), [
                    108, 108], 'left', '#000000'],
                ['ITEMKIND', [52, 134], 'center', '#000000'],
                [self.check_for_custom(self.code_data.kind), [
                    118, 134], 'left', '#000000'],
                ['GRIST TYPE', [64, 159], 'center', '#000000'],
                [self.code_data.grist, [146, 159], 'left', '#000000'],
                ['EFFECTIVE', [68, 184], 'center', '#000000'],
                ['INEFFECTIVE', [68, 209], 'center', '#000000'],
                ['INSPECT INFORMATION', [159, 305], 'center', '#000000'],
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '1'), [
                    286, 121], 'center', '#000000'],
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '2'), [
                    286, 146], 'center', '#000000'],
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '3'), [
                    286, 171], 'center', '#000000'],
                [codeDatabase.get_tier_damage_num(self.code_data.tier, 'BD'), [
                    286, 196], 'center', '#000000'],
                ['CST', [30, 332], 'center', '#000000'],
                ['DMG', [30, 362], 'center', '#000000'],
                ['CODE', [79, 400], 'center', '#000000'],
                [self.code_data.code, [151, 400], 'center', '#000000'],
                ['TIER', [223, 400], 'center', '#000000'],
                [self.code_data.tier, [265, 400], 'center', '#000000'],
                ['1', [250, 121], 'center', '#000000'],
                ['2', [250, 147], 'center', '#000000'],
                ['3', [250, 171], 'center', '#000000'],
                ['BD', [250, 196], 'center', '#000000'],
                ['/', [60, 332], 'center', '#000000'],
                ['/', [60, 362], 'center', '#000000'],
                ['/', [191, 346], 'center', '#000000']  # Max Char is 28
            ]
        )

        self.add_child(
            UIElement.get_ui_elem('CardInspectorButton')(self)
        )
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(81, 71, 'Trait1', self.trait_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(81, 96, 'Trait2', self.trait_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(27, 232, 'Action1', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(27, 257, 'Action2', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(159, 232, 'Action3', self.action_desc))
        self.add_child(UIElement.get_ui_elem(
            'CardInspectorCheck')(159, 257, 'Action4', self.action_desc))

        for _action in self.actions_values:
            self.add_child(_action)

        _images = self.apperance.kwargs['images']
        for _index, _eff in enumerate(codeDatabase.grist_data.get(self.code_data.grist).get('Effective')):
            _images.append(
                [codeDatabase.find_grist_image_small(
                    _eff), [127+(25*_index), 171]]
            )

        for _index, _diseff in enumerate(codeDatabase.grist_data.get(self.code_data.grist).get('Diseffective')):
            _images.append([codeDatabase.find_grist_image_small(
                _diseff), [127+(25*_index), 197]])

        self.apperance.change_images(_images)

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

        _text = self.apperance.kwargs['texts']

        while len(_text) > 28:
            _text.pop()

        _text.append(['/', [60, 332], 'center', '#000000'])
        _text.append(['/', [60, 362], 'center', '#000000'])
        _text.append(['/', [191, 346], 'center', '#000000'])

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
            if _count + len(_word) > 28:
                _count = len(_word) + 1
                _lines.append(_word + ' ')
            else:
                _count += len(_word) + 1
                _lines[len(_lines) - 1] += _word + ' '

        _section = 58 // len(_lines)

        _positions = []
        for _sec in range(_section):
            _positions.append([195, 317 + (_section // 2) + (_section * _sec)])

        return [_lines, _positions]

    def trait_desc(self, check: object):
        if check.job == 'Trait1':
            _lines_and_pos = self.line_positions(
                codeDatabase.get_trait_1_data(self.code_data))
        elif check.job == 'Trait2':
            _lines_and_pos = self.line_positions(
                codeDatabase.get_trait_2_data(self.code_data))

        _text = self.apperance.kwargs['texts']

        _text.pop()

        for _i in range(len(_lines_and_pos[0])):
            _text.append([_lines_and_pos[0][_i], _lines_and_pos[1]
                         [_i], 'center', '#000000'])

        self.apperance.kwargs['texts'] = _text
        self.apperance.reload_apperance()

    def action_desc(self, check: object):
        if check.job == 'Action1':
            _action_info = codeDatabase.get_action_info(
                self.code_data.action_1, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2))

        elif check.job == 'Action2':
            _action_info = codeDatabase.get_action_info(
                self.code_data.action_2, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2))

        elif check.job == 'Action3':
            _action_info = codeDatabase.get_action_info(
                self.code_data.action_3, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2))

        elif check.job == 'Action4':
            _action_info = codeDatabase.get_action_info(
                self.code_data.action_4, codeDatabase.get_weapon_type(self.code_data.kind, self.code_data.trait_2))

        _lines_and_pos = self.line_positions(_action_info[2])

        _text = self.apperance.kwargs['texts']

        _text[28] = [_action_info[0], [60, 332], 'center', '#000000']
        _text[29] = [_action_info[1], [60, 362], 'center', '#000000']

        _text.pop()

        for _i in range(len(_lines_and_pos[0])):
            _text.append([_lines_and_pos[0][_i], _lines_and_pos[1]
                         [_i], 'center', '#000000'])

        self.apperance.kwargs['texts'] = _text
        self.apperance.reload_apperance()
