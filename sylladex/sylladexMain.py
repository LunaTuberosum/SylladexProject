from sylladex.uiElements.baseUI import UIBase

from sylladex.uiElements.addCardButton import AddCardButton
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.listObject import ListObject
from sylladex.uiElements.modusCard import ModusCard
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.removeCardButton import RemoveCardButton
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.sidebarButton import SidebarButton
from sylladex.uiElements.stackingArea import StackingArea
from sylladex.uiElements.textField import TextField
from sylladex.uiElements.toolTip import ToolTip

from sylladex.captchalogueCards import codeDatabase

UIBase.AddCardButton = AddCardButton
UIBase.CardList = CardList
UIBase.GristCacheButton = GristCacheButton
UIBase.ListObject = ListObject
UIBase.ModusCard = ModusCard
UIBase.PopUp = PopUp
UIBase.RemoveCardButton = RemoveCardButton
UIBase.ScrollBar = ScrollBar
UIBase.SideBar = SideBar
UIBase.SidebarButton = SidebarButton
UIBase.StackingArea = StackingArea
UIBase.TextField = TextField
UIBase.ToolTip = ToolTip

UIBase.CodeDatabase = codeDatabase

import pygame as pg

def main():

    pg.init()

    clock = pg.time.Clock()

    screen = pg.display.set_mode((1920, 1080))
    pg.display.set_caption('SYLLADEX ALPHA 0.1')
    pg.key.set_repeat(500, 200)

    UIBase.StackingArea(0,0, (0,0), f"sylladex/uiElements/asset/{UIBase.get_modus()}/STACK_AREA.png")
    UIBase.SidebarButton(0, 537, (70, 70), f"sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_BUTTON.png", "")
    UIBase.GristCacheButton()

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
                            
                            if RemoveCardButton.eject == True:
                                if len(UIBase.CardList.listObj) == 0:
                                    RemoveCardButton.eject = False
                                else:
                                    for elem in UIBase.get_group("ui"):
                                        if isinstance(elem, UIBase.ListObject):    
                                            elem.redraw_card((230,230,230))

                            elif RemoveCardButton.eject == False:
                                for elem in UIBase.get_group("ui"):
                                    if isinstance(elem, UIBase.ListObject):    
                                        elem.redraw_card((255,255,255))
                            

            
            elif event.type == pg.MOUSEBUTTONUP:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.ScrollBar):
                        elem.selected = False
                        elem.image.fill((255, 0, 220))
            
            elif event.type == pg.MOUSEMOTION:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.ScrollBar):
                        if elem.selected == True:
                            elem.move_bar(event.pos)

            elif event.type == pg.MOUSEWHEEL:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.CardList):
                        if elem.rect.collidepoint(pg.mouse.get_pos()):
                            for elem in UIBase.get_group("ui"):
                                if isinstance(elem, ScrollBar):
                                    elem.move_bar_wheel(-event.y)

            if event.type == pg.KEYDOWN:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.TextField):
                        elem.typeing(event)




        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                if isinstance(elem, UIBase.PopUp):
                    elem.negate = True
                if hasattr(elem, "hover"):
                    if isinstance(elem, UIBase.ListObject)and UIBase.RemoveCardButton.eject == True:
                        elem.alt_hover()
                    else:
                        elem.hover()
                if hasattr(elem, "toolTipText"):
                    if hasattr(elem, "active") and elem.active == True:
                        pass
                    else:
                        ToolTip(pg.mouse.get_pos(), elem.toolTipText)
            else:
                if hasattr(elem, "negate"):
                    elem.negate = False
                if hasattr(elem, "no_hover")and elem.hovering == True:
                    if isinstance(elem, UIBase.ListObject)and UIBase.RemoveCardButton.eject == True:
                        elem.alt_no_hover()
                    else:
                        elem.no_hover()

            if isinstance(elem, UIBase.PopUp) and  hasattr(elem, "last") and nowTick - elem.last >= elem.timer:
                elem.remove()
                if elem:
                    elem.last = pg.time.get_ticks()

            if isinstance(elem, UIBase.ToolTip):
                UIBase.remove_fromGroup(elem)
                elem.kill()

            if hasattr(elem, "update"):
                elem.update()


        clock.tick(30)
        screen.fill((183, 183, 183))
        UIBase.get_group("ui").draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

