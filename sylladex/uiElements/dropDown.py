import pygame as pg

from uiElement import UIElement, Apperance


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
        self.options = options
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
            self.add_child(UIElement.get_ui_elem('DropDownBackground')(
                6,
                self.rect.h,
                [(self.collum_num * self.rect.w),
                 6 + (self.row_num * self.rect.h)],
                '#1C4587',
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
                            baseColors=[
                                '#C9DAF8',
                                '#D9E2F1',
                                '#9CB0D5'
                            ]
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
                            lookup=UIElement.CodeDatabase.kind_image_small,
                            baseColors=[
                                '#C9DAF8',
                                '#D9E2F1',
                                '#9CB0D5'
                            ]
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
