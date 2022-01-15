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

        self.left = None
        self.right = None

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
        entity = CaptchaCards((randint(205, 620), randint(40, 360)), WHITE, text, name, tier, scale, "STACK", cardIDs,)
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
    def move(self, velocity, stack, area, scale, modus, layers, sprites):

        if self.child == None and self.parent == None:
            self.rect.move_ip(velocity)
        elif self.parent != None:
            return
        else:
            parent = self
            parent_all = self
            move = 48* scale
            x = 0
            for s in stack:
                for sprite in sprites:
                    if s == sprite.cardID:
                        layers.change_layer(sprite, x)
                        x += 1


                if parent.child != None:

                    CaptchaCards.moveChild(parent.child, parent_all, velocity, move, modus, scale)
                    parent = parent.child
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
                                y = 48 * scale
                                outline = CaptaOutline((c.rect.x, c.rect.y + y), (255, 255, 255), c, scale)
            if len(all_dis) != 0:
                return outline

        else:
            for c in sprites:
                
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

        x = 0
        for s in stack:
            for sprite in sprites:
                if s == sprite.cardID:

                    layer.change_layer(toCombi, x)
                    x += 1

        toCombi.rect = outline.rect
        baseCombi.rect = basePos

        with open("data/list.txt", "w") as f:
            for sprite in sprites:
                for s in stack:    
                    if s == sprite.cardID:
                                    
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))

### PROLLY FINE
    def disconnect(toDis, baseDis, stack, sprites, scale):
        stack.remove(toDis.cardID)
        toDis.image = pg.image.load("GUI/cards/STACK/CAPTA_UP.png").convert_alpha()
        CaptchaCards.kindIcon(toDis, scale, "u")
        if len(stack) <= 1:
            stack.clear()
        with open("data/list.txt", "w") as f:
            for s in stack:    
                for sprite in sprites:
                    if s == sprite.cardID:
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))
        
        baseDis.child = None
        toDis.parent = None

class QueueCards(CaptchaCards):

    ### FINE
    def createCard(scale, sprite, layer, text, name, stack, tier, cardIDs):
        entity = CaptchaCards((randint(205, 620), randint(40, 360)), WHITE, text, name, tier, scale, "QUEUE", cardIDs)
        sprite.add(entity)
        layer.add(entity)
        CaptchaCards.checkCode(entity)

        CaptchaCards.kindIcon(entity, scale, "d")

    def disconnect(toDis, baseDis, stack, sprites, scale):
        stack.remove(toDis.cardID)
        toDis.image = pg.image.load("GUI/cards/QUEUE/CAPTA_UP.png").convert_alpha()
        CaptchaCards.kindIcon(toDis, scale, "u")
        if len(stack) <= 1:
            stack.clear()
        with open("data/list.txt", "w") as f:
            for s in stack:    
                for sprite in sprites:
                    if s == sprite.cardID:
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))
        
        baseDis.parent = None
        toDis.child = None

class TreeCards(CaptchaCards):

    def addTree(current, value, nodeNum,screen):

        if value.name[0] < current.name[0]:
            if current.left == None:
                current.left =  value
                value.rect.y = current.rect.y +(48 * nodeNum) 
                value.rect.x = current.rect.x
                value.rect.x -= (current.rect.w/2) * nodeNum
                pg.draw.line(screen, (151, 255, 0), (current.rect.x, current.rect.y ), (current.rect.x,value.rect.y), 5)
                pg.display.flip()


            else:
                TreeCards.addTree(current.left, value, nodeNum,screen)
        else:
            if current.right == None:
                current.right = value
                value.rect.y = current.rect.y + (48 * nodeNum) 
                value.rect.x = current.rect.x
                value.rect.x += (current.rect.w/2) * nodeNum
                pg.draw.line(screen, (151, 255, 0), (current.rect.x, current.rect.y ), (current.rect.x,value.rect.y), 5)
                pg.display.flip()


            else:
                TreeCards.addTree(current.right, value,nodeNum, screen)

    def debugPrintTree(current, root):
        
        if current == root:
            print("root:", current.name)
        if current.left:
            print(current.name + "'s'","l branch:", current.left.name)
            TreeCards.debugPrintTree(current.left, root)
        if current.right:
            print(current.name + "'s'","r branch:", current.right.name)
            TreeCards.debugPrintTree(current.right, root)
        

    def startTree(root, stack, sprites, screen):
        for s in sprites:
            if s.cardID == stack[0]:
                root = s
        stack.pop(0)
        current = root
        for c in stack:
            for s in sprites:
                print("stack",c)
                print("ID",s.cardID)
                if s.cardID == c:
                    TreeCards.addTree(root, s, len(stack)/2, screen)
                    break
        TreeCards.debugPrintTree(root, root)
        

    
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