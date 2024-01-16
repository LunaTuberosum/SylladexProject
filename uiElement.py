import math
import pygame as pg

# Class that creates UIElements apperance


class Apperance():
    __modus_color = {
        'STACK': {
            'background': '#9B2448',
            'foreground': '#FF00DC',
            'accent': '#FF61DC'
        },
        'QUEUE': {
            'background': '#CF560C',
            'foreground': '#FF6000',
            'accent': '#FF912B'
        },
        'TREE': {
            'background': '#7CA619',
            'foreground': '#96FF00',
            'accent': '#CDFF2B'
        }
    }

    def __init__(
        self,
        obj: object,
        base_size: list,
        *size_color_pos: list,
        **kwargs
    ):

        self.base_size = base_size

        self.obj = obj
        self.obj.image = pg.Surface(self.base_size)
        self.obj.image.fill('#D8DDFF')

        self.size_color_pos = size_color_pos
        self.kwargs = kwargs

        self.obj.rect = self.obj.image.get_rect(topleft=self.obj.rect)
        self.reload_apperance()

    def reload_apperance(self):

        self.obj.image = pg.Surface(self.base_size)
        self.obj.image.fill('#D8DDFF')
        self.obj.rect = self.obj.image.get_rect(topleft=self.obj.rect.topleft)

        if 'colorKey' in self.kwargs:
            self.obj.image.set_colorkey('#D8DDFF')

        for _rect in self.size_color_pos:
            _rect_ = pg.Surface(_rect[0])
            if _rect[1] == 'ModusBackground':
                _rect_.fill(Apperance.__modus_color.get(
                    UIElement.get_modus()).get('background'))
            elif _rect[1] == 'ModusForeground':
                _rect_.fill(Apperance.__modus_color.get(
                    UIElement.get_modus()).get('foreground'))
            elif _rect[1] == 'ModusAccent':
                _rect_.fill(Apperance.__modus_color.get(
                    UIElement.get_modus()).get('accent'))
            else:
                _rect_.fill(_rect[1])
            self.obj.image.blit(_rect_, _rect[2])

        if 'alpha' in self.kwargs:
            self.obj.image.set_alpha(self.kwargs['alpha'])

        if 'images' in self.kwargs:
            for _image in self.kwargs['images']:
                _img = pg.image.load(_image[0]).convert_alpha()
                if 'imageAlpha' in self.kwargs:
                    _img.set_alpha(self.kwargs['imageAlpha'])
                self.obj.image.blit(_img, _image[1])

        if 'texts' in self.kwargs:
            for _text in self.kwargs['texts']:

                if len(_text) == 5:
                    self.obj.font = pg.font.Font(_text[4][0], _text[4][1])

                if _text[3] == 'ModusBackground':
                    _text_ = self.obj.font.render(_text[0], True,
                                                  Apperance.__modus_color.get(UIElement.get_modus()).get('background'))
                elif _text[3] == 'ModusForeground':
                    _text_ = self.obj.font.render(_text[0], True,
                                                  Apperance.__modus_color.get(UIElement.get_modus()).get('foreground'))
                elif _text[3] == 'ModusAccent':
                    _text_ = self.obj.font.render(_text[0], True,
                                                  Apperance.__modus_color.get(UIElement.get_modus()).get('accent'))
                else:
                    _text_ = self.obj.font.render(_text[0], True, _text[3])
                if _text[2] == 'center':
                    self.obj.image.blit(_text_, [
                                        _text[1][0]-(_text_.get_width()/2), (_text[1][1]-(_text_.get_height()/2))])
                elif _text[2] == 'left':
                    self.obj.image.blit(
                        _text_, [_text[1][0], (_text[1][1]-(_text_.get_height()/2))])

    def change_images(self, images: list):
        self.kwargs['images'] = images
        self.reload_apperance()

    def change_size(self, size: list, new_size_color_pos: list):
        self.base_size = size
        self.size_color_pos = new_size_color_pos
        self.reload_apperance()


# Class that holds data for all UIElements

class UIElement(pg.sprite.Sprite):
    __modus = "STACK"
    __ui_elements = pg.sprite.Group()
    __ui_layers = pg.sprite.LayeredUpdates()

    __current_ui = {}

    code_database = None
    code_data = None

    def __init__(
        self,
        x: int,
        y: int,
        obj_name: str,
        startLayer: int,
    ):

        super().__init__()

        UIElement.add_to_group(self)
        UIElement.change_layer(self, startLayer)

        self.obj_name = obj_name
        self.tool_tip_text = ''
        self.hovering = False

        self.children = []

        self.rect = [x, y]
        self.apperance = None

        self.clock = pg.time.Clock()
        self.current_tick = 0

    def add_child(self, elem):
        self.children.append(elem)

        elem.rect.x += self.rect.x
        elem.rect.y += self.rect.y

        if UIElement.has_children(elem):
            for child in elem.children:
                child.rect.x += self.rect.x
                child.rect.y += self.rect.y

    def on_click(self):
        pass

    def hover(self):
        pass

    def no_hover(self):
        pass

    @classmethod
    def move_element(cls, elem: object, moveAmount: list):
        if UIElement.has_children(elem):
            _child_offsets = []
            for _child in elem.children:
                _child_offsets.append([
                    abs(elem.rect.x - _child.rect.x),
                    abs(elem.rect.y - _child.rect.y)])

        elem.rect.x = moveAmount[0]
        elem.rect.y = moveAmount[1]

        if UIElement.has_children(elem):
            for _index, _child in enumerate(elem.children):
                UIElement.move_element(
                    _child,
                    [elem.rect.x + _child_offsets[_index][0],
                     elem.rect.y + _child_offsets[_index][1]])

    @classmethod
    def add_current_ui(cls, ui_array: list):
        for _elem in ui_array:
            cls.__current_ui[f'{_elem.__name__}'] = _elem

    @classmethod
    def get_ui_elem(cls, elem: str) -> object:
        try:
            return UIElement.__current_ui.get(elem)
        except:
            raise Exception(f'Could not find {elem} in current UI')

    @classmethod
    def check_for_ui(cls, elem: str) -> bool:
        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem(elem)):
                return True

        return False

    @classmethod
    def find_current_ui(cls, elem: str, object_name: str = '') -> object:
        for _elem in UIElement.get_group('ui'):
            if isinstance(_elem, UIElement.get_ui_elem(elem)):
                if object_name != '':
                    if _elem.obj_name == object_name:
                        return _elem
                    else:
                        continue
                return _elem

    @classmethod
    def set_modus(cls, _modus: str):
        cls.__modus = _modus

        for _elem in cls.get_group('ui'):
            _elem.apperance.reload_apperance()

    @classmethod
    def get_modus(cls) -> str:
        return cls.__modus

    @classmethod
    def get_group(cls, whichGroup: str) -> pg.sprite.Group | pg.sprite.LayeredUpdates:
        if whichGroup == "ui":
            return cls.__ui_elements
        elif whichGroup == "layer":
            return cls.__ui_layers

    @classmethod
    def add_to_group(cls, elem: object):
        cls.get_group("ui").add(elem)
        cls.get_group("layer").add(elem)

    @classmethod
    def change_layer(cls, elem: object, newLayer: int):
        cls.get_group('layer').change_layer(elem, newLayer)

    @classmethod
    def find_highest_elem(cls, elem_collection: list) -> object:
        if len(elem_collection) > 0:
            _highest_elem = elem_collection[0]
            for _elem in elem_collection:
                if cls._compare_layer(_elem, _highest_elem):
                    _highest_elem = _elem

            return _highest_elem
        else:
            return None

    @classmethod
    def _compare_layer(cls, elem: object, other_elem: object) -> bool:
        return cls.get_group('layer').get_layer_of_sprite(
            elem) > cls.get_group('layer').get_layer_of_sprite(other_elem)

    @classmethod
    def remove_from_group(cls, elem: object):
        cls.get_group("ui").remove(elem)
        cls.get_group("layer").remove(elem)

        if cls.has_children(elem):
            for _child in elem.children:
                cls.remove_from_group(_child)

        elem.kill()

    @classmethod
    def has_children(cls, elem: object) -> bool:
        if len(elem.children) > 0:
            return True
        return False

    @classmethod
    def get_parent(cls, elem: object) -> object:
        for _elem in cls.get_group('ui'):
            if len(_elem.children) > 0:
                for child in _elem.children:
                    if child == elem:
                        return _elem

    @classmethod
    def is_child(cls, elem: object) -> bool:
        for _elem in cls.get_group('ui'):
            if len(_elem.children) > 0:
                for child in _elem.children:
                    if child == elem:
                        return True
        return False

    @staticmethod
    def lerp(start_point: int, end_point: int, speed: float) -> int:
        if start_point < end_point:
            return math.ceil(start_point + (end_point - start_point) * speed)
        elif start_point > end_point:
            return math.floor(start_point + (end_point - start_point) * speed)
