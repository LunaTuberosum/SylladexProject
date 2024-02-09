import pygame as pg

from uiElement import UIElement, Apperance
import settings


class DropDown(UIElement):
    def __init__(self, x: int, y: int, size: list, job: str, tool_tip_text: str, options: list, defult_option: str, show_type: str, **kwargs: dict):

        super().__init__(
            x,
            y,
            f'DropDown ({job})',
            kwargs['startLayer'] if 'startLayer' in kwargs else 1
        )

        self.kwargs = kwargs
        self.size = size

        self.job = job
        _options = []
        for _opt in options:
            if _opt != '':
                _options.append(_opt)
        self.options = _options
        self.current_option = defult_option

        self.hovering = False

        self.tool_tip_text = tool_tip_text
        self.show_type = show_type

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self.configure_kwargs()

        if self.show_type == 'Text':
            self.apperance = Apperance(
                self,
                self.size,
                [self.size, self.base_color, [0, 0]],
                texts=[
                    [self.current_option, [self.size[0] / 2,
                                           self.size[1] / 2], 'center', '#000000']
                ]
            )
        elif self.show_type == 'Image':
            self.apperance = Apperance(
                self,
                self.size,
                [self.size, self.base_color, [0, 0]],
                images=[
                    [self.lookup.get(self.current_option), [0, 0]]
                ]
            )

    def configure_kwargs(self):
        if 'lookup' in self.kwargs:
            self.lookup = self.kwargs['lookup']
        elif self.show_type == 'Image':
            raise Exception('Drop down with image show type needs a look up.')

        if 'grid' in self.kwargs:
            self.collum_num = self.kwargs['grid'][0]
            self.row_num = self.kwargs['grid'][1]
        else:
            self.collum_num = 1
            self.row_num = len(self.options)

        if 'baseColors' in self.kwargs:
            self.base_color = self.kwargs['baseColors'][0]
            self.hover_color = self.kwargs['baseColors'][1]
            self.selected_color = self.kwargs['baseColors'][2]
        else:
            self.base_color = (255, 255, 255)
            self.hover_color = (230, 230, 230)
            self.selected_color = (170, 170, 170)

        if 'exitCommand' in self.kwargs:
            self.exit_command = self.kwargs['exitCommand']
        else:
            self.exit_command = None

    def reload_apperance(self):
        _color = self.base_color
        if self.hovering:
            _color = self.hover_color

        if self.show_type == 'Text':
            self.apperance.kwargs['texts'] = [[self.current_option, [self.size[0] / 2,
                                                                     self.size[1] / 2], 'center', '#000000']]

        elif self.show_type == 'Image':
            self.apperance.change_images(
                [
                    [self.lookup.get(self.current_option), [0, 0]]
                ])

        self.apperance.size_color_pos = [[self.size, _color, [0, 0]]]
        self.apperance.reload_apperance()

    def hover(self):
        if len(self.children) == 0:
            self.hovering = True
            self.reload_apperance()

    def no_hover(self):
        if len(self.children) == 0:
            self.hovering = False
            self.reload_apperance()

    def on_click(self):
        if len(self.children) > 0:
            self.exit_field()
        else:
            if (6 + (self.row_num * self.rect.h)) + self.rect.bottom > settings.SCREEN_HEIGHT:
                self.up_options()
            else:
                self.down_options()

    def up_options(self):
        self.add_child(UIElement.get_ui_elem('DropDownBackground')(
            6,
            -(6 + (self.row_num * self.rect.h)),
            [(self.collum_num * self.rect.w),
                6 + (self.row_num * self.rect.h) + (self.rect.h // 2)],
            self.selected_color,
            UIElement.get_group(
                'layer').get_layer_of_sprite(self) - 1
        ))

        _i = 0
        _x = 0
        _y = -(self.row_num * self.rect.h)
        for _col in range(self.collum_num):
            for _row in range(self.row_num):
                if self.show_type == 'Text':
                    self.add_child(UIElement.get_ui_elem('DropDownOption')(
                        _x,
                        _y,
                        self.size,
                        self.show_type,
                        self.options[_i],
                        startLayer=UIElement.get_group(
                            'layer').get_layer_of_sprite(self) + 1,
                        baseColors=self.kwargs['baseColors']
                    ))
                elif self.show_type == 'Image':
                    self.add_child(UIElement.get_ui_elem('DropDownOption')(
                        _x,
                        _y,
                        self.size,
                        self.show_type,
                        self.options[_i],
                        startLayer=UIElement.get_group(
                            'layer').get_layer_of_sprite(self) + 1,
                        lookup=UIElement.code_database.kind_image_small,
                        baseColors=self.kwargs['BaseColors']
                    ))
                _y += self.rect.h
                _i += 1
            _x += self.rect.w
            _y = -(self.row_num * self.rect.h)

    def down_options(self):
        self.add_child(UIElement.get_ui_elem('DropDownBackground')(
            6,
            self.rect.h,
            [(self.collum_num * self.rect.w),
                6 + (self.row_num * self.rect.h)],
            self.selected_color,
            UIElement.get_group(
                'layer').get_layer_of_sprite(self)
        ))

        _i = 0
        _x = 0
        _y = self.rect.h
        for _col in range(self.collum_num):
            for _row in range(self.row_num):
                if self.show_type == 'Text':
                    self.add_child(UIElement.get_ui_elem('DropDownOption')(
                        _x,
                        _y,
                        self.size,
                        self.show_type,
                        self.options[_i],
                        startLayer=UIElement.get_group(
                            'layer').get_layer_of_sprite(self) + 1,
                        baseColors=self.kwargs['baseColors']
                    ))
                elif self.show_type == 'Image':
                    self.add_child(UIElement.get_ui_elem('DropDownOption')(
                        _x,
                        _y,
                        self.size,
                        self.show_type,
                        self.options[_i],
                        startLayer=UIElement.get_group(
                            'layer').get_layer_of_sprite(self) + 1,
                        lookup=UIElement.code_database.kind_image_small,
                        baseColors=self.kwargs['BaseColors']
                    ))
                _y += self.rect.h
                _i += 1
            _x += self.rect.w
            _y = self.rect.h

    def exit_field(self):
        if self.exit_command:
            self.exit_command()
        for _child in self.children:
            _child.kill()
        self.children.clear()
