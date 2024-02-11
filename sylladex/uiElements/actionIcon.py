import pygame as pg

from uiElement import UIElement, Apperance


class ActionIcon(UIElement):

    def __init__(self, x: int, y: int, job: str, can_interact: bool = False, start_layer: int = 8):

        super().__init__(
            x,
            y,
            f'ActionIcon ({job})',
            start_layer
        )

        self.job = job
        self.can_interact = can_interact
        self.active = False
        self.hovering = False

        if self.can_interact:
            self.tool_tip_text = f'Change name of {self.job}'

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/fontstuck.ttf", 17)

        self.melee_color = '#FF4B2D'
        self.ranged_color = '#9B38F4'
        self.magic_color = '#6688FE'
        self.no_color = '#6D6D6D'
        self.basic_color = '#38F43D'
        self.buff_color = '#f1c232'

        self.current_color = self.melee_color
        self.prefix = 'AS'
        self.text = ''
        self.prev_tick = 0
        self.add_on = ''
        self.other = ''

        self.apperance = Apperance(
            self,
            [108, 24],
            [[107, 22], self.current_color, [0, 1]],
            [[101, 18], '#FFFFFF', [3, 3]],
            texts=[[self.prefix + self.text, [5, 13], 'left', self.current_color]]
        )

    def _change_type(self, new_type: str):
        if new_type == "AS":
            self.current_color = self.melee_color
            self.prefix = 'AS'
        elif new_type == "AR":
            self.current_color = self.ranged_color
            self.prefix = 'AR'
        elif new_type == "AC":
            self.current_color = self.magic_color
            self.prefix = 'AC'
        elif new_type == "AG":
            self.current_color = self.basic_color
            self.prefix = 'AG'
        elif new_type == "NO":
            self.current_color = self.no_color
            self.prefix = 'NO '
        elif new_type == "AB":
            self.current_color = self.buff_color
            self.prefix = 'AB'

        self.apperance.size_color_pos = [
            [[107, 22], self.current_color, [0, 1]],
            [[101, 18], '#FFFFFF', [3, 3]],
        ]

    def setup_icon(self, text: str) -> object:
        self._change_type(text[:2])
        self.text = text[2:]

        self.reload_text()

        return self

    def typing(self, event):
        if self.active:

            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pg.K_RETURN:
                self.exit_field()
                return

            else:
                if len(self.text) <= 8:
                    self.text += event.unicode
                    self.text = self.text.upper()

            self.reload_text()

    def exit_field(self):
        self.active = False
        self.reload_text()

        UIElement.get_parent(self).save_action_data()

    def update(self):
        if not self.active:
            return

        if pg.time.get_ticks() - self.prev_tick >= 1000:
            _temp = self.add_on
            self.add_on = self.other
            self.other = _temp
            self.prev_tick = pg.time.get_ticks()
        self.reload_text()

    def reload_text(self):
        if self.active:
            self.apperance.kwargs['texts'] = [
                [self.prefix + self.text + self.add_on, [5, 13], 'left', self.current_color]]
        else:
            self.apperance.kwargs['texts'] = [
                [self.prefix + self.text, [5, 13], 'left', self.current_color]]
        self.apperance.reload_apperance()

    def on_click(self):
        if not self.can_interact:
            return

        self.active = True
        self.reload_text()
        self.prev_tick = pg.time.get_ticks()
        self.add_on = '|'
        self.other = ''
