import pygame as pg

def main(screen, clock, UIBase):

    globalPrevTick = pg.time.get_ticks()

    UIBase.StackingArea(0,0, (0,0), f"STACK_AREA.png")
    UIBase.SidebarButton()
    UIBase.GristCacheButton()
    UIBase.CustomSettingButton()

    while True:

        nowTick = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    for elem in UIBase.get_group("ui"):
                        if hasattr(elem, "active") and elem.active == True:
                            elem.exit_field()
                        if hasattr(elem, "on_click") and elem.rect.collidepoint(event.pos):
                            elem.on_click()
                            
                            if UIBase.RemoveCardButton.eject == True:
                                if len(UIBase.CardList.children) == 0:
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
                if event.mod == pg.KMOD_LCTRL and event.key == pg.K_i:
                    if UIBase.DebugInspect == False:
                        UIBase.DebugInspect = True
                    else:
                        UIBase.DebugInspect = False
                        UIBase.Insepctors.clear()
                        for elem in UIBase.get_group('ui'):
                            if isinstance(elem, UIBase.DebugUIInspector):
                                UIBase.remove_fromGroup(elem)
                                elem.kill()
                elif event.key == pg.K_ESCAPE:
                    makeEscape = True
                    for elem in UIBase.get_group('ui'):
                        if isinstance(elem, UIBase.EscapeMenu):
                            for child in elem.children:
                                UIBase.remove_fromGroup(child)
                                child.kill()
                            UIBase.remove_fromGroup(elem)
                            elem.kill()
                            makeEscape = False

                    if makeEscape == True:
                        UIBase.EscapeMenu()
                    
                else:
                    for elem in UIBase.get_group("ui"):
                        if isinstance(elem, UIBase.TextField):
                            elem.typeing(event)

        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                
                if UIBase.DebugInspect == True:
                    dontMake = False
                    for elem2 in UIBase.get_group('ui'):
                        if isinstance(elem2, UIBase.DebugUIInspector):
                            if elem2.currentIns == elem:
                                dontMake = True

                    if dontMake == False:
                        UIBase.Insepctors.append(UIBase.DebugUIInspector(elem))

                    for index, inspector in enumerate(UIBase.Insepctors):
                        if index == 0:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(inspector.rect.w)
                            growingOffSet = inspector.rect.w+10
                        else:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(growingOffSet)-(inspector.rect.w)
                            growingOffSet += inspector.rect.w+10

                if isinstance(elem, UIBase.PopUp):
                    elem.negate = True
                if hasattr(elem, "hover") and elem.hovering == False:
                        if isinstance(elem, UIBase.ListObject)and UIBase.RemoveCardButton.eject == True:
                            elem.alt_hover()
                        else:
                            elem.hover()
                if hasattr(elem, "toolTipText"):
                    if hasattr(elem, "active") and elem.active == True:
                        pass
                    elif hasattr(elem, 'inactive') and elem.inactive == True:
                        pass
                    elif nowTick - globalPrevTick >= 1300:
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
                dontDelete = False
                for elem2 in UIBase.get_group('ui'):
                    if elem2.rect.collidepoint(pg.mouse.get_pos()) and hasattr(elem2, 'toolTipText'):
                        if elem2.toolTipText == elem.text:
                            dontDelete = True
                            UIBase.remove_fromGroup(elem)
                            elem.kill()
                            break
                if dontDelete == False:
                    UIBase.remove_fromGroup(elem)
                    elem.kill()
                    globalPrevTick = pg.time.get_ticks()

            if hasattr(elem, "update"):
                elem.update()


        clock.tick(30)
        screen.fill((183, 183, 183))
        UIBase.get_group("ui").draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

