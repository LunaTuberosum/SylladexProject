import sys
import pygame as pg

from uiElement import Apperance, UIElement


class EscapeMenu(UIElement):
    def __init__(self):
        super().__init__(
            750,
            360,
            'EscapeMenu',
            1000)

        self.apperance = Apperance(
            self,
            [420, 360],
            [[420, 360], '#000000', [0, 0]],
            images=[
                ['sylladex/uiElements/asset/MISC/ESCAPE_MENU.png', [0, 0]]
            ]
        )

        self.add_child(UIElement.get_ui_elem(
            'EscapeMenuOption')(110, 110, 'Settings', self.settings))
        self.add_child(UIElement.get_ui_elem(
            'EscapeMenuOption')(110, 171, 'Tutorials', self.tutorials))
        self.add_child(UIElement.get_ui_elem(
            'EscapeMenuOption')(110, 232, 'To Desktop', self.to_desktop))
        self.add_child(UIElement.get_ui_elem(
            'EscapeMenuOption')(110, 293, 'Log Out', self.log_out))

    def settings(self):
        pass

    def tutorials(self):
        pass

    def to_desktop(self):
        pg.quit()
        sys.exit()

    def log_out(self):
        pass
