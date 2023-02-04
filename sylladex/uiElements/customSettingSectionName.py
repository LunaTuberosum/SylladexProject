import pygame as pg

from baseUI import UIBase


class CustomSettingSectionName(UIBase):
    def __init__(self, parent, y, section):
        self.parent = parent
        self.section = section
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        super().__init__(self.parent.rect.x+12, self.parent.rect.y+y, (186,30), f'CustomSettingSectionName ({self.section})', (255,255,255))

        if self.section == 'ACTIONS': _text_value = 'CUSTOM MELEE ACTIONS'
        else: _text_value = 'CUSTOM ' + self.section
        
        self.create_appearance([[180, 24], '#1C4587', [6, 6]], [[180, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [[_text_value, [90, 12], 'center']])


    def update(self):
        if self.section == 'ACTIONS':
            for _elem in UIBase.get_group('ui'):
                if isinstance(_elem, UIBase.get_uiElem('ToggleButton')):
                    if _elem.job == 'meleeToggle':
                        if _elem.on == True:
                            self.create_appearance([[180, 24], '#1C4587', [6, 6]], [[180, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['CUSTOM MELEE ACTIONS', [90, 12], 'center']])

                    elif _elem.job == 'rangedToggle':
                        if _elem.on == True:
                            self.create_appearance([[180, 24], '#1C4587', [6, 6]], [[180, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['CUSTOM RANGED ACTIONS', [90, 12], 'center']])

                    elif _elem.job == 'magicToggle':
                        if _elem.on == True:
                            self.create_appearance([[180, 24], '#1C4587', [6, 6]], [[180, 24], '#3C78D8', [0, 0]], colorKey = True, texts = [['CUSTOM MAGIC ACTIONS', [90, 12], 'center']])