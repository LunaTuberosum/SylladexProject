import pygame as pg


class UIBase(pg.sprite.Sprite):
    modus = "STACK"
    uiElements = pg.sprite.Group()
    uiLayers = pg.sprite.LayeredUpdates()

    currentUI = {}

    CodeDatabase = None

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

    def add_current_UI(uiArray):
        for elem in uiArray:
            UIBase.currentUI[f'{elem.__name__}'] = elem

    def get_uiElem(elem):
        try:
            return UIBase.currentUI.get(elem)
        except:
            raise Exception(f'Could not find {elem} in current UI')

    def _create_appearance(self, *sizeColorPos, **options):
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

    def _reload_image(self, image, pos):
        _image = pg.image.load(image).convert_alpha()
        self.image.blit(_image, pos)

    def set_modus(modus):
        UIBase.modus = modus

        UIBase.modusBackground = UIBase.modusColor.get(UIBase.modus).get('background')
        UIBase.modusForground = UIBase.modusColor.get(UIBase.modus).get('forground')
        UIBase.modusAccent = UIBase.modusColor.get(UIBase.modus).get('accent')

        for elem in UIBase.get_group('ui'):
            if elem.isMisc == False:
                elem.image = pg.image.load(f'sylladex/uiElements/asset/{UIBase.get_modus()}/{elem.imageID}').convert_alpha()
            elif isinstance(elem, UIBase.ScrollBar):
                elem.image.fill(UIBase.modusForground)

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