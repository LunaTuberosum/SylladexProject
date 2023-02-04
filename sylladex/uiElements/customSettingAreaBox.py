import pygame as pg

from baseUI import UIBase

class CustomSettingAreaBox(UIBase):
    def __init__(self, parent, type_input, input_detail, y):
        self.type_input = type_input
        self.input_detail = input_detail
        self.parent = parent

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        if self.type_input == 'WEAPONKIND':
            _width = 280
            _height = 30
        elif self.type_input == 'ACTION':
            _width = 306
            _height = 102
        elif self.type_input == 'TRAIT':
            if self.input_detail[:4] == 'name':
                _width = 162
                _height = 30
            elif self.input_detail[:4] == 'tier':
                _width = 306
                _height = 78
        

        super().__init__(self.parent.rect.x+12, self.parent.rect.y+y, (_width,_height), f'CustomSettingAreaBox ({self.type_input})', (255,255,255))

        if self.type_input == 'WEAPONKIND':
            self.create_appearance([[274, 24], '#1C4587', [6, 6]], [[274, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['NAME', [48, 12], 'center'], ['TYPE', [202, 12], 'center']])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as _database:
                _custom_data = _database.readlines()

            if self.input_detail == 'kind1':
                curImage = _custom_data[1].split(',')[0]
                curKind = _custom_data[0].split(',')[0]
            elif self.input_detail == 'kind2':
                curImage = _custom_data[1].split(',')[1]
                curKind = _custom_data[0].split(',')[2]

            self.children = [
                UIBase.get_ui_elem('OptionToggle')(self.rect.x, self.rect.y, 24, 24, f'{self.input_detail}Icon' ,'#C9DAF8', list(UIBase.CodeDatabase.kind.keys()), curImage, curKind, 'Image'),
                UIBase.get_ui_elem('TextField')(self.rect.x+72, self.rect.y, 106, 24, 13, f'{self.input_detail}Name', f'Changes the name of {curKind}', 'Txt'),
                UIBase.get_ui_elem('OptionToggle')(self.rect.x+226, self.rect.y, 48, 24, f'{self.input_detail}Type' ,'#C9DAF8', ['NA','MELEE','RANGED','MAGIC'], UIBase.CodeDatabase.get_weaponType(curKind), curKind, 'Text')
            ]

            self.children[1].text = curKind
            self.children[1].font = self.font
            self.children[1].baseColor = '#C9DAF8'
            self.children[1].no_hover()
            self.children[1].hoverColor = '#D9E2F1'
            self.children[1].selectedColor = '#9CB0D5'

        elif self.type_input == 'ACTION':
            self.create_appearance([[300, 96], '#1C4587', [6, 6]], [[300, 96], '#3C78D8', [0, 0]], colorKey = True, texts = [['COST', [132, 12], 'center'], ['DMG', [228, 12], 'center'], ['ACTION DESCRPTION', [150, 36], 'center']])

            with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as _database:
                _custom_data = _database.readlines()

            if self.input_detail == 'action1':
                _cur_action = _custom_data[2].split(',')[0]
            elif self.input_detail == 'action2':
                _cur_action = _custom_data[2].split(',')[4]

            self.children = [
                UIBase.get_ui_elem('ActionIcon')(self.rect.x, self.rect.y, f'{self.input_detail}Icon'),
                UIBase.get_ui_elem('TextField')(self.rect.x+156, self.rect.y, 48, 24, 1, f'{self.input_detail}Cost', f'Change {_cur_action}\'s cost', 'Num'),
                UIBase.get_ui_elem('TextField')(self.rect.x+252, self.rect.y, 48, 24, 1, f'{self.input_detail}Dmg', f'Change {_cur_action}\'s damage', 'Num'),
                UIBase.get_ui_elem('LongTextField')(self.rect.x, self.rect.y+48, 300, 48, 28, 3, f'{self.input_detail}Desc', f'Change {_cur_action}\'s description')
            ]

            self.children[1].font = self.font
            self.children[1].baseColor = '#C9DAF8'
            self.children[1].no_hover()
            self.children[1].hoverColor = '#D9E2F1'
            self.children[1].selectedColor = '#9CB0D5'

            self.children[2].defultText = '/'
            self.children[2].font = self.font
            self.children[2].baseColor = '#C9DAF8'
            self.children[2].no_hover()
            self.children[2].hoverColor = '#D9E2F1'
            self.children[2].selectedColor = '#9CB0D5'

            self.children[3].font = self.font
            self.children[3].baseColor = '#C9DAF8'
            self.children[3].no_hover()
            self.children[3].hoverColor = '#D9E2F1'
            self.children[3].selectedColor = '#9CB0D5'


        elif self.type_input == 'TRAIT':
            if self.input_detail == 'name':
                self.create_appearance([[156, 24], '#1C4587', [6, 6]], [[156, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['NAME', [24, 12], 'center']])

                with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as _database:
                    _custom_data = _database.readlines()

                self.children = [
                    UIBase.get_ui_elem('TextField')(self.rect.x+48, self.rect.y, 108, 24, 13, 'traitName', f'Change the name of the trait', 'Txt')
                ]

                self.children[0].font = self.font
                self.children[0].baseColor = '#C9DAF8'
                self.children[0].no_hover()
                self.children[0].hoverColor = '#D9E2F1'
                self.children[0].selectedColor = '#9CB0D5'

            elif self.input_detail[:4] == 'tier':
                self.create_appearance([[300, 72], '#1C4587', [6, 6]], [[300, 72], '#3C78D8', [0, 0]], colorKey = True, texts = [['TIER '+self.input_detail[4:]+' DESCRIPTION', [150, 12], 'center']])

                self.children = [
                    UIBase.get_ui_elem('LongTextField')(self.rect.x, self.rect.y+24, 300, 48, 28, 3, f'{self.input_detail[4:]}Desc', f'Change the description for tiers {self.input_detail[4:]}')
                ]

                self.children[0].font = self.font
                self.children[0].baseColor = '#C9DAF8'
                self.children[0].no_hover()
                self.children[0].hoverColor = '#D9E2F1'
                self.children[0].selectedColor = '#9CB0D5'
    
    def update(self):

        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as _database:
                _custom_data = _database.readlines()

        if self.type_input == 'ACTION':
            for _elem in UIBase.get_group('ui'):
                if isinstance(_elem, UIBase.get_ui_elem('ToggleButton')):
                    if _elem.job == 'meleeToggle' and _elem.on == True:
                        if self.input_detail == 'action1':
                            if self.children[1].active == False:
                                self.children[1].text = _custom_data[2].split(',')[1]
                                self.children[1].no_hover()
                            if self.children[2].active == False:
                                self.children[2].text = _custom_data[2].split(',')[2]
                                self.children[2].no_hover()
                            break
                        elif self.input_detail == 'action2':
                            if self.children[1].active == False:
                                self.children[1].text = _custom_data[2].split(',')[5]
                                self.children[1].no_hover()
                            if self.children[2].active == False:
                                self.children[2].text = _custom_data[2].split(',')[6]
                                self.children[2].no_hover()
                            break
                    