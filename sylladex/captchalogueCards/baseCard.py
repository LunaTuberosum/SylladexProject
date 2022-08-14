import pygame as pg

import math

from baseUI import UIBase
from .cardOutline import CardOutline

from sylladex.captchalogueCards.stackManager import StackManager


class BaseCard(pg.sprite.Sprite):
    cards = pg.sprite.Group()

    def __init__(self, pos, listObj):
        super().__init__(UIBase.get_group('layer'), BaseCard.cards)

        self.hovering = False
        self.selected = False

        self.listObj = listObj
        self.kindImage = None

        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.kind_image()
        
        UIBase.get_group('layer').change_layer(self, 2)

        self.cardID = BaseCard.get_length()

        self.prevAnimTick = 0

        self.shaking = False
        self.moving = False
        self.prevPos = None

    def kind_image(self):
        if self.kindImage == None:
            self.kindImage = pg.image.load(UIBase.CodeDatabase.find_kindImage(self.listObj.kind)).convert_alpha()
        if self.selected == True:
            self.image.blit(self.kindImage, [15, 25])
        else:
            self.image.blit(self.kindImage, [5, 25])
        
    def hover(self):
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA_HIGHLIGHT.png').convert_alpha()
        self.kind_image()
        self.hovering = True

    def no_hover(self):
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        self.kind_image()
        self.hovering = False

    def on_click(self):
        for card in BaseCard.cards:
            if card.selected == True:
                return
        UIBase.get_group('layer').change_layer(self, 2)
        self.selected = True
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA_UP.png').convert_alpha()
        self.kind_image()
    
    def on_release(self):
        for elem in UIBase.get_group('ui'):
            if isinstance(elem, UIBase.get_uiElem('CardList')):
                if self.rect.colliderect(elem):
                    self.listObj.captaCard = None
                    self.listObj.redraw_card('#FFFFFF')
                    self.listObj.prevTick = 0
                    BaseCard.remove_cardFromGroup(self)

                    CardOutline.destroy_outline()

                    return

        UIBase.get_group('layer').change_layer(self, -1)
        self.selected = False
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        self.kind_image()

        self.combine()

        CardOutline.destroy_outline()

    def combine(self):
        for outline in CardOutline.currentOutline:
            if outline.rect.colliderect(self.rect):
                self.rect.topleft = outline.rect.topleft
                if StackManager.get_length():
                    StackManager.add_toStack(self)
                    StackManager.get_stack().change_layer(self, StackManager.get_length())
                else:
                    StackManager.add_toStack(self)
                    StackManager.get_stack().change_layer(self, StackManager.get_length())
                    StackManager.add_toStack(outline.focusedCard)
                    StackManager.get_stack().change_layer(outline.focusedCard, StackManager.get_length())
                print(StackManager.get_length())

    def move(self, velocity):
        self.rect.move_ip(velocity)  
        self.prevAnimTick = 0

        self.find_distance()

    def find_distance(self):
        all_dis = []

        for card in BaseCard.get_cardGroup():
            if UIBase.get_modus() == 'STACK':
                if StackManager.get_stack():
                    for stackCard in StackManager.get_stack():
                        if card == StackManager.get_top_card():
                            CardOutline(card)
                            return
                        elif stackCard == card:
                            return
                        

                x = self.rect.x
                y = self.rect.y
                x2 = card.rect.x
                y2 = card.rect.y
                distance = int(math.sqrt((x2 - x)**2+(y2 -y)**2))

                if distance != 0:
                    all_dis.append(distance)
                    for index, d in enumerate(all_dis):

                        if len(all_dis) == 1 or distance < d:
                            if CardOutline.currentOutline:
                                CardOutline.move_outline(card)
                            else:  
                                CardOutline(card)

    def update(self):
        if self.moving == True:
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('CardList')):
                    if self.rect.colliderect(elem):
                        if self.prevPos:
                            
                            if self.prevPos == self.rect.topleft:
                                self.shake_anaimation()
                            else:
                                self.prevPos = self.rect.topleft
                        else:
                            self.prevPos = self.rect.topleft

                    else:
                        self.prevPos = None
                        self.shaking = False

            if self.selected == True:
                self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA_UP.png').convert_alpha()
                self.kind_image()


    def shake_anaimation(self):
        self.shaking = True
        if self.prevAnimTick == 0:
            self.prevAnimTick = pg.time.get_ticks()
            self.prevPos = self.rect.topleft
            self.rect.x = self.prevPos[0] - 3
        else:
            if pg.time.get_ticks() -  self.prevAnimTick >= 200:
                self.rect.x = self.prevPos[0] - 3
                self.prevAnimTick = pg.time.get_ticks()
            elif pg.time.get_ticks() -  self.prevAnimTick >= 100:
                self.rect.x = self.prevPos[0] + 2

    @classmethod
    def get_length(cls):
        return len(cls.cards)

    @classmethod
    def get_cardGroup(cls):
        return cls.cards

    @classmethod
    def add_cardToGroup(cls, card):
        if UIBase.get_modus() == 'STACK':
            return StackManager.add_toStack(card)

    @classmethod
    def remove_cardFromGroup(cls, card):
        cls.get_cardGroup().remove(card)
        for _card in StackManager.get_stack():
            if _card == card:
                StackManager.get_stack().remove(card)
        UIBase.get_group('layer').remove(card)
        card.kill()
