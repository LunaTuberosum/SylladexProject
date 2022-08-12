import pygame as pg
import settings
from sylladex import sylladexMain

from baseUI import UIBase

from sylladex.captchalogueCards import codeDatabase

from sylladex.uiElements.debugUIInspector import DebugUIInspector

UIBase.CodeDatabase = codeDatabase

UIBase.DebugUIInspector = DebugUIInspector

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pg.display.set_caption('SYLLADEX ALPHA 0.1')
pg.key.set_repeat(200, 200)

if __name__ == '__main__':
    sylladexMain.main(screen, clock, UIBase)
