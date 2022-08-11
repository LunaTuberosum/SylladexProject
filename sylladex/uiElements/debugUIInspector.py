import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class DebugUIInspector(UIBase):
    def __init__(self, elem):
        super().__init__(pg.display.get_surface().get_width()-160, 40, (150,150), 'DebugUIInspector', (50,50,50))

        self._create_appearance([[150,150], (50,50,50), [0,0]], alpha = 130)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.children = []
        self.currentIns = elem

        self.children.append(self.font.render(f'Name: {self.currentIns.objName}', False, 'white'))
        if hasattr(self.currentIns, 'code'): self.children.append(self.font.render(f'Code: {self.currentIns.code}', False, 'white'))
        if hasattr(self.currentIns, 'kind'): self.children.append(self.font.render(f'Kind: {self.currentIns.kind}', False, 'white'))
        if hasattr(self.currentIns, 'grist'): self.children.append(self.font.render(f'Grist: {self.currentIns.grist}', False, 'white'))
        if hasattr(self.currentIns, 'trait1'): self.children.append(self.font.render(f'Trait1: {self.currentIns.trait1}', False, 'white'))
        if hasattr(self.currentIns, 'trait2'): self.children.append(self.font.render(f'Trait2: {self.currentIns.trait2}', False, 'white'))
        if hasattr(self.currentIns, 'action1'): self.children.append(self.font.render(f'Action1: {self.currentIns.action1}', False, 'white'))
        if hasattr(self.currentIns, 'action2'): self.children.append(self.font.render(f'Action2: {self.currentIns.action2}', False, 'white'))
        if hasattr(self.currentIns, 'action3'): self.children.append(self.font.render(f'Action3: {self.currentIns.action3}', False, 'white'))
        if hasattr(self.currentIns, 'action4'): self.children.append(self.font.render(f'Action4: {self.currentIns.action4}', False, 'white'))

        if hasattr(self.currentIns, 'toolTipText'): self.children.append(self.font.render(f'HasToolTip: {hasattr(self.currentIns, "toolTipText")}', False, 'white'))
        self.children.append(self.font.render(f'Position: ({self.currentIns.rect.x}, {self.currentIns.rect.y})', False, 'white'))
        self.children.append(self.font.render(f'Layer: {UIBase.get_group("layer").get_layer_of_sprite(self.currentIns)}', False, 'white'))

        if hasattr(self.currentIns, 'children'): self.children.append(self.font.render(f'#ofChildren: {len(self.currentIns.children)}', False, 'white'))
        if hasattr(self.currentIns, 'options'): 
            self.children.append(self.font.render(f'Options: [', False, 'white'))
            for index, option in enumerate(self.currentIns.options):
                if index == 21:
                    self.children.append(self.font.render(f'    ... {len(self.currentIns.options) - index} more ]', False, 'white'))
                    break
                elif index == len(self.currentIns.options)-1:
                    self.children.append(self.font.render(f'    {index}: {option} ]', False, 'white'))
                else:
                    self.children.append(self.font.render(f'    {index}: {option},', False, 'white'))
        if hasattr(self.currentIns, 'currentOption'): self.children.append(self.font.render(f'Current Option: {self.currentIns.currentOption}', False, 'white'))

        newWidth = self.rect.w
        for index, child in enumerate(self.children):
            if child.get_width()+20 > newWidth:
                newWidth = child.get_width()+20

        self.rect.w = newWidth
        self.rect.h = 40+(index*30)
        self.image = pg.transform.scale(self.image, (self.rect.w, self.rect.h))
        self.rect.x = pg.display.get_surface().get_width() - self.rect.w

        for index, child in enumerate(self.children):
            self.image.blit(child, (10, 10+(30*index)))

    def update(self):
        
        if self.currentIns.rect.collidepoint(pg.mouse.get_pos()):
            pass
        else:
            UIBase.Insepctors.remove(self)
            UIBase.remove_fromGroup(self)
            self.kill()