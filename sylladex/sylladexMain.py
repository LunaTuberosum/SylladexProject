from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.stackingArea import StackingArea
from sylladex.uiElements.sidebarButton import SidebarButton
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.numTextField import NumTextField
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.listObject import ListObject
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.toolTip import ToolTip

import pygame as pg

def main():

    pg.init()

    clock = pg.time.Clock()

    screen = pg.display.set_mode((1920, 1080))
    pg.display.set_caption('SYLLADEX ALPHA 0.1')
    pg.key.set_repeat(500, 200)

    StackingArea(0,0, (0,0), f"sylladex/uiElements/asset/{UIBase.get_modus()}/STACK_AREA.png")
    SidebarButton(0, 537, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png", "")
    GristCacheButton()

    prevTick = pg.time.get_ticks()

    while True:

        nowTick = pg.time.get_ticks()

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
                        elem.image.fill((255, 0, 220))
            
            elif event.type == pg.MOUSEMOTION:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, ScrollBar):
                        if elem.selected == True:
                            elem.move_bar(event.pos)

            elif event.type == pg.MOUSEWHEEL:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, CardList):
                        if elem.rect.collidepoint(pg.mouse.get_pos()):
                            for elem in UIBase.get_group("ui"):
                                if isinstance(elem, ScrollBar):
                                    elem.move_bar_wheel(-event.y)

            if event.type == pg.KEYDOWN:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, NumTextField):
                        elem.typeing(event)




        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                if isinstance(elem, PopUp):
                    elem.negate = True
                if hasattr(elem, "hover"):
                    elem.hover()
                if hasattr(elem, "toolTipText"):
                    ToolTip(pg.mouse.get_pos(), elem.toolTipText)
            else:
                if hasattr(elem, "negate"):
                    elem.negate = False
                if hasattr(elem, "no_hover"):
                    if elem.hovering == True:
                        elem.no_hover()

            if isinstance(elem, PopUp):
                if nowTick - elem.last >= elem.timer:
                    elem.remove()
                    if elem:
                        elem.last = pg.time.get_ticks()

            if isinstance(elem, ToolTip):
                UIBase.remove_fromGroup(elem)
                elem.kill()

            if isinstance(elem, ListObject):
                elem.update()
  

        clock.tick(30)
        screen.fill((183, 183, 183))
        UIBase.get_group("ui").draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

