import pygame as pg

from uiElement import UIElement, Apperance


class TextField(UIElement):

    def __init__(self, x: int, y: int, size: list, job: str, tool_tip_text: str, max_char: int, **kwargs: dict):

        super().__init__(
            x,
            y,
            f'TextField ({job})',
            kwargs['startLayer'] if 'startLayer' in kwargs else 1
        )

        self.kwargs = kwargs
        self.size = size

        self.max_char = max_char
        self.job = job
        self.active = False
        self.hovering = False

        self.tool_tip_text = tool_tip_text

        self.configure_kwargs()

        self.apperance = Apperance(
            self,
            self.size,
            [self.size, self.base_color, [0, 0]],
            texts=[[self.text, self.get_text_position(),
                    self.alginment[0], self.text_color]]
        )

    def configure_kwargs(self):
        if 'textColor' in self.kwargs:
            self.text_color = self.kwargs['textColor']
        else:
            self.text_color = '#000000'

        if 'textType' in self.kwargs:
            self.text_type = self.kwargs['textType']
        else:
            self.text_type = 'Txt'

        if 'fontSize' in self.kwargs:
            self.font_size = self.kwargs['fontSize']
        else:
            self.font_size = 24

        if 'textFont' in self.kwargs:
            self.text_font = self.kwargs['textFont']
        else:
            self.text_font = 'sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf'

        self.font = pg.font.Font(self.text_font, self.font_size)

        if 'baseColors' in self.kwargs:
            self.base_color = self.kwargs['baseColors'][0]
            self.hover_color = self.kwargs['baseColors'][1]
            self.selected_color = self.kwargs['baseColors'][2]
        else:
            self.base_color = (255, 255, 255)
            self.hover_color = (230, 230, 230)
            self.selected_color = (170, 170, 170)

        self.alginment = []
        if 'align' in self.kwargs:
            if self.kwargs['align'] == 'center':
                self.alginment.append('center')

            elif self.kwargs['align'] == 'right':
                self.alginment.append('right')
        else:
            self.alginment.append('left')

        if 'verticalAlign' in self.kwargs:
            if self.kwargs['verticalAlign'] == 'top':
                self.alginment.append('top')

            elif self.kwargs['verticalAlign'] == 'bottom':
                self.alginment.append('bottom')
        else:
            self.alginment.append('center')

        if self.text_type == 'Num':
            self.default_text = self.text = '0'
        else:
            self.default_text = self.text = ''

        if 'defaultText' in self.kwargs:
            self.default_text = self.text = self.kwargs['defaultText']

        if 'startText' in self.kwargs:
            self.text = self.kwargs['startText']

        if 'exitCommand' in self.kwargs:
            self.exit_command = self.kwargs['exitCommand']
        else:
            self.exit_command = None

    def exit_field(self):
        self.active = False

        if self.text == '':
            self.text = self.default_text

        self.apperance.size_color_pos = [
            [self.size, self.base_color, [0, 0]]
        ]
        self.reload_text()

        if self.exit_command:
            self.exit_command()

    def get_text_position(self):
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
            _pos.append(self.size[1] / 2)

        return _pos

    def typing(self, event):
        if self.active == True:

            if self.text == self.default_text:
                self.text = ''

            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pg.K_RETURN:

                self.exit_field()
                return

            else:
                if len(self.text) <= self.max_char:
                    if self.text_type == 'Num':
                        for _num in range(0, 10):
                            if event.unicode == str(_num):
                                self.text += event.unicode
                    else:
                        self.text += event.unicode

            self.reload_text()

    def reload_text(self):
        self.apperance.kwargs['texts'] = [
            [self.text, self.get_text_position(), self.alginment[0],
             self.text_color]
        ]
        self.apperance.reload_apperance()

    def hover(self):
        if self.active == False:
            self.apperance.size_color_pos = [
                [self.size, self.hover_color, [0, 0]]
            ]
            self.reload_text()
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.apperance.size_color_pos = [
                [self.size, self.base_color, [0, 0]]]
            self.reload_text()
            self.hovering = False

    def on_click(self):
        self.active = True
        self.apperance.size_color_pos = [
            [self.size, self.selected_color, [0, 0]]]
        self.apperance.reload_apperance()
