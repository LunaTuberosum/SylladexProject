import pygame as pg

from baseUI import UIBase
from sylladex.captchalogueCards.stackManager import StackManager


class BaseCard(pg.sprite.Sprite):
    cards = pg.sprite.Group()

    def __init__(self, pos, listObj):
        super().__init__()

        self.hovering = False
        self.selected = False

        self.listObj = listObj
        self.kindImage = None

        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.kind_image()

        BaseCard.cards.add(self)
        UIBase.get_group('layer').add(self)
        UIBase.get_group('layer').change_layer(self, 2)

        self.cardID = BaseCard.get_length()

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
                    return

        self.selected = False
        self.image = pg.image.load(f'sylladex/captchalogueCards/assets/{UIBase.get_modus()}/CAPTA.png').convert_alpha()
        self.kind_image()

    def move(self, velocity):
        self.rect.move_ip(velocity)                    

    def get_length():
        return len(BaseCard.cards)

    def get_cardGroup():
        return BaseCard.cards

    def add_cardToGroup(card):
        if UIBase.get_modus() == 'STACK':
            return StackManager.add_toStack(card)

    def remove_cardFromGroup(card):
        BaseCard.get_cardGroup().remove(card)
        for _card in StackManager.get_stack():
            if _card == card:
                StackManager.get_stack().remove(card)
        UIBase.get_group('layer').remove(card)
        card.kill()
