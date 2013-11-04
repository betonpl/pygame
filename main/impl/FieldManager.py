from main.api.Eventable import Eventable
from main.api.Tickable import Tickable

class FieldManager(Eventable, Tickable):

    def __init__(self, board, priority):
        Eventable.__init__(self)
        Tickable.__init__(self, priority)
        self.__board = board
        self.__fields = []
        self.__selected = None

    @property
    def fields(self):
        return self.__fields

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

    def tick(self):
        self.cleanDead()

    def reset(self):
        self.selected = None
        for field in self.fields:
            field.unit.resetActions()

    def click(self, pos):
        field = self.getFieldAtPos(pos)
        if(field != None and field.unit.owner == self.board.currentPlayer):
            self.selected = field

    def addField(self, field):
        self.__fields.append(field)

    def getFieldAtPos(self, pos):
        for field in self.fields:
            if field.pos == pos:
                return field
        return None




