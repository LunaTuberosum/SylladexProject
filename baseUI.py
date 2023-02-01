import pygame as pg

class Apperance():
    modusColor = {
        'STACK': {
            'background': '#9B2448',
            'foreground' : '#FF00DC',
            'accent': '#FF61DC'
        },
        'QUEUE': {
            'background': '#CF560C',
            'foreground' : '#FF6000',
            'accent': '#FF912B'
        },
        'TREE': {
            'background': '#7CA619',
            'foreground' : '#96FF00',
            'accent': '#CDFF2B'
        }
    }

    def __init__(self, obj: object, baseSize: list, *sizeColorPos: list, **kargs):

        self.baseSize = baseSize

        self.obj = obj
        self.obj.image = pg.Surface(self.baseSize)
        self.obj.image.fill('#D8DDFF')

        self.sizeColorPos = sizeColorPos
        self.options = kargs

        self.obj.rect = self.obj.image.get_rect(topleft=self.obj.rect)
        self.reload_apperance()

    def reload_apperance(self):


        self.obj.image = pg.Surface(self.baseSize)
        self.obj.image.fill('#D8DDFF')

        if 'colorKey' in self.options: self.obj.image.set_colorkey('#D8DDFF')

        for rect in self.sizeColorPos:
            newRect = pg.Surface(rect[0])
            if rect[1] == 'ModusBackground':
                newRect.fill(Apperance.modusColor.get(UIBase.get_modus()).get('background'))
            elif rect[1] == 'ModusForeground':
                newRect.fill(Apperance.modusColor.get(UIBase.get_modus()).get('foreground'))
            elif rect[1] == 'ModusAccent':
                newRect.fill(Apperance.modusColor.get(UIBase.get_modus()).get('accent'))
            else:
                newRect.fill(rect[1])
            self.obj.image.blit(newRect, rect[2])

        if 'alpha' in self.options: self.obj.image.set_alpha(self.options['alpha'])
        
        if 'image' in self.options: 
            image = pg.image.load(self.options['image'][0]).convert_alpha()
            self.obj.image.blit(image, self.options['image'][1])
        
        if 'texts' in self.options:
            for text in self.options['texts']:

                if len(text) == 5: self.obj.font = pg.font.Font(text[4][0], text[4][1])

                _text = self.obj.font.render(text[0], True, text[3])

                if text[2] == 'center':
                    self.obj.image.blit(_text, [text[1][0]-(_text.get_width()/2), (text[1][1]-(_text.get_height()/2))])
                elif text[2] == 'left':
                    self.obj.image.blit(_text, [text[1][0], (text[1][1]-(_text.get_height()/2))])

    def change_image(self, image: str, pos: list):
        self.options['image'] = [image, pos]
        self.reload_apperance()

class UIBase(pg.sprite.Sprite):
    modus = "STACK"
    uiElements = pg.sprite.Group()
    uiLayers = pg.sprite.LayeredUpdates()

    currentUI = {}

    CodeDatabase = None
    CodeData = None

    DebugUIInspector = None
    DebugInspect = False
    Insepctors = []

    prevTick = pg.time.get_ticks()

    def __init__(self, x: int, y: int, objName: str):
        super().__init__()
        UIBase.add_toGroup(self)
        UIBase.uiLayers.add(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.objName = objName

        self.rect = [x, y]
        self.apperance = None

    @classmethod
    def add_current_UI(cls, uiArray: list):
        for elem in uiArray:
            cls.currentUI[f'{elem.__name__}'] = elem

    @classmethod
    def get_uiElem(cls, elem: object) -> object:
        try:
            return UIBase.currentUI.get(elem)
        except:
            raise Exception(f'Could not find {elem} in current UI')

    @classmethod
    def check_forUI(cls, elem: str) -> bool:
        for _elem in UIBase.get_group('ui'):
            if isinstance(_elem, UIBase.get_uiElem(elem)):
                return True

        return False

    @classmethod
    def find_curUI(cls, elem: str) -> object:
        for _elem in UIBase.get_group('ui'):
            if isinstance(_elem, UIBase.get_uiElem(elem)):
                return _elem

    @classmethod
    def set_modus(cls, modus: str):
        cls.modus = modus

        for elem in cls.get_group('ui'):
            elem.apperance.reload_apperance()

    @classmethod
    def get_modus(cls) -> str:
        return cls.modus

    @classmethod
    def get_group(cls, whichGroup: str) -> pg.sprite.Group:
        if whichGroup == "ui":
            return cls.uiElements
        elif whichGroup == "layer":
            return cls.uiLayers

    @classmethod
    def add_toGroup(cls, elem: object):
        cls.get_group("ui").add(elem)
        cls.get_group("layer").add(elem)

    @classmethod
    def remove_fromGroup(cls, elem: object):
        cls.get_group("ui").remove(elem)
        cls.get_group("layer").remove(elem)

        if hasattr(elem, 'children'):
            for child in elem.children:
                UIBase.remove_fromGroup(child)

        elem.kill()