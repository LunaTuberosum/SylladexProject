import json
import pygame as pg

from uiElement import UIElement, Apperance


class CustomSettingMenu(UIElement):
    def __init__(self):

        super().__init__(
            -22 if UIElement.find_current_ui('SideBar') else -348,
            38,
            'CustomSettingMenu',
            6
        )

        self.apperance = Apperance(
            self,
            [348, 768],
            [[348, 768], '#666666', [0, 0]],
            [[326, 732], '#434343', [10, 24]],
            [[326, 732], '#1155CC', [0, 12]],
            colorKey=True,
        )

        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 36, 'WEAPONKINDS'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 66, "WEAPONKINDS", 'KIND1'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 96, "WEAPONKINDS", 'KIND2'))
        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 126, 'ACTIONS'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            210, 126, 'melee', 'ME', 'Changes view to custom MELEE actions', self.action_toggle, True))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            240, 126, 'ranged', 'RA', 'Changes view to custom RANGED actions', self.action_toggle))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            270, 126, 'magic', 'MA', 'Changes view to custom MAGIC actions', self.action_toggle))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 156, "ACTIONS", 'ACTION1'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 258, "ACTIONS", 'ACTION2'))
        self.add_child(UIElement.get_ui_elem('CustomSettingSectionName')(
            12, 360, 'TRAITS'))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            182, 390, 'TRAIT1', '1',  'Changes view to custom TRAIT 1', self.trait_toggle, True))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            212, 390, 'TRAIT2', '2',  'Changes view to custom TRAIT 2', self.trait_toggle))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            242, 390, 'TRAIT3', '3',  'Changes view to custom TRAIT 3', self.trait_toggle))
        self.add_child(UIElement.get_ui_elem('ToggleButton')(
            272, 390, 'TRAIT4', '4',  'Changes view to custom TRAIT 4', self.trait_toggle))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 390, "TRAITS", 'name'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 420, "TRAITS", 'tier 1-4'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 498, "TRAITS", 'tier 5-8'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 576, "TRAITS", 'tier 9-12'))
        self.add_child(UIElement.get_ui_elem('CustomSettingAreaBox')(
            12, 654, "TRAITS", 'tier 13-16'))

        if UIElement.find_current_ui('SideBar'):
            self.to_be_rect = 326
        else:
            self.to_be_rect = 0

    def update(self):
        if self.rect.x != self.to_be_rect:
            UIElement.move_element(
                self, [UIElement.lerp(self.rect.x, self.to_be_rect, 0.2), 0])
            UIElement.find_current_ui(
                'CustomSettingButton').rect.x = self.rect.right

        else:
            if self.to_be_rect == -348 or self.to_be_rect == -22:
                UIElement.remove_from_group(self)

    def trait_toggle(self, toggled: object):
        for _i in range(9, 14):
            if self.children[_i] == toggled:
                self.children[_i].on = True
            else:
                self.children[_i].on = False

        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        self.children[9].cur_toggle = toggled.text

        self.children[14].children[0].text = _custom_data['TRAIT' +
                                                          toggled.text]['NAME']
        self.children[14].children[0].reload_text()
        self.children[14].children[0].default_text = f'CUSTOM TRAIT ' + \
            self.children[9].cur_toggle

        self.update_trait_fields(self.children[15], _custom_data, toggled)
        self.update_trait_fields(self.children[16], _custom_data, toggled)
        self.update_trait_fields(self.children[17], _custom_data, toggled)
        self.update_trait_fields(self.children[18], _custom_data, toggled)

    def update_trait_fields(self, elem: object, custom_data: dict, toggled: object):
        elem.children[0].text = custom_data['TRAIT' +
                                            toggled.text][elem.job[5:]]
        elem.children[0].starter_text()
        elem.children[0].reload_text()

    def action_toggle(self, toggled: object):
        for _i in range(4, 7):
            if self.children[_i] == toggled:
                self.children[_i].on = True
            else:
                self.children[_i].on = False

        with open('sylladex/captchalogueCards/data/customData.json', 'r') as _custom_data_file:
            _custom_data = json.load(_custom_data_file)

        self.children[3].cur_toggle = toggled.text
        self.children[3].apperance.kwargs['texts'] = [[f"CUSTOM {(toggled.job).upper()} ACTIONS", [
            90, 12], 'center', '#000000']]
        self.children[3].apperance.reload_apperance()

        self.update_action_fields(self.children[7], _custom_data, toggled)
        self.update_action_fields(self.children[8], _custom_data, toggled)

    def update_action_fields(self, elem: object, custom_data: dict, toggled: object):
        elem.children[0].setup_icon(toggled.job, custom_data[elem.job])

        _actionData = custom_data[elem.job][elem.children[0].prefix]

        elem.children[1].text = _actionData['COST']
        elem.children[1].reload_text()

        elem.children[2].text = _actionData['DAMAGE']
        elem.children[2].reload_text()

        elem.children[3].text = _actionData['DESCRIPTION']
        elem.children[3].starter_text()
        elem.children[3].reload_text()
