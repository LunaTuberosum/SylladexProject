import pygame as pg

from baseUI import UIBase

class ListObject(UIBase):
    def __init__(self):
        super().__init__(24, 127, (249, 64), 'CardListObject', (255,255,255))

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf",24)

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
        self.captaCard = None

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

        self.prevTick = 0
    

    def update(self):
        if self.prevTick > 0:
            if pg.time.get_ticks() - self.prevTick >= 500:
                self.captaCard.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA_HIGHLIGHT.png').convert_alpha()
                self.captaCard.kind_image()

        if self.grabbed == True:
            self.rect.left = pg.mouse.get_pos()[0] - 32
            self.rect.top = pg.mouse.get_pos()[1] - 32
            self.redraw_card((255,255,255))

            self.hovering = False

        if self.rect.y >= 196 and self.rect.y <= 757:
            self.interactable = True
            if self.children:
                for child in self.children:
                    UIBase.get_group('layer').change_layer(child, -1)
                UIBase.get_group('layer').change_layer(self.children[3], 1)
        else:
            self.interactable = False
            if self.children:
                for child in self.children:
                    UIBase.get_group('layer').change_layer(child, -1)

    def redraw_card(self, color):
        if self.writing == False:
            if self.captaCard:
                self._create_appearance([[249, 64], color, [0, 0]],  [[10, 64], UIBase.modusForground, [239, 0]])

                self.kindImage = pg.image.load(UIBase.CodeDatabase.find_kindImage(self.kind)).convert_alpha()
                self.kindImage.set_alpha(125)
                self.image.blit(self.kindImage, (185, 3))

                nameTxt = self.font.render(self.name, True, (0,0,0))
                self.image.blit(nameTxt, (3,3))

                codeTxt = self.font.render(self.code, True, (0,0,0))
                self.image.blit(codeTxt, (3,37))

                tierTxt = self.font.render(self.tier, True, (0,0,0))
                self.image.blit(tierTxt, (129,37))

            elif self.code == "-":
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

    def place_children(self):
        self.children[0].rect.topleft = (self.rect.x+3, self.rect.y+3)
        self.children[1].rect.topleft = (self.rect.x+3, self.rect.y+35)
        self.children[2].rect.topleft = (self.rect.x+129, self.rect.y+35)
        self.children[3].rect.topleft = (78, self.rect.y+64)

    def start_card(self):

        self.image.fill((255,255,255))
        self.writing = True
        self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+3, self.rect.y+3, 243, 28, 22, "nameOverlay", "Input the name of the Captchalogue Card (A-z)", "Txt"))
        self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+3, self.rect.y+35, 105, 28, 8, "codeOverlay", "Input the code of the Captchalogue Card (!, ?, 0-9, A-Z, a-z)", "Txt"))
        self.children.append(UIBase.get_uiElem('TextField')(self.rect.x+129, self.rect.y+35, 33, 28, 2, "tierOverlay", "Input the tier of the Captchalogue Card (1-16)", "Txt"))
        

        for child in self.children:
            UIBase.get_group('layer').change_layer(child, -1)
            child.changeColors((230,230,230), (200,200,200), (170,170,170))

        self.children.append(UIBase.get_uiElem('FinishButton')(self))

        self.children[0].active = True
        self.children[0].image.fill((170,170,170))


        for elem in UIBase.get_group("ui"):
            if hasattr(elem, "job"):
                if elem.job == "nameOverlay" or elem.job == "codeOverlay" or elem.job == "tierOverlay":
                    elem.color = (235,235,235)
                    elem.no_hover()

    def hover(self):
        if self.captaCard:
            if self.prevTick == 0:
                self.prevTick = pg.time.get_ticks()

        if self.writing == False:
            self.redraw_card((230,230,230))
            self.hovering = True

    def no_hover(self):
        if self.writing == False:
            self.redraw_card((255,255,255))
            self.hovering = False

        if self.captaCard:
            self.prevTick = 0
            self.captaCard.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
            self.captaCard.kind_image()

    def alt_no_hover(self):
        self.redraw_card((230,230,230))
        self.hovering = False

    def alt_hover(self):
        self.redraw_card((255,255,255))
        self.hovering = True

    def on_click(self):
        if UIBase.get_uiElem('RemoveCardButton').eject == True and self.interactable == True:
            if self.empty == False:
                self.empty = True
                self.name = "-"
                self.code = "-"
                self.tier = "-"

                UIBase.get_uiElem('RemoveCardButton').eject = False
                for elem in UIBase.get_group("ui"):
                    if isinstance(elem, UIBase.get_uiElem('ListObject')):
                        elem.redraw_card((255,255,255))
                    elif isinstance(elem, UIBase.get_uiElem('CardList')):
                        elem.save_list()
            else: 
                UIBase.get_uiElem('PopUp')("You can\'t eject an empty card")
        elif self.interactable == True:
            if self.empty == False:
                self.grabbed = True
                self.prevPos = self.rect.topleft
                UIBase.get_group('layer').change_layer(self, len(UIBase.get_group('ui')))