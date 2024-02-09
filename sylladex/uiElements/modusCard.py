import json
import pygame as pg

from uiElement import UIElement, Apperance


class ModusCard(UIElement):
    def __init__(self, x: int, code: str, color: str, active: bool):

        self.code = code
        self.color = color

        with open('sylladex/uiElements/data/modusColors.json') as _modus_colors_file:
            _modus_colors = json.load(_modus_colors_file)

        self.main_color = _modus_colors[self.color]['foreground']
        self.side_color = _modus_colors[self.color]['background']

        super().__init__(
            x,
            910,
            f'ModusCard ({self.code})',
            11
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 16)

        self.apperance = Apperance(
            self,
            [78, 102],
            [[60, 70], self.side_color, [9, 15]],
            [[42, 77], self.main_color, [6, 5]],
            [[9, 61], self.main_color, [48, 21]],
            [[9, 52], self.main_color, [57, 30]],
            [[10, 40], self.side_color, [31, 30]],
            [[40, 10], self.side_color, [16, 45]],
            colorKey=True,
            images=[
                ['sylladex/uiElements/asset/MISC/MODUS.png', [0, 0]]
            ]
        )

        self.active = active
        if self.code == '-':
            self.tool_tip_text = 'Create new modus'
        else:
            self.tool_tip_text = f'Changes the modus to {UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(self.code[2], "3"), "SORT NAME")}-{UIElement.code_database.get_trait_info(UIElement.code_database.get_code_value(self.code[3], "4"), "RETRIEVE NAME")} MODUS'

        self.hovering = False

        self.to_be_rect = self.rect.y
        self.redraw()

    def redraw(self):
        if self.code != '-':
            self.apperance.size_color_pos = [
                [[60, 70], self.side_color, [9, 15]],
                [[42, 77], self.main_color, [6, 5]],
                [[9, 61], self.main_color, [48, 21]],
                [[9, 52], self.main_color, [57, 30]],
            ]

            self.apperance.kwargs['texts'] = [
                [UIElement.code_database.get_trait_info(
                    UIElement.code_database.get_code_value(self.code[2], '3'), 'SORT NAME'), [37, 46], 'center', '#FFFFFF'],
                [UIElement.code_database.get_trait_info(
                    UIElement.code_database.get_code_value(self.code[3], '4'), 'RETRIEVE NAME'), [37, 56], 'center', '#FFFFFF']
            ]
        else:
            self.apperance.size_color_pos = [
                [[60, 70], self.side_color, [9, 15]],
                [[42, 77], self.main_color, [6, 5]],
                [[9, 61], self.main_color, [48, 21]],
                [[9, 52], self.main_color, [57, 30]],
                [[10, 40], self.side_color, [31, 30]],
                [[40, 10], self.side_color, [16, 45]],
            ]

            self.apperance.kwargs['texts'] = []

        if self.active:

            self.apperance.change_images([
                ['sylladex/uiElements/asset/MISC/MODUS_ACTIVE.png', [0, 0]]
            ])

        self.apperance.reload_apperance()

    def update(self):

        if self.to_be_rect != self.rect.y:

            UIElement.move_element(self, [self.rect.x, UIElement.lerp(
                self.rect.y, self.to_be_rect, 0.2)])

    def on_click(self):
        if self.code == '-':
            if not UIElement.find_current_ui('ModusAddCard'):
                UIElement.get_ui_elem('ModusAddCard')()
        # UIElement.set_modus(self.modus)
        # for elem in UIElement.get_group("ui"):
        #     if isinstance(elem, UIElement.get_ui_elem('ModusCard')):
        #         if elem == self:
        #             elem.apperance.change_images(
        #                 [
        #                     [f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS_ACTIVE.png', [0, 0]]
        #                 ])
        #             elem.rect.y = 907
        #         else:
        #             elem.apperance.change_images(
        #                 [
        #                     [f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS.png', [6, 6]]
        #                 ])
        #             elem.rect.y = 910

        #     elem.apperance.reload_apperance()
        #     if hasattr(elem, 'reload_image'):
        #         elem.reload_image()

    def hover(self):
        self.rect.y = 900
        self.to_be_rect = 900
        self.hovering = True

    def no_hover(self):
        self.to_be_rect = 910
        self.hovering = False
