from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.stackingArea import StackingArea
from sylladex.uiElements.sidebarButton import SidebarButton
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.numTextField import NumTextField
from sylladex.uiElements.scrollBar import ScrollBar


import pygame as pg

def main():

    pg.init()

    clock = pg.time.Clock()

    screen = pg.display.set_mode((1920, 1080))
    pg.display.set_caption('SYLLADEX ALPHA 0.1')
    pg.key.set_repeat(500, 200)

    StackingArea(0,0, (0,0), f"sylladex/uiElements/asset/{UIBase.get_modus()}/STACK_AREA.png")
    SidebarButton(0, 537, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png", "open")
    GristCacheButton(0, 928, (70, 70), f"sylladex/uiElements/asset/MISC/GRIST_CACHE_BUTTON.png")

    while True:

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    for elem in UIBase.get_group("ui"):
                        if hasattr(elem, "active"):
                            elem.exit_field()
                        if hasattr(elem, "on_click") and elem.rect.collidepoint(event.pos):
                            elem.on_click()
            
            elif event.type == pg.MOUSEBUTTONUP:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, ScrollBar):
                        elem.selected = False
            
            elif event.type == pg.MOUSEMOTION:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, ScrollBar):
                        if elem.selected == True:
                            elem.move_bar(event.pos)

            if event.type == pg.KEYDOWN:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, NumTextField):
                        elem.typeing(event)



        for elem in UIBase.get_group("ui"):
            if isinstance(elem, PopUp) and elem.rect.collidepoint(event.pos):
                elem.negate = True
            else:
                elem.negate = False

        for elem in UIBase.get_group("ui"):
            if isinstance(elem, PopUp):
                if pg.time.get_ticks() - elem.last >= elem.timer:
                    elem.remove()
                    if elem:
                        elem.last = pg.time.get_ticks()

        clock.tick(30)
        screen.fill((183, 183, 183))
        UIBase.get_group("ui").draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

