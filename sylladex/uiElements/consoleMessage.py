import pygame as pg

from baseUI import UIBase, Apperance


class ConsoleMessage(UIBase):
    consoleMessages = []

    def __init__(self, text):

        super().__init__(pg.display.get_surface().get_width()-((len(text)*11.5)+25), pg.display.get_surface().get_height()-40, f'ConsoleMessage ({text})')

        self.font = pg.font.Font('sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf', 24)

        self.apperance = Apperance(
            self,
            [15+(len(text)*11.5), 30],
            [[15+(len(text)*11.5),30], (50,50,50), [0,0]],
            alpha=130,
            texts=[[text, [10, 15], 'left', '#ffffff']]
        )

        if len(ConsoleMessage.consoleMessages) > 0:
            self.rect.y = ConsoleMessage.consoleMessages[-1].rect.y - 40

        ConsoleMessage.consoleMessages.append(self)

        self.prevTick = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.prevTick >= 1000:
            self.kill()
            ConsoleMessage.consoleMessages.remove(self)
            #Fade to the right
        

