import pygame as pg
import pickle


class UIBase(pg.sprite.Sprite):
    modus = "STACK"
    uiElements = pg.sprite.Group()
    uiLayers = pg.sprite.LayeredUpdates()

    AddCardButton = None
    CardList = None
    GristCacheButton = None
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

    CodeDatabase = None

    def __init__(self, x, y, size, image):
        super().__init__()
        UIBase.add_toGroup(self)
        UIBase.uiLayers.add(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.image = pg.Surface(size)
        self.image.fill((255, 255, 255))
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def set_modus(modus):
        UIBase.modus = modus

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