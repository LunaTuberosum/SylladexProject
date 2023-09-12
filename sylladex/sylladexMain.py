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
from .uiElements.debugInspector import DebugInspector
from .uiElements.dropDown import DropDown
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
    ConsoleMessage,
    CustomSettingAreaBox,
    CustomSettingButton,
    CustomSettingMenu,
    CustomSettingSectionName,
    DebugInspector,
    DropDown,
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
    FinishButton,
])


def main(screen, clock):

    global_prev_tick = pg.time.get_ticks()

    UIElement.get_ui_elem('StackingArea')()
    UIElement.get_ui_elem('CenterObj')()
    UIElement.get_ui_elem('SideBarButton')()
    UIElement.get_ui_elem('GristCacheButton')()
    UIElement.get_ui_elem('CustomSettingButton')()
    # BaseCard.load_cards()
    move_card = False
    debug_inspect = False

    while True:

        now_tick = pg.time.get_ticks()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    move_card = True

                    for _elem in UIElement.get_group("ui"):
                        if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                            UIElement.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()

                    for _elem in UIElement.get_group('ui'):
                        if hasattr(_elem, "active") and _elem.active == True:
                            if hasattr(_elem, "exit_field"):
                                _elem.exit_field()
                        if hasattr(_elem, "on_click") and _elem.rect.collidepoint(event.pos):
                            _elem.on_click()
                            move_card = False

                            # if UIElement.get_ui_elem('RemoveCardButton').get_eject() == True:
                            #     if len(UIElement.get_ui_elem('CardList').children) == 0:
                            #         UIElement.get_ui_elem('RemoveCardButton').get_eject() = False
                            #     else:
                            #         for _elem in UIElement.get_group("ui"):
                            #             if isinstance(_elem, UIElement.get_ui_elem('ListObject')):
                            #                 _elem.redraw_card((230,230,230))

                            # elif UIElement.get_ui_elem('RemoveCardButton').get_eject() == False:
                            #     for _elem in UIElement.get_group("ui"):
                            #         if isinstance(_elem, UIElement.get_ui_elem('ListObject')):
                            #             _elem.redraw_card((255,255,255))

                    if move_card == True:
                        for _card in BaseCard.cards:
                            if _card.rect.collidepoint(pg.mouse.get_pos()) and _card.selected == False:
                                _card.on_click()
                                move_card = False
                elif event.button == 2:
                    for _card in BaseCard.get_cardGroup():
                        if _card.rect.collidepoint(event.pos):
                            _card.on_middleClick()

                elif event.button == 3:
                    for _elem in UIElement.get_group("ui"):
                        if hasattr(_elem, "on_altClick") and _elem.rect.collidepoint(event.pos):
                            _elem.on_altClick()

            elif event.type == pg.MOUSEBUTTONUP:
                for _card in BaseCard.cards:
                    if _card.selected == True:
                        _card.on_release()

                if BaseCard.get_length() > 0:
                    move_card = False

                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('ScrollBar')):
                        _elem.set_selected(False)

                    elif hasattr(_elem, 'grabbed') and _elem.grabbed == True:
                        if _elem.rect.x > 326:
                            if _elem.captaCard == None:
                                _elem.captaCard = BaseCard(
                                    _elem.rect.topleft, _elem.codeData)
                                _elem.codeData.cardID = _elem.captaCard.cardID
                                _elem.captaCard.codeData.cardID = _elem.captaCard.cardID
                                _elem.redraw_card('#FFFFFF')

                                for _elem in UIElement.get_group('ui'):
                                    if isinstance(_elem, UIElement.get_ui_elem('CardList')):
                                        _elem.save_list()
                                        break
                            else:
                                UIElement.get_ui_elem('PopUp')(
                                    'This _card is already deployed')
                        else:
                            UIElement.get_ui_elem('PopUp')(
                                'Drag the _card into the stacking area')

                        _elem.rect.topleft = _elem.prevPos
                        UIElement.get_group('layer').change_layer(_elem, -1)
                        for child in _elem.children:
                            UIElement.get_group(
                                'layer').change_layer(_elem, -1)
                        _elem.grabbed = False

            elif event.type == pg.MOUSEMOTION:
                for _elem in UIElement.get_group("ui"):
                    if isinstance(_elem, UIElement.get_ui_elem('ScrollBar')):
                        if _elem.get_selected() == True:
                            _elem.move_bar(event.pos)

                    for _elem in UIElement.get_group('ui'):
                        if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                            UIElement.remove_from_group(_elem)
                            break
                    global_prev_tick = pg.time.get_ticks()

                for _card in BaseCard.cards:
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

                elif event.mod == pg.KMOD_LCTRL and event.key == pg.K_r:
                    for _elem in UIElement.get_group('ui'):
                        if isinstance(_elem, UIElement.get_ui_elem('CenterObj')):
                            _elem.recenter()

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
                else:
                    for _elem in UIElement.get_group("ui"):
                        if isinstance(_elem, UIElement.get_ui_elem('TextField')):
                            _elem.typing(event)

        for _card in BaseCard.cards:
            if _card.rect.collidepoint(pg.mouse.get_pos()):
                if _card.hovering == False:
                    _card.hover()

            else:
                if _card.hovering == True:
                    _card.no_hover()

            _card.update()

        for _elem in UIElement.get_group("ui"):
            _elem.current_tick += _elem.clock.tick(30)

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

                if hasattr(_elem, "hover") and _elem.hovering == False:
                    if isinstance(_elem, UIElement.get_ui_elem('ListObject')) and UIElement.get_ui_elem('RemoveCardButton').get_eject() == True:
                        _elem.alt_hover()
                    else:
                        _elem.hover()

                if hasattr(_elem, "tool_tip_text"):
                    if hasattr(_elem, "active") and _elem.active == True:
                        pass
                    elif hasattr(_elem, 'inactive') and _elem.inactive == True:
                        pass
                    elif now_tick - global_prev_tick >= 1300:
                        UIElement.get_ui_elem('ToolTip')(
                            pg.mouse.get_pos(), _elem.tool_tip_text)
                        global_prev_tick = now_tick
            else:
                if hasattr(_elem, "negate"):
                    _elem.negate = False

                if hasattr(_elem, "no_hover") and _elem.hovering == True:
                    if isinstance(_elem, UIElement.get_ui_elem('ListObject')) and UIElement.get_ui_elem('RemoveCardButton').get_eject() == True:
                        _elem.alt_no_hover()
                    else:
                        _elem.no_hover()

            if isinstance(_elem, UIElement.get_ui_elem('PopUp')) and hasattr(_elem, "last") and now_tick - _elem.last >= _elem.timer:
                _elem.remove()
                if _elem:
                    _elem.last = pg.time.get_ticks()

            if isinstance(_elem, UIElement.get_ui_elem('ToolTip')):
                for _elem in UIElement.get_group('ui'):
                    if _elem.rect.collidepoint(pg.mouse.get_pos()):
                        pass
                    elif hasattr(_elem, 'toolTipText'):
                        if _elem.toolTipText == _elem.text:
                            UIElement.remove_from_group(_elem)
                            global_prev_tick = pg.time.get_ticks()
                            break

            if hasattr(_elem, "update"):
                _elem.update()

        clock.tick(30)
        screen.fill('#B7B7B7')
        UIElement.get_group("ui").draw(screen)
        BaseCard.cards.draw(screen)
        if UIElement.get_modus() == 'STACK' and StackManager.get_length():
            StackManager.get_stack().draw(screen)
        CardOutline.currentOutline.draw(screen)
        UIElement.get_group("layer").draw(screen)
        pg.display.flip()
