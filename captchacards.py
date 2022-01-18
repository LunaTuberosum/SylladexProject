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
        self.image = pg.image.load(f"GUI/cards/{modus}/CAPTA.png").convert_alpha()
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
        
    def revert(sprites, layers, scale, modus, stack):
        for s in sprites:
            s.left = None
            s.right = None
        parent = None
        layer = 0
        move = 48 * scale
        for c in stack:
            for s in sprites:
                if s.cardID == c:
                    if parent:
                        s.rect.x = parent.rect.x
                        s.rect.y = parent.rect.y + move
                        layers.change_layer(s, layer)
                        layer += 1
                    parent = s

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

    
    def moveAll(sprites, scale, velocity):
        for s in sprites:
            s.rect.move_ip(velocity)


    def move(self, velocity, stack):
        if len(stack) == 0:
            aloneObj = True
        else:
            for c in stack:
                if c == self.cardID:
                    aloneObj = False
                    break
                else:
                    aloneObj = True
        if aloneObj == True:
            self.rect.move_ip(velocity)
            return


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
            for s in stack:
                if s != self.cardID:
                    aloneObj = True
                else:
                    aloneObj = False
                    break
            if aloneObj ==  True:
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
            for s in stack:
                for sprite in sprites:  
                    if s == sprite.cardID:
                                    
                        f.writelines(f"{str(sprite.tier)} {sprite.captaCode} {sprite.name} \n")

### PROLLY FINE
    def disconnect(toDis, baseDis, stack, sprites, scale, modus):
        stack.remove(toDis.cardID)
        toDis.image = pg.image.load(f"GUI/cards/{modus}/CAPTA_UP.png").convert_alpha()
        CaptchaCards.kindIcon(toDis, scale, "u")
        if len(stack) <= 1:
            stack.clear()
        with open("data/list.txt", "w") as f:
            for s in stack:
                for sprite in sprites:  
                    if s == sprite.cardID: 
                        f.writelines(f"{str(sprite.tier)} {sprite.captaCode} {sprite.name} \n")
        
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
                                    
                        f.writelines(f"{str(sprite.tier)} {sprite.captaCode} {sprite.name} \n")
        
        baseDis.parent = None
        toDis.child = None

class TreeCards(CaptchaCards):

    def combine(toCombi, baseCombi, stack, sprites):
        if len(stack) == 0:
            stack.append(baseCombi.cardID)
        stack.append(toCombi.cardID)
        TreeCards.addTree(baseCombi, toCombi, len(stack)/2)
        

        with open("data/list.txt", "w") as f:
            for s in stack:
                for sprite in sprites:  
                    if s == sprite.cardID:
                                    
                        f.writelines(f"{str(sprite.tier)} {sprite.captaCode} {sprite.name} \n")

    def disconnect(toDis, stack, layers, sprites):
        if toDis.parent.left == toDis:
            toDis.parent.left = None
        elif toDis.parent.right == toDis:
            toDis.parent.right = None
        
        toDis.parent.child = None
        toDis.parent = None

        for s in stack:
            if s == toDis.cardID:
                stack.remove(toDis.cardID)
        if len(stack) <= 1:
            stack.clear()
        with open("data/list.txt", "w") as f:
            for s in stack:
                for sprite in sprites:  
                    if s == sprite.cardID:
                                    
                        f.writelines((str(sprite.tier) + " " + sprite.captaCode + " " + sprite.name +" \n"))
    def drawLines(value, lines, nodeNum):
        temp = nodeNum
        if value.left:
            value.left.rect.y = value.rect.y + 100
            value.left.rect.x = value.rect.x
            if nodeNum > 1:
                value.left.rect.x -= value.rect.w * nodeNum
            else:
                value.left.rect.x -= value.rect.w/2
            line = ((value.rect.x+(value.rect.w/2), value.rect.y+(value.rect.h/2) ), (value.left.rect.x+(value.rect.w/2),value.rect.y+(value.rect.h/2)), (value.left.rect.x+(value.rect.w/2), value.left.rect.y))
            lines.append(line)
            TreeCards.drawLines(value.left, lines, nodeNum-1)
        nodeNum = temp
        if value.right:
            value.right.rect.y = value.rect.y + 100
            value.right.rect.x = value.rect.x
            if nodeNum > 1:
                value.right.rect.x += value.rect.w * nodeNum
            else:
                value.right.rect.x += value.rect.w/2
            line = ((value.rect.x+(value.rect.w/2), value.rect.y+(value.rect.h/2) ), (value.right.rect.x+(value.rect.w/2),value.rect.y+(value.rect.h/2)), (value.right.rect.x+(value.rect.w/2), value.right.rect.y))
            lines.append(line)
            TreeCards.drawLines(value.right, lines, nodeNum-1)
        return lines

    def startLines(sprites, stack, lines):
        for sprite in sprites:
            if sprite.cardID == stack[0]:
                root = sprite
        lines = TreeCards.drawLines(root, lines, len(stack)/2)

        return lines

    def addTree(current, value, nodeNum):
    
        if value.name[0].lower() < current.name[0].lower():
            if current.left == None:
                current.left =  value
                value.parent = current
                current.child = value

            else:
                TreeCards.addTree(current.left, value, nodeNum-1)
        else:
            if current.right == None:
                current.right = value
                value.rect.y = current.rect.y + 100
                value.rect.x = current.rect.x
                value.parent = current
                current.child = value


            else:
                TreeCards.addTree(current.right, value,nodeNum-1)

    def debugPrintTree(current, root):
        
        if current == root:
            print("root:", current.name)
        if current.left:
            print(current.name + "'s'","l branch:", current.left.name)
            TreeCards.debugPrintTree(current.left, root)
        if current.right:
            print(current.name + "'s'","r branch:", current.right.name)
            TreeCards.debugPrintTree(current.right, root)
        

    def startTree(stack, sprites):
        if len(stack) > 0:
            for s in sprites:
                if s.cardID == stack[0]:
                    root = s
            stack.pop(0)
            current = root
            for c in stack:
                for s in sprites:
                    if s.cardID == c:
                        TreeCards.addTree(root, s, len(stack)/2)
                        break
            
            # TreeCards.debugPrintTree(root, root)
            stack.insert(0, root.cardID)
        

    
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