import pygame as pg

from baseUI import UIBase

class ActionIcon(UIBase):

    def __init__(self, x, y, job):
        super().__init__(x, y, (180, 24), f'ActionIcon ({job})', (0,0,0))

        self.job = job
        self.active = False
        self.hovering = False

        self.toolTipText = f'Change name of {job}'

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 8)

        self.image.set_colorkey((0,0,0))

        self.meleeColor = '#FF4B2D'
        self.rangedColor = '#9B38F4'
        self.magicColor = '#6688FE'
        self.currentColor = self.meleeColor

        self.prefix = 'AS'

        self._create_appearance([[107, 22], self.currentColor, [0, 1]], [[101, 18], '#FFFFFF', [3, 3]])

        self.text = ''

        txt_surf = self.font.render((self.prefix+self.text), False, self.currentColor)
        self.image.blit(txt_surf, [6, 8])

    def exit_field(self):
        self.active = False
        self.draw()
        if self.job == 'action1Icon':
            if self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Melee 1 Name', (self.prefix+self.text).upper())
            elif self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Ranged 1 Name', (self.prefix+self.text).upper())
            elif self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Magic 1 Name', (self.prefix+self.text).upper())
        elif self.job == 'action2Icon':
            if self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Melee 2 Name', (self.prefix+self.text).upper())
            elif self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Ranged 2 Name', (self.prefix+self.text).upper())
            elif self.currentColor == self.meleeColor: UIBase.CodeDatabase.change_codeValue('Magic 2 Name', (self.prefix+self.text).upper())

    def draw(self):
        self.backgroundColor = pg.Surface((107,22))
        self.backgroundColor.fill(self.currentColor)
        self.image.blit(self.backgroundColor, [0,1])
        
        self.foregroundColor = pg.Surface((101,18))
        self.foregroundColor.fill('#FFFFFF')
        self.image.blit(self.foregroundColor, [3, 3])

        txt_surf = self.font.render(self.prefix+self.text, False, self.currentColor)
        self.image.blit(txt_surf, [6, 8])

    def typeing(self, event):

        if self.active == True:
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
                self.draw()

            elif event.key == pg.K_RETURN:
                self.active = False
                self.draw()
                self.exit_field()
                return

            else:
                if event.key != pg.K_RETURN:
                    if len(self.text) != 9:
                        self.text += event.unicode
                        self.draw()

    def on_click(self):
        self.active = True
        self.draw()

    def update(self):
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                if elem.job == 'meleeToggle' and elem.on == True:
                    self.currentColor = self.meleeColor
                    self.prefix = 'AS'
                    self.draw()
                elif elem.job == 'rangedToggle' and elem.on == True:
                    self.currentColor = self.rangedColor
                    self.prefix = 'AR'
                    self.draw()
                elif elem.job == 'magicToggle' and elem.on == True:
                    self.currentColor = self.magicColor
                    self.prefix = 'AC'
                    self.draw()