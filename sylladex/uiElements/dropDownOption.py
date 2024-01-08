import pygame as pg

from uiElement import UIElement, Apperance


class DropDownOption(UIElement):
    def __init__(self, x: int, y: int, size: list, show_type: str, option: str, **kwargs: dict):

        super().__init__(
            x,
            y,
            f'DropDownOption ({option})',
            kwargs['startLayer'] if 'startLayer' in kwargs else 1
        )

        self.option = option
        self.kwargs = kwargs
        self.show_type = show_type
        self.size = size

        self.configure_kwargs()

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        if self.show_type == 'Text':
            self.apperance = Apperance(
                self,
                self.size,
                [self.size, self.base_color, [0, 0]],
                texts=[[self.option, [self.size[0] / 2,
                                      self.size[1] / 2], 'center', '#000000']]
            )
        elif self.show_type == 'Image':
            self.apperance = Apperance(
                self,
                self.size,
                [self.size, self.base_color, [0, 0]],
                image=[self.lookup.get(self.option), [0, 0]]
            )

    def configure_kwargs(self):
        if 'lookup' in self.kwargs:
            self.lookup = self.kwargs['lookup']
        elif self.show_type == 'Image':
            raise Exception(
                'Drop down option with image show type needs a look up.')

        if 'baseColors' in self.kwargs:
            self.base_color = self.kwargs['baseColors'][0]
            self.hover_color = self.kwargs['baseColors'][1]
            self.selected_color = self.kwargs['baseColors'][2]
        else:
            self.base_color = (255, 255, 255)
            self.hover_color = (230, 230, 230)
            self.selected_color = (170, 170, 170)

    def hover(self):
        self.hovering = True
        self.apperance.size_color_pos = [[self.size, self.hover_color, [0, 0]]]
        self.apperance.reload_apperance()

    def no_hover(self):
        self.hovering = False
        self.apperance.size_color_pos = [[self.size, self.base_color, [0, 0]]]
        self.apperance.reload_apperance()

    def on_click(self):
        _parent = UIElement.get_parent(self)

        _parent.current_option = self.option
        _parent.exit_field()
