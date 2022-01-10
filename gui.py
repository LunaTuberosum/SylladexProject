import pygame as pg

import codeDatabase

import time

white = (255, 255, 255)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('black')
BLACK = pg.Color('black')

class UIBase(pg.sprite.Sprite):

    def __init__(self, pos, image, job, typeing, parent, scale, size, opt):
        super().__init__()

        self.image = pg.Surface(size)
        self.image.fill(white)
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
        self.parent = parent
        self.active = True
        self.children = []

        self.font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 15*scale)
        self.fontBig = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)
        

        if typeing == "button":
            self.checked = False

        elif typeing == "inputbox":
            self.color = BLACK
            self.text = opt[0]
            self.txt_surface = opt[1].render(opt[0], True, self.color)

        elif typeing == "panel":
            if job == "CardInspection":
                self.inspectie = None
            
    ### PANEL FUNCTIONS ###

    def settingPanel(uis, layers, scale):

        toBeRemoved = ["sylSettings", "cardCreate", "name", "code", "tier", "modus", "textLabel"]
        for i in uis:
            
            if i.job == "SylladexPanel":
                panel = i
                panel.job = "Options"
                
                # i.rect.w = nW
                # i.rect.h = nH

            for t in toBeRemoved:
                if i.job == t:
                    uis.remove(i)
                    layers.remove(i)
                    if i.job == "name" or i.job == "code" or i.job == "tier":
                        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
        panel.image = pg.image.load("GUI/panel/OPTIONSPANEL.png")
        nW = panel.rect[2]
        nH = panel.rect[3]
        panel.image = pg.transform.scale(panel.image, (nW, nH))

        entityText = panel.fontBig.render("SETTINGS", True, white)

        panel.image.blit(entityText, [136*scale, 0*scale])

        entityText = panel.fontBig.render("CREDITS", True, white)

        panel.image.blit(entityText, [135*scale, 366*scale])
        
        UIBase.createUI((1, 12), "GUI/icon/FLIP_ALT.png", "sylPanel", "button", None, scale, (16, 16), layers, uis, [])

        resImage = ["GUI/icon/960x540_SELECTED.png", "GUI/icon/1920x1080.png", "GUI/icon/960x540.png", "GUI/icon/1920x1080_SELECTED.png"]

        rX = 1
        rZ = 1
        for r in range(int(len(resImage)/2)):
            if scale == rX:

                UIBase.createUI((144, 48), resImage[rZ-1], "960x540", "button", None, scale, (72, 24), layers, uis, [])

                UIBase.createUI((144, 72), resImage[rZ], "1920x1080", "button", None, scale, (72, 24), layers, uis, [])
            rX += 1
            rZ+= 2

    def reinit(text, panel, scale):

        font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 15*scale)
        fontBig = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        def makeText(label, text, x, y, scale):

            z = 1
            for c in ["CUSTOM TRAIT 1", "CUSTOM TRAIT 2", "CUSTOM TRAIT 3" ,"CUSTOM TRAIT 4" ]:
                if c == text:
                    text = "CUSTOM " + str(z)
                    break
                else:
                    z += 1
            entityText = font.render(text, 1, BLACK)

            H = entityText.get_height()
            label.image.blit(entityText, [x*scale, y*scale - H/2])

        def makeImage(label, image, x, y, scale):

            n = 0

            for c in [text.wKind, text.grist, text.eff[0], text.eff[1], text.eff[2], text.eff[3], text.deff[0], text.deff[1], text.deff[2], text.deff[3], ""]:
                
                if image == c:

                    entityImage = pg.Surface((16, 16))
                    entityImage.fill(white)

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
                    entityImage.fill(white)
                    entityImage = pg.image.load(codeDatabase.action.get(image)).convert_alpha()
                    nW = 108*scale
                    nH = 24*scale
                    entityImage = pg.transform.scale(entityImage, (nW, nH))

                    label.image.blit(entityImage, [x*scale, y*scale])


        textRef = ["CODE", 40, 372, text.captaCode, 94, 372,"TIER",174, 372, str(text.tier), 216, 372, "GRIST TYPE", 24, 132 , text.grist, 123, 132, "NAME", 16, 48, text.name,  54, 48, "ITEMKIND" , 16 , 108 , text.wKind, 99, 108, text.trait1, 42, 84, text.trait2, 126, 84, text.wType, 231, 72, "EFFECTIVE", 24, 156, "INEFFECTIVE", 18, 180, "INSPECT INFORMATION", 78, 276, "CST", 14, 303, "DMG", 12, 333, "1", 214, 108, "2", 214, 132, "3", 214, 156, "BD", 210, 180, codeDatabase.damgeNum.get(int(text.tier)).get("1"), 244, 108, codeDatabase.damgeNum.get(int(text.tier)).get("2"), 244, 132, codeDatabase.damgeNum.get(int(text.tier)).get("3"), 244, 156, codeDatabase.damgeNum.get(int(text.tier)).get("BD"), 240, 181]        
        
        x = 0
        for z in range(int(len(textRef)/3)):

            makeText(panel, textRef[x], textRef[x+1], textRef[x+2], scale)
            x += 3

        entityText = fontBig.render("CAPTCHALOGUE CARD", 2, white)
        panel.image.blit(entityText, [12*scale, 0*scale])

        imageRef = [text.grist, 91, 116, text.eff[0], 91, 140, text.eff[1], 115, 140, text.eff[2], 139, 140, text.eff[3], 163, 140, text.deff[0], 91 ,164, text.deff[1], 115, 164, text.deff[2], 139, 164, text.deff[3], 163, 164, text.wKind, 67 ,92, text.action1, 36, 204, text.action2, 36, 228, text.action3, 168, 204, text.action4, 168, 228]

        x = 0
        for z in range(int(len(imageRef)/3)):
            makeImage(panel, imageRef[x], imageRef[x+1], imageRef[x+2], scale)
            x += 3

    def panel(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        
        entity = UIBase(pos, image.get(job), job, typeing, parent, scale, size, opt)
        layers.add(entity)
        layers.change_layer(entity, opt)
        uis.add(entity)

    def cardInsPanel(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        for i in uis:
            if i.job == "CardInspection":
                UIBase.destroy(i, uis, layers)

        entity = UIBase(pos, image.get(job), job , typeing, parent, scale, size, opt)
        uis.add(entity)
        layers.add(entity)
        layers.change_layer(entity, 998)

        entity.inspectie = opt

        UIBase.reinit(opt, entity, scale)

        buttonPos = [12, 72, "trait1", 96, 72, "trait2", 12, 204, "action1",  144, 204, "action2", 12, 228, "action3",  144, 228, "action4"]

        x = 0
        for b in range(6):
            UIBase.createUI((pos[0]+buttonPos[x],pos[1]+buttonPos[x+1]), "GUI/button/CHECK_BOX.png", "inspect"+buttonPos[x+2], "button", entity, scale, (16, 16), layers, uis, [])
            x += 3

        UIBase.createUI((pos[0]+276,pos[1]), "GUI/icon/ALT_X.png", "closePanel", "button", entity, scale, (16, 16), layers, uis, [])

    ### BUTTON FUNCTIONS ###

    def button(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        entity = UIBase(pos, image, job , typeing, parent, scale, size, opt)
        uis.add(entity)
        layers.add(entity)
        layers.change_layer(entity, 998)
        if job == "modus":
            entity.active == False
        if parent != None:
            parent.children.append(entity)

    def captaButton(capta, sprites, layers, text, name, stack, tier, scale, modus):
        
        capta.createC(scale, sprites, layers,text, name, stack, tier, modus)

    ### LABEL FUNCTIONS ###

    def label(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        
        entity = UIBase(pos, image, job, typeing, parent, scale, size, opt)
        layers.add(entity)
        layers.change_layer(entity, 1000)
        uis.add(entity)


    ### MAIN FUNCTIONS ###

    def createUI(pos, image, job, typeing, parent, scale, size, layers, uis, opt):

        uiRedirct = {
            "CardInspection": UIBase.cardInsPanel,
        }

        if typeing == "panel":
            uiRedirct.get(job, UIBase.panel)(pos, image, job, typeing, parent, scale, size, layers, uis, opt)
        elif typeing == "button":
            UIBase.button(pos, image, job, typeing, parent, scale, size, layers, uis, opt)
        elif typeing == "label":
            UIBase.label(pos, image, job, typeing, parent, scale, size, layers, uis, opt)

    def destroy(i, uis, layer):
        
        uis.remove(i)
        layer.remove(i)
        if len(i.children) >= 1:
            for s in i.children:
                uis.remove(s)
                layer.remove(s)

class InputBox(pg.sprite.Sprite):

    def __init__(self, scale, x, y, w, h, FONT, job, size='l', text=''):
        
        super().__init__()
        self.image = pg.Surface((128, 32))
        self.image.fill(white)
        if size == 's':
            self.image = pg.image.load("GUI/textbox/TEXTBOX_SMALL.png").convert_alpha()
            
        elif size == 'm':
            self.image = pg.image.load("GUI/textbox/TEXTBOX_MEDIUM.png").convert_alpha()
        else:
            
            self.image = pg.image.load("GUI/textbox/TEXTBOX.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))
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
        self.color = BLACK
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        
        self.type = "inputBox"
        self.job = job

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
            
class TextLabel(pg.sprite.Sprite):

    def __init__(self, scale, x, y, image, size):
        super().__init__()

        self.image = pg.Surface(size)
        self.image.fill(white)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=((x, y)))
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
        self.type = "textLabel"
        self.job = 'textLabel'
        

    def create(scale, x, y, image, size, gui, l):
        entity = TextLabel(scale, x, y, image, size)
        
        gui.add(entity)
        l.add(entity)
        l.change_layer(entity, 998)
    
class Taskbar(pg.sprite.Sprite):

    def __init__(self,scale, x, y, image):
        super().__init__()

        self.image = pg.Surface((390, 32))
        self.image.fill(white)
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=((x, y)))
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
        self.type = "taskbar"
        self.job = "taskbar"

    def create(scale, x, y, image, uis, layers):
        entity = Taskbar(scale, x, y, image)
        
        uis.add(entity)
        layers.add(entity)
        layers.change_layer(entity, 0)

        UIBase.createUI((425, 505), "GUI/icon/TRASH.png", "trash", "label", None, scale, (20, 28), layers, uis, [])

        UIBase.createUI((513, 505), "GUI/icon/TRASH_ALL.png", "clear", "button", None, scale, (20, 29), layers, uis, [])

        UIBase.createUI((616, 510), "GUI/icon/EDIT.png", "edit", "button", None, scale, (24, 24), layers, uis, [])

    def destroy(taskbar, uis, layers):
        uis.remove(taskbar)
        layers.remove(taskbar)

        jobs = ["trash", "clear", "edit"]

        for i in uis:
            for j in jobs:
                if i.job == j:
                    uis.remove(i)
                    layers.remove(i)

