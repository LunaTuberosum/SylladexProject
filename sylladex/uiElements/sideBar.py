import json
import pygame as pg

from uiElement import UIElement, Apperance


class SideBar(UIElement):
    def __init__(self):

        super().__init__(
            -326,
            0,
            'SideBar',
            10
        )

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/fontstuck.ttf", 36)

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
            [[284, 199], 'ModusBackground', [21, 857]],
            [[284, 199], '#A4A4A4', [15, 851]],
            colorKey=True,
            texts=[
                ['SYLLADEX', [24, 20], 'left', 'ModusText'],
                ['NUM OF CARDS', [133, 170], 'center', '#000000'],
                ['FETCH MODUS', [21, 871], 'left', '#FFFFFF']
            ]
        )

        self.add_child(UIElement.get_ui_elem('AddCardButton')(
            28, 48))
        self.add_child(UIElement.get_ui_elem('RemoveCardButton')(
            110, 48))
        self.add_child(UIElement.get_ui_elem('EditCardButton')(
            218, 48))
        self.add_child(UIElement.get_ui_elem('TextField')(
            242,
            142,
            [53, 48],
            "numOfCards",
            "The Number of Cards in you Sylladex",
            3,
            startLayer=11,
            textType='Num',
            align='center',
            fontSize=24,
            exitCommand=UIElement.get_ui_elem('CardList').add_multi_to_list
        ))

        self.add_child(UIElement.get_ui_elem('CardList')(
            24, 196))
        self.add_child(UIElement.get_ui_elem('ScrollBar')(
            273, 196))

        with open('sylladex/uiElements/data/modusData.json', 'r') as _modus_data_file:
            _modus_data = json.load(_modus_data_file)

        self.add_child(UIElement.get_ui_elem('ModusCard')(
            20, _modus_data['1']['Code'], _modus_data['1']['Color'], _modus_data['1']['Active'], '1'))
        self.add_child(UIElement.get_ui_elem('ModusCard')(
            112, _modus_data['2']['Code'], _modus_data['2']['Color'], _modus_data['2']['Active'], '2'))
        self.add_child(UIElement.get_ui_elem('ModusCard')(
            204, _modus_data['3']['Code'], _modus_data['3']['Color'], _modus_data['3']['Active'], '3'))

        if UIElement.check_for_ui('GristCache'):
            if UIElement.find_current_ui('GristCache').to_be_rect != -719:
                UIElement.find_current_ui('GristCache').to_be_rect = 326
            else:
                UIElement.find_current_ui('GristCache').to_be_rect = -392

        self.to_be_rect = 0

    def update(self):
        if self.rect.x != self.to_be_rect:

            UIElement.move_element(
                self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 0])
            UIElement.find_current_ui('CardList').place_list()

            if not UIElement.find_current_ui('GristCache'):
                UIElement.find_current_ui(
                    'GristCacheButton').rect.x = self.rect.right
            if not UIElement.find_current_ui('CustomSettingMenu'):
                UIElement.find_current_ui(
                    'CustomSettingButton').rect.x = self.rect.right
            UIElement.find_current_ui('SideBarButton').rect.x = self.rect.right
        else:
            if self.to_be_rect == -326:
                UIElement.remove_from_group(self)
