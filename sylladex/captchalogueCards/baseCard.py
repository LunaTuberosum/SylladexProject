import pickle
import pygame as pg

import math

from uiElement import UIElement
from .cardOutline import CardOutline

from sylladex.captchalogueCards.stackManager import StackManager


class BaseCard(pg.sprite.Sprite):
    cards = pg.sprite.Group()

    def __init__(self, pos, codeData, loading=False):
        super().__init__(UIElement.get_group('layer'), BaseCard.cards)

        self.hovering = False
        self.selected = False

        self.codeData = codeData
        self.kindImage = None

        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.kind_image()
        
        UIElement.get_group('layer').change_layer(self, -2)

        self.cardID = BaseCard.get_length()

        self.prevAnimTick = 0

        self.shaking = False
        self.prevPos = None

        self.moving = False

        self.pulled = False
        self.prevPulledPos = None

        if loading == False:
            BaseCard.save_cards()

    def kind_image(self):
        if self.kindImage == None:
            self.kindImage = pg.image.load(UIElement.CodeDatabase.find_kindImage(self.codeData.kind)).convert_alpha()
        if self.selected == True:
            self.image.blit(self.kindImage, [15, 25])
        else:
            self.image.blit(self.kindImage, [5, 25])
        
    def hover(self):
        for card in BaseCard.cards:
            if card.hovering == True:
                if UIElement.get_modus() == 'STACK':
                    if StackManager.get_length() > 0:
                        if StackManager.get_stack().get_layer_of_sprite(self) > StackManager.get_stack().get_layer_of_sprite(card):
                            card.hovering = False
                            card.no_hover()
                            break
                return
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_HIGHLIGHT.png').convert_alpha()
        self.kind_image()
        self.hovering = True        

    def no_hover(self):
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
        self.kind_image()
        self.hovering = False

    def on_middleClick(self):
        for elem in UIElement.get_group('ui'):
            if isinstance(elem, UIElement.get_uiElem('CardInspector')):
                UIElement.remove_fromGroup(elem)
                elem.kill()
                for child in elem.children:
                    UIElement.remove_fromGroup(child)
                    child.kill()
        UIElement.get_uiElem('CardInspectorCheck').checks = []

        UIElement.get_uiElem('CardInspector')(self.codeData)

    def on_click(self):

        if UIElement.get_modus() == 'STACK':
            for card in StackManager.get_stack():
                if card == self:
                    
                    if self == StackManager.get_top_card('remove'):
                        StackManager.remove_fromStack(self)
                        for card in StackManager.get_stack():
                            if card != self:
                                card.pulled = False
                                card.selected = False
                                card.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
                                card.kind_image() 
                        StackManager.add_toStack(self)
                
                        self.selected = True
                        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png').convert_alpha()
                        UIElement.get_group('layer').change_layer(self, 2)
                        self.kind_image()
                        return

                    for card in StackManager.get_stack():
                        if card != self:
                            card.selected = False
                            card.pulled = False
                            card.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
                            card.kind_image()
                        else:
                            card.pulled = True
                            card.selected = True
                            self.prevPulledPos = self.rect.topleft
                            self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png').convert_alpha()
                            self.kind_image()
                            break
                    return

        UIElement.get_group('layer').change_layer(self, 2)

        if UIElement.get_modus() == 'STACK':
            if StackManager.get_length() > 0:
                StackManager.add_toStack(self)
                
        self.selected = True
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png').convert_alpha()
        self.kind_image()
    
    def on_release(self):

        if self.pulled == True:
            self.rect.topleft = self.prevPulledPos
            self.prevPulledPos = None
            self.pulled = False
            self.selected = False
            self.moving = False
            self.shaking = False
            self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
            self.kind_image()
            return

        elif UIElement.get_modus() == 'STACK':
            if StackManager.get_length() > 0 and self.shaking == False:
                StackManager.get_stack().remove(self)

        UIElement.get_group('layer').change_layer(self, -2)
                
        for elem in UIElement.get_group('ui'):
            if isinstance(elem, UIElement.get_uiElem('CardList')):
                if self.rect.colliderect(elem):
                    for listObj in elem.children:
                        if listObj.codeData == self.codeData:
                            listObj.captaCard = None
                            listObj.redraw_card('#FFFFFF')
                            listObj.prevTick = 0
                            break

                    BaseCard.remove_cardFromGroup(self)

                    CardOutline.destroy_outline()

                    return

        self.selected = False
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA.png').convert_alpha()
        self.kind_image()

        self.combine()

        CardOutline.destroy_outline()

    def combine(self):
        for outline in CardOutline.currentOutline:
            if outline.rect.colliderect(self.rect):
                self.rect.topleft = outline.rect.topleft
                if StackManager.get_length() > 0:
                    
                    StackManager.add_toStack(self)
                else:
                    StackManager.add_toStack(outline.focusedCard)
                    StackManager.add_toStack(self)
        BaseCard.save_cards()

    def move(self, velocity):
        if self.pulled == True: return
        self.rect.move_ip(velocity)  
        self.prevAnimTick = 0

        self.find_distance()

    def find_distance(self):
        all_dis = []

        for card in BaseCard.get_cardGroup():
            if UIElement.get_modus() == 'STACK':
                if StackManager.get_length() > 0:
                    if card == StackManager.get_top_card('distance'):
                        if CardOutline.currentOutline:
                            CardOutline.move_outline(card)
                        else:  
                            CardOutline(card)
                        return

                x = self.rect.x
                y = self.rect.y
                x2 = card.rect.x
                y2 = card.rect.y
                distance = [int(math.sqrt((x2 - x)**2+(y2 -y)**2)), card]

                if distance[0] != 0:
                    all_dis.append(distance)

        if len(all_dis) == 0:
            return
        for index, d in enumerate(all_dis):  
            if index == 0: possiableCard = d
            if d[0] < possiableCard[0]:
                possiableCard = d

        if CardOutline.currentOutline:
            CardOutline.move_outline(possiableCard[1])
        else:
            CardOutline(possiableCard[1])

    def update(self):
        if self.pulled == True:
            self.shake_anaimation()
            self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png').convert_alpha()
            self.kind_image()

        elif self.moving == True:
            for elem in UIElement.get_group('ui'):
                if isinstance(elem, UIElement.get_uiElem('CardList')):
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
                self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIElement.get_modus()}/CAPTA_UP.png').convert_alpha()
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
    def move_all_cards(cls, rel):
        for card in cls.get_cardGroup():
            card.rect.move_ip(rel)
            UIElement.get_group('layer').change_layer(card, -2)

        if UIElement.get_modus() == 'STACK': 
            for card in StackManager.get_stack():
                UIElement.get_group('layer').change_layer(card, -2)

    @classmethod
    def get_length(cls):
        return len(cls.cards)

    @classmethod
    def get_cardGroup(cls):
        return cls.cards

    @classmethod
    def add_cardToGroup(cls, card):
        if UIElement.get_modus() == 'STACK':
            return StackManager.add_toStack(card)

    @classmethod
    def remove_cardFromGroup(cls, card, temp=False):
        cls.get_cardGroup().remove(card)
        for _card in StackManager.get_stack():
            if _card == card:
                StackManager.get_stack().remove(card)
        UIElement.get_group('layer').remove(card)
        card.kill()

        if temp == False: BaseCard.save_cards()

    @classmethod
    def save_cards(cls):
        UIElement.get_uiElem('ConsoleMessage')('Saved Cards')
        tempArray = []
        for card in cls.get_cardGroup():
            tempArray.append([card.codeData, card.rect.topleft])

        with open('sylladex/captchalogueCards/data/cardData.plk', 'wb') as cardSave:
            pickle.dump(tempArray, cardSave, -1)

        if UIElement.get_modus() == 'STACK': StackManager.save_stack()

    @classmethod
    def load_cards(cls):

        with open('sylladex/captchalogueCards/data/cardData.plk', 'rb') as cardLoad:
            tempArray = pickle.load(cardLoad)

        for card in tempArray:
            BaseCard(card[1], card[0], True)

        if UIElement.get_modus() == 'STACK': StackManager.load_stack(BaseCard.get_cardGroup())
        UIElement.get_uiElem('ConsoleMessage')('Loaded Cards')
