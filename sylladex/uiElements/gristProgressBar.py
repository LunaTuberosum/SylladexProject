import pygame as pg

from uiElement import UIElement, Apperance


class GristProgressBar(UIElement):
    def __init__(self, parent: object):
        self.parent = parent
        self.prev_amount = self.parent.children[0].text

        self.progress = int(self.parent.children[0].text) / int(UIElement.find_current_ui('GristCacheLimit').limit_num)

        super().__init__(
            59, 
            30, 
            f'GristProgressBar ({self.parent.grist})', 
            1)

        self.apperance = Apperance(
            self,
            (99, 12),
            [[99*self.progress, 12], (67,178,222), [0,0]],
            colorKey=True
        )

    def update(self):
        if self.parent.children[0].text != self.prev_amount:

            if self.parent.children[0].text == '':
                self.prev_amount = '0'
                
                self.progress = 0

            else: 
                self.prev_amount = self.parent.children[0].text

                self.progress = int(self.parent.children[0].text) / int(UIElement.find_current_ui('GristCacheLimit').limit_num)

            self.apperance.size_color_pos = [
                [[99*self.progress, 12], (67,178,222), [0,0]]
                ]

            self.apperance.reload_apperance()
        
