import pygame as pg

from baseUI import UIBase

class LongTextField(UIBase):

    def __init__(self, x, y, width, height, maxChar, maxLineCount, job, toolTipText, textColor=(0,0,0)):
        super().__init__(x, y, (width, height), f'LongTextField ({job})', (255,255,255))

        self.textColor = textColor
        self.font = pg.font.Font("sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 24)

        self.maxChar = maxChar
        self.maxLineCount = maxLineCount

        self.job = job
        self.active = False
        self.hovering = False

        self.toolTipText = toolTipText

        self.baseColor = (255,255,255)
        self.hoverColor = (230,230,230)
        self.selectedColor = (170,170,170)

        self.lines = []

        for line in range(self.maxLineCount):
            self.lines.append('')

        self.activeLine = self.lines[0]
        self.activeLineIndex = 0

    def starter_text(self, newText):
        self.lines = []
        for line in range(self.maxLineCount):
            self.lines.append('')

        self.activeLineIndex = 0
        self.activeLine = self.lines[self.activeLineIndex]
      
        _newText = newText.split()

        totalChar = 0
        for index, text in enumerate(_newText):
            if text[-1:] == '.': text = text[:-1] + ','
            
            if totalChar + len(text) > self.maxChar:
                self.lines[self.activeLineIndex] = self.activeLine
                self.activeLineIndex += 1
                self.activeLine = self.lines[self.activeLineIndex]
                self.activeLine = text + ' '
                totalChar = 0

            else:
                self.activeLine += text + ' '
                totalChar += len(text) + 1

        self.lines[self.activeLineIndex] = self.activeLine
        self.draw()
        self.no_hover()

    def exit_field(self):
        self.image.fill(self.baseColor)
        self.active = False
        fullDesc = ''

        for line in self.lines:
            _lines = line.split()

            line = ''
            for _line in _lines:
                if _line[-1:] == ',':
                    line += _line[:-1]
                    line += '.'
                    line += ' '
                else:
                    line += _line
                    line += ' '
            fullDesc += line

        if self.job == 'action1Desc' or self.job == 'action2Desc':
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                    if elem.job == 'meleeToggle':
                        if elem.on == True:
                            if self.job == 'action1Desc':
                                UIBase.CodeDatabase.change_codeValue('Melee 1 Desc', fullDesc)
                            elif self.job == 'action2Desc':
                                UIBase.CodeDatabase.change_codeValue('Melee 2 Desc', fullDesc)
                    if elem.job == 'rangedToggle':
                        if elem.on == True:
                            if self.job == 'action1Desc':
                                UIBase.CodeDatabase.change_codeValue('Ranged 1 Desc', fullDesc)
                            elif self.job == 'action2Desc':
                                UIBase.CodeDatabase.change_codeValue('Ranged 2 Desc', fullDesc)
                    if elem.job == 'magicToggle':
                        if elem.on == True:
                            if self.job == 'action1Desc':
                                UIBase.CodeDatabase.change_codeValue('Magic 1 Desc', fullDesc)
                            elif self.job == 'action2Desc':
                                UIBase.CodeDatabase.change_codeValue('Magic 2 Desc', fullDesc)
        
        elif self.job == '1-4Desc' or self.job == '5-8Desc' or self.job == '9-12Desc' or self.job == '13-16Desc':
            for elem in UIBase.get_group('ui'):
                if isinstance(elem, UIBase.get_uiElem('ToggleButton')):
                    if elem.job == 't1Toggle':
                        if elem.on == True:
                            if self.job == '1-4Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 1 1-4', fullDesc)
                            elif self.job == '5-8Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 1 5-8', fullDesc)
                            elif self.job == '9-12Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 1 9-12', fullDesc)
                            elif self.job == '13-16Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 1 13-16', fullDesc)
                    if elem.job == 't2Toggle':
                        if elem.on == True:
                            if self.job == '1-4Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 2 1-4', fullDesc)
                            elif self.job == '5-8Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 2 5-8', fullDesc)
                            elif self.job == '9-12Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 2 9-12', fullDesc)
                            elif self.job == '13-16Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 2 13-16', fullDesc)
                    if elem.job == 't3Toggle':
                        if elem.on == True:
                            if self.job == '1-4Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 3 1-4', fullDesc)
                            elif self.job == '5-8Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 3 5-8', fullDesc)
                            elif self.job == '9-12Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 3 9-12', fullDesc)
                            elif self.job == '13-16Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 3 13-16', fullDesc)
                    if elem.job == 't4Toggle':
                        if elem.on == True:
                            if self.job == '1-4Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 4 1-4', fullDesc)
                            elif self.job == '5-8Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 4 5-8', fullDesc)
                            elif self.job == '9-12Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 4 9-12', fullDesc)
                            elif self.job == '13-16Desc':
                                UIBase.CodeDatabase.change_codeValue('Trait 4 13-16', fullDesc)

    def draw(self):
        self.image.fill(self.selectedColor)

        sections = self.rect.h/len(self.lines)

        for index, line in enumerate(self.lines):
            txt_surface = self.font.render(line, True, self.textColor)
            self.image.blit(txt_surface, (self.rect.w/2-txt_surface.get_width()/2, (sections*index)+((sections/2)-txt_surface.get_height()/2)))

    def typeing(self, event):

        if self.active == True:
            if event.key == pg.K_BACKSPACE:
                self.activeLine = self.activeLine[:-1]
        
                self.lines[self.activeLineIndex] = self.activeLine
                self.draw()

                if self.activeLineIndex > 0:
                    if len(self.activeLine) == 0:
                        self.activeLineIndex -= 1
                        self.activeLine = self.lines[self.activeLineIndex]

            elif event.key == pg.K_RETURN:
                if self.activeLineIndex == 0 and (self.activeLine == '' or self.activeLine == ' '):
                    self.activeLine = '/'
                self.active = False
                self.lines[self.activeLineIndex] = self.activeLine
                self.exit_field()
                self.draw()
                return

            else:
                if event.key != pg.K_RETURN:
                    self.activeLine += event.unicode

                    wordSections = self.activeLine.split()

                    totalCharCount = 0
                    for index, sect in enumerate(wordSections):
                        if totalCharCount + len(sect) > self.maxChar:
                            self.activeLine = self.activeLine[:-len(sect)]

                            self.lines[self.activeLineIndex] = self.activeLine
                            if self.activeLineIndex + 1 == self.maxLineCount:
                                return
                            
                            self.activeLineIndex += 1
                            self.activeLine = self.lines[self.activeLineIndex]

                            self.activeLine += sect
                        else:
                            totalCharCount += len(sect) + 1

                        self.lines[self.activeLineIndex] = self.activeLine
                        self.draw()

    def hover(self):
        if self.active == False:
            self.image.fill(self.hoverColor)
            sections = self.rect.h/len(self.lines)

            for index, line in enumerate(self.lines):
                txt_surface = self.font.render(line, True, self.textColor)
                self.image.blit(txt_surface, (self.rect.w/2-txt_surface.get_width()/2, (sections*index)+((sections/2)-txt_surface.get_height()/2)))
            self.hovering = True

    def no_hover(self):
        if self.active == False:
            self.image.fill(self.baseColor)
            sections = self.rect.h/len(self.lines)

            for index, line in enumerate(self.lines):
                txt_surface = self.font.render(line, True, self.textColor)
                self.image.blit(txt_surface, (self.rect.w/2-txt_surface.get_width()/2, (sections*index)+((sections/2)-txt_surface.get_height()/2)))
            self.hovering = False

    def on_click(self):
        self.active = True
        sections = self.rect.h/len(self.lines)
        self.draw()

        for index, line in enumerate(self.lines):
            txt_surface = self.font.render(line, True, self.textColor)
            self.image.blit(txt_surface, (self.rect.w/2-txt_surface.get_width()/2, (sections*index)+((sections/2)-txt_surface.get_height()/2)))
        