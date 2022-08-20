import pygame as pg

from baseUI import UIBase


class ConsoleMessage(UIBase):
    consoleMessages = []

    def __init__(self, text):

        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)
        self.txt_surface = self.font.render(text, False, 'white')

        super().__init__(pg.display.get_surface().get_width()-(self.txt_surface.get_width()+30), pg.display.get_surface().get_height()-40, (self.txt_surface.get_width()+20,30), 'ConsoleMessage ()', (50,50,50))

        if len(ConsoleMessage.consoleMessages) > 0:
            self.rect.y = ConsoleMessage.consoleMessages[-1].rect.y - 40

        ConsoleMessage.consoleMessages.append(self)

        self.image.set_alpha(130)
        self.image.blit(self.txt_surface, [10, 5])

        self.prevTick = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.prevTick >= 1000:
            self.kill()
            ConsoleMessage.consoleMessages.remove(self)
            #Fade to the right
        

