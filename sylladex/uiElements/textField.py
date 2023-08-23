import pygame as pg

from uiElement import UIElement, Apperance


class TextField(UIElement):

    def __init__(self, x: int, y: int, size: tuple, job: str, tool_tip_text: str, max_char: int, **kargs):

        super().__init__(
            x,
            y,
            f'TextField ({job})',
            kargs['startLayer'] if 'startLayer' in kargs else 1
        )

        self.kargs = kargs
        self.size = size

        self.max_char = max_char
        self.job = job
        self.active = False
        self.hovering = False

        self.tool_tip_text = tool_tip_text

        if 'textColor' in self.kargs:
            self.text_color = self.kargs['textColor']
        else:
            self.text_color = '#000000'

        if 'textType' in self.kargs:
            self.text_type = self.kargs['textType']
        else:
            self.text_type = 'Txt'

        if 'fontSize' in self.kargs:
            self.font_size = self.kargs['fontSize']
        else:
            self.font_size = 24

        if 'textFont' in self.kargs:
            self.text_font = self.kargs['textFont']
        else:
            self.text_font = 'sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf'

        self.font = pg.font.Font(self.text_font, self.font_size)

        if 'baseColors' in self.kargs:
            self.base_color = self.kargs['baseColors'][0]
            self.hover_color = self.kargs['baseColors'][1]
            self.selected_color = self.kargs['baseColors'][2]
        else:
            self.base_color = (255, 255, 255)
            self.hover_color = (230, 230, 230)
            self.selected_color = (170, 170, 170)

        if 'align' in self.kargs:
            if self.kargs['align'] == 'center':
                self.text_postion = [self.size[0]/2, self.size[1]/2]
                self.alginment = 'center'
            elif self.kargs['align'] == 'right':
                self.text_postion = [self.size[0]-2, self.size[1]/2]
                self.alginment = 'right'
        else:
            self.text_postion = [2, self.size[1]/2]
            self.alginment = 'left'

        if 'exitCommand' in self.kargs:
            self.exit_command = self.kargs['exitCommand']
        else:
            self.exit_command = None

        if self.text_type == 'Num':
            self.defult_text, self.text = '0', '0'

        else:
            self.defult_text, self.text = '', ''

        if 'startText' in self.kargs:
            self.text = self.kargs['startText']

        self.apperance = Apperance(
            self,
            self.size,
            [self.size, self.base_color, [0, 0]],
            texts=[[self.text, self.text_postion,
                    self.alginment, self.text_color]]
        )

    def exit_field(self):
        self.active = False

        if self.text == '':
            self.text = self.defult_text

        self.apperance.kargs['texts'] = [
            [self.text, self.text_postion, self.alginment, self.text_color]]
        self.apperance.size_color_pos = [[self.size, self.base_color, [0, 0]]]

        self.apperance.reload_apperance()

        if self.exit_command:
            self.exit_command()

    def typing(self, event):

        if self.active == True:

            if self.text == self.defult_text:
                self.text = ''

            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pg.K_RETURN:

                self.exit_field()
                return

            else:
                if len(self.text) < self.max_char:
                    if self.text_type == 'Num':
                        for _num in range(0, 9):
                            if event.unicode == str(_num):
                                self.text += event.unicode
                    else:
                        self.text += event.unicode

            self.apperance.kargs['texts'] = [
                [self.text, self.text_postion, self.alginment, self.text_color]]
            self.apperance.reload_apperance()

    def hover(self):
        if self.active == False:
            self.apperance.kargs['texts'] = [[self.text, [self.size[0]/2, self.size[1]/2],
                                              self.kargs['align'] if 'align' in self.kargs else 'center', self.text_color]]
            self.apperance.size_color_pos = [
                [self.size, self.hover_color, [0, 0]]]
            self.apperance.reload_apperance()
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.apperance.kargs['texts'] = [[self.text, [self.size[0]/2, self.size[1]/2],
                                              self.kargs['align'] if 'align' in self.kargs else 'center', self.text_color]]
            self.apperance.size_color_pos = [
                [self.size, self.base_color, [0, 0]]]
            self.apperance.reload_apperance()
            self.hovering = False

    def on_click(self):
        self.active = True
        self.apperance.size_color_pos = [
            [self.size, self.selected_color, [0, 0]]]
        self.apperance.reload_apperance()
