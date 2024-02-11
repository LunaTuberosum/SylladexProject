import pygame as pg

from uiElement import Apperance, UIElement


class DebugInspector(UIElement):
    __current_ins = []

    def __init__(self, elem):
        super().__init__(
            pg.display.get_surface().get_width()-160,
            40,
            'DebugUIInspector',
            999)

        self.font = pg.font.Font(
            "sylladex/uiElements/asset/FONTS/fontstuck.ttf", 24)

        self.current_inspectie = elem
        self.params = self.set_param()

        width = 0
        for _param in self.params:
            _width = self.font.render(
                _param[0], True, (0, 0, 0)).get_width() + 20
            if _width > width:
                width = _width

        self.appperance = Apperance(
            self,
            [width, 40 + (len(self.params) * 20)],
            [[width, 40 + (len(self.params) * 20)], '#323232', [0, 0]],
            alpha=130,
            texts=self.params
        )

        DebugInspector.__current_ins.append(self)

    def set_param(self):
        _params = []

        _params.append([f'Name: {self.current_inspectie.obj_name}', [
                       10, 20], 'left', '#FFFFFF'])

        y = 30
        # if hasattr(self.current_inspectie, 'code_data'):
        #     _params.append([f'Card Data:', [
        #                    10, y + (len(_params) * 20)], 'left', '#FFFFFF'])

        #     _params.append([f'Code: {self.current_inspectie.code_data.code}', [
        #                    20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Kind: {self.current_inspectie.code_data.kind}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Grist: {self.current_inspectie.code_data.grist}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Trait 1: {self.current_inspectie.code_data.trait_1}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Trait 2: {self.current_inspectie.code_data.trait_2}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Action 1: {self.current_inspectie.code_data.action_1}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Action 2: {self.current_inspectie.code_data.action_2}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Action 3: {self.current_inspectie.code_data.action_3}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     _params.append([f'Action 4: {self.current_inspectie.code_data.action_4}', [
        #         20, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        #     y += 10

        _params.append([f'HasToolTip: {self.current_inspectie.tool_tip_text != ""}', [
            10, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        _params.append([f'Position: ({self.current_inspectie.rect.x}, {self.current_inspectie.rect.y})', [
            10, y + (len(_params) * 20)], 'left', '#FFFFFF'])
        _params.append([f'Layer: {UIElement.get_group("layer").get_layer_of_sprite(self.current_inspectie)}', [
            10, y + (len(_params) * 20)], 'left', '#FFFFFF'])

        y += 10

        if hasattr(self.current_inspectie, 'children'):
            _params.append([f'NumofChildren: {len(self.current_inspectie.children)}', [
                10, y + (len(_params) * 20)], 'left', '#FFFFFF'])
            y += 10

        # if hasattr(self.current_inspectie, 'options'):
        #     self.children.append(self.font.render(
        #         f'Options: [', False, 'white'))
        #     for _index, option in enumerate(self.current_inspectie.options):
        #         if _index == 21:
        #             self.children.append(self.font.render(
        #                 f'    ... {len(self.current_inspectie.options) - _index} more ]', False, 'white'))
        #             break
        #         elif _index == len(self.current_inspectie.options)-1:
        #             self.children.append(self.font.render(
        #                 f'    {_index}: {option} ]', False, 'white'))
        #         else:
        #             self.children.append(self.font.render(
        #                 f'    {_index}: {option},', False, 'white'))
        # if hasattr(self.current_inspectie, 'currentOption'):
        #     self.children.append(self.font.render(
        #         f'Current Option: {self.current_inspectie.currentOption}', False, 'white'))

        return _params

    def update(self):

        if not self.current_inspectie.rect.collidepoint(pg.mouse.get_pos()):
            DebugInspector.__current_ins.remove(self)
            UIElement.remove_from_group(self)
            self.kill()

    @ classmethod
    def get_current_ins(cls):
        return cls.__current_ins

    @ classmethod
    def clear_inspectors(cls):
        cls.__current_ins.clear()
