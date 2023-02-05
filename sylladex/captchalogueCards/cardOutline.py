import pygame as pg

from uiElement import UIElement


class CardOutline(pg.sprite.Sprite):
    currentOutline = pg.sprite.GroupSingle()

    def __init__(self, parent):
        super().__init__(CardOutline.currentOutline, UIElement.get_group('layer'))
        UIElement.get_group('layer').change_layer(self, -2)

        self.focusedCard = parent

        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/MISC/CAPTA_OUTLINE.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.focusedCard.rect.x - 15, self.focusedCard.rect.y - 15))

    @classmethod
    def destroy_outline(cls):
        for outline in CardOutline.currentOutline: 
            UIElement.get_group('layer').remove(outline)
            CardOutline.currentOutline.remove(outline)
            outline.kill()

    @classmethod
    def move_outline(cls, card):
        for outline in CardOutline.currentOutline:
            outline.focusedCard = card
            outline.rect.x = card.rect.x - 15
            outline.rect.y = card.rect.y - 15

