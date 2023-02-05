import pygame as pg

from uiElement import UIElement
import settings
from sylladex.captchalogueCards import codeDatabase

class CardInspector(UIElement):
    def __init__(self, code_data):
        super().__init__(settings.SCREEN_WIDTH-343, settings.SCREEN_HEIGHT / 2 - 219.5, (343, 447), 'CardInspector', (209,158,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.code_data = code_data
        self.prev_desc_type = 'None'
        UIElement.get_group('layer').change_layer(self, 3)

        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIElement.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 47], "center"],
                [self.code_data.name, [65, 47], "left"], 
                [codeDatabase.get_weaponkind_type(self.code_data.kind), [278, 83], "center"], 
                ["TRAIT 1", [46, 83], "center"], 
                [self.code_data.trait_1, [110, 83], 'left'],
                ["TRAIT 2", [46, 108], "center"], 
                [self.code_data.trait_2, [110, 108], 'left'],
                ["ITEMKIND", [52, 133], "center"], 
                [self.code_data.kind, [121, 133], 'left'],
                ['GRIST TYPE', [64, 158], 'center'], 
                [self.code_data.grist, [146, 158], 'left'],
                ['EFFECTIVE', [68, 183], 'center'], 
                ['INEFFECTIVE', [68, 208], 'center'], 
                ['INSPECT INFORMATION', [159, 304], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '1'), [283, 120], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '2'), [283, 145], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '3'), [283, 170], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, 'BD'), [283, 195], 'center'], 
                ['CST', [30, 331], 'center'], 
                ['DMG', [30, 361], 'center'], 
                ['CODE', [79, 399], 'center'], 
                [self.code_data.code, [151, 399], "center"],
                ['TIER', [223, 399], 'center'], 
                [self.code_data.tier, [265, 399], "center"],
                ['1', [247, 120], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 170], 'center'], 
                ['BD', [247, 195], 'center'],
                ['/', [60, 331], 'center'],
                ['/', [60, 361], 'center'],
                ['/', [192, 346], 'center'] #Max Char is 28
                ]
            )

        self.children = [
            UIElement.get_ui_elem('CardInspectorButton')(self),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+81, self.rect.y+71, 'Trait1'),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+81, self.rect.y+96, 'Trait2'),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+27, self.rect.y+232, 'Action1'),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+27, self.rect.y+257, 'Action2'),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+159, self.rect.y+232, 'Action3'),
            UIElement.get_ui_elem('CardInspectorCheck')(self.rect.x+159, self.rect.y+257, 'Action4'),
        ]

        codeDatabase.get_action_image(self.code_data.action_1, self, [51, 232])
        codeDatabase.get_action_image(self.code_data.action_2, self, [51, 257])
        codeDatabase.get_action_image(self.code_data.action_3, self, [183, 232])
        codeDatabase.get_action_image(self.code_data.action_4, self, [183, 257])

        _kind_icon = pg.image.load(codeDatabase.find_kind_image(self.code_data.kind)).convert_alpha()
        _kind_icon = pg.transform.scale(_kind_icon, [24, 24])
        self.image.blit(_kind_icon, [92, 121])

        _grist_icon = pg.image.load(codeDatabase.find_grist_image(self.code_data.grist)).convert_alpha()
        _grist_icon = pg.transform.scale(_grist_icon, [24, 24])
        self.image.blit(_grist_icon, [116, 146])

        for _index, _eff in enumerate(codeDatabase.gristData.get(self.code_data.grist).get('Effective')):
            _eff_icon = pg.image.load(codeDatabase.find_grist_image(_eff)).convert_alpha()
            _eff_icon = pg.transform.scale(_eff_icon, [24, 24])
            self.image.blit(_eff_icon, [124+(25*_index), 171])

        for _index, _diseff in enumerate(codeDatabase.gristData.get(self.code_data.grist).get('Diseffective')):
            _diseff_icon = pg.image.load(codeDatabase.find_grist_image(_diseff)).convert_alpha()
            _diseff_icon = pg.transform.scale(_diseff_icon, [24, 24])
            self.image.blit(_diseff_icon, [124+(25*_index), 197])

    def update(self):
        for _check in UIElement.get_ui_elem('CardInspectorCheck').checks:
            if _check.selected == True:
                if _check.job == 'Trait1' and self.prev_desc_type != 'Trait1':
                    self.prev_desc_type = 'Trait1'
                    _trait_desc = codeDatabase.get_trat_1_data(self.code_data.trait_1, self.code_data.kind, int(self.code_data.tier)).split(' ')
                    _lines = ['']

                    _word_max = 0
                    _cur_line = 0
                    for _word in _trait_desc:
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word}')
                            _cur_line += 1
                    
                    self.change_description(_lines, len(_lines))

                elif _check.job == 'Trait2' and self.prev_desc_type != 'Trait2':
                    self.prev_desc_type = 'Trait2'
                    _trait_desc = codeDatabase.get_trat_2_data(self.code_data.trait_2, self.code_data.kind, int(self.code_data.tier)).split(' ')
                    _lines = ['']


                    _word_max = 0
                    _cur_line = 0
                    for _word in _trait_desc:
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word} ')
                            _cur_line += 1

                    self.change_description(_lines, len(_lines))

                elif _check.job == 'Action1' and self.prev_desc_type != 'Action1':
                    self.prev_desc_type = 'Action1'
                    _action_info = codeDatabase.get_action_info(self.code_data.action_1)

                    _lines = ['']


                    _word_max = 0
                    _cur_line = 0
                    for _word in _action_info[2].split(' '):
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word} ')
                            _cur_line += 1

                    self.change_description(_lines, len(_lines), True, _action_info)

                elif _check.job == 'Action2' and self.prev_desc_type != 'Action2':
                    self.prev_desc_type = 'Action2'
                    _action_info = codeDatabase.get_action_info(self.code_data.action_2)

                    _lines = ['']


                    _word_max = 0
                    _cur_line = 0
                    for _word in _action_info[2].split(' '):
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word} ')
                            _cur_line += 1

                    print(_lines)

                    self.change_description(_lines, len(_lines), True, _action_info)

                elif _check.job == 'Action3' and self.prev_desc_type != 'Action3':
                    self.prev_desc_type = 'Action3'
                    _action_info = codeDatabase.get_action_info(self.code_data.action_3)

                    _lines = ['']


                    _word_max = 0
                    _cur_line = 0
                    for _word in _action_info[2].split(' '):
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word} ')
                            _cur_line += 1

                    self.change_description(_lines, len(_lines), True, _action_info)

                elif _check.job == 'Action4' and self.prev_desc_type != 'Action4':
                    self.prev_desc_type = 'Action4'
                    _action_info = codeDatabase.get_action_info(self.code_data.action_4)

                    _lines = ['']


                    _word_max = 0
                    _cur_line = 0
                    for _word in _action_info[2].split(' '):
                        if _word_max + len(_word) < 28:
                            _word_max += len(_word) + 1
                            _lines[_cur_line] += f'{_word} '
                        else:
                            _word_max = len(_word) + 1
                            _lines.append(f'{_word} ')
                            _cur_line += 1

                    self.change_description(_lines, len(_lines), True, _action_info)
                return

        if self.prev_desc_type != 'None':
            self.change_description('/', 1)
            self.prev_desc_type = 'None'

    def change_description(self, new_desc, line_count, is_action = False, action_data = None):
        self.create_appearance(
            colorKey = True, 
            
            image = [
                f'sylladex/uiElements/asset/{UIElement.get_modus()}/CARD_INSPECTOR.png', [0, 0]
                ], 
            
            texts = [
                ["NAME", [36, 47], "center"],
                [self.code_data.name, [65, 47], "left"], 
                [codeDatabase.get_weaponkind_type(self.code_data.kind), [278, 83], "center"], 
                ["TRAIT 1", [46, 83], "center"], 
                [self.code_data.trait_1, [110, 83], 'left'],
                ["TRAIT 2", [46, 108], "center"], 
                [self.code_data.trait_2, [110, 108], 'left'],
                ["ITEMKIND", [52, 133], "center"], 
                [self.code_data.kind, [121, 133], 'left'],
                ['GRIST TYPE', [64, 158], 'center'], 
                [self.code_data.grist, [146, 158], 'left'],
                ['EFFECTIVE', [68, 183], 'center'], 
                ['INEFFECTIVE', [68, 208], 'center'], 
                ['INSPECT INFORMATION', [159, 304], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '1'), [283, 120], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '2'), [283, 145], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, '3'), [283, 170], 'center'], 
                [codeDatabase.get_tier_damage_num(self.code_data.tier, 'BD'), [283, 195], 'center'], 
                ['CST', [30, 331], 'center'], 
                ['DMG', [30, 361], 'center'], 
                ['CODE', [79, 399], 'center'], 
                [self.code_data.code, [151, 399], "center"],
                ['TIER', [223, 399], 'center'], 
                [self.code_data.tier, [265, 399], "center"],
                ['1', [247, 120], 'center'], 
                ['2', [247, 146], 'center'], 
                ['3', [247, 170], 'center'], 
                ['BD', [247, 195], 'center']
                ]
            )

        if is_action == False:
            self.create_appearance(texts = [
                ['/', [60, 331], 'center'],
                ['/', [60, 361], 'center']])
        else:
            self.create_appearance(texts = [
                [action_data[0], [60, 331], 'center'],
                [action_data[1], [60, 361], 'center']])

        
        if line_count == 1:
            self.create_appearance(texts = [[new_desc[0], [192, 346], 'center']])
        
        elif line_count == 2:
            self.create_appearance(texts = [[new_desc[0], [192, 337], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 355], 'center']])
        
        elif line_count == 3:
            self.create_appearance(texts = [[new_desc[0], [192, 328], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 346], 'center']])
            self.create_appearance(texts = [[new_desc[2], [192, 364], 'center']])
        
        elif line_count == 4:
            self.create_appearance(texts = [[new_desc[0], [192, 326], 'center']])
            self.create_appearance(texts = [[new_desc[1], [192, 342], 'center']])
            self.create_appearance(texts = [[new_desc[2], [192, 355], 'center']])
            self.create_appearance(texts = [[new_desc[3], [192, 368], 'center']])

        for _child in self.children:
            if isinstance(_child, UIElement.get_ui_elem('ActionIcon')):
                _no_action = True
                break
            else:
                _no_action = False

        if _no_action == False:
            codeDatabase.get_action_image(self.code_data.action_1, self, [51, 232])
            codeDatabase.get_action_image(self.code_data.action_2, self, [51, 257])
            codeDatabase.get_action_image(self.code_data.action_3, self, [183, 232])
            codeDatabase.get_action_image(self.code_data.action_4, self, [183, 257])

        _kind_icon = pg.image.load(codeDatabase.find_kind_image(self.code_data.kind)).convert_alpha()
        _kind_icon = pg.transform.scale(_kind_icon, [24, 24])
        self.image.blit(_kind_icon, [92, 121])

        _grist_icon = pg.image.load(codeDatabase.find_grist_image(self.code_data.grist)).convert_alpha()
        _grist_icon = pg.transform.scale(_grist_icon, [24, 24])
        self.image.blit(_grist_icon, [116, 146])

        for _index, _eff in enumerate(codeDatabase.gristData.get(self.code_data.grist).get('Effective')):
            _eff_icon = pg.image.load(codeDatabase.find_grist_image(_eff)).convert_alpha()
            _eff_icon = pg.transform.scale(_eff_icon, [24, 24])
            self.image.blit(_eff_icon, [124+(25*_index), 171])

        for _index, _diseff in enumerate(codeDatabase.gristData.get(self.code_data.grist).get('Diseffective')):
            _diseff_icon = pg.image.load(codeDatabase.find_grist_image(_diseff)).convert_alpha()
            _diseff_icon = pg.transform.scale(_diseff_icon, [24, 24])
            self.image.blit(_diseff_icon, [124+(25*_index), 196])
