import pygame as pg


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

    modusColor = {
        'STACK': {
            'background': '#9B2448',
            'forground' : '#FF00DC',
            'accent': '#FF61DC'
        },
        'QUEUE': {
            'background': '#CF560C',
            'forground' : '#FF6000',
            'accent': '#FF912B'
        },
        'TREE': {
            'background': '#7CA619',
            'forground' : '#96FF00',
            'accent': '#CDFF2B'
        }
    }

    modusBackground = modusColor.get(modus).get('background')
    modusForground = modusColor.get(modus).get('forground')
    modusAccent = modusColor.get(modus).get('accent')

    def __init__(self, x, y, size, objName, surfaceColor):
        super().__init__()
        UIBase.add_toGroup(self)
        UIBase.uiLayers.add(self)
        UIBase.uiLayers.change_layer(self, 1)

        self.objName = objName
        self.baseColor = surfaceColor
        self.image = pg.Surface(size)
        self.image.fill(surfaceColor)

        self.rect = self.image.get_rect(topleft=(x, y))

    @classmethod
    def add_current_UI(cls, uiArray):
        for elem in uiArray:
            cls.currentUI[f'{elem.__name__}'] = elem

    @classmethod
    def get_uiElem(cls, elem) -> object:
        try:
            return UIBase.currentUI.get(elem)
        except:
            raise Exception(f'Could not find {elem} in current UI')

    def create_appearance(self, *sizeColorPos, **options):
        if 'colorKey' in options and options['colorKey'] == True: self.image.set_colorkey(self.baseColor)

        for rect in sizeColorPos:
            newRect = pg.Surface(rect[0])
            newRect.fill(rect[1])
            self.image.blit(newRect, rect[2])

        if 'alpha' in options: self.image.set_alpha(options['alpha'])
        
        if 'image' in options: 
            image = pg.image.load(options['image'][0]).convert_alpha()
            self.image.blit(image, options['image'][1])
        
        elif 'texts' in options:
            for text in options['texts']:
                if len(text) == 4:
                    _text = self.font.render(text[0], True, text[3])
                else:
                    _text = self.font.render(text[0], True, (0,0,0))

                if text[2] == 'center':
                    self.image.blit(_text, [text[1][0]-(_text.get_width()/2), (text[1][1]-(_text.get_height()/2))])
                elif text[2] == 'left':
                    self.image.blit(_text, [text[1][0], (text[1][1]-(_text.get_height()/2))])

    def reload_image(self, image, pos):
        _image = pg.image.load(image).convert_alpha()
        self.image.blit(_image, pos)

    @classmethod
    def set_modus(cls, modus):
        cls.modus = modus

        cls.modusBackground = cls.modusColor.get(cls.modus).get('background')
        cls.modusForground = cls.modusColor.get(cls.modus).get('forground')
        cls.modusAccent = cls.modusColor.get(cls.modus).get('accent')

        for elem in cls.get_group('ui'):
            if elem.isMisc == False:
                elem.image = pg.image.load(f'sylladex/uiElements/asset/{cls.get_modus()}/{elem.imageID}').convert_alpha()
            elif isinstance(elem, UIBase.ScrollBar):
                elem.image.fill(cls.modusForground)

    @classmethod
    def get_modus(cls):
        return cls.modus

    @classmethod
    def get_group(cls, whichGroup):
        if whichGroup == "ui":
            return cls.uiElements
        elif whichGroup == "layer":
            return cls.uiLayers

    @classmethod
    def add_toGroup(cls, elem):
        cls.get_group("ui").add(elem)
        cls.get_group("layer").add(elem)

    @classmethod
    def remove_fromGroup(cls, elem):
        cls.get_group("ui").remove(elem)
        cls.get_group("layer").remove(elem)