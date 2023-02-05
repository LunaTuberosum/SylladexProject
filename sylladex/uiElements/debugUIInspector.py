import pygame as pg

from uiElement import UIElement


class DebugUIInspector(UIElement):
    def __init__(self, elem):
        super().__init__(pg.display.get_surface().get_width()-160, 40, (150,150), 'DebugUIInspector', (50,50,50))

        self.create_appearance([[150,150], (50,50,50), [0,0]], alpha = 130)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.children = []
        self.current_inspectie = elem

        self.children.append(self.font.render(f'Name: {self.current_inspectie.objName}', False, 'white'))
        if hasattr(self.current_inspectie, 'code'): self.children.append(self.font.render(f'Code: {self.current_inspectie.code}', False, 'white'))
        if hasattr(self.current_inspectie, 'kind'): self.children.append(self.font.render(f'Kind: {self.current_inspectie.kind}', False, 'white'))
        if hasattr(self.current_inspectie, 'grist'): self.children.append(self.font.render(f'Grist: {self.current_inspectie.grist}', False, 'white'))
        if hasattr(self.current_inspectie, 'trait1'): self.children.append(self.font.render(f'Trait1: {self.current_inspectie.trait1}', False, 'white'))
        if hasattr(self.current_inspectie, 'trait2'): self.children.append(self.font.render(f'Trait2: {self.current_inspectie.trait2}', False, 'white'))
        if hasattr(self.current_inspectie, 'action1'): self.children.append(self.font.render(f'Action1: {self.current_inspectie.action1}', False, 'white'))
        if hasattr(self.current_inspectie, 'action2'): self.children.append(self.font.render(f'Action2: {self.current_inspectie.action2}', False, 'white'))
        if hasattr(self.current_inspectie, 'action3'): self.children.append(self.font.render(f'Action3: {self.current_inspectie.action3}', False, 'white'))
        if hasattr(self.current_inspectie, 'action4'): self.children.append(self.font.render(f'Action4: {self.current_inspectie.action4}', False, 'white'))

        if hasattr(self.current_inspectie, 'toolTipText'): self.children.append(self.font.render(f'HasToolTip: {hasattr(self.current_inspectie, "toolTipText")}', False, 'white'))
        self.children.append(self.font.render(f'Position: ({self.current_inspectie.rect.x}, {self.current_inspectie.rect.y})', False, 'white'))
        self.children.append(self.font.render(f'Layer: {UIElement.get_group("layer").get_layer_of_sprite(self.current_inspectie)}', False, 'white'))

        if hasattr(self.current_inspectie, 'children'): self.children.append(self.font.render(f'#ofChildren: {len(self.current_inspectie.children)}', False, 'white'))
        if hasattr(self.current_inspectie, 'options'): 
            self.children.append(self.font.render(f'Options: [', False, 'white'))
            for _index, option in enumerate(self.current_inspectie.options):
                if _index == 21:
                    self.children.append(self.font.render(f'    ... {len(self.current_inspectie.options) - _index} more ]', False, 'white'))
                    break
                elif _index == len(self.current_inspectie.options)-1:
                    self.children.append(self.font.render(f'    {_index}: {option} ]', False, 'white'))
                else:
                    self.children.append(self.font.render(f'    {_index}: {option},', False, 'white'))
        if hasattr(self.current_inspectie, 'currentOption'): self.children.append(self.font.render(f'Current Option: {self.current_inspectie.currentOption}', False, 'white'))

        _new_width = self.rect.w
        for _index, child in enumerate(self.children):
            if child.get_width()+20 > _new_width:
                _new_width = child.get_width()+20

        self.rect.w = _new_width
        self.rect.h = 40+(_index*30)
        self.image = pg.transform.scale(self.image, (self.rect.w, self.rect.h))
        self.rect.x = pg.display.get_surface().get_width() - self.rect.w

        for _index, child in enumerate(self.children):
            self.image.blit(child, (10, 10+(30*_index)))

    def update(self):
        
        if self.current_inspectie.rect.collidepoint(pg.mouse.get_pos()):
            pass
        else:
            UIElement.Insepctors.remove(self)
            UIElement.remove_fromGroup(self)
            self.kill()