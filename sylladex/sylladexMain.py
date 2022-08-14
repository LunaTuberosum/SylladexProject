from lib2to3.pytree import Base
import pygame as pg

from baseUI import UIBase
from .captchalogueCards.stackManager import StackManager

from .captchalogueCards.cardOutline import CardOutline
from .captchalogueCards.baseCard import BaseCard

from .uiElements.actionIcon import ActionIcon
from .uiElements.addCardButton import AddCardButton
from .uiElements.cardList import CardList
from .uiElements.consoleMessage import ConsoleMessage
from .uiElements.customSettingAreaBox import CustomSettingAreaBox
from .uiElements.customSettingButton import CustomSettingButton
from .uiElements.customSettingMenu import CustomSettingMenu
from .uiElements.customSettingSectionName import CustomSettingSectionName
from .uiElements.escapeMenu import EscapeMenu
from .uiElements.escapeMenuOption import EscapeMenuOption
from .uiElements.gristCache import GristCache
from .uiElements.gristCacheButton import GristCacheButton
from .uiElements.gristCacheLimit import GristCacheLimit
from .uiElements.gristInfoBox import GristInfoBox
from .uiElements.gristProgressBar import GristProgressBar
from .uiElements.listObject import ListObject
from .uiElements.longTextField import LongTextField
from .uiElements.modusCard import ModusCard
from .uiElements.optionToggle import OptionToggle
from .uiElements.popUp import PopUp
from .uiElements.removeCardButton import RemoveCardButton
from .uiElements.scrollBar import ScrollBar
from .uiElements.sideBar import SideBar
from .uiElements.sidebarButton import SidebarButton
from .uiElements.stackingArea import StackingArea
from .uiElements.textField import TextField
from .uiElements.toggleButton import ToggleButton
from .uiElements.toolTip import ToolTip
from .uiElements.finishButton import FinishButton

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
                    for card in BaseCard.cards:
                        if card.rect.collidepoint(pg.mouse.get_pos()) and card.selected == False:
                            card.on_click()

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
                for card in BaseCard.cards:
                    if card.selected == True:
                        card.on_release()

                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        elem.selected = False
                    
                    elif hasattr(elem, 'grabbed') and elem.grabbed == True:
                        if elem.rect.x > 326 and elem.captaCard == None:
                            elem.captaCard = BaseCard(elem.rect.topleft, elem)
                            elem.redraw_card('#FFFFFF')
                        else:
                            UIBase.get_uiElem('PopUp')('This card is already deployed')

                        elem.rect.topleft = elem.prevPos
                        UIBase.get_group('layer').change_layer(elem, -1)
                        for child in elem.children:
                            UIBase.get_group('layer').change_layer(elem, -1)   
                        elem.grabbed = False
            
            elif event.type == pg.MOUSEMOTION:
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('ScrollBar')):
                        if elem.selected == True:
                            elem.move_bar(event.pos)
                
                for card in BaseCard.cards:
                    if card.selected == True:
                        card.move(event.rel)
                        card.moving = True
                    else:
                        card.moving = False

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
                            if isinstance(elem, UIBase.DebugUIInspector):
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
                        UIBase.get_uiElem('EscapeMenu')()
                    
                else:
                    for elem in UIBase.get_group("ui"):
                        if hasattr(elem, 'typeing'):
                            elem.typeing(event)

        for card in BaseCard.cards:
            if card.rect.collidepoint(pg.mouse.get_pos()):
                if card.hovering == False:
                    card.hover()
            else:
                if card.hovering == True:
                    card.no_hover()

            card.update()
            

        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                
                if UIBase.DebugInspect == True:
                    dontMake = False
                    for elem2 in UIBase.get_group('ui'):
                        if isinstance(elem2, UIBase.DebugUIInspector):
                            if elem2.currentIns == elem:
                                dontMake = True
                            elif elem2 == elem:
                                dontMake = True

                    if dontMake == False:
                        UIBase.Insepctors.append(UIBase.DebugUIInspector(elem))

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
        screen.fill('#B7B7B7')
        UIBase.get_group("ui").draw(screen)
        BaseCard.cards.draw(screen)
        if UIBase.get_modus() == 'STACK' and StackManager.get_length(): StackManager.get_stack().draw(screen)
        CardOutline.currentOutline.draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

