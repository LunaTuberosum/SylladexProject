import pygame as pg

import codeDatabase
import captchacards

import time
import math
import textwrap

WHITE = (255, 255, 255)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('black')
BLACK = pg.Color('black')

class UIBase(pg.sprite.Sprite):

    def __init__(self, pos, image, job, typeing, scale, modus, size):
        super().__init__()

        self.image = pg.Surface(size)
        self.image.fill(WHITE)
        self.image = pg.image.load(image).convert_alpha()
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

        self.type = typeing
        self.job = job
        self.active = True
        self.children = []
        self.parent = None

        self.fontSmall = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 12*scale)
        self.font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 15*scale)
        self.fontBig = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        self.color = BLACK
        self.text = ""
        self.txt_surface = self.fontBig.render("", True, self.color)
        self.active = False
        self.activeImage = ""
        self.inactiveImage = ""
        
        self.modus = modus

        self.checked = False

        self.inspectie = None

        self.insAtr = None
        self.insNum = None

    def updateAll(i, sprites, scale, uis, mColor, inputBox):
        if i.job == "CardInspection":
            i.image = pg.image.load("GUI/panel/" + i.modus + "/PANEL.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            UIBase.reinit(i.inspectie[0], i, scale)

        for b in inputBox:
            b.active = False

        uiChanger = {
            "sylladexPanel": "GUI/panel/" + i.modus + "/SYLLADEXPANEL.png",
            "stackingArea": "GUI/panel/" + i.modus + "/STACK_AREA.png",
            "cardInspection": "GUI/panel/" + i.modus + "/PANEL.png",
            "help": "GUI/icon/" + i.modus + "/HELP.png",
            "cardCreate": "GUI/button/" + i.modus + "/ADD.png",
            "sylSettings": "GUI/icon/" + i.modus + "/FLIP.png",
            "nameLabel": "GUI/label/" + i.modus + "/NAMELABEL.png",
            "codeLabel": "GUI/label/" + i.modus + "/CODELABEL.png",
            "tierLabel": "GUI/label/" + i.modus + "/TIERLABEL.png",
            "name": "GUI/textbox/" + i.modus + "/TEXTBOX.png",
            "code": "GUI/textbox/" + i.modus + "/TEXTBOX_MEDIUM.png",
            "tier": "GUI/textbox/" + i.modus + "/TEXTBOX_SMALL.png",
            "modusChanger": "GUI/panel/" + i.modus + "/MODUSLABEL.png",
            "taskbarOpen": "GUI/icon/" + i.modus + "/ARROW.png",
            "inspecttrait1": "GUI/button/CHECK_BOX.png",
            "inspecttrait2": "GUI/button/CHECK_BOX.png",
            "inspectaction1": "GUI/button/CHECK_BOX.png",
            "inspectaction2": "GUI/button/CHECK_BOX.png",
            "inspectaction3": "GUI/button/CHECK_BOX.png",
            "inspectaction4": "GUI/button/CHECK_BOX.png",
            "closePanel": "GUI/button/" + i.modus + "/ARROW.png",
            "taskbarClose": "GUI/icon/" + i.modus + "/ARROW_ACTIVE.png",
            "taskbar": "GUI/panel/" + i.modus + "/TASKBAR.png",
            "trash": "GUI/icon/" + i.modus + "/TRASH.png",
            "clear": "GUI/icon/" + i.modus + "/TRASH_ALL.png",
            "edit": "GUI/icon/" + i.modus + "/EDIT.png",
            "infoUIs": "GUI/panel/LABEL.png"
            
        }

        i.image = pg.image.load(uiChanger.get(i.job, "")).convert_alpha()
        nW = i.rect[2]
        nH = i.rect[3]
        i.image = pg.transform.scale(i.image, (nW, nH))


        if i.job == "sylladexPanel":
            sylladexText = i.fontBig.render('SYLLADEX' , True , WHITE)
            modusText = i.fontBig.render('fetch modus' , True , mColor)
            modusName = i.fontBig.render(i.modus, True, mColor)
    

            i.image.blit(sylladexText, [12*scale, 0*scale])
            i.image.blit(modusText, [12*scale, 366*scale])
            i.image.blit(modusName, [84*scale, 504*scale])
        elif i.job == "cardInspection":
            CardInspector.reinit(i.inspectie, i, scale)

        for s in sprites:
            s.image = pg.image.load("GUI/cards/" + i.modus + "/CAPTA.png").convert_alpha()
            captchacards.CaptchaCards.kindIcon(s, scale, "d")
            nW = s.rect[2]
            nH = s.rect[3]
            s.image = pg.transform.scale(s.image, (nW, nH))

class StackingArea(UIBase):

    def create(scale, modus, layers, uis):
        entity = StackingArea((252,0), "GUI/panel/"+modus+"/STACK_AREA.png", "stackingArea", "panel", scale, modus, (708,540))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

class SylladexPanel(UIBase):

    def create(scale, modus, layers, uis, modusColor):
        entity = StackingArea((0,0), "GUI/panel/"+modus+"/SYLLADEXPANEL.png", "sylladexPanel", "panel", scale, modus, (252,540))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

        sylladexText = entity.fontBig.render('SYLLADEX' , True , WHITE)
        modusText = entity.fontBig.render('fetch modus' , True , modusColor.get(modus)[0])
        modusName = entity.fontBig.render(modus, True, modusColor.get(modus)[0])
        
        entity.image.blit(sylladexText, [12*scale, 0*scale])
        entity.image.blit(modusText, [12*scale, 366*scale])
        entity.image.blit(modusName, [84*scale, 504*scale])

class ModusChanger(UIBase):

    def create(scale, modus, layers, uis):
        entity = StackingArea((12, 391), "GUI/panel/"+modus+"/MODUSLABEL.png", "modusChanger", "button", scale, modus, (214, 113))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

    def modusChange(i, mColor, m, scale, uis, sprites, layers, cardIDs): 
        if m == "STACK":
            m = "QUEUE"
        elif m == "QUEUE":
            m = "TREE"
        elif m == "TREE":
            m = "STACK"
            captchacards.CaptchaCards.revert(sprites, layers, scale, m, cardIDs)

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        sylladexText = FONT.render('SYLLADEX' , True , WHITE)
        modusText = FONT.render('fetch modus' , True , mColor)
        modusName = FONT.render(m, True, mColor)
        
        for i in uis:
            if i.job == "sylladexPanel":
                i.image.blit(sylladexText, [12*scale, 0*scale])
                i.image.blit(modusText, [12*scale, 366*scale])
                i.image.blit(modusName, [84*scale, 504*scale])
            
        return m

class Label(UIBase):
    
    def create(scale, modus, layers, uis, label, job, pos):
        entity = StackingArea(pos, "GUI/label/"+modus+"/"+label+".png", job, "label", scale, modus, (0,0))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

class Textbox(UIBase):
    
    def create(scale, modus, layers, uis, box, job, pos, active, inactive):
        entity = Textbox(pos, "GUI/textbox/"+modus+"/"+box+".png", job, "textbox", scale, modus, (0,0))
        entity.activeImage = active
        entity.inactiveImage = inactive
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

        return entity

    def draw(box, screen):
        # Blit the text.
        screen.blit(box.txt_surface, (box.rect.x+5, box.rect.y))

    def nameBox(curBox, otherBox, color):
        for b in otherBox:
            b.active = False
            b.image = pg.image.load("GUI/textbox/" + b.modus + "/" + b.inactiveImage + ".png").convert_alpha()
            nW = b.rect[2]
            nH = b.rect[3]
            b.image = pg.transform.scale(b.image, (nW, nH))

        curBox.active = not curBox.active
        curBox.color = color
        curBox.image = pg.image.load("GUI/textbox/" + curBox.modus + "/" + curBox.activeImage + ".png").convert_alpha()
        nW = curBox.rect[2]
        nH = curBox.rect[3]

class AddButton(UIBase):
    
    def create(scale, modus, layers, uis, job, pos):
        entity = AddButton(pos, "GUI/button/"+modus+"/ADD.png", job, "button", scale, modus, (68, 36))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)   

    def captaButton(sprites, layers, text, name, stack, tier, scale, modus, cardIDs):

        if modus == "STACK":
            captchacards.CaptchaCards.createCard(scale, sprites, layers,text, name, stack, tier, cardIDs)
        elif modus == "QUEUE":
            captchacards.QueueCards.createCard(scale, sprites, layers,text, name, stack, tier, cardIDs)

    def cardCreate(i, textboxs,   sprites, layers, currentStack, scale, cardIDs):

        i.image = pg.image.load("GUI/button/" + i.modus + "/ADD_DOWN.png").convert_alpha()
        
        for b in textboxs:
            if b.text == "":
                return
    
        AddButton.captaButton(sprites, layers, textboxs[1].text, textboxs[0].text, currentStack, int(textboxs[2].text), scale, i.modus, cardIDs)

        for b in textboxs:
            b.text = ""
            b.txt_surface = i.fontBig.render(b.text, True, b.color)
            b.active = False
            b.image = pg.image.load("GUI/textbox/" + i.modus + "/" + b.inactiveImage + ".png").convert_alpha()

    def setEdit(sprites, uis, editing, stack, scale, modus):
        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)
        for s in sprites:
            if s.edited == True:
                for i in uis:
                    if i.job == "name":
                        s.name = i.text
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                        i.active = False
                        i.image = pg.image.load("GUI/textbox/" + i.modus + "/" + i.inactiveImage + ".png").convert_alpha()
                    elif i.job == "code":
                        s.captaCode = i.text
                        stack.pop(len(stack)-1)
                        stack.append(i.text)
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                        i.active = False
                        i.image = pg.image.load("GUI/textbox/" + i.modus + "/" + i.inactiveImage + ".png").convert_alpha()
                        s.image = pg.image.load("GUI/cards/" + modus + "/CAPTA.png").convert_alpha()
                        captchacards.CaptchaCards.kindIcon(s, scale, "d")
                    elif i.job == "tier":
                        s.tier = i.text
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                        i.active = False
                        i.image = pg.image.load("GUI/textbox/" + i.modus + "/" + i.inactiveImage + ".png").convert_alpha()
                    if i.job == "endEdit":
                        i.image = pg.image.load("GUI/icon/" + modus + "/EDIT.png").convert_alpha()
                        i.job = "edit"
                    for j in uis:
                        if j.job == "set":
                            
                            j.image = pg.image.load("GUI/button/" + modus + "/ADD.png").convert_alpha()
                            j.job = "cardCreate"
        editing = False
        return editing

class CheckBox(UIBase):

    def create(pos, job,  scale, modus, layers, uis, parent, insAtr, insNum):
        entity = CheckBox(pos, "GUI/button/CHECK_BOX.png", job, "button", scale, modus, (0,0))
        parent.children.append(entity)
        entity.parent = parent
        entity.insAtr = insAtr
        entity.insNum = insNum
        layers.add(entity)
        layers.change_layer(entity, 1000)
        uis.add(entity)
       
    def inspect(i, b, c):

        i.parent.image = pg.image.load("GUI/panel/" + c[4] + "/PANEL.png").convert_alpha()
        nW = i.parent.rect[2]
        nH = i.parent.rect[3]
        i.parent.image = pg.transform.scale(i.parent.image, (nW, nH))
        CardInspector.reinit(i.parent.inspectie, i.parent, c[3])
        inspectList = ["trait1", "trait2", "action1", "action2", "action3", "action4"]
        
        font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 14*c[3])
        

        if i.checked == False:
            for l in c[1]:
                for j in inspectList:
                    if l.job == "inspect"+j:
                        l.image = pg.image.load("GUI/button/CHECK_BOX.png").convert_alpha()
                        nW = l.rect[2]
                        nH = l.rect[3]
                        l.image = pg.transform.scale(l.image, (nW, nH))
                        l.checked = False

            i.checked = True

            if c[0] == 0:
                codies = [i.parent.inspectie.trait1, i.parent.inspectie.trait2, i.parent.inspectie.action1 ,i.parent.inspectie.action2 ,i.parent.inspectie.action3, i.parent.inspectie.action4]

                textPoses = [297*c[3], 312*c[3], 327*c[3], 342*c[3]]
            
                i.image = pg.image.load("GUI/button/CHECKED_BOX.png").convert_alpha()
                nW = i.rect[2]
                nH = i.rect[3]
                i.image = pg.transform.scale(i.image, (nW, nH))
                
            
                tier = math.ceil(int(i.parent.inspectie.tier)/4)
                if len(b.get(codies[c[0]]).get("WEAPON").get(str(tier))) >= 33:
                    string = math.ceil(len(b.get(codies[c[0]]).get("WEAPON").get(str(tier))) /33)
                    text = textwrap.wrap(b.get(codies[c[0]]).get("WEAPON").get(str(tier)), 33)
                    x = 0
                    for j in range(string):
                        entityText = font.render(text[x], 1, BLACK)
                        w = entityText.get_width()
                        wN = 168*c[3] - w/2
                        h = entityText.get_height()
                        hN = textPoses[x] - h/2
                        i.parent.image.blit(entityText, [wN, hN])
                        x+=1
                else:
                    entityText = font.render(b.get(codies[c[0]]).get("WEAPON").get(str(tier)), 1, BLACK)

                    w = entityText.get_width()
                    wN = 168*c[3] - w/2
                    h = entityText.get_height()
                    hN = 345*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])

            elif c[0] == 1:
                codies = [i.parent.inspectie.trait1, i.parent.inspectie.trait2, i.parent.inspectie.action1 ,i.parent.inspectie.action2 ,i.parent.inspectie.action3, i.parent.inspectie.action4]

                textPoses = [297*c[3], 314*c[3], 327*c[3], 342*c[3]]
            
                i.image = pg.image.load("GUI/button/CHECKED_BOX.png").convert_alpha()
                nW = i.rect[2]
                nH = i.rect[3]
                i.image = pg.transform.scale(i.image, (nW, nH))
            
                tier = math.ceil(int(i.parent.inspectie.tier)/4)
                if len(b.get(codies[c[0]]).get("WEAPON").get(str(tier)).get(i.parent.inspectie.wType)) >= 33:
                    string = math.ceil(len(b.get(codies[c[0]]).get("WEAPON").get(str(tier)).get(i.parent.inspectie.wType)) /33)
                    text = textwrap.wrap(b.get(codies[c[0]]).get("WEAPON").get(str (tier)).get(i.parent.inspectie.wType), 33)
                    x = 0
                    for j in range(string):
                        entityText = font.render(text[x], 1, BLACK)
                        w = entityText.get_width()
                        wN = 168*c[3] - w/2
                        h = entityText.get_height()
                        hN = textPoses[x] - h/2
                        i.parent.image.blit(entityText, [wN, hN])
                        x+=1
                else:
                    entityText = font.render(b.get(codies[c[0]]).get("WEAPON").get(str(tier)).get(i.parent.inspectie.wType), 1, BLACK)

                    w = entityText.get_width()
                    wN = 168*c[3] - w/2
                    h = entityText.get_height()
                    hN = 345*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])

            else:
                codies = [i.parent.inspectie.trait1, i.parent.inspectie.trait2, i.parent.inspectie.action1 ,i.parent.inspectie.action2 ,i.parent.inspectie.action3, i.parent.inspectie.action4]

                textPoses = [297*c[3], 314*c[3], 327*c[3], 342*c[3]]
            
                i.image = pg.image.load("GUI/button/CHECKED_BOX.png").convert_alpha()
                nW = i.rect[2]
                nH = i.rect[3]
                i.image = pg.transform.scale(i.image, (nW, nH))

            
                if len(b.get(codies[c[0]])[2]) >= 33:
                    string = math.ceil(len(b.get(codies[c[0]])[2])/33)
                    text = textwrap.wrap(b.get(codies[c[0]])[2], 33)
                    x = 0
                    for j in range(string):
                        entityText = font.render(text[x], 1, BLACK)
                        w = entityText.get_width()
                        wN = 168*c[3] - w/2
                        h = entityText.get_height()
                        hN = textPoses[x] - h/2
                        i.parent.image.blit(entityText, [wN, hN])
                        x+=1
                    entityText = font.render(b.get(codies[c[0]])[0], 1, BLACK)
                    w = entityText.get_width()
                    wN = 48*c[3] - w/2
                    h = entityText.get_height()
                    hN = 302*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])

                    entityText = font.render(b.get(codies[c[0]])[1], 1, BLACK)
                    w = entityText.get_width()
                    wN = 48*c[3] - w/2
                    h = entityText.get_height()
                    hN = 332*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])
                else:
                    entityText = font.render(b.get(codies[c[0]])[2], 1, BLACK)

                    w = entityText.get_width()
                    wN = 168*c[3] - w/2
                    h = entityText.get_height()
                    hN = 321*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])

                    entityText = font.render(b.get(codies[c[0]])[0], 1, BLACK)
                    w = entityText.get_width()
                    wN = 48*c[3] - w/2
                    h = entityText.get_height()
                    hN = 302*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])

                    entityText = font.render(b.get(codies[c[0]])[1], 1, BLACK)
                    w = entityText.get_width()
                    wN = 48*c[3] - w/2
                    h = entityText.get_height()
                    hN = 332*c[3] - h/2
                    i.parent.image.blit(entityText, [wN, hN])
        else:
            i.image = pg.image.load("GUI/button/CHECK_BOX.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            i.checked = False

class CloseButton(UIBase):

    def create(pos, modus, job, parent, scale, layers, uis):
        entity = CloseButton(pos, "GUI/button/" + modus + "/ARROW.png", job, "button", scale, modus, (16,16))
        parent.children.append(entity)
        entity.parent = parent
        layers.add(entity)
        layers.change_layer(entity, 1000)
        uis.add(entity)

    def closePanel(i, uis, layers):
        UIBase.destroy(i.parent, uis, layers)

class CardInspector(UIBase):
    
    def create(scale, modus, layers, uis, pos, sprite):
        for i in uis:
            if i.job == "cardInspection":
                CardInspector.closePanel(uis, layers)
        entity = CardInspector(pos, "GUI/panel/"+modus+"/PANEL.png","cardInspection", "label", scale, modus, (16,16))
        layers.add(entity)
        layers.change_layer(entity, 1000)
        uis.add(entity)

        entity.inspectie = sprite

        CardInspector.reinit(sprite, entity, scale)

        buttonPos = [12, 72, "trait1", 96, 72, "trait2", 12, 204, "action1",  144, 204, "action2", 12, 228, "action3",  144, 228, "action4"]

        x = 0
        y = 0
        insAtr = [codeDatabase.trait1Desc, codeDatabase.trait2Desc, codeDatabase.actionData, codeDatabase.actionData, codeDatabase.actionData, codeDatabase.actionData]
        for b in range(6):
            CheckBox.create((pos[0]+buttonPos[x],pos[1]+buttonPos[x+1]), "inspect"+buttonPos[x+2], scale, modus, layers, uis, entity, insAtr[y], y)
            x += 3
            y += 1

        CloseButton.create((pos[0]-38,pos[1]+194), modus, "closePanel", entity, scale, layers, uis)

    def closePanel(uis, layer):
        for i in uis:
            if i.job == "cardInspection":
                for c in i.children:
                    uis.remove(c)
                    layer.remove(c)
                uis.remove(i)
                layer.remove(i)

    def reinit(text, panel, scale):

        def makeText(label, text, x, y, scale, name):

            z = 1
            for c in ["CUSTOM TRAIT 1", "CUSTOM TRAIT 2", "CUSTOM TRAIT 3" ,"CUSTOM TRAIT 4" ]:
                if c == text:
                    text = "CUSTOM " + str(z)
                    break
                else:
                    z += 1

            if text == "INSPECT INFORMATION" or text == name or text == "INEFFECTIVE" or text == "GRIST TYPE":

                entityText = panel.font.render(text, 1, BLACK)

            elif len(text) >= 10:
                
                entityText = panel.fontSmall.render(text, 1, BLACK)
            
            else:
                entityText = panel.font.render(text, 1, BLACK)

            H = entityText.get_height()
            label.image.blit(entityText, [x*scale, y*scale - H/2])

        def makeImage(label, image, x, y, scale):

            n = 0

            for c in [text.wKind, text.grist, text.eff[0], text.eff[1], text.eff[2], text.eff[3], text.deff[0], text.deff[1], text.deff[2], text.deff[3], ""]:
            
                if image == c:

                    entityImage = pg.Surface((16, 16))
                    entityImage.fill(WHITE)

                    if image == text.wKind:
                        inImage = codeDatabase.kind.get(image)
                    else:
                        inImage = codeDatabase.grist.get(image)

                    entityImage = pg.image.load(inImage).convert_alpha()

                    nW = 32*scale
                    nH = 32*scale
                    entityImage = pg.transform.scale(entityImage, (nW, nH))

                    label.image.blit(entityImage, [x*scale, y*scale])
                    break
                else:
                    n += 1

                if n == 10:
                    entityImage = pg.Surface((16, 16))
                    entityImage.fill(WHITE)
                    entityImage = pg.image.load(codeDatabase.action.get(image)).convert_alpha()
                    nW = 108*scale
                    nH = 24*scale
                    entityImage = pg.transform.scale(entityImage, (nW, nH))

                    label.image.blit(entityImage, [x*scale, y*scale])


        textRef = ["CODE", 40, 372, text.captaCode, 94, 372,"TIER",174, 372, str(text.tier), 216, 372, "GRIST TYPE", 16, 132 , text.grist, 123, 132, "NAME", 16, 48, text.name,  54, 48, "ITEMKIND" , 16 , 108 , text.wKind, 99, 108, text.trait1, 39, 84, text.trait2, 123, 84, text.wType, 231, 72, "EFFECTIVE", 16, 156, "INEFFECTIVE", 16, 180, "INSPECT INFORMATION", 78, 276, "CST", 14, 303, "DMG", 12, 333, "1", 214, 108, "2", 214, 132, "3", 214, 156, "BD", 210, 180, codeDatabase.damgeNum.get(int(text.tier)).get("1"), 244, 108, codeDatabase.damgeNum.get(int(text.tier)).get("2"), 244, 132, codeDatabase.damgeNum.get(int(text.tier)).get("3"), 244, 156, codeDatabase.damgeNum.get(int(text.tier)).get("BD"), 240, 181]        
    
        x = 0
        for z in range(int(len(textRef)/3)):
            makeText(panel, textRef[x], textRef[x+1], textRef[x+2], scale, text.name)
            x += 3

        entityText = panel.fontBig.render("CAPTCHALOGUE CARD", 2, WHITE)
        panel.image.blit(entityText, [12*scale, 0*scale])

        imageRef = [text.grist, 91, 116, text.eff[0], 91, 140, text.eff[1], 115, 140, text.eff[2], 139, 140, text.eff[3], 163, 140, text.deff[0], 91 ,164, text.deff[1], 115, 164, text.deff[2], 139, 164, text.deff[3], 163, 164, text.wKind, 67 ,92, text.action1, 36, 204, text.action2, 36, 228, text.action3, 168, 204, text.action4, 168, 228]
        x = 0
        for z in range(int(len(imageRef)/3)):
            print(imageRef[x])
            makeImage(panel, imageRef[x], imageRef[x+1], imageRef[x+2], scale)
            x += 3

class HelpButton(UIBase):
    
    def create(scale, modus, layers, uis, pos):
        entity = StackingArea(pos, "GUI/icon/"+modus+"/HELP.png", "help", "button", scale, modus, (16,16))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

    def toggleHelp(helpT, uis, modus):
        if helpT == False:
            cursor =  pg.image.load("GUI/icon/" + modus + "/MOUSE_HELP.png").convert_alpha()
            helpT = True
        else:
            cursor =  pg.image.load("GUI/icon/MOUSE.png").convert_alpha()
            helpT = False

        return helpT, cursor

    def createLabel(pos, job, typeing, scale, size, layers, uis):
        entity = UIBase(pos, "GUI/panel/LABEL.png", job, "label", scale, "", size)
        layers.add(entity)
        layers.change_layer(entity, 1000)
        uis.add(entity)

        return entity

    def placeInfo(rects, uis, layers, scale):
        info = [
            "An area to put info to create CAPTCHALOUGE CARDS.", 
            "An area to input the name of the CAPTCHALOUGE CARD.", 
            "An area to input an 8 digit code tha changes what the CAPTCHALOUGE CARD is.", 
            "An area to input a number between 1 and 16 to decied the strength of the CAPTCHALOUGE CARD.", 
            "A button that creates cards or changes what info is in a card when editing.", 
            "A button that opens a task bar to let you delete, clear, edit, and [WORK IN PROGRESS].",
            "A button that would change you fetch moudes.", 
            "In this area you can stack and move CAPTCHALOUGE CARDS.", 
            "When a CAPTCHALOUGE CARD is brought over this symbol it will delete it.", 
            "This button destroys all CAPTCHALOUGE CARDS on the screen.", 
            "This button lets you edit the contents of a CAPTCHALOUGE CARD."]

        z = 0
        for i in rects:
            if i.collidepoint(pg.mouse.get_pos()):

                if z != 12:
                    if z >= 9 or z == 8:
                        x, y = pg.mouse.get_pos()
                        y -= 126
                    else:
                        x, y = pg.mouse.get_pos()
                    for i in uis:
                        if i.job == "infoUIs":
                            HelpButton.destroy(i, uis, layers)
                    panel = HelpButton.createLabel((x, y), "infoUIs", "label", scale, (68, 36), layers, uis,)
                    text = textwrap.wrap(info[z], 22)
                    k = 0
                    for g in range(len(text)):

                        entityText = panel.fontBig.render(text[g], 2, WHITE)
                        panel.image.blit(entityText, [6*scale, 6+k*scale])
                        k+= 24
                else:
                    for i in uis:
                        if i.job == "infoUIs":
                            HelpButton.destroy(i, uis, layers)
                    return
            z += 1

    def destroy(i, uis, layer):
        
        uis.remove(i)
        layer.remove(i)

class MenuButtons(UIBase):

    def create(pos, image, job, scale, layers, ui, modus):
        entity = StackingArea(pos, image, job, "button", scale, modus, (16, 32))
        layers.add(entity)
        layers.change_layer(entity, -1)

class Taskbar(UIBase):

    def create(scale, pos, uis, layers, modus):
        entity = Taskbar(pos, "GUI/panel/"+modus+"/TASKBAR.png", "taskbar", "panel", scale, modus, (0,0))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

        Taskbar.createButton(scale, "TRASH", modus, "trash", layers, uis, (425, 505), entity)

        Taskbar.createButton(scale ,  "TRASH_ALL", modus, "clear", layers, uis, (513, 505), entity)

        Taskbar.createButton(scale, "EDIT", modus, "edit", layers, uis, (616, 510), entity)
    
    def createButton(scale, image, modus, job, layers, uis, pos, parent=None):
        entity = Taskbar(pos, "GUI/icon/"+modus+"/"+image+".png", job, "label", scale, modus, (0,0))
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)
        if job != "taskbarOpen":
            parent.children.append(entity)

    def taskbarOpen(i, uis, layers, scale, modus):
        i.image = pg.image.load("GUI/icon/" + modus + "/ARROW_ACTIVE.png").convert_alpha()
        nW = i.rect[2]
        nH = i.rect[3]
        i.image = pg.transform.scale(i.image, (nW, nH))
        i.job = "taskbarClose"
        i.rect.y -= 40*scale
        
        Taskbar.create(scale, (382, 492), uis, layers, modus)

    def taskbarClose(i, uis , layers, scale, modus):
        i.image = pg.image.load("GUI/icon/" + modus + "/ARROW.png").convert_alpha()
        nW = i.rect[2]
        nH = i.rect[3]
        i.image = pg.transform.scale(i.image, (nW, nH))
        i.job = "taskbarOpen"
        i.rect.y += 40*scale

        for j in uis:
            if j.job == "taskbar":
                for c in j.children:
                    uis.remove(c)
                    layers.remove(c)
                uis.remove(j)
                layers.remove(j)
    
    def editToggle(i, uis, editing, modus):
        i.image = pg.image.load("GUI/icon/" + modus + "/ALT_X.png").convert_alpha()
        i.job = "endEdit"
        for j in uis:
            if j.job == "cardCreate":
                j.image = pg.image.load("GUI/button/" + modus + "/SET.png").convert_alpha()
                j.job = "set"
        editing = True
        return editing

    def editEnd(i, uis, editing, modus):
        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)
        i.image = pg.image.load("GUI/icon/" + modus + "/EDIT.png").convert_alpha()
        i.job = "edit"
        for j in uis:
            if j.job == "set":
                j.image = pg.image.load("GUI/button/" + modus + "/ADD.png").convert_alpha()
                j.job = "cardCreate"
            iBox = ["name", "code", "tier"]
            for l in iBox:
                if j.job == l:
                    
                    j.text = ""
                    j.txt_surface = FONT.render(j.text, True, j.color)
        editing = False
        return editing

    def captaEdit(sprite, t1, t2, t3):
        t1.text = sprite.name
        t1.txt_surface = t1.fontBig.render(t1.text, True, t1.color)
        t2.text = sprite.captaCode
        t2.txt_surface = t2.fontBig.render(t2.text, True, t2.color)
        t3.text = sprite.tier
        t3.txt_surface = t3.fontBig.render(t3.text, True, t3.color)

        sprite.edited = True

    def clear(currentStack, layers, sprites):
        for s in sprites:
            layers.remove(s)
            sprites.remove(s)
        currentStack.clear()
        
        with open("data/list.txt", "w") as f:
            f.writelines("")

            