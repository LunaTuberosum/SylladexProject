from sylladex import sylladexMain

from sylladex.uiElements.baseUI import UIBase

from sylladex.uiElements.addCardButton import AddCardButton
from sylladex.uiElements.cardList import CardList
from sylladex.uiElements.gristCacheButton import GristCacheButton
from sylladex.uiElements.listObject import ListObject
from sylladex.uiElements.modusCard import ModusCard
from sylladex.uiElements.popUp import PopUp
from sylladex.uiElements.removeCardButton import RemoveCardButton
from sylladex.uiElements.scrollBar import ScrollBar
from sylladex.uiElements.sideBar import SideBar
from sylladex.uiElements.sidebarButton import SidebarButton
from sylladex.uiElements.stackingArea import StackingArea
from sylladex.uiElements.textField import TextField
from sylladex.uiElements.toolTip import ToolTip
from sylladex.uiElements.finishButton import FinishButton
from sylladex.captchalogueCards import codeDatabase

UIBase.AddCardButton = AddCardButton
UIBase.CardList = CardList
UIBase.GristCacheButton = GristCacheButton
UIBase.ListObject = ListObject
UIBase.ModusCard = ModusCard
UIBase.PopUp = PopUp
UIBase.RemoveCardButton = RemoveCardButton
UIBase.ScrollBar = ScrollBar
UIBase.SideBar = SideBar
UIBase.SidebarButton = SidebarButton
UIBase.StackingArea = StackingArea
UIBase.TextField = TextField
UIBase.ToolTip = ToolTip
UIBase.FinishButton = FinishButton

UIBase.CodeDatabase = codeDatabase

if __name__ == '__main__':
    sylladexMain.main()
