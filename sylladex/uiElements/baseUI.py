import pygame as pg


class UIBase(pg.sprite.Sprite):
    modus = "STACK"
    uiElements = pg.sprite.Group()
    uiLayers = pg.sprite.LayeredUpdates()

    AddCardButton = None
    CardList = None
    ConsoleMessage = None
    CustomSettingButton = None
    EscapeMenu = None
    EscapeMenuOption = None
    GristCache = None
    GristCacheButton = None
    GristCacheLimit = None
    GristInfoBox = None
    GristProgressBar = None
    ListObject = None
    ModusCard = None
    PopUp = None
    RemoveCardButton = None
    ScrollBar = None
    SideBar = None
    SidebarButton = None
    StackingArea = None
    TextField = None
    ToolTip = None
    FinishButton = None

    CodeDatabase = None

    DebugUIInspector = None
    DebugInspect = False
    Insepctors = []

    prevTick = pg.time.get_ticks()

    def __init__(self, x, y, size, image, objName, misc=False, surfaceColor=(0,0,0)):
        super().__init__()
        UIBase.add_toGroup(self)
        UIBase.uiLayers.add(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.objName = objName
        self.imageID = image
        self.isMisc = misc
        if image == 'surfaceRect':
            self.image = pg.Surface(size)
            self.image.fill(surfaceColor)
        else:
            if self.isMisc == True:
                self.image = pg.image.load(f'sylladex/uiElements/asset/MISC/{image}').convert_alpha()
            else:
                self.image = pg.image.load(f'sylladex/uiElements/asset/{UIBase.get_modus()}/{self.imageID}').convert_alpha()

        self.rect = self.image.get_rect(topleft=(x, y))

    def set_modus(modus):
        UIBase.modus = modus

        for elem in UIBase.get_group('ui'):
            if elem.isMisc == False:
                elem.image = pg.image.load(f'sylladex/uiElements/asset/{UIBase.get_modus()}/{elem.imageID}').convert_alpha()
            elif isinstance(elem, UIBase.ScrollBar):
                elem.image.fill(UIBase.ScrollBar.modusColorDict[UIBase.get_modus()]['base'])

    def get_modus():
        return UIBase.modus

    def get_group(whichGroup):
        if whichGroup == "ui":
            return UIBase.uiElements
        elif whichGroup == "layer":
            return UIBase.uiLayers

    def add_toGroup(elem):
        UIBase.get_group("ui").add(elem)
        UIBase.get_group("layer").add(elem)

    def remove_fromGroup(elem):
        UIBase.get_group("ui").remove(elem)
        UIBase.get_group("layer").remove(elem)