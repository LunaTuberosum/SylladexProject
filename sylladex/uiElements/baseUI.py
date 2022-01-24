import pygame as pg

class UIBase(pg.sprite.Sprite):
    modus = ""
    uiElements = pg.sprite.Group()

    def __init__(self, x, y, size, image):
        super().__init__()
        UIBase.add_toGroup(self)

        self.image = pg.Surface(size)
        self.image.fill((255, 255, 255))
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def set_modus(modus):
        UIBase.modus = modus

    def get_modus():
        return UIBase.modus

    def get_group():
        return UIBase.uiElements

    def add_toGroup(card):
        UIBase.get_group().add(card)