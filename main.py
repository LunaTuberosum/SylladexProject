import pygame as pg
import settings
from sylladex import sylladexMain

from uiElement import UIElement

from sylladex.captchalogueCards import codeDatabase
from sylladex.uiElements.listObject import CodeData

from sylladex.uiElements.debugUIInspector import DebugUIInspector


UIElement.CodeDatabase = codeDatabase
UIElement.CodeData = CodeData

UIElement.DebugUIInspector = DebugUIInspector

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pg.display.set_caption('SYLLADEX ALPHA 0.2')
pg.key.set_repeat(200, 200)

_icon = pg.image.load('icon.png').convert_alpha()

pg.display.set_icon(_icon)
if __name__ == '__main__':
    sylladexMain.main(screen, clock)
