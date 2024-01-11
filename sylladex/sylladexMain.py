import pygame as pg

from uiElement import UIElement
from .captchalogueCards.stackManager import StackManager

from .captchalogueCards.cardOutline import CardOutline
from .captchalogueCards.baseCard import BaseCard

from .uiElements.actionIcon import ActionIcon
from .uiElements.addCardButton import AddCardButton
from .uiElements.cardInspector import CardInspector
from .uiElements.cardInspectorButton import CardInspectorButton
from .uiElements.cardInspectorCheck import CardInspectorCheck
from .uiElements.cardList import CardList
from .uiElements.centerObj import CenterObj
from .uiElements.consoleMessage import ConsoleMessage
from .uiElements.customSettingAreaBox import CustomSettingAreaBox
from .uiElements.customSettingButton import CustomSettingButton
from .uiElements.customSettingMenu import CustomSettingMenu
from .uiElements.customSettingSectionName import CustomSettingSectionName
<<<<<<< HEAD
=======
from .uiElements.debugInspector import DebugInspector
from .uiElements.dropDown import DropDown
from .uiElements.dropDownBackground import DropDownBackground
from .uiElements.dropDownOption import DropDownOption
>>>>>>> CodeAndVisual
from .uiElements.editCardButton import EditCardButton
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

UIElement.add_current_ui([
    ActionIcon,
    AddCardButton,
    CardInspector,
    CardInspectorButton,
    CardInspectorCheck,
    CardList,
    CenterObj,
<<<<<<< HEAD
    ConsoleMessage, 
    CustomSettingAreaBox, 
    CustomSettingButton, 
    CustomSettingMenu, 
    CustomSettingSectionName, 
    EditCardButton, 
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
=======
    ConsoleMessage,
    CustomSettingAreaBox,
    CustomSettingButton,
    CustomSettingMenu,
    CustomSettingSectionName,
    DebugInspector,
    DropDown,
    DropDownBackground,
    DropDownOption,
    EditCardButton,
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
    PopUp,
    RemoveCardButton,
    ScrollBar,
    SideBar,
    SideBarButton,
    StackingArea,
    TextField,
    ToggleButton,
    ToolTip,
>>>>>>> CodeAndVisual
    FinishButton,
])


def main(screen, clock):

    global_prev_tick = pg.time.get_ticks()

    UIElement.get_ui_elem('StackingArea')()
    UIElement.get_ui_elem('CenterObj')()
    UIElement.get_ui_elem('SideBarButton')()
    UIElement.get_ui_elem('GristCacheButton')()
    UIElement.get_ui_elem('CustomSettingButton')()
    BaseCard.load_cards()
    move_card = False
    debug_inspect = False

    while True:

        now_tick = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    move_card = True

<<<<<<< HEAD
                    for elem in UIBase.get_group("ui"):
                        if isinstance(elem, UIBase.get_uiElem('ToolTip')):
                            UIBase.remove_fromGroup(elem)
                            elem.kill()
                            globalPrevTick = pg.time.get_ticks()
                        
                    for elem in UIBase.get_group('ui'):
                        if hasattr(elem, "active") and elem.active == True:
                            if hasattr(elem, "exit_field"):
                                elem.draw()
                                elem.exit_field()
                        if hasattr(elem, "on_click") and elem.rect.collidepoint(event.pos):
                            elem.on_click()
                            moveCard = False
                            
                            if UIBase.get_uiElem('RemoveCardButton').eject == True:
                                if len(UIBase.get_uiElem('CardList').children) == 0:
                                    UIBase.get_uiElem('RemoveCardButton').eject = False
=======
                    for _elem in UIElement.get_group("ui"):
                        if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                            UIElement.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()

                    _clicked_element = []
                    for _elem in UIElement.get_group('ui'):
                        if hasattr(_elem, "active") and _elem.active == True:
                            if hasattr(_elem, "exit_field"):
                                _elem.exit_field()

                        if _elem.rect.collidepoint(event.pos):
                            _clicked_element.append(_elem)
                            move_card = False

                    _clicked = UIElement.find_highest_elem(_clicked_element)
                    if _clicked:
                        _clicked.on_click()

                    if move_card == True:
                        _clicked_card = []
                        for _card in BaseCard.get_cards():
                            if _card.rect.collidepoint(pg.mouse.get_pos()) and _card.selected == False:
                                _clicked_card.append(_card)
                                move_card = False

                        _clicked_c = BaseCard.find_highest_card(_clicked_card)
                        if _clicked_c:
                            _clicked_c.on_click()
>>>>>>> CodeAndVisual

                elif event.button == 2:
                    _clicked_card = []
                    for _card in BaseCard.get_cards():
                        if _card.rect.collidepoint(event.pos):
                            _clicked_card.append(_card)

                    _clicked_c = BaseCard.find_highest_card(_clicked_card)
                    if _clicked_c:
                        _clicked_c.on_middle_click()

                elif event.button == 3:
                    for _elem in UIElement.get_group("ui"):
                        if hasattr(_elem, "on_altClick") and _elem.rect.collidepoint(event.pos):
                            _elem.on_altClick()

            elif event.type == pg.MOUSEBUTTONUP:
                for _card in BaseCard.get_cards():
                    if _card.selected == True:
                        _card.on_release()

                if BaseCard.get_length() > 0:
                    move_card = False

                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('ScrollBar')):
                        _elem.set_selected(False)

                    elif hasattr(_elem, 'grabbed') and _elem.grabbed == True:
                        _elem.on_release(event.pos)

            elif event.type == pg.MOUSEMOTION:
                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('ScrollBar')):
                        if _elem.get_selected() == True:
                            _elem.move_bar(event.rel[1])

                    if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                        UIElement.remove_from_group(_elem)
                        break

                    if isinstance(_elem, UIElement.get_ui_elem('ListObject')):
                        _elem.move(event.rel)

                    global_prev_tick = pg.time.get_ticks()

                for _card in BaseCard.get_cards():
                    if _card.selected == True:
                        _card.move(event.rel)
                        _card.moving = True
                    else:
                        _card.moving = False

                if BaseCard.get_length() > 0:
                    if move_card == True:
                        BaseCard.move_all_cards(event.rel)
                        for _elem in UIElement.get_group('ui'):
                            if isinstance(_elem, UIElement.get_ui_elem('CenterObj')):
                                _elem.move_self(event.rel)

            elif event.type == pg.MOUSEWHEEL:
                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('CardList')):
                        if _elem.rect.collidepoint(pg.mouse.get_pos()):
                            for _elem in UIElement.get_group("ui"):
                                if isinstance(_elem, UIElement.get_ui_elem('ScrollBar')):
                                    _elem.move_bar_wheel(-event.y)

            if event.type == pg.KEYDOWN:
                if event.mod == pg.KMOD_LCTRL and event.key == pg.K_i:
                    if debug_inspect == False:
                        debug_inspect = True
                    else:
                        debug_inspect = False
                        UIElement.get_ui_elem(
                            'DebugInspector').clear_inspectors()
                        for _elem in UIElement.get_group('ui'):
                            if isinstance(_elem, UIElement.get_ui_elem('DebugInspector')):
                                UIElement.remove_from_group(_elem)

                elif event.mod == pg.KMOD_LCTRL and event.key == pg.K_HOME:
                    UIElement.find_current_ui('CenterObj').only_center_self()
                    BaseCard.save_cards()
                    UIElement.get_ui_elem('ConsoleMessage')(
                        'Saved new center')

                elif event.key == pg.K_HOME:
                    UIElement.find_current_ui('CenterObj').recenter()

                elif event.key == pg.K_ESCAPE:
                    _load_escape_screen = True
                    for _elem in UIElement.get_group('ui'):
                        if isinstance(_elem, UIElement.get_ui_elem('EscapeMenu')):
                            for child in _elem.children:
                                UIElement.remove_from_group(child)
                                child.kill()
                            UIElement.remove_from_group(_elem)
                            _load_escape_screen = False

                    if _load_escape_screen == True:
                        UIElement.get_ui_elem('EscapeMenu')()

                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('TextField')):
                        _elem.typing(event)

                    if isinstance(_elem, UIElement.get_ui_elem('ActionIcon')):
                        _elem.typing(event)

        _hovered_card = []
        for _card in BaseCard.get_cards():
            _card.no_hover()

            if _card.rect.collidepoint(pg.mouse.get_pos()):
                if _card.hovering == False:
                    _hovered_card.append(_card)

            _card.update()

        _hovered_c = BaseCard.find_highest_card(_hovered_card)
        if _hovered_c:
            _hovered_c.hover()

        _hovered_element = []
        _tooled_element = []
        for _elem in UIElement.get_group("ui"):
            _elem.current_tick += _elem.clock.tick(30)
            _elem.no_hover()

            if _elem.rect.collidepoint(pg.mouse.get_pos()):

                if debug_inspect == True:
                    _make_inspector = True
                    for _ins in UIElement.get_ui_elem('DebugInspector').get_current_ins():
                        if _ins.current_inspectie == _elem:
                            _make_inspector = False

                    if isinstance(_elem, UIElement.get_ui_elem('DebugInspector')):
                        _make_inspector = False

                    if hasattr(_elem, 'interactable') and _elem.interactable == False:
                        _make_inspector = False

                    if _make_inspector == True:
                        UIElement.get_ui_elem('DebugInspector')(_elem)

                    for _index, _ins in enumerate(UIElement.get_ui_elem('DebugInspector').get_current_ins()):
                        if _index == 0:
                            _ins.rect.x = (
                                pg.display.get_surface().get_width() - 10) - (_ins.rect.w)
                            growingOffSet = _ins.rect.w + 20
                        else:
                            _ins.rect.x = (pg.display.get_surface(
                            ).get_width() - 10) - (growingOffSet)-(_ins.rect.w)
                            growingOffSet += _ins.rect.w + 20

                if isinstance(_elem, UIElement.get_ui_elem('PopUp')):
                    _elem.negate = True

                if _elem.hovering == False:
                    _hovered_element.append(_elem)

                if hasattr(_elem, "active") and _elem.active == True:
                    pass
                elif hasattr(_elem, 'inactive') and _elem.inactive == True:
                    pass
                elif now_tick - global_prev_tick >= 1300:
                    _tooled_element.append(_elem)

            else:
                if hasattr(_elem, "negate"):
                    _elem.negate = False

            if isinstance(_elem, UIElement.get_ui_elem('PopUp')) and hasattr(_elem, "last") and now_tick - _elem.last >= _elem.timer:
                _elem.remove()
                if _elem:
                    _elem.last = pg.time.get_ticks()

<<<<<<< HEAD
        for elem in UIBase.get_group("ui"):
            if elem.rect.collidepoint(pg.mouse.get_pos()):
                
                if UIBase.DebugInspect == True:
                    dontMake = False
                    for _elem in UIBase.get_group('ui'):
                        if isinstance(_elem, UIBase.DebugUIInspector):
                            if _elem.currentIns == elem:
                                dontMake = True
                            elif _elem == elem:
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
                        if isinstance(elem, UIBase.get_uiElem('ListObject')) and (UIBase.get_uiElem('RemoveCardButton').eject == True or UIBase.get_uiElem('EditCardButton').edit == True):
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
                    if isinstance(elem, UIBase.get_uiElem('ListObject')) and (UIBase.get_uiElem('RemoveCardButton').eject == True or UIBase.get_uiElem('EditCardButton').edit == True):
                        elem.alt_no_hover()
                    else:
                        elem.no_hover()

            if isinstance(elem, UIBase.get_uiElem('PopUp')) and  hasattr(elem, "last") and nowTick - elem.last >= elem.timer:
                elem.remove()
                if elem:
                    elem.last = pg.time.get_ticks()

            if isinstance(elem, UIBase.get_uiElem('ToolTip')):
                for _elem in UIBase.get_group('ui'):
=======
            if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                for _elem in UIElement.get_group('ui'):
>>>>>>> CodeAndVisual
                    if _elem.rect.collidepoint(pg.mouse.get_pos()):
                        pass
                    elif hasattr(_elem, 'toolTipText'):
                        if _elem.toolTipText == _elem.text:
                            UIElement.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()
                            break

            if hasattr(_elem, "update"):
                _elem.update()

        _hovered = UIElement.find_highest_elem(_hovered_element)
        if _hovered:
            _hovered.hover()

        _tooled = UIElement.find_highest_elem(_tooled_element)
        if _tooled:
            if _tooled.tool_tip_text != '':
                UIElement.get_ui_elem('ToolTip')(
                    pg.mouse.get_pos(), _tooled.tool_tip_text)
                global_prev_tick = now_tick

        clock.tick(30)
        screen.fill('#B7B7B7')
        UIElement.get_group("ui").draw(screen)

        _temp_group = pg.sprite.LayeredUpdates()
        for _card in BaseCard.get_cards():
            _temp_group.add(_card)
            _temp_group.change_layer(_card, -_card.rect.y)
        _temp_group.draw(screen)
        _temp_group.empty()
        if UIElement.get_modus() == 'STACK' and StackManager.get_length():
            StackManager.get_stack().draw(screen)
        CardOutline.current_outline.draw(screen)
        UIElement.get_group("layer").draw(screen)
        BaseCard.grabbed_card.draw(screen)
        pg.display.flip()
