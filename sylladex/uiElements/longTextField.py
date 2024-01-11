import pygame as pg

from sylladex.uiElements.textField import TextField


class LongTextField(TextField):

    def __init__(self, x: int, y: int, size: list, job: str, tool_tip_text: str, max_char: int, **kargs):
        super().__init__(x, y, size, job, tool_tip_text, max_char, **kargs)
        self.reload_text()

    def configure_kwargs(self):
        super().configure_kwargs()

        self.starter_text()

        if 'maxLine' in self.kwargs:
            self.max_line = self.kwargs['maxLine']
        else:
            self.max_line = 1

    def starter_text(self):
        self.lines = ['']
        _new_text = self.text.split(' ')

        _total_char = 0
        for _i, _text in enumerate(_new_text):
            if _total_char + len(_text) >= self.max_char:
                self.lines.append(_text + ' ')
                _total_char = len(_text) + 1

            else:
                self.lines[len(self.lines) - 1] += _text + ' '
                _total_char += len(_text) + 1

            if _i + 1 == len(_new_text):
                self.lines[len(self.lines) -
                           1] = self.lines[len(self.lines) - 1][:-1]

        self.text = self.lines[len(self.lines) - 1]

    def get_text_position(self, index=0):
        _pos = []
        if self.alginment[0] == 'center':
            _pos.append(self.size[0] / 2)
        elif self.alginment[0] == 'right':
            _pos.append(self.size[0]-2)
        else:
            _pos.append(2)

        if self.alginment[1] == 'up':
            _pos.append(2)
        elif self.alginment[1] == 'down':
            _pos.append(self.size[1]-2)
        else:
            _section = (self.size[1] / len(self.lines)) * (index)
            _pos.append(_section + ((self.size[1] / len(self.lines)) / 2))

        return _pos

    def reload_text(self):
        _texts = []
        for _i, _line in enumerate(self.lines):
            _texts.append([_line, self.get_text_position(
                _i), self.alginment[0], self.text_color])

        self.apperance.kwargs['texts'] = _texts
        self.apperance.reload_apperance()

    def typing(self, event):
        if self.active == True:
            if event.key == pg.K_BACKSPACE and len(self.lines) > 1:
                if len(self.text) == 0 or self.text == ' ':
                    self.lines.pop(len(self.lines) - 1)
                    self.text = self.lines[len(self.lines) - 1]
            super().typing(event)

            _text = self.text.split(' ')

            self.lines[len(self.lines) - 1] = ''

            _word_count = 0
            for _i, _word in enumerate(_text):
                if _word_count + len(_word) > self.max_char:
                    self.lines.append(_word)
                    if len(self.lines) > self.max_line:
                        self.lines.pop(len(self.lines) - 1)
                        self.lines[len(self.lines) - 1] += _word
                        self.text = self.text[:-1]
                    else:
                        self.text = self.lines[len(self.lines) - 1]
                        _word_count = len(_text)

                else:
                    self.lines[len(self.lines) - 1] += _word + ' '
                    _word_count += len(_word) + 1

            self.reload_text()

    def exit_field(self):

        if len(self.lines) == 1 and self.lines[0] == ' ':
            self.lines[0] = self.default_text
            self.text = self.default_text

        super().exit_field()

        self.reload_text()
