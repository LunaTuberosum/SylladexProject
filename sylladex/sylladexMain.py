import pygame as pg

from baseUI import UIBase
from .captchalogueCards.stackManager import StackManager

from .captchalogueCards.cardOutline import CardOutline
from .captchalogueCards.baseCard import BaseCard

from .uiElements.actionIcon import ActionIcon
from .uiElements.addCardButton import AddCardButton
from .uiElements.cardInspector import CardInspector
from .uiElements.cardInspectorButton import CardInspectorButton
from sylladex.uiElements.cardInspectorCheck import CardInspectorCheck
from .uiElements.cardList import CardList
from .uiElements.centerObj import CenterObj
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
from .uiElements.sidebarButton import SideBarButton
from .uiElements.stackingArea import StackingArea
from .uiElements.textField import TextField
from .uiElements.toggleButton import ToggleButton
from .uiElements.toolTip import ToolTip
from .uiElements.finishButton import FinishButton

UIBase.add_current_ui([
    ActionIcon, 
    AddCardButton, 
    CardInspector,
    CardInspectorButton,
    CardInspectorCheck,
    CardList, 
    CenterObj,
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
    SideBarButton, 
    StackingArea, 
    TextField, 
    ToggleButton, 
    ToolTip, 
    FinishButton,
    ])

def main(screen, clock):

    global_prev_tick = pg.time.get_ticks()

    UIBase.get_ui_elem('StackingArea')()
    UIBase.get_ui_elem('CenterObj')()
    UIBase.get_ui_elem('SideBarButton')()
    UIBase.get_ui_elem('GristCacheButton')()
    UIBase.get_ui_elem('CustomSettingButton')()
    # BaseCard.load_cards()
    _move_card = False

    while True:

        now_tick = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    _move_card = True

                    for _elem in UIBase.get_group("ui"):
                        if isinstance(_elem, UIBase.get_ui_elem('ToolTip')):
                            UIBase.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()
                        
                    for _elem in UIBase.get_group('ui'):
                        if hasattr(_elem, "active") and _elem.active == True:
                            if hasattr(_elem, "exit_field"):
                                _elem.exit_field()
                        if hasattr(_elem, "on_click") and _elem.rect.collidepoint(event.pos):
                            _elem.on_click()
                            _move_card = False
                            
                            # if UIBase.get_ui_elem('RemoveCardButton').get_eject() == True:
                            #     if len(UIBase.get_ui_elem('CardList').children) == 0:
                            #         UIBase.get_ui_elem('RemoveCardButton').get_eject() = False
                            #     else:
                            #         for _elem in UIBase.get_group("ui"):
                            #             if isinstance(_elem, UIBase.get_ui_elem('ListObject')):    
                            #                 _elem.redraw_card((230,230,230))

                            # elif UIBase.get_ui_elem('RemoveCardButton').get_eject() == False:
                            #     for _elem in UIBase.get_group("ui"):
                            #         if isinstance(_elem, UIBase.get_ui_elem('ListObject')):    
                            #             _elem.redraw_card((255,255,255))

                    if _move_card == True:
                        for _card in BaseCard.cards:
                            if _card.rect.collidepoint(pg.mouse.get_pos()) and _card.selected == False:
                                _card.on_click()
                                _move_card = False
                elif event.button == 2:
                    for _card in BaseCard.get_cardGroup():
                        if _card.rect.collidepoint(event.pos):
                            _card.on_middleClick()

                elif event.button == 3:
                    for _elem in UIBase.get_group("ui"):
                        if hasattr(_elem, "on_altClick") and _elem.rect.collidepoint(event.pos):
                            _elem.on_altClick()
            
            elif event.type == pg.MOUSEBUTTONUP:
                for _card in BaseCard.cards:
                    if _card.selected == True:
                        _card.on_release()

                if BaseCard.get_length() > 0:
                    _move_card = False

                for _elem in UIBase.get_group("ui"):
                    if isinstance(_elem, UIBase.get_ui_elem('ScrollBar')):
                        _elem.set_selected(False)
                    
                    elif hasattr(_elem, 'grabbed') and _elem.grabbed == True:
                        if _elem.rect.x > 326:
                            if _elem.captaCard == None:
                                _elem.captaCard = BaseCard(_elem.rect.topleft, _elem.codeData)
                                _elem.codeData.cardID = _elem.captaCard.cardID
                                _elem.captaCard.codeData.cardID = _elem.captaCard.cardID
                                _elem.redraw_card('#FFFFFF')

                                for _elem in UIBase.get_group('ui'):
                                    if isinstance(_elem, UIBase.get_ui_elem('CardList')):
                                        _elem.save_list()
                                        break
                            else:
                                UIBase.get_ui_elem('PopUp')('This _card is already deployed')
                        else:
                            UIBase.get_ui_elem('PopUp')('Drag the _card into the stacking area')

                        _elem.rect.topleft = _elem.prevPos
                        UIBase.get_group('layer').change_layer(_elem, -1)
                        for child in _elem.children:
                            UIBase.get_group('layer').change_layer(_elem, -1)   
                        _elem.grabbed = False
            
            elif event.type == pg.MOUSEMOTION:
                for _elem in UIBase.get_group("ui"):
                    if isinstance(_elem, UIBase.get_ui_elem('ScrollBar')):
                        if _elem.get_selected() == True:
                            _elem.move_bar(event.pos)

                    for _elem in UIBase.get_group('ui'):
                        if isinstance(_elem, UIBase.get_ui_elem('ToolTip')):
                            UIBase.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()
                            break
                
                for _card in BaseCard.cards:
                    if _card.selected == True:
                        _card.move(event.rel)
                        _card.moving = True
                    else:
                        _card.moving = False
                
                if BaseCard.get_length() > 0:
                    if _move_card == True:
                        BaseCard.move_all_cards(event.rel)
                        for _elem in UIBase.get_group('ui'):
                            if isinstance(_elem, UIBase.get_ui_elem('CenterObj')):
                                _elem.move_self(event.rel)

            elif event.type == pg.MOUSEWHEEL:
                for _elem in UIBase.get_group("ui"):
                    if isinstance(_elem, UIBase.get_ui_elem('CardList')):
                        if _elem.rect.collidepoint(pg.mouse.get_pos()):
                            for _elem in UIBase.get_group("ui"):
                                if isinstance(_elem, UIBase.get_ui_elem('ScrollBar')):
                                    _elem.move_bar_wheel(-event.y)

            if event.type == pg.KEYDOWN:
                if event.mod == pg.KMOD_LCTRL and event.key == pg.K_i:
                    if UIBase.DebugInspect == False:
                        UIBase.DebugInspect = True
                    else:
                        UIBase.DebugInspect = False
                        UIBase.Insepctors.clear()
                        for _elem in UIBase.get_group('ui'):
                            if isinstance(_elem, UIBase.DebugUIInspector):
                                UIBase.remove_from_group(_elem)

                elif event.mod == pg.KMOD_LCTRL and event.key == pg.K_r:
                    for _elem in UIBase.get_group('ui'):
                        if isinstance(_elem, UIBase.get_ui_elem('CenterObj')):
                            _elem.recenter()

                elif event.key == pg.K_ESCAPE:
                    _load_escape_screen = True
                    for _elem in UIBase.get_group('ui'):
                        if isinstance(_elem, UIBase.get_ui_elem('EscapeMenu')):
                            for child in _elem.children:
                                UIBase.remove_from_group(child)
                                child.kill()
                            UIBase.remove_from_group(_elem)
                            _load_escape_screen = False

                    if _load_escape_screen == True:
                        UIBase.get_ui_elem('EscapeMenu')()
                else:
                    for _elem in UIBase.get_group("ui"):
                        if isinstance(_elem, UIBase.get_ui_elem('TextField')):
                            _elem.typing(event)

        for _card in BaseCard.cards:
            if _card.rect.collidepoint(pg.mouse.get_pos()):
                if _card.hovering == False:
                    _card.hover()

            else:
                if _card.hovering == True:
                    _card.no_hover()            

            _card.update()

        for _elem in UIBase.get_group("ui"):
            _elem.current_tick += _elem.clock.tick(30)

            if _elem.rect.collidepoint(pg.mouse.get_pos()):
                
                if UIBase.DebugInspect == True:
                    _dont_make_debug = False
                    for _elem in UIBase.get_group('ui'):
                        if isinstance(_elem, UIBase.DebugUIInspector):
                            if _elem.currentIns == _elem:
                                _dont_make_debug = True
                            elif _elem == _elem:
                                _dont_make_debug = True

                    if _dont_make_debug == False:
                        UIBase.Insepctors.append(UIBase.DebugUIInspector(_elem))

                    for index, inspector in enumerate(UIBase.Insepctors):
                        if index == 0:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(inspector.rect.w)
                            _growing_off_set = inspector.rect.w+20
                        else:
                            inspector.rect.x = (pg.display.get_surface().get_width()-10)-(_growing_off_set)-(inspector.rect.w)
                            _growing_off_set += inspector.rect.w+20

                if isinstance(_elem, UIBase.get_ui_elem('PopUp')):
                    _elem.negate = True
                if hasattr(_elem, "hover") and _elem.hovering == False:
                        if isinstance(_elem, UIBase.get_ui_elem('ListObject'))and UIBase.get_ui_elem('RemoveCardButton').get_eject() == True:
                            _elem.alt_hover()
                        else:
                            _elem.hover()

                if hasattr(_elem, "toolTipText"):
                    if hasattr(_elem, "active") and _elem.active == True:
                        pass
                    elif hasattr(_elem, 'inactive') and _elem.inactive == True:
                        pass
                    elif now_tick - global_prev_tick >= 1300:
                        UIBase.get_ui_elem('ToolTip')(pg.mouse.get_pos(), _elem.toolTipText)
            else:
                if hasattr(_elem, "negate"):
                    _elem.negate = False
                if hasattr(_elem, "no_hover")and _elem.hovering == True:
                    if isinstance(_elem, UIBase.get_ui_elem('ListObject'))and UIBase.get_ui_elem('RemoveCardButton').get_eject() == True:
                        _elem.alt_no_hover()
                    else:
                        _elem.no_hover()

            if isinstance(_elem, UIBase.get_ui_elem('PopUp')) and  hasattr(_elem, "last") and now_tick - _elem.last >= _elem.timer:
                _elem.remove()
                if _elem:
                    _elem.last = pg.time.get_ticks()

            if isinstance(_elem, UIBase.get_ui_elem('ToolTip')):
                for _elem in UIBase.get_group('ui'):
                    if _elem.rect.collidepoint(pg.mouse.get_pos()):
                        pass
                    elif hasattr(_elem, 'toolTipText'):
                        if _elem.toolTipText == _elem.text:
                            UIBase.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()
                            break

            if hasattr(_elem, "update"):
                _elem.update()


        clock.tick(30)
        screen.fill('#B7B7B7')
        UIBase.get_group("ui").draw(screen)
        BaseCard.cards.draw(screen)
        if UIBase.get_modus() == 'STACK' and StackManager.get_length(): 
            StackManager.get_stack().draw(screen)
        CardOutline.currentOutline.draw(screen)
        UIBase.get_group("layer").draw(screen)
        pg.display.flip()

