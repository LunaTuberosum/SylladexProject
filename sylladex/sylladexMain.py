from sylladex.uiElements.baseUI import UIBase

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
                            
                            if UIBase.RemoveCardButton.eject == True:
                                if len(UIBase.CardList.listObj) == 0:
                                    UIBase.RemoveCardButton.eject = False
                                else:
                                    for elem in UIBase.get_group("ui"):
                                        if isinstance(elem, UIBase.ListObject):    
                                            elem.redraw_card((230,230,230))

                            elif UIBase.RemoveCardButton.eject == False:
                                for elem in UIBase.get_group("ui"):
                                    if isinstance(elem, UIBase.ListObject):    
                                        elem.redraw_card((255,255,255))


            
            elif event.type == pg.MOUSEBUTTONUP:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.ScrollBar):
                        elem.selected = False
                        elem.image.fill((255, 0, 220))
                    
                    elif hasattr(elem, 'grabbed') and elem.grabbed == True:
                        elem.rect.topleft = elem.prevPos
                        elem.grabbed = False
            
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
                                if isinstance(elem, UIBase.ScrollBar):
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
                        UIBase.ToolTip(pg.mouse.get_pos(), elem.toolTipText)
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

