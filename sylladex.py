import pygame as pg
from pygame.locals import *
import captchacards
from gui import *
import sys
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
treeColor = (150, 255, 0)


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
        "QUEUE": [queueColor, "GUI/panel/QUEUE/MODUSLABEL.png"],
        "TREE": [treeColor, "GUI/panel/TREE/MODUSLABEL.png"]
    }

    ## Making stack and starting arrays
    currentStack = []
    nameStart = []
    tierStart = []

    ## Making code input panel

    StackingArea.create(scale, modus, layers, uis)
    SylladexPanel.create(scale, modus, layers, uis, modusColor)
    ModusChanger.create(scale, modus, layers, uis)
    Label.create(scale, modus, layers, uis, "NAMELABEL", "nameLabel", (40, 60))
    Label.create(scale, modus, layers, uis, "CODELABEL", "codeLabel", (40, 142))
    Label.create(scale, modus, layers, uis, "TIERLABEL", "tierLabel", (40, 224))
    input_box1 = Textbox.create(scale, modus, layers, uis, "TEXTBOX", "name", (30, 98), "TEXTBOX_ACTIVE", "TEXTBOX")
    input_box2 = Textbox.create(scale, modus, layers, uis, "TEXTBOX_MEDIUM", "code", (30, 180), "TEXTBOX_MEDIUM_ACTIVE", "TEXTBOX_MEDIUM")
    input_box3 = Textbox.create(scale, modus, layers, uis, "TEXTBOX_SMALL", "tier", (30, 262), "TEXTBOX_SMALL_ACTIVE", "TEXTBOX_SMALL")
    AddButton.create(scale, modus, layers, uis, "cardCreate", (120, 260))
    HelpButton.create(scale, modus, layers, uis, (925, 20))
    Taskbar.createButton(scale, "ARROW", modus, "taskbarOpen", layers, uis, (565, 503))

    cardInput = [input_box1, input_box2, input_box3]

    for i in uis:
        if i.job == "stackingArea":
            area = i.rect

    ## Defining import variables
    moveCard = False 
    selected = None

    editing = False
    helpT = False

    bool1 = False
    lines = []

    moveAllCard = False

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
            entity = captchacards.CaptchaCards((500, a), WHITE, v, nameStart[z], tierStart[z], scale, modus, cardIDs)
            sprites.add(entity)
            layers.add(entity)
            captchacards.CaptchaCards.kindIcon(entity, scale, "d")
            if modus != "TREE":
                ## If stack is 2 or longer make parents and children
                if z >= 1:
                    if parent:
                        parent.child = entity
                        entity.parent = parent
                parent = entity

            ## Make them stack proprly
            layers.change_layer(entity, z)
            z += 1

            a += 48

    if modus == "TREE":
        global screen
        captchacards.TreeCards.startTree(currentStack, sprites)


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

        infoRects = [syl_cus, nam_txt, cod_txt, tir_txt, add_set, tsk_bar, mod_res, stk_ara, tsh_but, clr_but, edt_but]

        bool1 = True
        

        screen = screenNew  

        ## Checking for inputs
        for event in pg.event.get():

            ## Quitting software
            if event.type == pg.QUIT:
                return

            ## Checking if mouse is used
            elif event.type == pg.MOUSEBUTTONDOWN:

                ## Checking if its left mouse button
                if event.button == 1:

                    moveAllCard = True

                    for b in cardInput:
                        if b.rect.collidepoint(event.pos):
                            for bm in cardInput:
                                bm.modus = modus
                            Textbox.nameBox(b, cardInput, BLACK)
                    
                    if helpT == True:
                        HelpButton.placeInfo(infoRects,uis, layers, scale)

                    ## Checking which ui element is being pressed
                    for i in uis:

                        if i.rect.collidepoint(event.pos):
                            if i.job == "modusChanger" and helpT == False:
                                modus = ModusChanger.modusChange(i, modusColor[modus][0], modus, scale, uis, sprites, layers, cardIDs)
                                if modus == "TREE":
                                    captchacards.TreeCards.startTree(currentStack, sprites)

                            elif i.job == "cardCreate" and helpT == False:
                                i.modus = modus
                                AddButton.cardCreate(i, cardInput, sprites, layers, currentStack, scale, cardIDs)
                            elif i.job == "closePanel":
                                CardInspector.closePanel(uis, layers)
                            elif i.job == "help":
                                helpT, mouseCursor = HelpButton.toggleHelp(helpT, uis, modus)
                                for i in uis:
                                    if i.job == "infoUIs":
                                        HelpButton.destroy(i, uis, layers)
                            elif i.job == "taskbarOpen" and helpT == False:
                                Taskbar.taskbarOpen(i, uis,layers, scale, modus)
                            elif i.job == "taskbarClose" and helpT == False:
                                Taskbar.taskbarClose(i, uis,layers, scale, modus)
                            elif i.job == "edit":
                                editing = Taskbar.editToggle(i, uis, editing, modus)
                            elif i.job == "endEdit":
                                editing = Taskbar.editEnd(i, uis, editing, modus)
                            elif i.job == "set":
                                editing = AddButton.setEdit(sprites, uis, editing, currentStack, scale, modus)
                            elif i.job == "clear":
                                Taskbar.clear(currentStack, layers, sprites)
                            
                            for ins in [ "inspecttrait1","inspecttrait2", "inspectaction1","inspectaction2","inspectaction3","inspectaction4",]:
                                if i.job == ins:
                                    CheckBox.inspect(i, i.insAtr, [i.insNum, uis, layers, scale, modus] )
                
                    ## Checking which card is being touched
                    for sprite in sprites:
                        
                        if sprite.rect.collidepoint(event.pos):

                            
                            
                            ## Defining which sprite it is
                            selected = sprite

                            if editing == True:
                                Taskbar.captaEdit(selected, input_box1, input_box2, input_box3)

                            ### Checking how to move sprite
                            if len(currentStack) == 0:
                                moveing = True
                            for s in currentStack:
                                if s != sprite.cardID:
                                    moveing = True
                                else:
                                    moveing = False
                                    break

                            if moveing == True:
                                moveAllCard = False
                                ## Picks up image and places it above all
                                sprite.image = pg.image.load(f"GUI/cards/{modus}CAPTA_UP.png").convert_alpha()
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
                            CardInspector.create(scale, modus, layers, uis, (648, 66), s)   

                ## Checking if its right button
                elif event.button == 3:

                    ## Checking which card is being pressed
                    for sprite in sprites:
                        
                        if sprite.rect.collidepoint(event.pos):
                            selected = sprite
                            
                            if currentStack:
                                if modus == "STACK":
                                    if selected.cardID == currentStack[len(currentStack)-1]:
                                        ## Disconnect it
                                        captchacards.CaptchaCards.disconnect(selected,selected.parent,currentStack, sprites, scale)

                                elif modus == "QUEUE":
                                    ## Cheaking if the card has no child but has a parent
                                    if selected.parent and selected.child != None:

                                        ## If it is the top on the stack
                                        if layers.get_layer_of_sprite(selected) == 0:

                                            ## Disconnect it
                                            captchacards.QueueCards.disconnect(selected,selected.child,currentStack, sprites, scale)

                                            
                                        else:

                                            ## Sets selected to none
                                            selected = None
                                elif modus == "TREE":
                                    if selected.left == None and selected.right == None:
                                        captchacards.TreeCards.disconnect(selected, currentStack, layers, sprites)
                                    
                            
            ## Checking if the mouse buttons is up
            elif event.type == pg.MOUSEBUTTONUP:

                if bool1 == True:
                    for c in sprites:

                        c.image = pg.image.load(f"GUI/cards/{modus}/CAPTA.png").convert_alpha()
                        captchacards.CaptchaCards.kindIcon(c, scale, "d")
                        nW = c.rect[2]
                        nH = c.rect[3]
                        c.image = pg.transform.scale(c.image, (nW, nH))
                        

                        if c.parent == None and c.child == None:

                            layers.change_layer(c, 0)
                    bool1 = False                     
                
                moveCard = False
                moveAllCard = False

                ## Set the add button to netural
                for i in uis:

                    if i.job == 'cardCreate':

                        i.image = pg.image.load(f"GUI/button/{modus}/ADD.png").convert_alpha()
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
                                
                                if modus == "TREE":
                                    captchacards.TreeCards.combine(selectedM, out.parent, currentStack, sprites)
                                else:
                                    captchacards.CaptchaCards.combine(selectedM, out.parent, out, currentStack, layers, sprites)
                                outlines.empty()

                            else:
                                outlines.empty()

                    ## Destroys card if its touching Trash
                    captchacards.CaptchaCards.destroy(sprite, uis, layers, sprites)

                ## Reseting the cards sprites
                

            ## Checking if the mouse is moved
            elif event.type == pg.MOUSEMOTION:    
                if moveAllCard:
                    captchacards.CaptchaCards.moveAll(sprites, scale, event.rel)            

                for i in uis:
                    if i.job == "codePanel":
                        captchacards.CaptchaCards.cardBorder(i, sprites, event.rel)

                ## Checking and moving a sprite
                if selected:

                    ## If card can be moved
                    if moveCard == True:

                        ## Move card based on mouse
                        selected.move(event.rel, currentStack)
                        
                        ## Makes a list of all sprites that can have an outline
                        avalible_sprites.empty()

                        if modus == "TREE":
                            for c in sprites:
                                if len(currentStack) == 0:
                                    for s in sprites:

                                        ## If it has no children add it
                                        if s.child == None:

                                            avalible_sprites.add(s)

                                    ## If the list is longer than one make outline
                                    if avalible_sprites.__len__() >= 1:
                                        outlines.add(captchacards.CaptchaCards.distance(selected, avalible_sprites, currentStack, scale))
                                else:
                                    if c.cardID == currentStack[0]:
                                        outlines.add(captchacards.CaptaOutline((c.rect.x, c.rect.y - 48), (255, 255, 255), c, scale))
                        else:
                            for s in sprites:

                                ## If it has no children add it
                                if s.child == None:

                                    avalible_sprites.add(s)

                            ## If the list is longer than one make outline
                            if avalible_sprites.__len__() >= 1:

                                
                                outlines.add(captchacards.CaptchaCards.distance(selected, avalible_sprites, currentStack, scale))
                    
                       
            ## Checking if keys are being pressed
            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    menu()

                if event.key == pg.K_RETURN:
                    for b in cardInput:
                        if b.active:
                            b.active = False
                            b.image = pg.image.load(f"GUI/textbox/{modus}/{b.inactiveImage}.png").convert_alpha()

                ## Checking if the input boxs are active                
                if input_box1.active or input_box2.active or input_box3.active:
                    
                    for b in cardInput:
                        if b.active == True:
                            if event.key == pg.K_BACKSPACE:
                                b.text = b.text[:-1]

                        ## Checking if box1 and adds text
                            else:
                                if event.key != pg.K_RETURN:
                                    b.text += event.unicode
                        
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
                    input_box1.txt_surface = input_box1.fontBig.render(input_box1.text, True, input_box1.color)
                    input_box2.txt_surface = input_box2.fontBig.render(input_box2.text, True, input_box2.color)
                    input_box3.txt_surface = input_box3.fontBig.render(input_box3.text, True, input_box3.color)

        ## Buch of updating stuff
        sprites.update()
        screen.fill((183, 183, 183))
        lines.clear()
        if currentStack:
            lines =  captchacards.TreeCards.startLines(sprites, currentStack, lines)
            for line in lines:
                lineNew = pg.draw.lines(screen, (124, 166, 25), False, line, 5)
        sprites.draw(screen)
        layers.draw(screen)
        outlines.draw(screen)
        uis.draw(screen)
        

        for b in cardInput:
            Textbox.draw(b, screen)
        x, y = pg.mouse.get_pos()
        if helpT == True:

            screen.blit(mouseCursor, (x-5 , y-5))
        else:
            screen.blit(mouseCursor, (x-15 , y-10))

        pg.display.flip()
        clock.tick(60)
        if modusD != modus or scaleD != scale:
            with open("data/var.txt", "w") as f:
                f.writelines((modus, " ", str(scale)))
            for i in uis:
                i.modus = modus
                UIBase.updateAll(i, sprites, scale, uis, modusColor[modus][0], cardInput)


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

        MenuButtons.create((592, 226), "MAINSCREEN/START.png", "start", 1, layer, ui, "")

        MenuButtons.create((592, 314), "MAINSCREEN/QUIT.png", "quit", 1, layer, ui, "")
        
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
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
        x, y = pg.mouse.get_pos()
        screen.blit(mouseCursor, (x-15 , y-10))

        pg.display.update()
        clock.tick(60)
        