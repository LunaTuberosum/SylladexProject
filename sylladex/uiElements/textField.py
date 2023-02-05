import pygame as pg

from uiElement import UIElement, Apperance

class TextField(UIElement):

    def __init__(self, x: int, y: int, size: tuple, job: str, tool_tip_text: str, max_char: int, **kargs):
        super().__init__(x, y, f'TextField ({job})', kargs['layerChange'] if 'layerChange' in kargs else 1)

        self.kargs = kargs
        self.size = size

        self.max_char = max_char
        self.job = job
        self.active = False
        self.hovering = False

        self.tool_tip_text = tool_tip_text

        if 'textColor' in self.kargs: self.text_color = self.kargs['textColor']
        else: self.text_color = '#000000'

        if 'textType' in self.kargs: self.text_type = self.kargs['textType']
        else: self.text_type = 'Txt'

        if 'fontSize' in self.kargs: self.font_size = self.kargs['fontSize']
        else: self.font_size = 24

        if 'textFont' in self.kargs: self.text_font = self.kargs['textFont']
        else: self.text_font = 'sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf'
        
        self.font = pg.font.Font(self.text_font, self.font_size)

        if 'baseColors' in self.kargs:
            self.base_color = self.kargs['baseColors'][0]
            self.hover_color = self.kargs['baseColors'][1]
            self.selected_color = self.kargs['baseColors'][2]
        else:
            self.base_color = (255,255,255)
            self.hover_color = (230,230,230)
            self.selected_color = (170,170,170)

        if 'align' in self.kargs:
            if self.kargs['align'] == 'center':
                self.text_postion = [self.size[0]/2, self.size[1]/2]
                self.alginment = 'center'
            elif self.kargs['align'] == 'right':
                self.text_postion = [self.size[0]-2, self.size[1]/2]
                self.alginment = 'right'
        else:
            self.text_postion = [2, self.size[1]/2]
            self.alginment = 'left'
        
        if 'exitCommand' in self.kargs: self.exit_command = self.kargs['exitCommand']
        else: self.exit_command = None

        if self.text_type == 'Num':
            self.defult_text, self.text = '0', '0'

        else:
            self.defult_text, self.text = '', ''

        self.apperance = Apperance(
            self,
            self.size,
            [self.size, self.base_color, [0, 0]],
            texts = [[self.text, self.text_postion, self.alginment, self.text_color]]
        )

    def exit_field(self):
        self.active = False

        if self.text == '':
            self.text = self.defult_text

        self.apperance.options = {'texts': [[self.text, self.text_postion, self.alginment, self.text_color]]}
        self.apperance.size_color_pos = [[self.size, self.base_color, [0,0]]]

        self.apperance.reload_apperance()       

        if self.exit_command: self.exit_command() 

    # def exit_field(self):
    #     self.active = False
        
    #     for elem in UIElement.get_group("ui"):
    #         if isinstance(elem, UIElement.get_uiElem('CardList')) and self.job == "numOfCards":
    #             amount = int(self.text) - len(elem.children)
    #             if amount < 0:
    #                 for removeCard in range(0, amount*-1):
    #                     elem.remove_fromList(self)
    #                 elem.place_list()
    #             else:
    #                 for newCard in range(0, amount):
    #                     elem.add_to_list()

    #         elif isinstance(elem, UIElement.get_uiElem('ToggleButton')):
    #             if elem.job == 'meleeToggle':
    #                 if elem.on == True:
    #                     if self.job == 'action1Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Melee 1 Cost', self.text)
    #                     elif self.job == 'action1Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Melee 1 Dmg', self.text)
    #                     elif self.job == 'action2Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Melee 2 Cost', self.text)
    #                     elif self.job == 'action2Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Melee 2 Dmg', self.text)
    #             elif elem.job == 'rangedToggle':
    #                 if elem.on == True:
    #                     if self.job == 'action1Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Ranged 1 Cost', self.text)
    #                     elif self.job == 'action1Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Ranged 1 Dmg', self.text)
    #                     elif self.job == 'action2Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Ranged 2 Cost', self.text)
    #                     elif self.job == 'action2Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Ranged 2 Dmg', self.text)
    #             elif elem.job == 'magicToggle':
    #                 if elem.on == True:
    #                     if self.job == 'action1Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Magic 1 Cost', self.text)
    #                     elif self.job == 'action1Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Magic 1 Dmg', self.text)
    #                     elif self.job == 'action2Cost':
    #                         UIElement.CodeDatabase.change_codeValue('Magic 2 Cost', self.text)
    #                     elif self.job == 'action2Dmg':
    #                         UIElement.CodeDatabase.change_codeValue('Magic 2 Dmg', self.text)

    #             elif elem.job == 't1Toggle':
    #                 if elem.on == True:
    #                     if self.job == 'traitName':
    #                         UIElement.CodeDatabase.change_codeValue('Trait 1 Name', self.text)
    #             elif elem.job == 't2Toggle':
    #                 if elem.on == True:
    #                     if self.job == 'traitName':
    #                         UIElement.CodeDatabase.change_codeValue('Trait 2 Name', self.text)
    #             elif elem.job == 't3Toggle':
    #                 if elem.on == True:
    #                     if self.job == 'traitName':
    #                         UIElement.CodeDatabase.change_codeValue('Trait 3 Name', self.text)
    #             elif elem.job == 't4Toggle':
    #                 if elem.on == True:
    #                     if self.job == 'traitName':
    #                         UIElement.CodeDatabase.change_codeValue('Trait 4 Name', self.text)

    #     if self.job == 'kind1Name':
    #         UIElement.CodeDatabase.change_codeValue('Customkind 1', self.text)
    #         self.job = f'{self.text}Name'
    #         self.objName = f'TextField ({self.job})'
    #         self.tool_tip_text = f'Changes the name of {self.text}'
    #     elif self.job == 'kind2Name':
    #         UIElement.CodeDatabase.change_codeValue('Customkind 2', self.text)
    #         self.job = f'{self.text}Name'
    #         self.objName = f'TextField ({self.job})'
    #         self.tool_tip_text = f'Changes the name of {self.text}'

    def typing(self, event):

        if self.active == True:

            if self.text == self.defult_text:
                self.text = ''

            if event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]

            elif event.key == pg.K_RETURN:

                self.exit_field()
                return

            else:
                if len(self.text) < self.max_char:
                    if self.text_type == 'Num':
                        for _num in range(0, 9):
                            if event.unicode == str(_num):
                                self.text += event.unicode
                    else:
                        self.text += event.unicode

            self.apperance.options = {'texts': [[self.text, self.text_postion, self.alginment, self.text_color]]}
            self.apperance.reload_apperance()

    # def typeing(self, event):
        
    #     if self.active == True:
    #         if event.key == pg.K_BACKSPACE:
    #             self.text = self.text[:-1]
    #             self.draw()

    #         elif event.key == pg.K_RETURN:
                
    #             if len(self.text) > 1:
    #                 if self.text[0] == '0':
    #                     self.text = self.text[1:]

    #             if len(self.job) > 6 and self.job[-6:] == 'NumBox':
    #                 for elem in UIElement.get_group('ui'):
    #                     if isinstance(elem, UIElement.get_uiElem('GristCacheLimit')):
    #                         if self.text > elem.limitNum:
    #                             self.text = elem.limitNum
    #                             self.draw()
    #                         for elem in UIElement.get_group('ui'):
    #                             if isinstance(elem, UIElement.get_uiElem('GristCache')):
    #                                 elem.save_cache()
                            
    #             if self.text == "":
    #                 if self.job == 'traitName':
    #                     for elem in UIElement.get_group('ui'):
    #                         if isinstance(elem, UIElement.get_uiElem('ToggleButton')):
    #                             if elem.job == 't1Toggle' and elem.on == True: 
    #                                 self.text = 'CUSTOM TRAIT 1'
    #                                 self.no_hover()
    #                             if elem.job == 't2Toggle' and elem.on == True: 
    #                                 self.text = 'CUSTOM TRAIT 2'
    #                                 self.no_hover()
    #                             if elem.job == 't3Toggle' and elem.on == True: 
    #                                 self.text = 'CUSTOM TRAIT 3'
    #                                 self.no_hover()
    #                             if elem.job == 't4Toggle' and elem.on == True: 
    #                                 self.text = 'CUSTOM TRAIT 4'
    #                                 self.no_hover()

    #                 elif self.text_type == 'Num':
    #                     self.text = self.defult_text
    #                     self.draw()
    #                     for elem in UIElement.get_group('ui'):
    #                         if isinstance(elem, UIElement.get_uiElem('GristCache')):
    #                             elem.save_cache()
    #                 elif self.text_type == 'Txt':
    #                     self.text = self.defult_text
    #             self.exit_field()
    #             return

    #         elif event.key == pg.K_TAB:
    #             if pg.time.get_ticks() - UIElement.prevTick >= 1:
    #                 if self.job == 'nameOverlay':
    #                     nextText = 'codeOverlay'
    #                 elif self.job == 'codeOverlay':
    #                     nextText = 'tierOverlay'
    #                 elif self.job == 'tierOverlay':
    #                     nextText = 'nameOverlay'

    #                 for elem in UIElement.get_group('ui'):
    #                     if isinstance(elem, UIElement.get_uiElem('TextField')):
    #                         if elem.job == nextText:
    #                             elem.on_click()
    #                             elem.draw()
    #                             self.exit_field()
    #                             self.no_hover()
    #                             UIElement.prevTick = pg.time.get_ticks()

    #         else:
    #             if event.key != pg.K_RETURN and len(self.text) < self.max_char:
                    
    #                 self.text += event.unicode

    #                 if len(self.job) > 6 and self.job[-6:] == 'NumBox':
    #                     isNum = False
    #                     for num in range(0,10):
    #                         if len(self.text) > 0 and self.text[-1] == str(num):
    #                             isNum = True
    #                     if isNum == False:
    #                         if len(self.text) > 0:
    #                             self.text = self.text[:-1]

    #                 self.draw()

    def hover(self):
        if self.active == False:
            self.apperance.options = {'texts': [[self.text, [self.size[0]/2, self.size[1]/2], self.kargs['align'] if 'align' in self.kargs else 'center', self.text_color]]}
            self.apperance.size_color_pos = [[self.size, self.hover_color, [0,0]]]
            self.apperance.reload_apperance()
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.apperance.options = {'texts': [[self.text, [self.size[0]/2, self.size[1]/2], self.kargs['align'] if 'align' in self.kargs else 'center', self.text_color]]}
            self.apperance.size_color_pos = [[self.size, self.base_color, [0,0]]]
            self.apperance.reload_apperance()
            self.hovering = False

    def on_click(self):
        self.active = True
        self.apperance.size_color_pos = [[self.size, self.selected_color, [0,0]]]
        self.apperance.reload_apperance()
        
        