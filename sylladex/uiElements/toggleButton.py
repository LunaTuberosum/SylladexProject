import pygame as pg

from baseUI import UIBase


class ToggleButton(UIBase):
    def __init__(self, x, y, job, text):
        super().__init__(x, y, (30,30), f'ToggleButton ({job})', '#ffffff')

        self.job = job
        self.text = text

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)

        self._create_appearance([[24,24], '#1C4587', [6,6]], [[24,24], '#3C78D8', [0,0]], texts = [[self.text, [12, 12], 'center']], colorKey = True)

        self.on = False
        self.hovering = False

    def hover(self):
        if self.on == False:
            self.backgroundColor = pg.Surface((24,24))
            self.backgroundColor.fill('#1C4587')
            self.image.blit(self.backgroundColor, [6, 6])
            
            self.foregroundColor = pg.Surface((24,24))
            self.foregroundColor.fill('#C9DAF8')
            self.image.blit(self.foregroundColor, [0, 0])
            txt_surf = self.font.render(self.text, True, (0,0,0))
            self.image.blit(txt_surf, [12-(txt_surf.get_width()/2), 12-(txt_surf.get_height()/2)])
            self.hovering = True

    def no_hover(self):
        if self.on == False:
            self.backgroundColor = pg.Surface((24,24))
            self.backgroundColor.fill('#1C4587')
            self.image.blit(self.backgroundColor, [6, 6])
            
            self.foregroundColor = pg.Surface((24,24))
            self.foregroundColor.fill('#3C78D8')
            self.image.blit(self.foregroundColor, [0, 0])
            txt_surf = self.font.render(self.text, True, (0,0,0))
            self.image.blit(txt_surf, [12-(txt_surf.get_width()/2), 12-(txt_surf.get_height()/2)])
            self.hovering = False

    def on_click(self):
        with open('sylladex/captchalogueCards/data/codeDatabase.txt', 'r') as database:
            customData = database.readlines()

        if self.job == 'meleeToggle' or self.job == 'rangedToggle' or self.job == 'magicToggle':
            if self.on == False:
                for elem in UIBase.get_group('ui'):
                    if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                        
                        if elem.job == 'meleeToggle': 
                            elem.on = False
                            elem.no_hover()
                        elif elem.job == 'rangedToggle': 
                            elem.on = False
                            elem.no_hover()
                        elif elem.job == 'magicToggle': 
                            elem.on = False
                            elem.no_hover()

                    if isinstance(elem, UIBase.get_uiElem('ActionIcon')):
                        if elem.job == 'action1Icon':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[0][2:]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[0][2:]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[0][2:]
                            elem.draw()
                        elif elem.job == 'action2Icon':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[4][2:]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[4][2:]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[4][2:]
                            elem.draw()

                    elif isinstance(elem, UIBase.get_uiElem('TextField')):
                        if elem.job == 'action1Cost':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[1]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[1]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[1]
                            elem.no_hover()
                        elif elem.job == 'action2Cost':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[5]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[5]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[5]
                            elem.no_hover()

                        elif elem.job == 'action1Dmg':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[2]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[2]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[2]
                            elem.no_hover()
                        elif elem.job == 'action2Dmg':
                            if self.job == 'meleeToggle': elem.text = customData[2].split(',')[6]
                            elif self.job == 'rangedToggle': elem.text = customData[3].split(',')[6]
                            elif self.job == 'magicToggle': elem.text = customData[4].split(',')[6]
                            elem.no_hover()
                    
                    elif isinstance(elem, UIBase.get_uiElem('LongTextField')):
                        if elem.job == 'action1Desc':
                            if self.job == 'meleeToggle': elem.starter_text(customData[2].split(',')[3])
                            elif self.job == 'rangedToggle': elem.starter_text(customData[3].split(',')[3])
                            elif self.job == 'magicToggle': elem.starter_text(customData[4].split(',')[3])
                        elif elem.job == 'action2Desc':
                            if self.job == 'meleeToggle': elem.starter_text(customData[2].split(',')[7])
                            elif self.job == 'rangedToggle': elem.starter_text(customData[3].split(',')[7])
                            elif self.job == 'magicToggle': elem.starter_text(customData[4].split(',')[7])
            
        elif self.job == 't1Toggle' or self.job == 't2Toggle' or self.job == 't3Toggle' or self.job == 't4Toggle':
            if self.on == False:
                for elem in UIBase.get_group('ui'):
                    if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                        
                        if elem.job == 't1Toggle': 
                            elem.on = False
                            elem.no_hover()
                        elif elem.job == 't2Toggle': 
                            elem.on = False
                            elem.no_hover()
                        elif elem.job == 't3Toggle': 
                            elem.on = False
                            elem.no_hover()
                        elif elem.job == 't4Toggle': 
                            elem.on = False
                            elem.no_hover()

                    elif isinstance(elem, UIBase.get_uiElem('TextField')):
                        if elem.job == 'traitName':
                            if self.job == 't1Toggle': elem.text = customData[5].split(',')[0]
                            elif self.job == 't2Toggle': elem.text = customData[6].split(',')[0]
                            elif self.job == 't3Toggle': elem.text = customData[7].split(',')[0]
                            elif self.job == 't4Toggle': elem.text = customData[8].split(',')[0]
                            elem.no_hover()

                    elif isinstance(elem, UIBase.get_uiElem('LongTextField')):
                        if elem.job == '1-4Desc':
                            if self.job == 't1Toggle': elem.starter_text(customData[5].split(',')[1])
                            elif self.job == 't2Toggle': elem.starter_text(customData[6].split(',')[1])
                            elif self.job == 't3Toggle': elem.starter_text(customData[7].split(',')[1])
                            elif self.job == 't4Toggle': elem.starter_text(customData[8].split(',')[1])
                        if elem.job == '5-8Desc':
                            if self.job == 't1Toggle': elem.starter_text(customData[5].split(',')[2])
                            elif self.job == 't2Toggle': elem.starter_text(customData[6].split(',')[2])
                            elif self.job == 't3Toggle': elem.starter_text(customData[7].split(',')[2])
                            elif self.job == 't4Toggle': elem.starter_text(customData[8].split(',')[2])
                        if elem.job == '9-12Desc':
                            if self.job == 't1Toggle': elem.starter_text(customData[5].split(',')[3])
                            elif self.job == 't2Toggle': elem.starter_text(customData[6].split(',')[3])
                            elif self.job == 't3Toggle': elem.starter_text(customData[7].split(',')[3])
                            elif self.job == 't4Toggle': elem.starter_text(customData[8].split(',')[3])
                        if elem.job == '13-16Desc':
                            if self.job == 't1Toggle': elem.starter_text(customData[5].split(',')[4])
                            elif self.job == 't2Toggle': elem.starter_text(customData[6].split(',')[4])
                            elif self.job == 't3Toggle': elem.starter_text(customData[7].split(',')[4])
                            elif self.job == 't4Toggle': elem.starter_text(customData[8].split(',')[4])

        self.hover()
        self.on = True