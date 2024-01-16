import pygame as pg

from uiElement import UIElement, Apperance


class ScrollBar(UIElement):
    __selected = False

    def __init__(self, x, y):

        super().__init__(
            x,
            y,
            'ScrollBar',
            11
        )

        self.apperance = Apperance(
            self,
            [23, 0],
            [[23, 0], '#999999', [0, 0]]
        )
        self.update_size()

        self.rect_temp = self.rect.y

        self.hovering = False

    def update_size(self):
        if len(UIElement.get_ui_elem('CardList').get_list()) == 0:
            _size = 0
        else:
            if len(UIElement.get_ui_elem('CardList').get_list()) > 9:
                _sections = 625 / \
                    len(UIElement.get_ui_elem('CardList').get_list())
                _size = _sections * 8
            else:
                _size = 0

        self.apperance.change_size_color_pos(
            [23, _size], [[[23, _size], '#999999', [0, 0]]])

    def hover(self):
        self.image.fill('#D9D9D9')
        self.hovering = True

    def no_hover(self):
        self.image.fill('#999999')
        self.hovering = False

    def on_click(self):
        ScrollBar.set_selected(True)

    def move_bar(self, pos):
        _check_num = 625 / len(UIElement.get_ui_elem('CardList').get_list())
        self.rect.move_ip([0, pos])

        _move_amount = [0, 0]

        if self.rect.y <= 196:
            self.rect.y = 196
            _move_amount = [0, 196]

        elif self.rect.y + self.rect.h >= 821:
            self.rect.y = 821 - self.rect.h
            _move_amount = [0, 196]

        else:
            _num = _check_num
            _all_checks = []
            for _new_check in range(0, len(UIElement.get_ui_elem('CardList').get_list())-9):
                _all_checks.append(_num + 196)
                _num += _check_num

            for _check in _all_checks:
                if self.rect.y >= _check:
                    if UIElement.get_ui_elem('CardList').get_list()[0].rect.y > 196 - (70 * _all_checks.index(_check)):
                        _move_amount = [0, -70]

                if self.rect.y <= _check:
                    if UIElement.get_ui_elem('CardList').get_list()[0].rect.y < 196 - (70 * _all_checks.index(_check)):
                        _move_amount = [0, 70]

        for _list_obj in UIElement.get_ui_elem('CardList').get_list():
            _indv_move_amount = [_list_obj.rect.x,  _list_obj.rect.y]

            if self.rect.y == 196:
                _indv_move_amount[1] = (70 * UIElement.get_ui_elem(
                    'CardList').get_list().index(_list_obj))

            elif self.rect.y == 821 - self.rect.h:
                _indv_move_amount[1] = -(70 * ((len(UIElement.get_ui_elem('CardList').get_list(
                ))-9) - UIElement.get_ui_elem('CardList').get_list().index(_list_obj)))

            _indv_move_amount[0] += _move_amount[0]
            _indv_move_amount[1] += _move_amount[1]

            UIElement.move_element(_list_obj, _indv_move_amount)

    def move_bar_wheel(self, rel):
        self.move_bar(rel * 10)

    @classmethod
    def get_selected(cls):
        return cls.__selected

    @classmethod
    def set_selected(cls, new_selected):
        cls.__selected = new_selected
