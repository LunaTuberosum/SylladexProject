import pygame as pg

from sylladex.uiElements.baseUI import UIBase

class ListObject(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.Surface((249, 64))
        self.image.fill((255,255,255))
        self.rect = pg.Rect(24, 127, 249, 64)

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.kindImage = pg.image.load("sylladex/uiElements/asset/KINDS/CustomKind.png").convert_alpha()
        self.kindImage.set_alpha(125)
        self.image.blit(self.kindImage, (185, 3))

        self.txt_surface = self.font.render("-", True, (0,0,0))
        self.image.blit(self.txt_surface, (3,3))
        self.image.blit(self.txt_surface, (3,37))
        self.image.blit(self.txt_surface, (129,37))
        self.children = []

        self.interactable = True
        self.prevPos = None
        self.grabbed = False
        self.hovering = False
        self.writing = False

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
        if self.grabbed == True:
            self.rect.left = pg.mouse.get_pos()[0] - 32
            self.rect.top = pg.mouse.get_pos()[1] - 32
            self.redraw_card((255,255,255))

            self.hovering = False
        if self.rect.y >= 196 and self.rect.y <= 757:
            self.interactable = True
        else:
            self.interactable = False

    def redraw_card(self, color):
        if self.writing == False:
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
                UIBase.CodeDatabase.read_code(self.code, self)
                self.image.fill(color)
                self.kindImage = pg.image.load(UIBase.CodeDatabase.find_kindImage(self.kind)).convert_alpha()
                self.kindImage.set_alpha(125)
                self.image.blit(self.kindImage, (185, 3))

                nameTxt = self.font.render(self.name, True, (0,0,0))
                self.image.blit(nameTxt, (3,3))

                codeTxt = self.font.render(self.code, True, (0,0,0))
                self.image.blit(codeTxt, (3,37))

                tierTxt = self.font.render(self.tier, True, (0,0,0))
                self.image.blit(tierTxt, (129,37))

    def start_card(self):

        self.image.fill((255,255,255))
        self.writing = True
        self.children.append(UIBase.TextField(self.rect.x+3, self.rect.y+3, 243, 28, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", ""))
        self.children.append(UIBase.TextField(self.rect.x+3, self.rect.y+35, 105, 28, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", ""))
        self.children.append(UIBase.TextField(self.rect.x+129, self.rect.y+35, 33, 28, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", ""))
        self.children.append(UIBase.FinishButton(self))

        for child in self.children:
            UIBase.get_group('layer').change_layer(child, -1)

        self.children[0].active = True
        self.children[0].image.fill((170,170,170))


        for elem in UIBase.get_group("ui"):
            if hasattr(elem, "job"):
                if elem.job == "nameOverlay" or elem.job == "codeOverlay" or elem.job == "tierOverlay":
                    elem.color = (235,235,235)
                    elem.no_hover()

    def hover(self):
        if self.writing == False:
            self.redraw_card((230,230,230))
            self.hovering = True

    def no_hover(self):
        if self.writing == False:
            self.redraw_card((255,255,255))
            self.hovering = False

    def alt_no_hover(self):
        self.redraw_card((230,230,230))
        self.hovering = False

    def alt_hover(self):
        self.redraw_card((255,255,255))
        self.hovering = True

    def on_click(self):
        if UIBase.RemoveCardButton.eject == True and self.interactable == True:
            if self.empty == False:
                self.empty = True
                self.name = "-"
                self.code = "-"
                self.tier = "-"

                UIBase.RemoveCardButton.eject = False
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.ListObject):
                        elem.redraw_card((255,255,255))
            else: 
                UIBase.PopUp("You can\'t eject an empty card")
        elif self.interactable == True:
            if self.empty == False:
                self.grabbed = True
                self.prevPos = self.rect.topleft