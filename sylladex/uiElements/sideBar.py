import pygame as pg

from uiElement import UIElement, Apperance


class SideBar(UIElement):
    def __init__(self):

        super().__init__(
            -326, 
            0, 
            'SideBar', 
            4
            )

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/fontstuck.ttf", 18)

        self.apperance = Apperance(
            self,
            [326, 1080],
            [[326, 1080], 'ModusBackground', [0, 0]], 
            [[320, 1080], 'ModusForeground', [0, 0]], 
            [[284, 691], 'ModusBackground', [18, 136]], 
            [[284, 60], 'ModusBackground', [18, 136]], 
            [[218, 48], '#B7B7B7', [24, 142]], 
            [[54, 48], '#999999', [242, 142]], 
            [[249, 625], '#D8DDFF', [24, 196]], 
            [[23, 625], '#B7B7B7', [273, 196]], 
            [[278, 199], 'ModusBackground', [24, 857]], 
            [[278, 199], '#A4A4A4', [18, 851]], 
            colorKey = True, 
            texts = [
                ['SYLLADEX', [24, 20], 'left', '#FFFFFF'], 
                ['NUM OF CARDS', [133, 170], 'center', '#000000'], 
                ['FETCH MODUS', [21, 871], 'left', '#FFFFFF']])

        self.add_child(UIElement.get_ui_elem('AddCardButton')(30, 50))
        self.add_child(UIElement.get_ui_elem('RemoveCardButton')(112, 50))
        self.add_child(UIElement.get_ui_elem('TextField')(
            242, 
            142, 
            [53, 48], 
            "numOfCards", 
            "The Number of Cards in you Sylladex", 
            3,
            startLayer=4,
            textType='Num',
            align='center',
            fontSize=24,
            ))

        self.add_child(UIElement.get_ui_elem('CardList')(24, 196))
        self.add_child(UIElement.get_ui_elem('ScrollBar')(273, 196))

        self.add_child(UIElement.get_ui_elem('ModusCard')(33, 910, "STACK"))
        self.add_child(UIElement.get_ui_elem('ModusCard')(121, 910, "QUEUE"))
        self.add_child(UIElement.get_ui_elem('ModusCard')(209, 910, "TREE"))

        if UIElement.check_for_ui('GristCache'): 
            if UIElement.find_current_ui('GristCache').to_be_rect != -719: 
                UIElement.find_current_ui('GristCache').to_be_rect = 326
            else:
                UIElement.find_current_ui('GristCache').to_be_rect = -392

        self.to_be_rect = 0

    def update(self):
        if self.rect.x != self.to_be_rect:

            UIElement.move_element(self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 0])
            self.children[3].place_list()

            if not UIElement.find_current_ui('GristCache'):
                UIElement.find_current_ui('GristCacheButton').rect.x = self.rect.right
            if not UIElement.find_current_ui('CustomSettingMenu'):
                UIElement.find_current_ui('CustomSettingButton').rect.x = self.rect.right            
            UIElement.find_current_ui('SideBarButton').rect.x = self.rect.right
        else:
            if self.to_be_rect == -326:
                UIElement.remove_from_group(self)