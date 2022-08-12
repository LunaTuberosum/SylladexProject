import pygame as pg

from baseUI import UIBase

from sylladex.uiElements.actionIcon import ActionIcon
from sylladex.uiElements.addCardButton import AddCardButton
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.consoleMessage import ConsoleMessage
from sylladex.uiElements.customSettingAreaBox import CustomSettingAreaBox
from sylladex.uiElements.customSettingButton import CustomSettingButton
from sylladex.uiElements.customSettingMenu import CustomSettingMenu
from sylladex.uiElements.customSettingSectionName import CustomSettingSectionName
from sylladex.uiElements.escapeMenu import EscapeMenu
from sylladex.uiElements.escapeMenuOption import EscapeMenuOption
from sylladex.uiElements.gristCache import GristCache
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.gristCacheLimit import GristCacheLimit
from sylladex.uiElements.gristInfoBox import GristInfoBox
from sylladex.uiElements.gristProgressBar import GristProgressBar
from sylladex.uiElements.listObject import ListObject
from sylladex.uiElements.longTextField import LongTextField
from sylladex.uiElements.modusCard import ModusCard
from sylladex.uiElements.optionToggle import OptionToggle
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.removeCardButton import RemoveCardButton
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.sidebarButton import SidebarButton
from sylladex.uiElements.stackingArea import StackingArea
from sylladex.uiElements.textField import TextField
from sylladex.uiElements.toggleButton import ToggleButton
from sylladex.uiElements.toolTip import ToolTip
from sylladex.uiElements.finishButton import FinishButton

UIBase.add_current_UI([
    ActionIcon, 
    AddCardButton, 
    CardList, 
    ConsoleMessage, 
    CustomSettingAreaBox, 
    CustomSettingButton, 
    CustomSettingMenu, 
    CustomSettingSectionName, 
    EscapeMenu, 
    EscapeMenuOption, 
    GristCache, 
    GristCacheButton, 
    GristCacheLimit, 
    GristInfoBox, 
    GristProgressBar, 
    ListObject, 
    LongTextField, 
    ModusCard, 
    OptionToggle, 
    PopUp, 
    RemoveCardButton, 
    ScrollBar, 
    SideBar, 
    SidebarButton, 
    StackingArea, 
    TextField, 
    ToggleButton, 
    ToolTip, 
    FinishButton,
    ])

def main(screen, clock, UIBase):

    globalPrevTick = pg.time.get_ticks()

    UIBase.get_uiElem('StackingArea')()
    UIBase.get_uiElem('SidebarButton')()
    UIBase.get_uiElem('GristCacheButton')()
    UIBase.get_uiElem('CustomSettingButton')()

    while True:

        nowTick = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    for elem in UIBase.get_group("ui"):
                        if hasattr(elem, "active") and elem.active == True:
                            if hasattr(elem, "exit_field"):
                                elem.draw()
                                elem.exit_field()
                        if hasattr(elem, "on_click") and elem.rect.collidepoint(event.pos):
                            elem.on_click()
                            
                            if UIBase.get_uiElem('RemoveCardButton').eject == True:
                                if len(UIBase.get_uiElem('CardList').children) == 0:
                                    UIBase.get_uiElem('RemoveCardButton').eject = False
                                else:
                                    for elem in UIBase.get_group("ui"):
                                        if isinstance(elem, UIBase.get_uiElem('ListObject')):    
                                            elem.redraw_card((230,230,230))

                            elif UIBase.get_uiElem('RemoveCardButton').eject == False:
                                for elem in UIBase.get_group("ui"):
                                    if isinstance(elem, UIBase.get_uiElem('ListObject')):    
                                        elem.redraw_card((255,255,255))

                elif event.button == 3:
                    for elem in UIBase.get_group("ui"):
                        if hasattr(elem, "on_altClick") and elem.rect.collidepoint(event.pos):
                            elem.on_altClick()
            
            elif event.type == pg.MOUSEBUTTONUP:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        elem.selected = False
                    
                    elif hasattr(elem, 'grabbed') and elem.grabbed == True:
                        elem.rect.topleft = elem.prevPos
                        elem.grabbed = False
            
            elif event.type == pg.MOUSEMOTION:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        if elem.selected == True:
                            elem.move_bar(event.pos)

            elif event.type == pg.MOUSEWHEEL:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('CardList')):
                        if elem.rect.collidepoint(pg.mouse.get_pos()):
                            for elem in UIBase.get_group("ui"):
                                if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                                    elem.move_bar_wheel(-event.y)

            if event.type == pg.KEYDOWN:
                if event.mod == pg.KMOD_LCTRL and event.key == pg.K_i:
                    if UIBase.DebugInspect == False:
                        UIBase.DebugInspect = True
                    else:
                        UIBase.DebugInspect = False
                        UIBase.Insepctors.clear()
                        for elem in UIBase.get_group('ui'):
                            if isinstance(elem, UIBase.get_uiElem('DebugUIInspector')):
                                UIBase.remove_fromGroup(elem)
                                elem.kill()
                elif event.key == pg.K_ESCAPE:
                    makeEscape = True
                    for elem in UIBase.get_group('ui'):
                        if isinstance(elem, UIBase.get_uiElem('EscapeMenu')):
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
                        if hasattr(elem, 'typeing'):
                            elem.typeing(event)

        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                
                if UIBase.DebugInspect == True:
                    dontMake = False
                    for elem2 in UIBase.get_group('ui'):
                        if isinstance(elem2, UIBase.get_uiElem('DebugUIInspector')):
                            if elem2.currentIns == elem:
                                dontMake = True
                            elif elem2 == elem:
                                dontMake = True

                    if dontMake == False:
                        UIBase.Insepctors.append(UIBase.get_uiElem('DebugUIInspector')(elem))

                    for index, inspector in enumerate(UIBase.Insepctors):
                        if index == 0:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(inspector.rect.w)
                            growingOffSet = inspector.rect.w+20
                        else:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(growingOffSet)-(inspector.rect.w)
                            growingOffSet += inspector.rect.w+20

                if isinstance(elem, UIBase.get_uiElem('PopUp')):
                    elem.negate = True
                if hasattr(elem, "hover") and elem.hovering == False:
                        if isinstance(elem, UIBase.get_uiElem('ListObject'))and UIBase.get_uiElem('RemoveCardButton').eject == True:
                            elem.alt_hover()
                        else:
                            elem.hover()
                if hasattr(elem, "toolTipText"):
                    if hasattr(elem, "active") and elem.active == True:
                        pass
                    elif hasattr(elem, 'inactive') and elem.inactive == True:
                        pass
                    elif nowTick - globalPrevTick >= 1300:
                        UIBase.get_uiElem('ToolTip')(pg.mouse.get_pos(), elem.toolTipText)
            else:
                if hasattr(elem, "negate"):
                    elem.negate = False
                if hasattr(elem, "no_hover")and elem.hovering == True:
                    if isinstance(elem, UIBase.get_uiElem('ListObject'))and UIBase.get_uiElem('RemoveCardButton').eject == True:
                        elem.alt_no_hover()
                    else:
                        elem.no_hover()

            if isinstance(elem, UIBase.get_uiElem('PopUp')) and  hasattr(elem, "last") and nowTick - elem.last >= elem.timer:
                elem.remove()
                if elem:
                    elem.last = pg.time.get_ticks()

            if isinstance(elem, UIBase.get_uiElem('ToolTip')):
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

