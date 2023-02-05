import pygame as pg

from uiElement import UIElement

class LongTextField(UIElement):

    def __init__(self, x, y, width, height, max_char, max_line_count, job, tool_tip_text, text_color=(0,0,0)):
        super().__init__(x, y, (width, height), f'LongTextField ({job})', (255,255,255))

        self.text_color = text_color
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.max_char = max_char
        self.max_line_count = max_line_count

        self.job = job
        self.active = False
        self.hovering = False

        self.tool_tip_text = tool_tip_text

        self.base_color = (255,255,255)
        self.hover_color = (230,230,230)
        self.selected_color = (170,170,170)

        self.lines = []

        for _line in range(self.max_line_count):
            self.lines.append('')

        self.active_line = self.lines[0]
        self.active_line_index = 0

    def starter_text(self, newText):
        self.lines = []
        for _line in range(self.max_line_count):
            self.lines.append('')

        self.active_line_index = 0
        self.active_line = self.lines[self.active_line_index]
      
        _new_text = newText.split()

        _total_char = 0
        for _index, _text in enumerate(_new_text):
            if _text[-1:] == '.': _text = _text[:-1] + ','
            
            if _total_char + len(_text) > self.max_char:
                self.lines[self.active_line_index] = self.active_line
                self.active_line_index += 1
                self.active_line = self.lines[self.active_line_index]
                self.active_line = _text + ' '
                _total_char = 0

            else:
                self.active_line += _text + ' '
                _total_char += len(_text) + 1

        self.lines[self.active_line_index] = self.active_line
        self.draw()
        self.no_hover()

    def exit_field(self):
        self.image.fill(self.base_color)
        self.active = False
        _full_desc = ''

        for _line in self.lines:
            _lines = _line.split()

            _line = ''
            for _line in _lines:
                if _line[-1:] == ',':
                    _line += _line[:-1]
                    _line += '.'
                    _line += ' '
                else:
                    _line += _line
                    _line += ' '
            _full_desc += _line

        if self.job == 'action1Desc' or self.job == 'action2Desc':
            for _elem in UIElement.get_group('ui'):
                if isinstance(_elem, UIElement.get_ui_elem('ToggleButton')):
                    if _elem.job == 'meleeToggle':
                        if _elem.on == True:
                            if self.job == 'action1Desc':
                                UIElement.CodeDatabase.change_code_value('Melee 1 Desc', _full_desc)
                            elif self.job == 'action2Desc':
                                UIElement.CodeDatabase.change_code_value('Melee 2 Desc', _full_desc)
                    if _elem.job == 'rangedToggle':
                        if _elem.on == True:
                            if self.job == 'action1Desc':
                                UIElement.CodeDatabase.change_code_value('Ranged 1 Desc', _full_desc)
                            elif self.job == 'action2Desc':
                                UIElement.CodeDatabase.change_code_value('Ranged 2 Desc', _full_desc)
                    if _elem.job == 'magicToggle':
                        if _elem.on == True:
                            if self.job == 'action1Desc':
                                UIElement.CodeDatabase.change_code_value('Magic 1 Desc', _full_desc)
                            elif self.job == 'action2Desc':
                                UIElement.CodeDatabase.change_code_value('Magic 2 Desc', _full_desc)
        
        elif self.job == '1-4Desc' or self.job == '5-8Desc' or self.job == '9-12Desc' or self.job == '13-16Desc':
            for _elem in UIElement.get_group('ui'):
                if isinstance(_elem, UIElement.get_ui_elem('ToggleButton')):
                    if _elem.job == 't1Toggle':
                        if _elem.on == True:
                            if self.job == '1-4Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 1 1-4', _full_desc)
                            elif self.job == '5-8Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 1 5-8', _full_desc)
                            elif self.job == '9-12Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 1 9-12', _full_desc)
                            elif self.job == '13-16Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 1 13-16', _full_desc)
                    if _elem.job == 't2Toggle':
                        if _elem.on == True:
                            if self.job == '1-4Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 2 1-4', _full_desc)
                            elif self.job == '5-8Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 2 5-8', _full_desc)
                            elif self.job == '9-12Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 2 9-12', _full_desc)
                            elif self.job == '13-16Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 2 13-16', _full_desc)
                    if _elem.job == 't3Toggle':
                        if _elem.on == True:
                            if self.job == '1-4Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 3 1-4', _full_desc)
                            elif self.job == '5-8Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 3 5-8', _full_desc)
                            elif self.job == '9-12Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 3 9-12', _full_desc)
                            elif self.job == '13-16Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 3 13-16', _full_desc)
                    if _elem.job == 't4Toggle':
                        if _elem.on == True:
                            if self.job == '1-4Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 4 1-4', _full_desc)
                            elif self.job == '5-8Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 4 5-8', _full_desc)
                            elif self.job == '9-12Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 4 9-12', _full_desc)
                            elif self.job == '13-16Desc':
                                UIElement.CodeDatabase.change_code_value('Trait 4 13-16', _full_desc)

    def draw(self):
        self.image.fill(self.selected_color)

        _sections = self.rect.h/len(self.lines)

        for _index, _line in enumerate(self.lines):
            _txt_surface = self.font.render(_line, True, self.text_color)
            self.image.blit(_txt_surface, (self.rect.w/2-_txt_surface.get_width()/2, (_sections*_index)+((_sections/2)-_txt_surface.get_height()/2)))

    def typeing(self, event):

        if self.active == True:
            if event.key == pg.K_BACKSPACE:
                self.active_line = self.active_line[:-1]
        
                self.lines[self.active_line_index] = self.active_line
                self.draw()

                if self.active_line_index > 0:
                    if len(self.active_line) == 0:
                        self.active_line_index -= 1
                        self.active_line = self.lines[self.active_line_index]

            elif event.key == pg.K_RETURN:
                if self.active_line_index == 0 and (self.active_line == '' or self.active_line == ' '):
                    self.active_line = '/'
                self.active = False
                self.lines[self.active_line_index] = self.active_line
                self.exit_field()
                self.draw()
                return

            else:
                if event.key != pg.K_RETURN:
                    self.active_line += event.unicode

                    wordSections = self.active_line.split()

                    totalCharCount = 0
                    for _index, sect in enumerate(wordSections):
                        if totalCharCount + len(sect) > self.max_char:
                            self.active_line = self.active_line[:-len(sect)]

                            self.lines[self.active_line_index] = self.active_line
                            if self.active_line_index + 1 == self.max_line_count:
                                return
                            
                            self.active_line_index += 1
                            self.active_line = self.lines[self.active_line_index]

                            self.active_line += sect
                        else:
                            totalCharCount += len(sect) + 1

                        self.lines[self.active_line_index] = self.active_line
                        self.draw()

    def hover(self):
        if self.active == False:
            self.image.fill(self.hover_color)
            _sections = self.rect.h/len(self.lines)

            for _index, _line in enumerate(self.lines):
                _txt_surface = self.font.render(_line, True, self.text_color)
                self.image.blit(_txt_surface, (self.rect.w/2-_txt_surface.get_width()/2, (_sections*_index)+((_sections/2)-_txt_surface.get_height()/2)))
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.image.fill(self.base_color)
            _sections = self.rect.h/len(self.lines)

            for _index, _line in enumerate(self.lines):
                _txt_surface = self.font.render(_line, True, self.text_color)
                self.image.blit(_txt_surface, (self.rect.w/2-_txt_surface.get_width()/2, (_sections*_index)+((_sections/2)-_txt_surface.get_height()/2)))
            self.hovering = False

    def on_click(self):
        self.active = True
        _sections = self.rect.h/len(self.lines)
        self.draw()

        for _index, _line in enumerate(self.lines):
            _txt_surface = self.font.render(_line, True, self.text_color)
            self.image.blit(_txt_surface, (self.rect.w/2-_txt_surface.get_width()/2, (_sections*_index)+((_sections/2)-_txt_surface.get_height()/2)))
        