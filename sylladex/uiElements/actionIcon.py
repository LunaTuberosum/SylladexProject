import pygame as pg

from uiElement import UIElement, Apperance

class ActionIcon(UIElement):

    def __init__(self, x: int, y: int, job: str, image_item: bool = False, action_type: str = "NA", custom_name: str = ''):

        super().__init__(
            x, 
            y, 
            f'ActionIcon ({job})',
            2
            )

        self.job = job
        self.active = False
        self.hovering = False
        self.image_item = image_item

        self.tool_tip_text = f'Change name of {job}'

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 8)

        self.melee_color = '#FF4B2D'
        self.ranged_color = '#9B38F4'
        self.magic_color = '#6688FE'

        if self.image_item == False:
            self.current_color = self.melee_color

            self.prefix = 'AS'

            self.text = ''
        else:

            if action_type == "MELEE":
                self.current_color = self.melee_color
                self.prefix = 'AS'
            elif action_type == "RANGED":
                self.current_color = self.ranged_color
                self.prefix = 'AR'
            elif action_type == "MAGIC":
                self.current_color = self.magic_color
                self.prefix = 'AC'

            self.text = custom_name[2:]

        self.apperance = Apperance(
            self,
            [180, 24],
            [[107, 22], self.current_color, [0, 1]], 
            [[101, 18], '#FFFFFF', [3, 3]],
            texts=[[self.prefix + self.text, [5, 13], 'left', self.current_color]]
            )

    # def exit_field(self):
    #     self.active = False
    #     self.draw()
    #     if self.job == 'action1Icon':
    #         if self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Melee 1 Name', (self.prefix+self.text).upper())
    #         elif self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Ranged 1 Name', (self.prefix+self.text).upper())
    #         elif self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Magic 1 Name', (self.prefix+self.text).upper())
    #     elif self.job == 'action2Icon':
    #         if self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Melee 2 Name', (self.prefix+self.text).upper())
    #         elif self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Ranged 2 Name', (self.prefix+self.text).upper())
    #         elif self.current_color == self.melee_color: UIElement.CodeDatabase.change_codeValue('Magic 2 Name', (self.prefix+self.text).upper())

    # def draw(self):
    #     self.backgroundColor = pg.Surface((107,22))
    #     self.backgroundColor.fill(self.current_color)
    #     self.image.blit(self.backgroundColor, [0,1])
        
    #     self.foregroundColor = pg.Surface((101,18))
    #     self.foregroundColor.fill('#FFFFFF')
    #     self.image.blit(self.foregroundColor, [3, 3])

    #     txt_surf = self.font.render(self.prefix+self.text, False, self.current_color)
    #     self.image.blit(txt_surf, [6, 8])

    # def typeing(self, event):

    #     if self.active == True:
    #         if event.key == pg.K_BACKSPACE:
    #             self.text = self.text[:-1]
    #             self.draw()

    #         elif event.key == pg.K_RETURN:
    #             self.active = False
    #             self.draw()
    #             self.exit_field()
    #             return

    #         else:
    #             if event.key != pg.K_RETURN:
    #                 if len(self.text) != 9:
    #                     self.text += event.unicode
    #                     self.draw()

    # def on_click(self):
    #     self.active = True
    #     self.draw()

    # def update(self):
    #     for elem in UIElement.get_group('ui'):
    #         if isinstance(elem, UIElement.get_uiElem('ToggleButton')):
    #             if elem.job == 'meleeToggle' and elem.on == True:
    #                 self.current_color = self.melee_color
    #                 self.prefix = 'AS'
    #                 self.draw()
    #             elif elem.job == 'rangedToggle' and elem.on == True:
    #                 self.current_color = self.ranged_color
    #                 self.prefix = 'AR'
    #                 self.draw()
    #             elif elem.job == 'magicToggle' and elem.on == True:
    #                 self.current_color = self.magic_color
    #                 self.prefix = 'AC'
    #                 self.draw()