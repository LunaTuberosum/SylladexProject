import pygame as pg

from uiElement import Apperance, UIElement


class CardOutline(pg.sprite.Sprite):
    current_outline = pg.sprite.GroupSingle()

    def __init__(self, parent):
        super().__init__(CardOutline.current_outline, UIElement.get_group('layer'))
        UIElement.get_group('layer').change_layer(self, -1)

        self.focused_card = parent

        self.rect = [self.focused_card.rect.x -
                     15, self.focused_card.rect.y - 15]

        self.apperance = Apperance(
            self,
            [85, 116],
            colorKey=True,
            images=[
                [f'sylladex/captchalogueCards/assets/MISC/CAPTA_OUTLINE.png', [
                    0, 0]],
            ]
        )

        self.interactable = False

    @classmethod
    def destroy_outline(cls):
        for outline in CardOutline.current_outline:
            UIElement.get_group('layer').remove(outline)
            CardOutline.current_outline.remove(outline)
            outline.kill()

    @classmethod
    def move_outline(cls, card):
        for outline in CardOutline.current_outline:
            outline.focused_card = card
            outline.rect.x = card.rect.x - 15
            outline.rect.y = card.rect.y - 15
