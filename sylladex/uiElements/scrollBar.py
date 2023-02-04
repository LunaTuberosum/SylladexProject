import pygame as pg

from baseUI import UIBase, Apperance


class ScrollBar(UIBase):
    __selected = False

    def __init__(self):
        if len(UIBase.get_ui_elem('CardList').get_list()) == 0:
            _size = 0
        else:
            if len(UIBase.get_ui_elem('CardList').get_list()) > 9:
                _sections = 625 / len(UIBase.get_ui_elem('CardList').get_list()) 
                _size = _sections * 8
            else:
                _size = 0

        super().__init__(273, 196, 'ScrollBar')

        self.apperance = Apperance(
            self, 
            [23, _size],
            [[23, _size], '#999999', [0, 0]]
        )

        self.rect_temp = self.rect.y

        self.hovering = False

    def hover(self):
        self.image.fill('#D9D9D9')
        self.hovering = True

    def no_hover(self):
        self.image.fill('#999999')
        self.hovering = False

    def on_click(self):
        ScrollBar.set_selected(True)

    def move_bar(self, pos):
        _check_num = 625 / len(UIBase.get_ui_elem('CardList').get_list())
        self.rect.y = pos[1]
        if self.rect.y < 196:
            self.rect.y = 196
            for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                _list_obj.rect.y = 196 + (70 * UIBase.get_ui_elem('CardList').get_list().index(_list_obj))
                if _list_obj.children:
                    _list_obj.place_children()

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                _list_obj.rect.y = 196 - (70 * ((len(UIBase.get_ui_elem('CardList').get_list())-9) - UIBase.get_ui_elem('CardList').get_list().index(_list_obj)))
                if _list_obj.children:
                    _list_obj.place_children()

        else:
            _num = _check_num
            _all_checks = []
            for _new_check in range(0, len(UIBase.get_ui_elem('CardList').get_list())-9):
                _all_checks.append(_num + 196)
                _num += _check_num

            for _check in _all_checks:
                if self.rect.y >= _check:

                    if UIBase.get_ui_elem('CardList').get_list()[0].rect.y > 196 - (70 * _all_checks.index(_check)):
                        
                        for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                            _list_obj.rect.y -= 70
                            if _list_obj.children:
                                _list_obj.place_children()
                
                if self.rect.y <= _check:

                    if UIBase.get_ui_elem('CardList').get_list()[0].rect.y < 196 - (70 * _all_checks.index(_check)):
                        
                        for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                            _list_obj.rect.y += 70
                            if _list_obj.children:
                                _list_obj.place_children()
                

    def move_bar_wheel(self, rel):
        _check_num = 625 / len(UIBase.get_ui_elem('CardList').get_list())
        self.rect.y += rel * 10
        if self.rect.y < 196:
            self.rect.y = 196
            for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                _list_obj.rect.y = 196 + (70 * UIBase.get_ui_elem('CardList').get_list().index(_list_obj))
                if _list_obj.children:
                    _list_obj.place_children()

        elif self.rect.y + self.rect.h > 821:
            self.rect.y = 821 - self.rect.h
            for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                _list_obj.rect.y = 196 - (70 * ((len(UIBase.get_ui_elem('CardList').get_list())-9) - UIBase.get_ui_elem('CardList').get_list().index(_list_obj)))
                if _list_obj.children:
                    _list_obj.place_children()

        else:
            _num = _check_num
            _all_checks = []
            for _new_check in range(0, len(UIBase.get_ui_elem('CardList').get_list())-9):
                _all_checks.append(_num + 196)
                _num += _check_num

            for _check in _all_checks:
                if self.rect.y >= _check:

                    if UIBase.get_ui_elem('CardList').get_list()[0].rect.y > 196 - (70 * _all_checks.index(_check)):
                        
                        for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                            _list_obj.rect.y -= 70
                            if _list_obj.children:
                                _list_obj.place_children()

                if self.rect.y <= _check:

                    if UIBase.get_ui_elem('CardList').get_list()[0].rect.y < 196 - (70 * _all_checks.index(_check)):
                        
                        for _list_obj in UIBase.get_ui_elem('CardList').get_list():
                            _list_obj.rect.y += 70
                            if _list_obj.children:
                                _list_obj.place_children()

    @classmethod
    def get_selected(cls):
        return cls.__selected

    @classmethod
    def set_selected(cls, new_selected):
        cls.__selected = new_selected