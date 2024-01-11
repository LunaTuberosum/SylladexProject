import pygame as pg
import json

from uiElement import UIElement, Apperance


class CustomSettingAreaBox(UIElement):
    def __init__(self, x: int, y: int, section: str, job: str):

        self.section = section
        self.job = job

        super().__init__(
            x,
            y,
            f'CustomSettingAreaBox ({self.section})',
            7
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        if self.section == "WEAPONKINDS":
            self.create_kind_area(_custom_data)

        elif self.section == "ACTIONS":
            self.create_action_area(_custom_data)

        elif self.section == "TRAITS":
            self.create_trait_area(_custom_data)

    def create_kind_area(self, _custom_data):
        _kind_data = _custom_data[self.job]

        self.apperance = Apperance(
            self,
            [286, 102],
            [[280, 24], '#1C4587', [6, 6]],
            [[280, 24], '#3C78D8', [0, 0]],
            [[24, 24], '#C9DAF8', [0, 0]],
            [[106, 24], '#C9DAF8', [72, 0]],
            [[54, 24], '#C9DAF8', [226, 0]],
            colorKey=True,
            texts=[
                ['NAME', [48, 12], 'center', '#000000'],
                ['TYPE', [202, 12], 'center', '#000000']]
        )

        self.add_child(UIElement.get_ui_elem('DropDown')(
            0,
            0,
            [24, 24],
            f'{self.job}Icon',
            f'The icon of custom {self.job}',
            list(UIElement.CodeDatabase.kind_image_small.keys()),
            _kind_data['ICON'],
            'Image',
            startLayer=8,
            lookup=UIElement.CodeDatabase.kind_image_small,
            grid=[9, 7],
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            exitCommand=self.save_kind_data
        ))

        self.add_child(UIElement.get_ui_elem('TextField')(
            72,
            0,
            [106, 24],
            f'{self.job}Name',
            f'The name of custom {self.job}',
            12,
            startLayer=8,
            fontSize=18,
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            defaultText=f'CUSTOMKIND {self.job[-1]}',
            startText=_kind_data['NAME'],
            exitCommand=self.save_kind_data
        ))

        self.add_child(UIElement.get_ui_elem('DropDown')(
            226,
            0,
            [54, 24],
            f'{self.job}Type',
            f'The type of custom {self.job}',
            [
                'NA',
                'MELEE',
                'RANGED',
                'MAGIC'
            ],
            _kind_data['TYPE'],
            'Text',
            startLayer=8,
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            exitCommand=self.save_kind_data
        ))

    def update_card_and_list(self):
        _card_list = UIElement.find_current_ui('CardList')
        if _card_list:
            for _card in _card_list.get_list():
                if '!' in _card.code_data.code or '?' in _card.code_data.code:
                    _id = _card.code_data.cardID

                    UIElement.CodeDatabase.read_code(
                        _card.code_data.name, _card.code_data.code, _card.code_data.tier, _card)

                    _card.code_data.cardID = _id
                    _card.card.redraw_card()

                    if _card.capta_card:
                        _card.capta_card.code_data = _card.code_data
                        _card.capta_card.redraw_card()

    def save_kind_data(self):
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        _custom_data[self.job]['ICON'] = self.children[0].current_option
        _custom_data[self.job]['NAME'] = self.children[1].text
        _custom_data[self.job]['TYPE'] = self.children[2].current_option

        _new_custon_data = json.dumps(_custom_data, indent=4)

        with open('sylladex/captchalogueCards/data/customData.json', 'w') as _custom_data_file:
            _custom_data_file.write(_new_custon_data)
        self.update_card_and_list()

        UIElement.get_ui_elem('ConsoleMessage')('Saved Custom')

    def create_action_area(self, _custom_data: dict):
        _action_data = _custom_data[self.job]

        self.apperance = Apperance(
            self,
            [306, 102],
            [[300, 96], '#1C4587', [6, 6]],
            [[300, 96], '#3C78D8', [0, 0]],
            [[108, 24], '#C9DAF8', [0, 0]],
            [[48, 24], '#C9DAF8', [156, 0]],
            [[48, 24], '#C9DAF8', [252, 0]],
            [[300, 48], '#C9DAF8', [0, 48]],
            colorKey=True,
            texts=[
                ['COST', [132, 12], 'center', '#000000'],
                ['DMG', [228, 12], 'center', '#000000'],
                ['ACTION DESCRPTION', [150, 36], 'center', '#000000']
            ]
        )

        self.add_child(UIElement.get_ui_elem('ActionIcon')(
            self.job, True).setup_icon('melee', _action_data))

        self.add_child(UIElement.get_ui_elem('TextField')(
            156,
            0,
            [48, 24],
            f'{self.job}Cost',
            f'The cost of custom {self.job}',
            1,
            startLayer=8,
            fontSize=18,
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            align='center',
            defaultText='/',
            startText=_action_data['AS']['COST'],
            exitCommand=self.save_action_data
        ))

        self.add_child(UIElement.get_ui_elem('TextField')(
            252,
            0,
            [48, 24],
            f'{self.job}Damage',
            f'The damage of custom {self.job}',
            1,
            startLayer=8,
            fontSize=18,
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            align='center',
            defaultText='/',
            startText=_action_data['AS']['DAMAGE'],
            exitCommand=self.save_action_data
        ))

        self.add_child(UIElement.get_ui_elem('LongTextField')(
            0,
            48,
            [300, 48],
            f'{self.job}Description',
            f'The description of custom {self.job}',
            36,
            startLayer=8,
            fontSize=18,
            baseColors=[
                '#C9DAF8',
                '#D9E2F1',
                '#9CB0D5'
            ],
            align='center',
            maxLine=4,
            defaultText='/',
            startText=_action_data['AS']['DESCRIPTION'],
            exitCommand=self.save_action_data
        ))

    def save_action_data(self):
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        _custom_data[self.job][self.children[0].prefix]['NAME'] = self.children[0].text
        _custom_data[self.job][self.children[0].prefix]['COST'] = self.children[1].text
        _custom_data[self.job][self.children[0].prefix]['DAMAGE'] = self.children[2].text
        _custom_data[self.job][self.children[0].prefix]['DESCRIPTION'] = ''.join(
            self.children[3].lines)

        _new_custon_data = json.dumps(_custom_data, indent=4)

        with open('sylladex/captchalogueCards/data/customData.json', 'w') as _custom_data_file:
            _custom_data_file.write(_new_custon_data)
        self.update_card_and_list()

        UIElement.get_ui_elem('ConsoleMessage')('Saved Custom')

    def create_trait_area(self, _custom_data: dict):
        _trait = 'TRAIT' + UIElement.find_current_ui("CustomSettingSectionName",
                                                     "CustomSettingSectionName (TRAITS)").cur_toggle
        _trait_data = _custom_data[_trait]

        if self.job[:4] == "tier":

            self.apperance = Apperance(
                self,
                [306, 102],
                [[300, 72], '#1C4587', [6, 6]],
                [[300, 72], '#3C78D8', [0, 0]],
                [[300, 48], '#C9DAF8', [0, 24]],
                colorKey=True,
                texts=[
                    [f'{self.job.upper()} DESCRIPTION', [150, 12],
                        'center', '#000000'],
                ]
            )

            self.add_child(UIElement.get_ui_elem('LongTextField')(
                0,
                24,
                [300, 48],
                f'{(self.job).upper()}Description',
                f'The description of custom TIER levels {self.job[5:]}',
                36,
                startLayer=8,
                fontSize=18,
                baseColors=[
                    '#C9DAF8',
                    '#D9E2F1',
                    '#9CB0D5'
                ],
                align='center',
                maxLine=4,
                defaultText='/',
                startText=_trait_data[self.job[5:]],
                exitCommand=self.save_trait_data
            ))

        else:

            self.apperance = Apperance(
                self,
                [168, 30],
                [[162, 24], '#1C4587', [6, 6]],
                [[162, 24], '#3C78D8', [0, 0]],
                [[114, 24], '#C9DAF8', [48, 0]],
                colorKey=True,
                texts=[
                    ['NAME', [24, 12],
                        'center', '#000000'],
                ]
            )

            self.add_child(UIElement.get_ui_elem('TextField')(
                48,
                0,
                [114, 24],
                f'{_trait}Name',
                f'The name of custom TRAIT',
                12,
                startLayer=8,
                fontSize=18,
                baseColors=[
                    '#C9DAF8',
                    '#D9E2F1',
                    '#9CB0D5'
                ],
                align='center',
                defaultText=f'CUSTOM TRAIT ' +
                UIElement.find_current_ui(
                    'CustomSettingMenu').children[9].cur_toggle,
                startText=_trait_data['NAME'],
                exitCommand=self.save_trait_data
            ))

    def save_trait_data(self):
        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        _trait_data = _custom_data['TRAIT' + UIElement.find_current_ui(
            'CustomSettingMenu').children[9].cur_toggle]

        if self.job == 'name':
            _trait_data['NAME'] = self.children[0].text
        else:
            _trait_data[self.job[5:]] = ''.join(self.children[0].lines)

        _new_custon_data = json.dumps(_custom_data, indent=4)

        with open('sylladex/captchalogueCards/data/customData.json', 'w') as _custom_data_file:
            _custom_data_file.write(_new_custon_data)
        self.update_card_and_list()

        UIElement.get_ui_elem('ConsoleMessage')('Saved Custom')
