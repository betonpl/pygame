from main.api.Eventable import Eventable
from main.api.Tickable import Tickable
from main.api.Field import Field

class FieldManager(Eventable, Tickable):

    def __init__(self, board, priority):
        Eventable.__init__(self)
        Tickable.__init__(self, priority)
        self.__board = board
        self.__fields = self.__selected = self.__actions = None
        self.resetManager()
    @property
    def fields(self):
        return self.__fields

    @property
    def actions(self):
        return self.__actions

    @property
    def board(self):
        return self.__board

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, value):
        self.__selected = value

    def cleanDead(self):
        for field in self.fields:
            if field.unit.isDead():
                self.fields.remove(field)

    def parseActions(self):
        for action in self.__actions:
            if(action['action'] == "move"):
                action['source'].moveTo(action['dest'])
                self.__actions.remove(action)

    def checkExhausting(self):
        if self.selected != None and self.selected.unit.isExhausted():
            self.selected = None

    def tick(self):
        self.cleanDead()
        self.parseActions();
        self.checkExhausting();

    def reset(self):
        self.selected = None
        for field in self.fields:
            field.unit.resetActions()

    def resetManager(self):
        self.selected = None
        self.__fields = []
        self.__actions = []

    def click(self, clickPos):
        if(not self.board.isInside(clickPos)):
            return False
        field = self.getFieldAtPos(clickPos)
        if(field != None and field.unit.owner == self.board.currentPlayer and not field.unit.isExhausted()):
            self.selected = field
        elif self.selected != None:
            selectedUnit = self.selected.unit
            if not selectedUnit.isExhausted():
                if field == None and clickPos in Field.getRange(self.selected, selectedUnit.stats.moveRange):
                    self.addAction(dict(source=self.selected, action="move", dest=clickPos))
                elif field != None and clickPos in Field.getRange(self.selected, selectedUnit.stats.attackRange):
                    if field.unit.owner != self.board.currentPlayer:
                        self.addAction(dict(source=self.selected, action="attack", dest=field))

    def addField(self, field):
        self.__fields.append(field)

    def addAction(self, action):
        self.__actions.append(action)
        self.selected = None

    def getFieldAtPos(self, pos):
        for field in self.fields:
            if field.pos == pos:
                return field
        return None
