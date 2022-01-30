import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.captchalogueCards import codeDatabase
from sylladex.uiElements.removeCardButton import RemoveCardButton
from sylladex.uiElements.popUp import PopUp


class ListObject(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        UIBase.add_toGroup(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.image = pg.Surface((249, 64))
        self.image.fill((255,255,255))
        self.rect = pg.Rect(24, 127, 249, 64)

        UIBase.uiLayers.change_layer(self, 0)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.kindImage = pg.image.load("sylladex/uiElements/asset/KINDS/CustomKind.png").convert_alpha()
        self.kindImage.set_alpha(125)
        self.image.blit(self.kindImage, (185, 3))

        self.txt_surface = self.font.render("-", True, (0,0,0))
        self.image.blit(self.txt_surface, (3,3))
        self.image.blit(self.txt_surface, (3,37))
        self.image.blit(self.txt_surface, (129,37))

        self.interactable = True
        self.hovering = False

        self.empty = True

        self.name = "-"
        self.code = "-"
        self.tier = "-"
        
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

    def redraw_card(self, color):
        if self.code == "-":
            self.image.fill(color)
            self.kindImage = pg.image.load("sylladex/uiElements/asset/KINDS/CustomKind.png").convert_alpha()
            self.kindImage.set_alpha(125)
            self.image.blit(self.kindImage, (185, 3))

            self.txt_surface = self.font.render("-", True, (0,0,0))
            self.image.blit(self.txt_surface, (3,3))
            self.image.blit(self.txt_surface, (3,37))
            self.image.blit(self.txt_surface, (129,37))
        else:
            codeDatabase.read_code(self.code, self)
            self.image.fill(color)
            self.kindImage = pg.image.load(codeDatabase.find_kindImage(self.kind)).convert_alpha()
            self.kindImage.set_alpha(125)
            self.image.blit(self.kindImage, (185, 3))

            nameTxt = self.font.render(self.name, True, (0,0,0))
            self.image.blit(nameTxt, (3,3))

            codeTxt = self.font.render(self.code, True, (0,0,0))
            self.image.blit(codeTxt, (3,37))

            tierTxt = self.font.render(self.tier, True, (0,0,0))
            self.image.blit(tierTxt, (129,37))

    def start_card(self):
        ## max is 22 characters
        self.name = input("Name > ")
        ## max is 8 characters
        self.code = input("Code > ")
        ## max is 2 characters
        self.tier = input("Tier > ")

        self.redraw_card((255,255,255))

    def hover(self):
        self.redraw_card((230,230,230))
        self.hovering = True

    def no_hover(self):
        self.redraw_card((255,255,255))
        self.hovering = False

    def alt_no_hover(self):
        self.redraw_card((230,230,230))
        self.hovering = False

    def alt_hover(self):
        self.redraw_card((255,255,255))
        self.hovering = True

    def on_click(self):
        if RemoveCardButton.eject == True:
            if self.empty == False:
                self.empty = True
                self.name = "-"
                self.code = "-"
                self.tier = "-"

                RemoveCardButton.eject = False
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, ListObject):
                        elem.redraw_card((255,255,255))
            else: 
                PopUp("You can\'t wject an empty card")