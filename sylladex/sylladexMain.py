from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.stackingArea import StackingArea


import pygame as pg

def main():
    pg.init()

    screen = pg.display.set_mode((1920, 1080))
    pg.display.set_caption('SYLLADEX ALPHA 0.1')
    pg.key.set_repeat(500, 200)

    StackingArea(0,0, (0,0), "sylladex/uiElements/asset/STACK_AREA.png")

    while True:
        screen.fill((183, 183, 183))
        UIBase.get_group().draw(screen)
        pg.display.flip()

