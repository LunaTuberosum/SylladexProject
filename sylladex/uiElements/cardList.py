### 9 items can fit before scroll
import pygame as pg

from sylladex.uiElements.baseUI import UIBase
from sylladex.uiElements.listObject import ListObject
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.popUp import PopUp

class CardList(UIBase):
    listObj = []

    def __init__(self, x, y, size, image):
        super().__init__(x, y, size, image)
        self.uiLayers.change_layer(self, -1)
        
    def add_toList(self):
        self.listObj.append(ListObject(24, 127, (249, 64), "sylladex/uiElements/asset/MISC/LIST_OBJ.png", str(len(self.listObj))))
        self.place_list()

    def remove_fromList(self, NumTextField):
        if self.listObj[len(self.listObj)-1].empty == True:
            self.listObj[len(self.listObj)-1].kill()
            self.listObj.remove(self.listObj[len(self.listObj)-1])
        else:
            PopUp("You can only remove empty cards. Eject cards first")
            NumTextField.text = str(len(self.listObj))
            NumTextField.draw()
            return
        
        

    def start_list(self):
        for card in self.listObj:
            UIBase.add_toGroup(card)
            UIBase.uiLayers.change_layer(card, -1)
        self.place_list

    def place_list(self):
        offset = 70
        for card in self.listObj:
            
            card.rect.y = 127 + offset
            offset += 70
        for elem in UIBase.get_group("ui"):
            if isinstance(elem, ScrollBar):
                UIBase.uiElements.remove(elem)
                UIBase.uiLayers.remove(elem)
                elem.kill()
        ScrollBar(self.listObj)