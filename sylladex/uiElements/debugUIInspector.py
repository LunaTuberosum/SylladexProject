import pygame as pg

from sylladex.uiElements.baseUI import UIBase


class DebugUIInspector(UIBase):
    def __init__(self, elem):
        super().__init__(pg.display.get_surface().get_width()-160, 10, (150,150), 'surfaceRect', True, (50,50,50))

        self.image.set_alpha(130)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.children = []
        self.currentIns = elem

        self.children.append(self.font.render(f'Name: {elem.objName}', False, 'white'))
        if hasattr(self.currentIns, 'code'): self.children.append(self.font.render(f'Code: {elem.code}', False, 'white'))
        if hasattr(self.currentIns, 'kind'): self.children.append(self.font.render(f'Kind: {elem.kind}', False, 'white'))
        if hasattr(self.currentIns, 'grist'): self.children.append(self.font.render(f'Grist: {elem.grist}', False, 'white'))
        if hasattr(self.currentIns, 'trait1'): self.children.append(self.font.render(f'Trait1: {elem.trait1}', False, 'white'))
        if hasattr(self.currentIns, 'trait2'): self.children.append(self.font.render(f'Trait2: {elem.trait2}', False, 'white'))
        if hasattr(self.currentIns, 'action1'): self.children.append(self.font.render(f'Action1: {elem.action1}', False, 'white'))
        if hasattr(self.currentIns, 'action2'): self.children.append(self.font.render(f'Action2: {elem.action2}', False, 'white'))
        if hasattr(self.currentIns, 'action3'): self.children.append(self.font.render(f'Action3: {elem.action3}', False, 'white'))
        if hasattr(self.currentIns, 'action4'): self.children.append(self.font.render(f'Action4: {elem.action4}', False, 'white'))

        self.children.append(self.font.render(f'ImageID: {elem.imageID}', False, 'white'))
        self.children.append(self.font.render(f'Position: ({elem.rect.x}, {elem.rect.y})', False, 'white'))

        if hasattr(self.currentIns, 'children'): self.children.append(self.font.render(f'#ofChildren: {len(elem.children)}', False, 'white'))

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