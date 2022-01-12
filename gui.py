import pygame as pg

import codeDatabase
import captchacards

import time

WHITE = (255, 255, 255)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('black')
BLACK = pg.Color('black')

class UIBase(pg.sprite.Sprite):

    def __init__(self, pos, image, job, typeing, scale, modus, size, activeI="", codeBox=""):
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

        self.font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 15*scale)
        self.fontBig = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        self.color = BLACK
        self.text = ""
        self.txt_surface = self.fontBig.render("", True, self.color)
        self.active = False
        self.activeImage = activeI
        self.inactiveImage = image
        self.codeBox = codeBox
        
        self.modus = modus

        self.checked = False

        self.inspectie = None

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
            "closePanel": "GUI/icon/" + i.modus + "/ALT_X.png",
            "taskbarClose": "GUI/icon/" + i.modus + "/ARROW_ACTIVE.png",
            "taskbar": "GUI/panel/" + i.modus + "/TASKBAR.png",
            "trash": "GUI/icon/" + i.modus + "/TRASH.png",
            "clear": "GUI/icon/" + i.modus + "/TRASH_ALL.png",
            "edit": "GUI/icon/" + i.modus + "/EDIT.png"
            
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

    def modusChange(i, mColor, m, scale, uis, sprites): 
        if m == "STACK":
            m = "QUEUE"
        elif m == "QUEUE":
            m = "STACK"

        uiChanger = {
            "SylladexPanel": "GUI/panel/" + m + "/SYLLADEXPANEL.png",
            "StackingArea": "GUI/panel/" + m + "/STACK_AREA.png",
            "CardInspection": "GUI/panel/" + m + "/PANEL.png"
        }

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
    
    def create(scale, modus, layers, uis, box, job, pos, active, codeBox):
        entity = StackingArea(pos, "GUI/textbox/"+modus+"/"+box+".png", job, "textbox", scale, modus, (0,0), active, codeBox)
        layers.add(entity)
        layers.change_layer(entity, -1)
        uis.add(entity)

        return entity

    def draw(box, screen):
        # Blit the text.
        screen.blit(box.txt_surface, (box.rect.x+5, box.rect.y))

    def nameBox(curBox, otherBox, color, codeBox):
        for b in otherBox:
            b.active = False
            b.image = pg.image.load(b.inactiveImage).convert_alpha()
            nW = b.rect[2]
            nH = b.rect[3]
            b.image = pg.transform.scale(b.image, (nW, nH))

        curBox.active = not curBox.active
        curBox.color = color
        curBox.image = pg.image.load("GUI/textbox/" + curBox.modus + "/" + curBox.activeImage + ".png").convert_alpha()
        nW = curBox.rect[2]
        nH = curBox.rect[3]
        return codeBox
        

#     ### PANEL FUNCTIONS ###

#     def settingPanel(uis, layers, scale, modus):

#         toBeRemoved = ["sylSettings", "cardCreate", "name", "code", "tier", "modus", "nameLabel", "codeLabel", "tierLabel",]
#         for i in uis:
            
#             if i.job == "SylladexPanel":
#                 panel = i
#                 panel.job = "Options"
                
#                 # i.rect.w = nW
#                 # i.rect.h = nH

#             for t in toBeRemoved:
#                 if i.job == t:
#                     uis.remove(i)
#                     layers.remove(i)
#                     if i.job == "name" or i.job == "code" or i.job == "tier":
#                         FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)
#                         i.text = ""
#                         i.txt_surface = FONT.render(i.text, True, i.color)
#         panel.image = pg.image.load("GUI/panel/OPTIONSPANEL.png")
#         nW = panel.rect[2]
#         nH = panel.rect[3]
#         panel.image = pg.transform.scale(panel.image, (nW, nH))

#         entityText = panel.fontBig.render("SETTINGS", True, white)

#         panel.image.blit(entityText, [136*scale, 0*scale])

#         entityText = panel.fontBig.render("CREDITS", True, white)

#         panel.image.blit(entityText, [135*scale, 366*scale])
        
#         UIBase.createUI((1, 12), "GUI/icon/" + modus + "/FLIP_ALT.png", "sylPanel", "button", None, scale, (16, 16), layers, uis, [])

#         resImage = ["GUI/icon/960x540_SELECTED.png", "GUI/icon/1920x1080.png", "GUI/icon/960x540.png", "GUI/icon/1920x1080_SELECTED.png"]

#         rX = 1
#         rZ = 1
#         for r in range(int(len(resImage)/2)):
#             if scale == rX:

#                 UIBase.createUI((144, 48), resImage[rZ-1], "960x540", "button", None, scale, (72, 24), layers, uis, [])

#                 UIBase.createUI((144, 72), resImage[rZ], "1920x1080", "button", None, scale, (72, 24), layers, uis, [])
#             rX += 1
#             rZ+= 2

#     def reinit(text, panel, scale):

#         font = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 15*scale)
#         fontBig = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

#         def makeText(label, text, x, y, scale):

#             z = 1
#             for c in ["CUSTOM TRAIT 1", "CUSTOM TRAIT 2", "CUSTOM TRAIT 3" ,"CUSTOM TRAIT 4" ]:
#                 if c == text:
#                     text = "CUSTOM " + str(z)
#                     break
#                 else:
#                     z += 1
#             entityText = font.render(text, 1, BLACK)

#             H = entityText.get_height()
#             label.image.blit(entityText, [x*scale, y*scale - H/2])

#         def makeImage(label, image, x, y, scale):

#             n = 0

#             for c in [text.wKind, text.grist, text.eff[0], text.eff[1], text.eff[2], text.eff[3], text.deff[0], text.deff[1], text.deff[2], text.deff[3], ""]:
                
#                 if image == c:

#                     entityImage = pg.Surface((16, 16))
#                     entityImage.fill(white)

#                     if image == text.wKind:
#                         inImage = codeDatabase.kind.get(image)
#                     else:
#                         inImage = codeDatabase.grist.get(image)

#                     entityImage = pg.image.load(inImage).convert_alpha()

#                     nW = 32*scale
#                     nH = 32*scale
#                     entityImage = pg.transform.scale(entityImage, (nW, nH))

#                     label.image.blit(entityImage, [x*scale, y*scale])
#                     break
#                 else:
#                     n += 1

#                 if n == 10:
#                     entityImage = pg.Surface((16, 16))
#                     entityImage.fill(white)
#                     entityImage = pg.image.load(codeDatabase.action.get(image)).convert_alpha()
#                     nW = 108*scale
#                     nH = 24*scale
#                     entityImage = pg.transform.scale(entityImage, (nW, nH))

#                     label.image.blit(entityImage, [x*scale, y*scale])


#         textRef = ["CODE", 40, 372, text.captaCode, 94, 372,"TIER",174, 372, str(text.tier), 216, 372, "GRIST TYPE", 24, 132 , text.grist, 123, 132, "NAME", 16, 48, text.name,  54, 48, "ITEMKIND" , 16 , 108 , text.wKind, 99, 108, text.trait1, 42, 84, text.trait2, 126, 84, text.wType, 231, 72, "EFFECTIVE", 24, 156, "INEFFECTIVE", 18, 180, "INSPECT INFORMATION", 78, 276, "CST", 14, 303, "DMG", 12, 333, "1", 214, 108, "2", 214, 132, "3", 214, 156, "BD", 210, 180, codeDatabase.damgeNum.get(int(text.tier)).get("1"), 244, 108, codeDatabase.damgeNum.get(int(text.tier)).get("2"), 244, 132, codeDatabase.damgeNum.get(int(text.tier)).get("3"), 244, 156, codeDatabase.damgeNum.get(int(text.tier)).get("BD"), 240, 181]        
        
#         x = 0
#         for z in range(int(len(textRef)/3)):

#             makeText(panel, textRef[x], textRef[x+1], textRef[x+2], scale)
#             x += 3

#         entityText = fontBig.render("CAPTCHALOGUE CARD", 2, white)
#         panel.image.blit(entityText, [12*scale, 0*scale])

#         imageRef = [text.grist, 91, 116, text.eff[0], 91, 140, text.eff[1], 115, 140, text.eff[2], 139, 140, text.eff[3], 163, 140, text.deff[0], 91 ,164, text.deff[1], 115, 164, text.deff[2], 139, 164, text.deff[3], 163, 164, text.wKind, 67 ,92, text.action1, 36, 204, text.action2, 36, 228, text.action3, 168, 204, text.action4, 168, 228]

#         x = 0
#         for z in range(int(len(imageRef)/3)):
#             makeImage(panel, imageRef[x], imageRef[x+1], imageRef[x+2], scale)
#             x += 3

#     def panel(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        
#         entity = UIBase(pos, image.get(job), job, typeing, parent, scale, size, opt)
#         layers.add(entity)
#         layers.change_layer(entity, opt)
#         uis.add(entity)

#     def cardInsPanel(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
#         for i in uis:
#             if i.job == "CardInspection":
#                 UIBase.destroy(i, uis, layers)
#         entity = UIBase(pos, image.get(job), job , typeing, parent, scale, size, opt[0])
#         uis.add(entity)
#         layers.add(entity)
#         layers.change_layer(entity, 998)

#         entity.inspectie = opt

#         UIBase.reinit(opt[0], entity, scale)

#         buttonPos = [12, 72, "trait1", 96, 72, "trait2", 12, 204, "action1",  144, 204, "action2", 12, 228, "action3",  144, 228, "action4"]

#         x = 0
#         for b in range(6):
#             UIBase.createUI((pos[0]+buttonPos[x],pos[1]+buttonPos[x+1]), "GUI/button/CHECK_BOX.png", "inspect"+buttonPos[x+2], "button", entity, scale, (16, 16), layers, uis, [])
#             x += 3

#         UIBase.createUI((pos[0]+288,pos[1]+24), "GUI/icon/" + opt[1] + "/ALT_X.png", "closePanel", "button", entity, scale, (16, 16), layers, uis, [])

#     ### BUTTON FUNCTIONS ###

#     def button(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
#         entity = UIBase(pos, image, job , typeing, parent, scale, size, opt)
#         uis.add(entity)
#         layers.add(entity)
#         layers.change_layer(entity, 998)
#         if parent != None:
#             parent.children.append(entity)

#     def captaButton(sprites, layers, text, name, stack, tier, scale, modus, cardIDs):

#         if modus == "STACK":
#             captchacards.CaptchaCards.createCard(scale, sprites, layers,text, name, stack, tier, cardIDs)
#         elif modus == "QUEUE":
#             captchacards.QueueCards.createCard(scale, sprites, layers,text, name, stack, tier, cardIDs)
            

#     ### LABEL FUNCTIONS ###

#     def label(pos, image, job, typeing, parent, scale, size, layers, uis, opt):
        
#         entity = UIBase(pos, image, job, typeing, parent, scale, size, opt)
#         layers.add(entity)
#         layers.change_layer(entity, 1000)
#         uis.add(entity)


#     ### MAIN FUNCTIONS ###

#     def createUI(pos, image, job, typeing, parent, scale, size, layers, uis, opt):

#         uiRedirct = {
#             "CardInspection": UIBase.cardInsPanel,
#         }

#         if typeing == "panel":
#             uiRedirct.get(job, UIBase.panel)(pos, image, job, typeing, parent, scale, size, layers, uis, opt)
#         elif typeing == "button":
#             UIBase.button(pos, image, job, typeing, parent, scale, size, layers, uis, opt)
#         elif typeing == "label":
#             UIBase.label(pos, image, job, typeing, parent, scale, size, layers, uis, opt)

#     def destroy(i, uis, layer):
        
#         uis.remove(i)
#         layer.remove(i)
#         if len(i.children) >= 1:
#             for s in i.children:
#                 uis.remove(s)
#                 layer.remove(s)

# class InputBox(pg.sprite.Sprite):

#     def __init__(self, scale, x, y, w, h, FONT, job, modus, size='l', text=''):
        
#         super().__init__()
#         self.image = pg.Surface((128, 32))
#         self.image.fill(white)
#         if size == 's':
#             self.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_SMALL.png").convert_alpha()
            
#         elif size == 'm':
#             self.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_MEDIUM.png").convert_alpha()
#         else:
            
#             self.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX.png").convert_alpha()
#         self.rect = self.image.get_rect(topleft=(x,y))
#         if scale == 1:
#             pass
#         else:
#             nW = self.rect[2]*scale
#             nH = self.rect[3]*scale
#             nX = self.rect[0]*scale
#             nY = self.rect[1]*scale
#             self.rect.x = nX
#             self.rect.y = nY
#             self.image = pg.transform.scale(self.image, (nW, nH))
#             self.rect.w = nW
#             self.rect.h = nH
#         self.color = BLACK
#         self.text = text
#         self.txt_surface = FONT.render(text, True, self.color)
#         self.active = False
        
#         self.type = "inputBox"
#         self.job = job


            
# class TextLabel(pg.sprite.Sprite):

#     def __init__(self, scale, x, y, image, size, job):
#         super().__init__()

#         self.image = pg.Surface(size)
#         self.image.fill(white)
#         self.image = pg.image.load(image).convert_alpha()
#         self.rect = self.image.get_rect(topleft=((x, y)))
#         if scale == 1:
#             pass
#         else:
#             nW = self.rect[2]*scale
#             nH = self.rect[3]*scale
#             nX = self.rect[0]*scale
#             nY = self.rect[1]*scale
#             self.rect.x = nX
#             self.rect.y = nY
#             self.image = pg.transform.scale(self.image, (nW, nH))
#             self.rect.w = nW
#             self.rect.h = nH
#         self.type = "textLabel"
#         self.job = job
        

#     def create(scale, x, y, image, size, gui, l, job):
#         entity = TextLabel(scale, x, y, image, size, job)
        
#         gui.add(entity)
#         l.add(entity)
#         l.change_layer(entity, 998)
    
# class Taskbar(pg.sprite.Sprite):

#     def __init__(self,scale, x, y, image):
#         super().__init__()

#         self.image = pg.Surface((390, 32))
#         self.image.fill(white)
#         self.image = pg.image.load(image).convert_alpha()
#         self.rect = self.image.get_rect(topleft=((x, y)))
#         if scale == 1:
#             pass
#         else:
#             nW = self.rect[2]*scale
#             nH = self.rect[3]*scale
#             nX = self.rect[0]*scale
#             nY = self.rect[1]*scale
#             self.rect.x = nX
#             self.rect.y = nY
#             self.image = pg.transform.scale(self.image, (nW, nH))
#             self.rect.w = nW
#             self.rect.h = nH
#         self.type = "taskbar"
#         self.job = "taskbar"

#     def create(scale, x, y, image, uis, layers, modus):
#         entity = Taskbar(scale, x, y, image,)
        
#         uis.add(entity)
#         layers.add(entity)
#         layers.change_layer(entity, 0)

#         UIBase.createUI((425, 505), "GUI/icon/" + modus + "/TRASH.png", "trash", "label", None, scale, (20, 28), layers, uis, [])

#         UIBase.createUI((513, 505), "GUI/icon/" + modus + "/TRASH_ALL.png", "clear", "button", None, scale, (20, 29), layers, uis, [])

#         UIBase.createUI((616, 510), "GUI/icon/" + modus + "/EDIT.png", "edit", "button", None, scale, (24, 24), layers, uis, [])

#     def destroy(taskbar, uis, layers):
#         uis.remove(taskbar)
#         layers.remove(taskbar)

#         jobs = ["trash", "clear", "edit"]

#         for i in uis:
#             for j in jobs:
#                 if i.job == j:
#                     uis.remove(i)
#                     layers.remove(i)

