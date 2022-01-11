import pygame as pg
from math import *
from random import *
import codeDatabase
WHITE = (255, 255, 255)

class CaptchaCards(pg.sprite.Sprite):

    def __init__(self, pos, color, text, name, tier, scale, modus, cardIDs):
        super().__init__()
        self.image = pg.Surface((64, 64))
        self.image.fill(color)
        self.image = pg.image.load("GUI/cards/" + modus + "/CAPTA.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        if scale == 1:
            pass
        else:
            nW = self.rect[2]*scale
            nH = self.rect[3]*scale
            nX = self.rect[0]*scale
            nY = self.rect[1]*scale
            self.rect.x = nX
            self.rect.y = nY
            self.image = pg.transform.scale(self.image, (nW, nH))
            self.rect.w = nW
            self.rect.h = nH
            
        self.captaCode = text
        self.tier = tier
        self.child = None
        self.parent = None
        self.edited = False
        self.type = modus

        self.name = name
        self.wKind = "Artifactkind"
        self.wType = "NA"
        self.grist = "ARTIFACT"
        self.eff = []
        self.deff = []
        self.trait1 = "None"
        self.trait2 = "None"
        self.action1 = "No Action"
        self.action2 = "No Action"
        self.action3 = "No Action"
        self.action4 = "No Action"

        self.cardID = len(cardIDs)
        cardIDs.append(self.cardID)
        print(self.cardID)

### FINE
    def kindIcon(entity, scale, style):
        CaptchaCards.checkCode(entity)
        entityImage = pg.Surface((16, 16))
        entityImage.fill(WHITE)
        entityImage = pg.image.load(codeDatabase.kind.get(entity.wKind)).convert_alpha()
        nW = 64*scale
        nH = 64*scale
        entityImage = pg.transform.scale(entityImage, (nW, nH))

        if style == "d":
            entity.image.blit(entityImage, [5*scale, 30*scale])
        else:
            entity.image.blit(entityImage, [15*scale, 30*scale])
        
### FINE
    def destroy(sel, uis, layers, sprites):
        for i in uis:
            if i.job == "trash" and i.active == True:
                if sel.rect.colliderect(i.rect) and sel.parent == None and sel.child == None:
                    sprites.remove(sel)
                    layers.remove(sel)

### FINE
    def checkCode(self):
        codeDatabase.readCode(self.captaCode, codeDatabase.code, "NA", self.tier, self)

    ### FINE
    def createCard(scale, sprite, layer, text, name, stack, tier, cardIDs):
        entity = CaptchaCards((randint(205, 620), randint(40, 360)), WHITE, text, name, tier, scale, "STACK", cardIDs)
        sprite.add(entity)
        layer.add(entity)
        CaptchaCards.checkCode(entity)

        CaptchaCards.kindIcon(entity, scale, "d")

### PROLLY FINE
    def moveChild(self, parent, velocity, move, modus, scale):
        
        self.rect.move_ip(velocity)
        parent.rect.x = self.rect.x
        parent.rect.y = self.rect.y - move
        nW = parent.rect[2]
        nH = parent.rect[3]
        parent.image = pg.transform.scale(parent.image, (nW, nH))

### PROLLY FINE
    def move(self, velocity, stack, area, scale, modus):

        if self.child == None and self.parent == None:
            self.rect.move_ip(velocity)
        elif self.parent != None:
            return
        else:
            parent = self
            parent_all = self
            move = 48* scale
            for s in stack:
                if parent.child != None:
                    child = parent.child
                    CaptchaCards.moveChild(child, parent_all, velocity, move, modus, scale)
                    parent = child
                    move += 48 * scale

### SIMPLIFIED
    def distance(self, sprites, stack, scale):
        
        if len(stack) == 0:
            all_dis= []
            for c in sprites:
                if c.child == None:
                    x = self.rect.x
                    y = self.rect.y
                    x2 = c.rect.x
                    y2 = c.rect.y
                    distance = int(sqrt((x2 - x)**2+(y2 -y)**2))
                    

                    if distance != 0:
                        all_dis.append(distance)
                        for d in all_dis:
                            if len(all_dis) == 1 or distance < d:
                                selected = c
                                y = 48 * scale
                                outline = CaptaOutline((c.rect.x, c.rect.y + y), (255, 255, 255), c, scale)
            if len(all_dis) != 0:
                return outline

        else:
            for c in sprites:
                print(c.cardID)
                if c.cardID == stack[len(stack)-1]:
                    y = 48 * scale
                    outline = CaptaOutline((c.rect.x, c.rect.y + y), (255, 255, 255), c, scale)
                    return outline

### PROLLY FINE
    def combine(toCombi, baseCombi, outline, stack, layer, sprites):

        basePos = baseCombi.rect

        if len(stack) == 0:
            stack.append(baseCombi.cardID)
        stack.append(toCombi.cardID)
        baseCombi.child = toCombi
        toCombi.parent = baseCombi
        print(stack)
        layer.change_layer(baseCombi, len(stack)-1)
        layer.change_layer(toCombi, len(stack))
        toCombi.rect = outline.rect
        baseCombi.rect = basePos

        with open("data/list.txt", "w") as f:
            for sprite in sprites:
                for s in stack:    
                    if s == sprite.cardID:
                                    
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))

### PROLLY FINE
    def disconnect(toDis, baseDis, stack, sprites):
        print(stack)
        stack.remove(toDis.cardID)
        print(stack)
        if len(stack) == 0:
            stack.clear()
        r = 0
        with open("data/list.txt", "w") as f:
            for s in stack:    
                for sprite in sprites:
                    if s == sprite.cardID:
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))
        
        baseDis.child = None
        toDis.parent = None

class QueueCards(CaptchaCards):

    ### FINE
    def createCard(scale, sprite, layer, text, name, stack, tier):
        entity = CaptchaCards((randint(205, 620), randint(40, 360)), WHITE, text, name, tier, scale, "QUEUE")
        sprite.add(entity)
        layer.add(entity)
        CaptchaCards.checkCode(entity)

        CaptchaCards.kindIcon(entity, scale, "d")

    def combine(toCombi, baseCombi, outline, stack, layer, sprites):

        basePos = baseCombi.rect

        if len(stack) == 0:
            stack.append(baseCombi.captaCode)
        stack.insert(0, toCombi.captaCode)
        baseCombi.child = baseCombi
        toCombi.parent = toCombi
        layer.change_layer(baseCombi, len(stack))
        layer.change_layer(toCombi, len(stack)-1)
        toCombi.rect = outline.rect
        baseCombi.rect = basePos

        with open("data/list.txt", "w") as f:
            for sprite in sprites:
                for s in stack:    
                    if s == sprite.captaCode:
                                    
                        f.writelines((str(sprite.tier) + " " + s + " " + sprite.name +" \n"))

    def distance(self, sprites, stack, scale):
        
        if len(stack) == 0:
            all_dis= []
            for c in sprites:
                if c.child == None:
                    x = self.rect.x
                    y = self.rect.y
                    x2 = c.rect.x
                    y2 = c.rect.y
                    distance = int(sqrt((x2 - x)**2+(y2 -y)**2))

                    if len(all_dis) == 0 :
                        selected = c
                    for d in all_dis:
                        if distance != 0:
                            if d != None:
                                if distance < d:
                                    selected = c
                    if distance != 0:
                        all_dis.append(distance)

            y = -48 * scale
            outline = CaptaOutline((selected.rect.x, selected.rect.y + y), (255, 255, 255), selected, scale)
            return outline

        else:
            for c in sprites:
                if c.captaCode == stack[len(stack)-1]:
                    y = 48 * scale
                    outline = CaptaOutline((c.rect.x, c.rect.y + y), (255, 255, 255), c, scale)
                    return outline

    
class CaptaOutline(pg.sprite.Sprite):

    def __init__(self, pos, color, p, scale):
        super().__init__()
        self.image = pg.Surface((64, 64))
        self.image.fill(color)
        self.image = pg.image.load("GUI/cards/CAPTA_OUTLINE.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        if scale == 1:
            pass
        else:
            nW = self.rect[2]*scale
            nH = self.rect[3]*scale
            self.image = pg.transform.scale(self.image, (nW, nH))
            self.rect.w = nW
            self.rect.h = nH
        self.parent = p