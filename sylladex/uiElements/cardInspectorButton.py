from turtle import circle
import pygame as pg

from baseUI import UIBase


class CardInspectorButton(UIBase):
    def __init__(self, cInspect):
        super().__init__(cInspect.rect.x-70, cInspect.rect.y+((cInspect.rect.h/2)-35), (70,70), 'CardInspectorButton', (0,0,0))

        self.create_appearance([[64, 64], UIBase.modusBackground, [0, 6]], [[64, 64], UIBase.modusAccent, [6, 0]], colorKey = True, image = [f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0]])

        self.toolTipText = 'Closes Card Inspector'
        self.hovering = False

        self.cInspect = cInspect

    def hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON_HOVER.png', [6, 0])
        self.hovering = True

    def no_hover(self):
        self.reload_image(f'sylladex/uiElements/asset/{UIBase.get_modus()}/SIDE_BAR_ICON.png', [6, 0])
        self.hovering = False

    def on_click(self):
        UIBase.remove_fromGroup(self.cInspect)
        self.cInspect.kill()
        for child in self.cInspect.children:
            UIBase.remove_fromGroup(child)
            child.kill()