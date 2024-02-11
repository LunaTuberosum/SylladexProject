import inspect
import pygame as pg

from uiElement import UIElement
from .captchalogueCards.stackManager import StackManager

from .captchalogueCards.cardOutline import CardOutline
from .captchalogueCards.baseCard import BaseCard

from . import uiElements

for _class_name, _class_obj in inspect.getmembers(uiElements):
    if _class_name == '__doc__':
        continue
    for _class in dir(_class_obj):
        if _class_name.upper() == _class.upper():
            UIElement.add_current_ui(getattr(_class_obj, _class))


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

                elif event.button == 2:
                    _clicked = []
                    for _elem in UIElement.get_group('ui'):
                        if _elem.rect.collidepoint(event.pos):
                            _clicked.append(_elem)

                    _clicked = UIElement.find_highest_elem(_clicked)
                    if _clicked:
                        _clicked.on_middle_click()

                    _clicked_card = []
                    for _card in BaseCard.get_cards():
                        if _card.rect.collidepoint(event.pos):
                            _clicked_card.append(_card)

                    _clicked_c = BaseCard.find_highest_card(_clicked_card)
                    if _clicked_c:
                        _clicked_c.on_middle_click()

                elif event.button == 3:
                    _clicked = []
                    for _elem in UIElement.get_group('ui'):
                        if _elem.rect.collidepoint(event.pos):
                            _clicked.append(_elem)

                    _clicked = UIElement.find_highest_elem(_clicked)
                    if _clicked:
                        _clicked.on_right_click()

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
                        if _elem.rect.collidepoint(pg.mouse.get_pos()) and len(_elem.get_list()):
                            UIElement.find_current_ui(
                                'ScrollBar').move_bar_wheel(-event.y)

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
            if not UIElement.get_group('ui').has(_elem):
                continue
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
        update_screen(screen)

        pg.display.flip()


def update_screen(screen):

    _card_pass = pg.sprite.LayeredUpdates()
    for _card in BaseCard.get_cards():
        _card_pass.add(_card)
        _card_pass.change_layer(_card, -_card.rect.y)

    _card_pass.draw(screen)
    _card_pass.empty()

    _elem_pass = pg.sprite.Group()

    for _elem in UIElement.get_group('ui'):
        if _elem.interactable:
            _elem_pass.add(_elem)

    _elem_pass.draw(screen)
    _elem_pass.empty()

    # if UIElement.get_modus() == 'STACK' and StackManager.get_length():
    #     StackManager.get_stack().draw(screen)

    CardOutline.current_outline.draw(screen)

    _layering_pass = pg.sprite.LayeredUpdates()

    for _elem in UIElement.get_group('layer'):
        if _elem.interactable:
            _layering_pass.add(_elem)
            _layering_pass.change_layer(_elem, UIElement.get_group(
                'layer').get_layer_of_sprite(_elem))

    _layering_pass.draw(screen)
    _layering_pass.empty()

    BaseCard.grabbed_card.draw(screen)
