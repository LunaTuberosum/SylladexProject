import pygame as pg
import textwrap

from uiElement import Apperance, UIElement


class PopUp(UIElement):
    def __init__(self, text, question=False):
        self.font = pg.font.Font(
            "sylladex/uiElements/asset/MISC/DisposableDroidBB.ttf", 48)

        super().__init__(
            660,
            380,
            'PopUp',
            999
        )

        _lines = ['']
        _new_text = text.split(' ')

        _total_char = 0
        for _i, _text in enumerate(_new_text):
            if _total_char + len(_text) >= 25:
                _lines.append(_text + ' ')
                _total_char = len(_text) + 1

            else:
                _lines[len(_lines) - 1] += _text + ' '
                _total_char += len(_text) + 1

        _texts = []
        for _i, _line in enumerate(_lines):
            _texts.append(
                [_line, [330, 80 + (_i * 80)], 'center', '#000000'])

        self.apperance = Apperance(
            self,
            [600, 320],
            [[600, 320], '#999999', [0, 0]],
            [[576, 296], '#D9D9D9', [12, 12]],
            texts=_texts

        )

        self.last = pg.time.get_ticks()
        self.timer = 1200
        self.negate = False

    def remove(self):
        if self.negate == False:
            UIElement.remove_from_group(self)
