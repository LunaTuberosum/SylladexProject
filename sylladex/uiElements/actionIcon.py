import pygame as pg

from uiElement import UIElement, Apperance


class ActionIcon(UIElement):

    def __init__(self, job: str, image_item: bool = False, action_type: str = "NA", custom_name: str = ''):

        super().__init__(
            0,
            0,
            f'ActionIcon ({job})',
            2
        )

        self.job = job
        self.active = False
        self.hovering = False
        self.image_item = image_item

        self.tool_tip_text = f'Change name of {job}'

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 8)

        self.melee_color = '#FF4B2D'
        self.ranged_color = '#9B38F4'
        self.magic_color = '#6688FE'

        if self.image_item == False:
            self.current_color = self.melee_color

            self.prefix = 'AS'

            self.text = ''
        else:

            if action_type == "MELEE":
                self.current_color = self.melee_color
                self.prefix = 'AS'
            elif action_type == "RANGED":
                self.current_color = self.ranged_color
                self.prefix = 'AR'
            elif action_type == "MAGIC":
                self.current_color = self.magic_color
                self.prefix = 'AC'

            self.text = custom_name[2:]

        self.apperance = Apperance(
            self,
            [108, 24],
            [[107, 22], self.current_color, [0, 1]],
            [[101, 18], '#FFFFFF', [3, 3]],
            texts=[[self.prefix + self.text, [5, 13], 'left', self.current_color]]
        )

    def change_type(self, new_type):
        if new_type == "melee":
            self.current_color = self.melee_color
            self.prefix = 'AS'
        elif new_type == "ranged":
            self.current_color = self.ranged_color
            self.prefix = 'AR'
        elif new_type == "magic":
            self.current_color = self.magic_color
            self.prefix = 'AC'

        self.apperance.size_color_pos = [
            [[107, 22], self.current_color, [0, 1]],
            [[101, 18], '#FFFFFF', [3, 3]],
        ]

        self.apperance.kargs['texts'] = [
            [self.prefix + self.text, [5, 13], 'left', self.current_color]]

        self.apperance.reload_apperance()
