import pygame as pg
import captchacards
from gui import UIBase, InputBox, TextLabel, Taskbar
import math, textwrap

BLACK= (0,0,0)
WHITE = (255, 255, 255)

class CheckButtons():

    def editToggle(i, uis, editing):
        if i.active == True:
            i.image = pg.image.load("GUI/icon/ALT_X.png").convert_alpha()
            i.job = "endEdit"
            for j in uis:
                if j.job == "cardCreate":
                    j.image = pg.image.load("GUI/button/STACK/SET.png").convert_alpha()
                    j.job = "set"
            editing = True
        return editing

    def editEnd(i, uis, editing):
        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)
        i.image = pg.image.load("GUI/icon/EDIT.png").convert_alpha()
        i.job = "edit"
        for j in uis:
            if j.job == "set":
                j.image = pg.image.load("GUI/button/STACK/ADD.png").convert_alpha()
                j.job = "cardCreate"
            iBox = ["name", "code", "tier"]
            for l in iBox:
                if j.job == l:
                    
                    j.text = ""
                    j.txt_surface = FONT.render(j.text, True, j.color)
        editing = False
        return editing

    def setEdit(sprites, uis, editing, stack, scale):
        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)
        for s in sprites:
            if s.edited == True:
                for i in uis:
                    if i.job == "name":
                        s.name = i.text
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                    elif i.job == "code":
                        s.captaCode = i.text
                        stack.pop(len(stack)-1)
                        stack.append(i.text)
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                        s.image = pg.image.load("GUI/cards/STACK/CAPTA.png").convert_alpha()
                        captchacards.CaptchaCards.kindIcon(s, scale, "d")
                    elif i.job == "tier":
                        s.tier = i.text
                        i.text = ""
                        i.txt_surface = FONT.render(i.text, True, i.color)
                    if i.job == "endEdit":
                        i.image = pg.image.load("GUI/icon/EDIT.png").convert_alpha()
                        i.job = "edit"
                    for j in uis:
                        if j.job == "set":
                            
                            j.image = pg.image.load("GUI/button/STACK/ADD.png").convert_alpha()
                            j.job = "cardCreate"
        editing = False
        return editing

    def toggleHelp(helpT, uis):
        
        if helpT == False:
            cursor =  pg.image.load("GUI/icon/MOUSE_HELP.png").convert_alpha()
            for i in uis:
                if i.job == "trash":
                    i.active = False
                elif i.job == "clear":
                    i.active = False
                elif i.job == "edit":
                    i.active = False
                elif i.job == "taskbarOpen" or i.job == "taskbarClose":
                    i.active = False
            helpT = True
        else:
            cursor =  pg.image.load("GUI/icon/MOUSE.png").convert_alpha()
            for i in uis:
                if i.job == "trash":
                    i.active = True
                elif i.job == "clear":
                    i.active = True
                elif i.job == "edit":
                    i.active = True
                elif i.job == "taskbarOpen" or i.job == "taskbarClose":
                    i.active = True
            helpT = False

        return helpT, cursor

    def cardCreate(i, groups, boxs):

        if not boxs[2].text.isdigit():
            i.image = pg.image.load("GUI/button/" + groups[5] + "/ADD_DOWN.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            return
        elif boxs[1].text == '' or boxs[0].text == '' or boxs[2].text == '':
            i.image = pg.image.load("GUI/button/" + groups[5] + "/ADD_DOWN.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            return
        elif not len(boxs[1].text) == 8:
            i.image = pg.image.load("GUI/button/" + groups[5] + "/ADD_DOWN.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            return
        else:

            i.image = pg.image.load("GUI/button/" + groups[5] + "/ADD_DOWN.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
        
            UIBase.captaButton(groups[0], groups[1], boxs[1].text, boxs[0].text, groups[2], int(boxs[2].text), groups[4], groups[5], groups[6])

            boxs[1].text = ''
            boxs[1].txt_surface = groups[3].render(boxs[1].text, True, boxs[1].color)
            boxs[1].active = False
            boxs[1].image = pg.image.load("GUI/textbox/TEXTBOX_MEDIUM.png").convert_alpha()
            nW = boxs[1].rect[2]
            nH = boxs[1].rect[3]
            boxs[1].image = pg.transform.scale(boxs[1].image, (nW, nH))
            boxs[0].text = ''
            boxs[0].txt_surface = groups[3].render(boxs[0].text, True, boxs[0].color)
            boxs[0].active = False
            boxs[0].image = pg.image.load("GUI/textbox/TEXTBOX.png").convert_alpha()
            nW = boxs[0].rect[2]
            nH = boxs[0].rect[3]
            boxs[0].image = pg.transform.scale(boxs[0].image, (nW, nH))
            boxs[2].text = ''
            boxs[2].txt_surface = groups[3].render(boxs[2].text, True, boxs[2].color)
            boxs[2].active = False
            boxs[2].image = pg.image.load("GUI/textbox/TEXTBOX_SMALL.png").convert_alpha()
            nW = boxs[2].rect[2]
            nH = boxs[2].rect[3]
            boxs[2].image = pg.transform.scale(boxs[2].image, (nW, nH))

    def closePanel(i, uis, layers):

        UIBase.destroy(i.parent, uis, layers)

    def settings(i, uis, c):
        UIBase.settingPanel(uis, c[0], c[1])    

    def clear(currentStack, c, sprites):
        if c[1].active == True:
            for s in sprites:
                c[0].remove(s)
                sprites.remove(s)
            currentStack.clear()
            
            with open("data/list.txt", "w") as f:
                f.writelines("")
    
    def taskbarOpen(i, uis, c):
        if i.active == True:
            i.image = pg.image.load("GUI/icon/ARROW_ACTIVE.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            i.job = "taskbarClose"
            i.rect.y -= 40*c[1]
            
            Taskbar.create(c[1], 382, 492, "GUI/panel/STACK/TASKBAR.png", uis, c[0])
    
    def taskbarClose(i, uis , c):
        if i.active == True:
            i.image = pg.image.load("GUI/icon/ARROW.png").convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
            i.job = "taskbarOpen"
            i.rect.y += 40*c[1]

            for j in uis:
                if j.job == "taskbar":
                    Taskbar.destroy(j, uis, c[0])

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
        
        if i.job == "modus":
            i.image = pg.image.load(mColor.get(m)[1]).convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
        elif uiChanger.get(i.job):
            i.image = pg.image.load(uiChanger.get(i.job, "")).convert_alpha()
            nW = i.rect[2]
            nH = i.rect[3]
            i.image = pg.transform.scale(i.image, (nW, nH))
        
        for sprite in sprites:
            sprite.image = pg.image.load("GUI/cards/" + m + "/CAPTA.png").convert_alpha()
            captchacards.CaptchaCards.kindIcon(sprite, scale, "d")
            nW = sprite.rect[2]
            nH = sprite.rect[3]
            sprite.image = pg.transform.scale(sprite.image, (nW, nH))

        if i.job == "CardInspection":
            UIBase.reinit(i.inspectie, i, scale)

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        sylladexText = FONT.render('SYLLADEX' , True , WHITE)
        modusText = FONT.render('fetch modus' , True , mColor.get(m)[0])
        modusName = FONT.render(m, True, mColor.get(m)[0])
        
        for i in uis:
            if i.job == "SylladexPanel":
                i.image.blit(sylladexText, [12*scale, 0*scale])
                i.image.blit(modusText, [12*scale, 366*scale])
                i.image.blit(modusName, [84*scale, 504*scale])
            
        return m

    def inspect(i, b, c):

        i.parent.image = pg.image.load("GUI/panel/STACK/PANEL.png").convert_alpha()
        nW = i.parent.rect[2]
        nH = i.parent.rect[3]
        i.parent.image = pg.transform.scale(i.parent.image, (nW, nH))
        UIBase.reinit(i.parent.inspectie, i.parent, c[3])
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

    def captaEdit(sprite, t1, t2, t3, FONT):
        t1.text = sprite.name
        t1.txt_surface = FONT.render(t1.text, True, t1.color)
        t2.text = sprite.captaCode
        t2.txt_surface = FONT.render(t2.text, True, t2.color)
        t3.text = sprite.tier
        t3.txt_surface = FONT.render(t3.text, True, t3.color)

        sprite.edited = True
    
    
class CheckTextboxes():

    def nameBox(box, color, image):
        box[1].active = False
        box[1].image = pg.image.load(image[1]).convert_alpha()
        nW = box[1].rect[2]
        nH = box[1].rect[3]
        box[1].image = pg.transform.scale(box[1].image, (nW, nH))
        box[2].active = False
        box[2].image = pg.image.load(image[2]).convert_alpha()
        nW = box[2].rect[2]
        nH = box[2].rect[3]
        box[2].image = pg.transform.scale(box[2].image, (nW, nH))

        box[0].active = not box[0].active
        box[0].color = color
        box[0].image = pg.image.load(image[0]).convert_alpha()
        nW = box[0].rect[2]
        nH = box[0].rect[3]
        box[0].image = pg.transform.scale(box[0].image, (nW, nH))
    
    def TabTextBoxes(boxs):
        images = ["GUI/textbox/TEXTBOX.png", "GUI/textbox/TEXTBOX_MEDIUM.png", "GUI/textbox/TEXTBOX_SMALL.png"]
        imagesActive = ["GUI/textbox/TEXTBOX_ACTIVE.png", "GUI/textbox/TEXTBOX_MEDIUM_ACTIVE.png", "GUI/textbox/TEXTBOX_SMALL_ACTIVE.png"]

        x = -1
        for b in boxs:
            if b.active == True:
                b.active = False
                b.image = pg.image.load(images[x-1]).convert_alpha()
                nW = b.rect[2]
                nH = b.rect[3]
                b.image = pg.transform.scale(b.image, (nW, nH))
                x += 1
                break
            
            x += 1

        if x == 2:
            boxs[0].active = True
            boxs[0].image = pg.image.load(imagesActive[0]).convert_alpha()
            nW = boxs[0].rect[2]
            nH = boxs[0].rect[3]
            boxs[0].image = pg.transform.scale(boxs[0].image, (nW, nH))
        else:
            boxs[x+1].active = True
            boxs[x+1].image = pg.image.load(imagesActive[x+1]).convert_alpha()
            nW = boxs[x+1].rect[2]
            nH = boxs[x+1].rect[3]
            boxs[x+1].image = pg.transform.scale(boxs[x+1].image, (nW, nH))
            

class MakingUI():

    def captaInputbox(scale, uis, layers, FONT, labImg, func, x, y, x1, y1, size="l"):
        TextLabel.create(scale, x, y, labImg, (64, 32), uis, layers)
        entity = InputBox(scale, x1, y1, 64, 32, FONT, func,size)
        uis.add(entity)
        layers.add(entity)
        layers.change_layer(entity, 999)
        return entity

    def sylladexMain(uis,uisImageDict, layers, modus, modusColor, scale):
        for i in uis:
            if i.job == "Options":
                i.job= "SylladexPanel"
                i.iamge = pg.image.load(uisImageDict.get(i.job)).convert_alpha()
            else:
                UIBase.createUI((0,0), uisImageDict, "SylladexPanel", "panel", None, scale, (252,540), layers, uis, 0)

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)

        sylladexText = FONT.render('SYLLADEX' , True , WHITE)
        modusText = FONT.render('fetch modus' , True , modusColor.get(modus)[0])
        modusName = FONT.render(modus, True, modusColor.get(modus)[0])
        
        for i in uis:
            if i.job == "SylladexPanel":
                i.image.blit(sylladexText, [12*scale, 0*scale])
                i.image.blit(modusText, [12*scale, 366*scale])
                i.image.blit(modusName, [84*scale, 504*scale])
        
        
        ## Create the main ui buttons
        UIBase.createUI((120, 260), "GUI/button/" + modus + "/ADD.png", "cardCreate", "button", None, scale, (68, 36), layers, uis, [])

        UIBase.createUI((215, 12), "GUI/icon/FLIP.png", "sylSettings", "button", None, scale, (27, 29), layers, uis, [])

        

        

        ## Making the capta input boxes
        input_box1 = MakingUI.captaInputbox(scale, uis, layers, FONT, "GUI/label/NAMELABEL.png", "name", 40, 60, 30, 98)

        input_box2 = MakingUI.captaInputbox(scale, uis, layers, FONT, "GUI/label/CODELABEL.png", 'code', 40, 142, 30, 180, 'm')

        input_box3 = MakingUI.captaInputbox(scale, uis, layers, FONT, "GUI/label/TIERLABEL.png", 'tier', 40, 224, 30, 262, 's')


        UIBase.createUI((12, 391), modusColor.get(modus)[1], "modus", "button", None, scale, (214, 113), layers, uis, [])

        for i in uis:

            if i.job == "sylPanel":
                uis.remove(i)
                layers.remove(i)
            elif i.job == "960x540":
                uis.remove(i)
                layers.remove(i)
            elif i.job == "1920x1080":
                uis.remove(i)
                layers.remove(i)

        return input_box1, input_box2, input_box3

    def changeRes(scale, uis, sprites):

        def scaler(group, scale):
            for l in group:
                nW = l.rect[2]*scale
                nH = l.rect[3]*scale
                nX = l.rect[0]*scale
                nY = l.rect[1]*scale
                l.rect.x = nX
                l.rect.y = nY
                l.image = pg.transform.scale(l.image, (nW, nH))
                l.rect.w = nW
                l.rect.h = nH
        
        reses = []
        
        if scale == 1:
            reses = ["960x540", "1920x1080"]
            screen = pg.display.set_mode((960, 540))
        elif scale == 2:
            reses = ["1920x1080", "960x540"]
            screen = pg.display.set_mode((1902, 1080))

        for i in uis:
            if i.job == reses[0]:
                i.image = pg.image.load("GUI/icon/"+reses[0]+"_SELECTED.png")
            elif i.job == reses[1]:
                i.image = pg.image.load("GUI/icon/"+reses[1]+".png")
        
        if scale == 1:
            scaleS = .5
        else:
            scaleS = scale
        scaler(uis, scaleS)
        scaler(sprites, scaleS)
        
        return screen, scale

    def placeInfo(rects, uis, layers, scale):
        info = ["An area to put info to create CAPTCHALOUGE CARDS.", "An area to input the name of the CAPTCHALOUGE CARD.", "An area to input an 8 digit code tha changes what the CAPTCHALOUGE CARD is.", "An area to input a number between 1 and 16 to decied the strength of the CAPTCHALOUGE CARD.", "A button that creates cards or changes what info is in a card when editing.", "A button that flips the main SYLLADEX card show the settings and flips it back.", "A button that opens a task bar to let you delete, clear, edit, and [WORK IN PROGRESS].","A button that would change you fetch moudes but this feture is currently disabled.", "In this area you can stack and move CAPTCHALOUGE CARDS.", "When a CAPTCHALOUGE CARD is brought over this symbol it will delete it.", "This button destroys all CAPTCHALOUGE CARDS on the screen.", "This button lets you edit the contents of a CAPTCHALOUGE CARD."]

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)

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
                            UIBase.destroy(i, uis, layers)
                    UIBase.createUI((x, y), "GUI/panel/LABEL.png", "infoUIs", "label", None, scale, (68, 36), layers, uis, [])
                    for i in uis:
                        if i.job == "infoUIs":
                            panel = i
                        
                    text = textwrap.wrap(info[z], 22)
                    k = 0
                    for g in range(len(text)):

                        entityText = FONT.render(text[g], 2, WHITE)
                        panel.image.blit(entityText, [6*scale, 6+k*scale])
                        k+= 24
                else:
                    for i in uis:
                        if i.job == "infoUIs":
                            UIBase.destroy(i, uis, layers)
                    return
            z += 1

    

