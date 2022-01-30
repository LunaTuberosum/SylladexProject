import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase


class ListObject(UIBase):
    def __init__(self, x, y, size, image, length):
        super().__init__(x, y, size, image)
        self.uiLayers.change_layer(self, 0)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.kindImage = pg.image.load("sylladex/uiElements/asset/KINDS/CustomKind.png").convert_alpha()
        self.kindImage.set_alpha(125)
        self.image.blit(self.kindImage, (185, 3))

        self.txt_surface = self.font.render("-", True, (0,0,0))
        self.image.blit(self.txt_surface, (3,3))
        self.image.blit(self.txt_surface, (3,37))
        self.image.blit(self.txt_surface, (129,37))

        self.interactable = True

        self.empty = True
        
        self.kind = None
        self.grist = None
        self.trait1 = None
        self.trait2 = None
        self.action1 = None
        self.action2 = None
        self.action3 = None
        self.action4 = None
    
    def update(self):
        if self.rect.y >= 196 and self.rect.y <= 757:
            self.interactable = True
        else:
            self.interactable = False

    def start_card(self):
        tempNameIn = input("Name > ")
        tempCodeIn = input("Code > ")
        tempTierIn = input("Tier > ")


        codeDatabase.read_code(tempCodeIn, self)
        self.image = pg.image.load("sylladex/uiElements/asset/MISC/LIST_OBJ.png")
        codeDatabase.find_kindImage(self)
        self.kindImage = pg.image.load(codeDatabase.find_kindImage(self)).convert_alpha()
        self.kindImage.set_alpha(125)
        self.image.blit(self.kindImage, (185, 3))

        nameTxt = self.font.render(tempNameIn, True, (0,0,0))
        self.image.blit(nameTxt, (3,3))

        codeTxt = self.font.render(tempCodeIn, True, (0,0,0))
        self.image.blit(codeTxt, (3,37))

        tierTxt = self.font.render(tempTierIn, True, (0,0,0))
        self.image.blit(tierTxt, (129,37))