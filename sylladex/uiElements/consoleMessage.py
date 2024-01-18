import pygame as pg

from uiElement import UIElement, Apperance


class ConsoleMessage(UIElement):
    __current_messages = []

    def __init__(self, text):

        super().__init__(
            pg.display.get_surface().get_width()-((len(text)*11.5)+25),
            pg.display.get_surface().get_height()-40,
            f'ConsoleMessage ({text})',
            999
        )

        self.apperance = Apperance(
            self,
            [15+(len(text)*11.5), 30],
            [[15+(len(text)*11.5), 30], (50, 50, 50), [0, 0]],
            alpha=130,
            fonts=[
                ['sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf', 24]
            ],
            texts=[[text, [10, 15], 'left', '#ffffff']]
        )

        if len(ConsoleMessage.__current_messages) > 0:
            self.rect.y = ConsoleMessage.__current_messages[-1].rect.y - 40

        ConsoleMessage.__current_messages.append(self)

    def update(self):
        if self.current_tick >= 1000:
            UIElement.remove_from_group(self)
            ConsoleMessage.__current_messages.remove(self)
            # Fade to the right
