import pygame as pg
from pygame.locals import *
import captchacards
from gui import UIBase, InputBox, TextLabel
import sys
from functions import CheckButtons, CheckTextboxes, MakingUI
import codeDatabase

## Colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
GRAY = (95, 99, 105)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
PINK = (255, 0, 220)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('black')

stackColor = (255, 0, 220)
queueColor = (255, 96, 0)

## Initalizations
pg.init()

pg.key.set_repeat(500, 200)

screen = pg.display.set_mode((960, 540))


pg.mouse.set_visible(False)

clock = pg.time.Clock()
sprites = pg.sprite.Group()   
outlines = pg.sprite.GroupSingle()
layers = pg.sprite.LayeredUpdates()
uis = pg.sprite.Group()
avalible_sprites = pg.sprite.Group()

pg.display.set_caption('SYLLADEX ALPHA 0.1')

image = pg.image.load("MAINSCREEN/ICON.png").convert_alpha()
pg.display.set_icon(image)

## Main loop
def main():
    
    mouseCursor =  pg.image.load("GUI/icon/MOUSE.png").convert_alpha()

    with open("data/var.txt", "r") as f:
        x = f.readlines()
        lines = x[0].split()
        modus = lines[0]
        scale = int(lines[1])
    modusD = modus
    scaleD = scale
    

    modusColor = {
        "STACK": [stackColor, "GUI/panel/STACK/MODUSLABEL.png"],
        "QUEUE": [queueColor, "GUI/panel/QUEUE/MODUSLABEL.png"]
    }

    uisImageDict = {
        "SylladexPanel": "GUI/panel/" + modus + "/SYLLADEXPANEL.png",
        "StackingArea": "GUI/panel/" + modus + "/STACK_AREA.png",
        "CardInspection": "GUI/panel/" + modus + "/PANEL.png",

        "closePanel": "GUI/icon/" + modus + "/ALT_X.png",
        "taskbarOpen": "GUI/icon/" + modus + "/ARROW.png"
        }   


    ## Making stack and starting arrays
    currentStack = []
    nameStart = []
    tierStart = []

    ## Making code input panel

    UIBase.createUI((252,0), uisImageDict, "StackingArea", "panel", None, scale, (708,540), layers, uis, -1)

    for i in uis:
        if i.job == "StackingArea":
            area = i.rect

    UIBase.createUI((925, 20), "GUI/icon/" + modus + "/HELP.png", "help", "button", None, scale, (32, 32), layers, uis, [])
    
    input_box1, input_box2, input_box3 = MakingUI.sylladexMain(uis,uisImageDict, layers, modus, modusColor, scale)

    UIBase.createUI((565, 503), uisImageDict.get("taskbarOpen"), "taskbarOpen", "button", None, scale, (25, 24), layers, uis, [])
    

    codeBox = ""

    ## Defining import variables
    moveCard = False 
    selected = None

    editing = False
    helpT = False

    bool1 = False

    cardIDs = []

    screenNew = pg.display.set_mode((960*scale, 540*scale))
    
    info = pg.Rect(0, 0, 0, 0)
    

    ### Recreate previous stack

    ## Open stack file
    with open("data/list.txt", "r") as f:

        count = 0
        startingStackCodes = []

        ## Search through and splt based on " "
        for x in f:

            y = x.split()

            ## Add the capta code to stack variable
            startingStackCodes.append(y[1])
            currentStack.append(count)
            count+=1

            ## Adds name to a temp array
            name = y[2]

            ## If name has a space in it
            if len(y) > 3:

                ## Added all extra parts of the name
                for j in range(len(y)-3):

                    name += (" " + y[j+3])

            ## Adds name and tier to start up arrays
            nameStart.append(name)
            tierStart.append(y[0])

    ## if the stack variable is long enough make new stack
    if len(currentStack) >= 1:

        ## temp variables
        z = 0
        a = 50
        parent = None

        ## Checks all codes in stack
        for v in startingStackCodes:

            ## Makes cards based of capta codes from file
            entity = captchacards.CaptchaCards((300, a), WHITE, v, nameStart[z], tierStart[z], scale, modus, cardIDs)
            sprites.add(entity)
            layers.add(entity)
            captchacards.CaptchaCards.kindIcon(entity, scale, "d")

            ## If stack is 2 or longer make parents and children
            if z >= 1:

                entity.parent = parent
                parent.child = entity

            parent = entity

            ## Make them stack proprly
            layers.change_layer(entity, z)
            z += 1

            a += 48

    ## Programs start
    while True:

        ## Making the Card area
        syl_cus = pg.Rect(0, 0, 252, 353)
        nam_txt = pg.Rect(30, 98, 160, 32)
        cod_txt = pg.Rect(30, 180, 110, 32)
        tir_txt = pg.Rect(30, 262, 80, 32)
        add_set = pg.Rect(120, 260, 68, 36)
        for i in uis:
            if i.job == "SylladexPanel":
                flp_syl = pg.Rect(215, 12, 27, 29)
            elif i.job == "Options": 
                flp_syl = pg.Rect(1, 12, 27, 29)
            if i.job == "taskbarOpen":
                tsk_bar = pg.Rect(565, 503, 25, 24)
            elif i.job == "taskbarClose":
                tsk_bar = pg.Rect(565, 463, 25, 24)
        mod_res = pg.Rect(0, 365, 252, 175)

        stk_ara = pg.Rect(252, 0, 708, 540)
        
        tsh_but = pg.Rect(425, 505, 20, 28)
        clr_but = pg.Rect(513, 505, 20, 29)
        edt_but = pg.Rect(616, 510, 24, 24)
        hlp_but = pg.Rect(925, 20, 32, 32)

        infoRects = [syl_cus, nam_txt, cod_txt, tir_txt, add_set, flp_syl, tsk_bar, mod_res, stk_ara, tsh_but, clr_but, edt_but, hlp_but]

        
        

        screen = screenNew

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24*scale)
        
        uisImageDict = {
            "SylladexPanel": "GUI/panel/" + modus + "/SYLLADEXPANEL.png",
            "StackingArea": "GUI/panel/" + modus + "/STACK_AREA.png",
            "CardInspection": "GUI/panel/" + modus + "/PANEL.png",

            "closePanel": "GUI/icon/" + modus + "/ALT_X.png",
            "taskbarOpen": "GUI/icon/" + modus + "/ARROW.png"
        }   

        ## Checking for inputs
        for event in pg.event.get():

            ## Quitting software
            if event.type == pg.QUIT:
                return

            ## Checking if mouse is used
            elif event.type == pg.MOUSEBUTTONDOWN:

                ## Checking if its left mouse button
                if event.button == 1:

                    if helpT == True:
                        
                        MakingUI.placeInfo(infoRects,uis, layers, scale)

                    input_box1.active = False
                    input_box1.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX.png").convert_alpha()
                    nW = input_box1.rect[2]
                    nH = input_box1.rect[3]
                    input_box1.image = pg.transform.scale(input_box1.image, (nW, nH))

                    input_box2.active = False
                    input_box2.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_MEDIUM.png").convert_alpha()
                    nW = input_box2.rect[2]
                    nH = input_box2.rect[3]
                    input_box2.image = pg.transform.scale(input_box2.image, (nW, nH))

                    input_box3.active = False
                    input_box3.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_SMALL.png").convert_alpha()
                    nW = input_box3.rect[2]
                    nH = input_box3.rect[3]
                    input_box3.image = pg.transform.scale(input_box3.image, (nW, nH))


                    ## Checking which ui element is being pressed
                    for i in uis:

                        if i.rect.collidepoint(event.pos):

                            ## Makes switch case to exacute uis funcs
                            uiElements = {

                                ## Buttons

                                "cardCreate": {
                                    1 : CheckButtons.cardCreate,
                                    2 : [i, [sprites,layers, currentStack, FONT, scale, modus, cardIDs], [input_box1, input_box2, input_box3]]
                                    },
                            
                                "closePanel": {
                                    1: CheckButtons.closePanel, 
                                    2 : [i, uis, layers]
                                    },

                                "sylSettings": {
                                    1: CheckButtons.settings,
                                    2 : [i, uis, [layers, scale, modus]]
                                    },
                                    
                                "clear": {
                                    1: CheckButtons.clear,
                                    2: [currentStack, [layers, i], sprites]
                                },

                                "taskbarOpen": {
                                    1: CheckButtons.taskbarOpen,
                                    2: [i, uis, [layers, scale, modus]]
                                },

                                "taskbarClose": {
                                    1: CheckButtons.taskbarClose,
                                    2: [i, uis, [layers, scale, modus]]
                                },

                                "edit": {
                                    1: CheckButtons.editToggle,
                                    2: [i, uis, editing]
                                },

                                "endEdit": {
                                    1: CheckButtons.editEnd,
                                    2: [i, uis, editing]
                                },

                                "set": {
                                    1: CheckButtons.setEdit,
                                    2: [sprites, uis, editing, currentStack, scale]
                                },

                                "help": {
                                    1: CheckButtons.toggleHelp,
                                    2: [helpT, uis]
                                },

                                "modus": {
                                    1: CheckButtons.modusChange,
                                    2: [uis, modusColor, modus]
                                },

                                "inspecttrait1": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.trait1Desc, [0, uis, layers, scale, modus]]
                                },

                                "inspecttrait2": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.trait2Desc, [1, uis, layers, scale, modus]]
                                },

                                "inspectaction1": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.actionData, [2, uis, layers, scale, modus]]
                                },

                                "inspectaction2": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.actionData, [3, uis, layers, scale, modus]]
                                },

                                "inspectaction3": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.actionData, [4, uis, layers, scale, modus]]
                                },
                                

                                "inspectaction4": {
                                    1: CheckButtons.inspect,
                                    2: [i, codeDatabase.actionData, [5, uis, layers, scale, modus]]
                                },

                                "sylPanel": {
                                    1: MakingUI.sylladexMain,
                                    2: [uis,uisImageDict, layers, modus, modusColor]
                                },

                                "960x540": {
                                    1: MakingUI.changeRes,
                                    2: [1, uis, sprites]
                                },

                                "1920x1080": {
                                    1: MakingUI.changeRes,
                                    2: [2, uis, sprites]
                                },
                                
                                ## Textboxes

                                "name": {
                                    1: CheckTextboxes.nameBox,
                                    2: [[input_box1, input_box2, input_box3], BLACK, ["GUI/textbox/" + modus + "/TEXTBOX_ACTIVE.png", "GUI/textbox/" + modus + "/TEXTBOX_MEDIUM.png", "GUI/textbox/" + modus + "/TEXTBOX_SMALL.png"]],
                                    3: "box1"
                                },

                                "code": {
                                    1: CheckTextboxes.nameBox,
                                    2: [[input_box2, input_box1, input_box3], BLACK, ["GUI/textbox/" + modus + "/TEXTBOX_MEDIUM_ACTIVE.png", "GUI/textbox/" + modus + "/TEXTBOX.png", "GUI/textbox/" + modus + "/TEXTBOX_SMALL.png"]],
                                    3: "box2"
                                },

                                "tier": {
                                    1: CheckTextboxes.nameBox,
                                    2: [[input_box3, input_box2, input_box1], BLACK, ["GUI/textbox/" + modus + "/TEXTBOX_SMALL_ACTIVE.png","GUI/textbox/" + modus + "/TEXTBOX_MEDIUM.png", "GUI/textbox/" + modus + "/TEXTBOX.png"]],
                                    3: "box3"
                                }
                            }

                            ## If its a button
                            if i.job == 'modus':
                                ## Finds the variable to parse thro
                                atrabuites = uiElements.get(i.job).get(2)

                                ## Calls the func
                                for j in uis:
                                    modus = uiElements.get(i.job).get(1)(j,atrabuites[1],atrabuites[2], scale,uis, sprites)

                            elif i.job == "help":

                                atrabuites = uiElements.get(i.job).get(2)

                                helpT, mouseCursor = uiElements.get(i.job).get(1)(atrabuites[0], atrabuites[1], modus)

                            elif i.job == "edit" or i.job == "endEdit":

                                atrabuites = uiElements.get(i.job).get(2)

                                editing = uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1], atrabuites[2])
                            
                            elif i.job == "set":

                                atrabuites = uiElements.get(i.job).get(2)

                                editing = uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1], atrabuites[2], atrabuites[3],  atrabuites[4])

                            elif i.job == "960x540" or i.job == "1920x1080":

                                atrabuites = uiElements.get(i.job).get(2)

                                screenNew, scale = uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1], atrabuites[2])

                            elif i.job == "sylPanel":

                                atrabuites = uiElements.get(i.job).get(2)

                                input_box1.text = ""
                                input_box2.text = "" 
                                input_box3.tex = ""

                                input_box1, input_box2, input_box3 = uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1],atrabuites[2],atrabuites[3],atrabuites[4], scale)

                            elif i.type == 'button':

                                ## Finds the variable to parse thro
                                atrabuites = uiElements.get(i.job).get(2)

                                ## Calls the func
                                uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1],atrabuites[2])

                            ## If its a textbox
                            elif i.type == 'inputBox':

                                ## Finds the variable to parse thro
                                atrabuites = uiElements.get(i.job).get(2)

                                ## Calls the func
                                uiElements.get(i.job).get(1)(atrabuites[0],atrabuites[1],atrabuites[2])

                                ## Assigns which level of codebox
                                codeBox = uiElements.get(i.job).get(3)
                
                                
                    ## Checking which card is being touched
                    for sprite in sprites:
                        
                        if sprite.rect.collidepoint(event.pos):

                            bool1 = True
                            
                            ## Defining which sprite it is
                            selected = sprite

                            if editing == True:
                                CheckButtons.captaEdit(selected, input_box1, input_box2, input_box3, FONT)

                                
                            
                            else:

                                ### Checking how to move sprite
                                
                                ## If the sprite has no parent
                                if selected.parent == None:

                                    ## if it still has a child
                                    if selected.child != None:

                                        ## Changes the sprite to be up
                                        sprite.image = pg.image.load("GUI/cards/" + modus + "/CAPTA_UP.png").convert_alpha()
                                        captchacards.CaptchaCards.kindIcon(sprite, scale, "u")
                                        nW = sprite.rect[2]
                                        nH = sprite.rect[3]
                                        sprite.image = pg.transform.scale(sprite.image, (nW, nH))

                                        ## Temp var
                                        x = 1


                                        ## Can move the card now
                                        moveCard = True

                                        ## Checks all sprites for children
                                        for sprite in sprites:

                                            for s in sprites:

                                                if sprite.child == s:

                                                    ## Sets every child in assending order in the stack
                                                    x += 1
                                                    s.image = pg.image.load("GUI/cards/" + modus + "/CAPTA_UP.png").convert_alpha()
                                                    captchacards.CaptchaCards.kindIcon(s, scale, "u")
                                                    nW = s.rect[2]
                                                    nH = s.rect[3]
                                                    s.image = pg.transform.scale(s.image, (nW, nH))

                                    ## If the sprite is by its self
                                    else:

                                        ## Picks up image and places it above all
                                        sprite.image = pg.image.load("GUI/cards/" + modus + "/CAPTA_UP.png").convert_alpha()
                                        captchacards.CaptchaCards.kindIcon(sprite, scale, "u")
                                        nW = sprite.rect[2]
                                        nH = sprite.rect[3]
                                        sprite.image = pg.transform.scale(sprite.image, (nW, nH))
                                        layers.change_layer(sprite, len(currentStack)+1)

                                        ## Can move card
                                        moveCard = True
                                   
                ## If middle click
                elif event.button == 2:

                    ## Checks which sprite is be
                    for s in sprites:
                        if s.rect.collidepoint(pg.mouse.get_pos()):
                            captchacards.CaptchaCards.checkCode(s)
                            UIBase.createUI((648,42), uisImageDict, "CardInspection", "panel", None, scale, (312,420), layers, uis, [s, modus])

                            # Panel.create(scale, uis, (612, 42), (360, 540), uisImageDict, None, layers, "CardInspection", s)     

                ## Checking if its right button
                elif event.button == 3:

                    ## Checking which card is being pressed
                    for sprite in sprites:
                        
                        if sprite.rect.collidepoint(event.pos):
                            selectedd = sprite
                            
                            if modus == "STACK":
                                ## Cheaking if the card has no child but has a parent
                                if selectedd.parent != None and selectedd.child == None:

                                    ## If it is the top on the stack
                                    if layers.get_layer_of_sprite(selectedd) == len(currentStack)-1:

                                        ## Be able to move the card
                                        moveCard = True

                                        ## Disconnect it
                                        captchacards.CaptchaCards.disconnect(selectedd,selectedd.parent,currentStack, sprites)
                                        
                                    else:

                                        ## Sets selected to none
                                        selected = None
                            elif modus == "QUEUE":
                                ## Cheaking if the card has no child but has a parent
                                if selectedd.parent == None and selectedd.child != None:

                                    ## If it is the top on the stack
                                    if layers.get_layer_of_sprite(selectedd) == 0:

                                        ## Be able to move the card
                                        moveCard = True

                                        ## Disconnect it
                                        captchacards.QueueCards.disconnect(selectedd,selectedd.child,currentStack, sprites)

                                        
                                    else:

                                        ## Sets selected to none
                                        selected = None
                                
                            
            ## Checking if the mouse buttons is up
            elif event.type == pg.MOUSEBUTTONUP:

                if bool1 == True:
                    for c in sprites:

                        c.image = pg.image.load("GUI/cards/" + modus +"/CAPTA.png").convert_alpha()
                        captchacards.CaptchaCards.kindIcon(c, scale, "d")
                        nW = c.rect[2]
                        nH = c.rect[3]
                        c.image = pg.transform.scale(c.image, (nW, nH))
                        

                        if c.parent == None and c.child == None:

                            layers.change_layer(c, 0)
                    bool1 = False                     
                
                moveCard = False

                ## Set the add button to netural
                for i in uis:

                    if i.job == 'cardCreate':

                        i.image = pg.image.load("GUI/button/"+ modus +"/ADD.png").convert_alpha()
                        nW = i.rect[2]
                        nH = i.rect[3]
                        i.image = pg.transform.scale(i.image, (nW, nH))
                        

                ## Checks all sprites
                for sprite in sprites:

                    if sprite.rect.collidepoint(pg.mouse.get_pos()):

                        selectedM = sprite
                        ## If the outline is touching selected
                        for out in outlines:
                            
                            
                            if selectedM.rect.colliderect(out) and selectedM.rect.colliderect(area): 
                                
                                captchacards.CaptchaCards.combine(selectedM, out.parent, out, currentStack, layers, sprites)
                                layers.change_layer(selectedM, len(currentStack))
                                outlines.empty()

                            else:
                                outlines.empty()

                    ## Destroys card if its touching Trash
                    captchacards.CaptchaCards.destroy(sprite, uis, layers, sprites)

                ## Reseting the cards sprites
                

            ## Checking if the mouse is moved
            elif event.type == pg.MOUSEMOTION:                

                for i in uis:
                    if i.job == "codePanel":
                        captchacards.CaptchaCards.cardBorder(i, sprites, event.rel)

                ## Checking and moving a sprite
                if selected:

                    ## If card can be moved
                    if moveCard == True:

                        ## Move card based on mouse
                        selected.move(event.rel, currentStack, area, scale, modus, layers, sprites)
                        
                        ## Makes a list of all sprites that can have an outline
                        avalible_sprites.empty()

                        for s in sprites:

                            ## If it has no children add it
                            if s.child == None:

                                avalible_sprites.add(s)

                        ## If the list is longer than one make outline
                        if avalible_sprites.__len__() >= 1 and selected.child == None and selected.parent == None:

                            
                            outlines.add(captchacards.CaptchaCards.distance(selected, avalible_sprites, currentStack, scale))
                    
                       
            ## Checking if keys are being pressed
            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    menu()

                ## Checking if the input boxs are active                
                if input_box1.active or input_box2.active or input_box3.active:

                    ## Checking when you press enter(return)
                    if event.key == pg.K_RETURN:

                        ## If codeBox is box1 then deactivate the name box
                        if codeBox == "box1":

                            ## Sets input box 1 inactive and resets code box
                            input_box1.active = False
                            input_box1.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX.png").convert_alpha()
                            nW = input_box1.rect[2]
                            nH = input_box1.rect[3]
                            input_box1.image = pg.transform.scale(input_box1.image, (nW, nH))
                            codeBox = ""

                        ## If codeBox is box2 then deactivate the code box
                        elif codeBox == "box2":

                            ## Sets input box 2 inactive and resets code box
                            input_box2.active = False
                            input_box2.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_MEDIUM.png").convert_alpha()
                            nW = input_box2.rect[2]
                            nH = input_box2.rect[3]
                            input_box2.image = pg.transform.scale(input_box2.image, (nW, nH))
                            codeBox = ""

                        ## If codeBox is box3 then deactivate the tier box
                        elif codeBox == "box3":

                            ## Sets input box 3 inactive and resets code box
                            input_box3.active = False
                            input_box3.image = pg.image.load("GUI/textbox/" + modus + "/TEXTBOX_SMALL.png").convert_alpha()
                            nW = input_box3.rect[2]
                            nH = input_box3.rect[3]
                            input_box3.image = pg.transform.scale(input_box3.image, (nW, nH))
                            codeBox = ""
                        
                    ## Checking if the backspace is being pressed
                    if event.key == pg.K_BACKSPACE:

                        ## Checking if box1 and deletes text
                        if codeBox == "box1":

                            input_box1.text = input_box1.text[:-1]

                        ## Checking if box2 and deletes text
                        elif codeBox == "box2":

                            input_box2.text = input_box2.text[:-1]

                        ## Checking if box3 and deletes text
                        elif codeBox == "box3":

                            input_box3.text = input_box3.text[:-1]

                    ## When any key but backspace is being pressed add text
                    else:

                        ## Checking if box1 and adds text
                        if codeBox == "box1":

                            if event.key != pg.K_RETURN:

                                input_box1.text += event.unicode

                        ## Checking if box2 and adds text
                        elif codeBox == "box2":

                            if event.key != pg.K_RETURN:

                                input_box2.text += event.unicode

                        ## Checking if box3 and deletes text
                        elif codeBox == "box3":

                            if event.key != pg.K_RETURN:

                                input_box3.text += event.unicode
                            
                    ## If box 1 has more than 12 letters delete it
                    if len(input_box1.text) >= 13:

                        input_box1.text = input_box1.text[:-1]

                    ## If box 2 has more than 9 letters delete it
                    if len(input_box2.text) >= 9:

                        input_box2.text = input_box2.text[:-1]

                    ## If box 3 has more than 3 letters delete it
                    if len(str(input_box3.text)) >= 3:

                        input_box3.text = input_box3.text[:-1]

                    ## Renders the text surfaces
                    input_box1.txt_surface = FONT.render(input_box1.text, True, input_box1.color)
                    input_box2.txt_surface = FONT.render(input_box2.text, True, input_box2.color)
                    input_box3.txt_surface = FONT.render(input_box3.text, True, input_box3.color)

        ## Buch of updating stuff
        sprites.update()
        screen.fill((102, 102, 102))

        if helpT == True:
            pg.draw.rect(screen, GRAY, info, 0)
            for i in uis:
                
                if i.job == "SylladexPanel":
                    pg.draw.rect(screen, queueColor, nam_txt, 2)
                    pg.draw.rect(screen, queueColor, cod_txt, 2)
                    pg.draw.rect(screen, queueColor, tir_txt, 2)
                    pg.draw.rect(screen, queueColor, add_set, 2)

                if i.job == "taskbarClose":
                    pg.draw.rect(screen, queueColor, tsh_but, 2)
                    pg.draw.rect(screen, queueColor, clr_but, 2)
                    pg.draw.rect(screen, queueColor, edt_but, 2)

            pg.draw.rect(screen, queueColor, syl_cus, 2)

            pg.draw.rect(screen, queueColor, flp_syl, 2)

            pg.draw.rect(screen, queueColor, mod_res, 2)

            pg.draw.rect(screen, queueColor, stk_ara, 2)

            pg.draw.rect(screen, queueColor, tsk_bar, 2)

            pg.draw.rect(screen, queueColor, hlp_but, 2)       
        
        uis.draw(screen)
        sprites.draw(screen)
        layers.draw(screen)
        outlines.draw(screen)
        input_box1.draw(screen)
        input_box2.draw(screen)
        input_box3.draw(screen)
        screen.blit(mouseCursor, pg.mouse.get_pos())

        pg.display.flip()
        clock.tick(60)

        if modusD != modus or scaleD != scale:
            with open("data/var.txt", "w") as f:
                f.writelines((modus, " ", str(scale)))
                
        modusD = modus
        scaleD = scale


def menu():
    mouseCursor =  pg.image.load("GUI/icon/MOUSE.png").convert_alpha()
    running = True

    layer = pg.sprite.LayeredUpdates()
    ui = pg.sprite.Group()

    while running:
        screen.fill((0,0,0))

        image = pg.image.load("MAINSCREEN/TITLE.png").convert_alpha()
        screen.blit(image, (0,0))

        image = pg.image.load("MAINSCREEN/ICON.png").convert_alpha()
        nW = 128
        nH = 128
        entityImage = pg.transform.scale(image, (nW, nH))

        screen.blit(entityImage, (214, 268))

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 60)

        titleText = FONT.render('SYLLADEX TEST' , True , WHITE)

        FONT = pg.font.Font("GUI/font/DisposableDroidBB.ttf", 24)

        versionText = FONT.render('ALPHA VERSION 0.1' , True , WHITE)

        screen.blit(titleText, (110, 78))
        screen.blit(versionText, (504, 96))

        UIBase.createUI((592, 226), "MAINSCREEN/START.png", "start", "button", None, 1, (16, 16), layer, ui, [])
        UIBase.createUI((592, 314), "MAINSCREEN/QUIT.png", "quit", "button", None, 1, (16, 16), layer, ui, [])
        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in ui:
                    if i.job == "start":
                        if i.rect.collidepoint(pg.mouse.get_pos()):
                            i.image = pg.image.load("MAINSCREEN/START_ACTIVE.png").convert_alpha()
                            running = False
                    if i.job == "quit":
                        if i.rect.collidepoint(pg.mouse.get_pos()):
                            i.image = pg.image.load("MAINSCREEN/QUIT_ACTIVE.png").convert_alpha()
                            pg.quit()
                            sys.exit()

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        
        ui.draw(screen)
        layer.draw(screen)
        screen.blit(mouseCursor, pg.mouse.get_pos())

        pg.display.update()
        clock.tick(60)
        

## Running main loop

if __name__ == '__main__':
    menu()
    main()
    pg.quit()
    sys.quit()