import pygame as pg

from uiElement import UIElement, Apperance

class DropDown(UIElement):
    def __init__(self, x: int, y: int, size: list, job: str, color: str, options: list, defult_option: str, custom_obj: str, show_type: str):
        
        super().__init__(
            x, 
            y, 
            f'DropDown ({job})',
            2
            )

        self.job = job
        self.options = options
        self.current_option = defult_option

        self.custom_obj = custom_obj
        self.tool_tip_text = f'Change weapon type for {self.custom_obj}'
        
        if show_type == 'Image':
            self.tool_tip_text = f'Change weaponkind icon for {self.custom_obj}'
        self.show_type = show_type

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 16)

        for _index, _option in enumerate(self.options):
            if _option == self.current_option:
                self.current_index = _index

        if self.show_type == 'Text':

            self.apperance = Apperance(
                self, 
                size,
                [size, color, [0, 0]],
                texts=[[self.current_option, [size[0] / 2, size[1]/ 2], 'center', '#000000']]
            )

        elif self.show_type == 'Image':

            self.apperance = Apperance(
                self, 
                size,
                [size, color, [0, 0]],
                image=[
                    UIElement.CodeDatabase.find_kind_image(self.current_option),
                    [0,0]
                ]
            )

            
    # def on_click(self):
    #     self.current_index += 1
    #     if self.current_index == len(self.options): self.current_index = 0
    #     self.current_option = self.options[self.current_index]

    #     self.image.fill('#C9DAF8')

    #     if self.show_type == 'Text':
    #         self.current_text = self.font.render(f'{self.current_option}', True, (0,0,0))
    #         self.image.blit(self.current_text, [(24-(self.current_text.get_width()/2)), 12-(self.current_text.get_height()/2)])

    #         UIElement.CodeDatabase.change_code_value(f'{self.custom_obj} Type', self.current_option)
    #     elif self.show_type == 'Image':
    #         self.current_image = pg.image.load(UIElement.CodeDatabase.find_kind_image(self.current_option)).convert_alpha()
    #         self.current_image = pg.transform.scale(self.current_image, (24,24))
    #         self.image.blit(self.current_image, [0,0])

    #         UIElement.CodeDatabase.change_code_value(f'{self.custom_obj} Icon', self.current_option)

    # def on_altClick(self):
    #     self.current_index -= 1
    #     if self.current_index == -1: self.current_index = len(self.options)-1
    #     self.current_option = self.options[self.current_index]

    #     self.image.fill('#C9DAF8')

    #     if self.show_type == 'Text':
    #         self.current_text = self.font.render(f'{self.current_option}', True, (0,0,0))
    #         self.image.blit(self.current_text, [(24-(self.current_text.get_width()/2)), 12-(self.current_text.get_height()/2)])

    #         UIElement.CodeDatabase.change_code_value(f'{self.custom_obj} Type', self.current_option)
    #     elif self.show_type == 'Image':
    #         self.current_image = pg.image.load(UIElement.CodeDatabase.find_kind_image(self.current_option)).convert_alpha()
    #         self.current_image = pg.transform.scale(self.current_image, (24,24))
    #         self.image.blit(self.current_image, [0,0])

    #         UIElement.CodeDatabase.change_code_value(f'{self.custom_obj} Icon', self.current_option)
