import pygame as pg

from uiElement import UIElement, Apperance


class ModusCard(UIElement):
    def __init__(self, x, modus):

        self.modus = modus
        self.tool_tip_text = f'Changes the modus to {self.modus} MODUS'

        super().__init__(
            x,
            910,
            f'ModusCard ({self.modus})',
            11
        )

        self.apperance = Apperance(
            self,
            [78, 102],
            colorKey=True,
            image=[
                f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS.png', [6, 6]]
        )

        self.hovering = False

        if UIElement.get_modus() == self.modus:
            self.current = True
            self.apperance.change_image(
                f'sylladex/uiElements/asset/MISC/{self.modus}_MODUS_ACTIVE.png', [0, 0])
            self.rect.y = 907
        else:
            self.current = False

        self.to_be_rect = self.rect.y

    def update(self):

        if self.to_be_rect != self.rect.y:

            UIElement.move_element(self, [self.rect.x, UIElement.lerp(
                self.rect.y, self.to_be_rect, 0.2)])

    def on_click(self):
        UIElement.set_modus(self.modus)
        for elem in UIElement.get_group("ui"):
            if isinstance(elem, UIElement.get_ui_elem('ModusCard')):
                if elem == self:
                    elem.apperance.change_image(
                        f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS_ACTIVE.png', [0, 0])
                    elem.rect.y = 907
                else:
                    elem.apperance.change_image(
                        f'sylladex/uiElements/asset/MISC/{elem.modus}_MODUS.png', [6, 6])
                    elem.rect.y = 910

            elem.apperance.reload_apperance()
            if hasattr(elem, 'reload_image'):
                elem.reload_image()

    def hover(self):
        self.rect.y = 900
        self.to_be_rect = 900
        self.hovering = True

    def no_hover(self):
        self.to_be_rect = 910
        self.hovering = False
