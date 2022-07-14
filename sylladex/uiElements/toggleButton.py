import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class ToggleButton(UIBase):
    def __init__(self, x, y, job, text):
        super().__init__(x, y, (30,30), "surfaceRect", f'ToggleButton ({job})', True, '#ffffff')

        self.job = job
        self.text = text

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 18)
        self.image.set_colorkey((255,255,255))

        self.backgroundColor = pg.Surface((24,24))
        self.backgroundColor.fill('#1C4587')
        self.image.blit(self.backgroundColor, [6, 6])
        
        self.foregroundColor = pg.Surface((24,24))
        self.foregroundColor.fill('#3C78D8')
        self.image.blit(self.foregroundColor, [0, 0])

        txt_surf = self.font.render(self.text, True, (0,0,0))
        self.image.blit(txt_surf, [12-(txt_surf.get_width()/2), 12-(txt_surf.get_height()/2)])

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
                    if isinstance(elem, UIBase.ToggleButton):
                        
                        if elem.job == 'meleeToggle': 
                            elem.on = False
                            elem.no_hover()
                        if elem.job == 'rangedToggle': 
                            elem.on = False
                            elem.no_hover()
                        if elem.job == 'magicToggle': 
                            elem.on = False
                            elem.no_hover()

                    if isinstance(elem, UIBase.ActionIcon):
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

                    if isinstance(elem, UIBase.TextField):
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
                    if isinstance(elem, UIBase.LongTextField):
                        if elem.job == 'action1Desc':
                            if self.job == 'meleeToggle': elem.starter_text(customData[2].split(',')[3])
                            elif self.job == 'rangedToggle': elem.starter_text(customData[3].split(',')[3])
                            elif self.job == 'magicToggle': elem.starter_text(customData[4].split(',')[3])
                        elif elem.job == 'action2Desc':
                            if self.job == 'meleeToggle': elem.starter_text(customData[2].split(',')[7])
                            elif self.job == 'rangedToggle': elem.starter_text(customData[3].split(',')[7])
                            elif self.job == 'magicToggle': elem.starter_text(customData[4].split(',')[7])

            self.hover()
            self.on = True
