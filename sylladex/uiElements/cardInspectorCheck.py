from uiElement import UIElement

import pygame as pg

class CardInspectorCheck(UIElement):
    __checks = []

    def __init__(self, x, y, job):
        super().__init__(x, y, (24, 24), f'CardInspectorCheck({job})', (255,255,255))

        self.create_appearance([[16, 16], '#434343', [4,4]], [[12, 12], '#ffffff', [6, 6]], colorKey = True)

        CardInspectorCheck.__checks.append(self)
        UIElement.get_group('layer').change_layer(self, 4)

        self.job = job

        self.selected = False

    def on_click(self):
        if self.selected == False:
            for _check in CardInspectorCheck.__checks:
                if _check.selected == True:
                    _check.selected = False
                    _check.create_appearance([[16, 16], '#434343', [4,4]], [[12, 12], '#ffffff', [6, 6]], colorKey = True)
            self.selected = True
            self.create_appearance([[16, 16], '#434343', [4,4]], colorKey = True)
        
        else: 
            self.selected = False
            self.create_appearance([[16, 16], '#434343', [4,4]], [[12, 12], '#ffffff', [6, 6]], colorKey = True)

