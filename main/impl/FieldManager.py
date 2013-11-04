from main.api.Eventable import Eventable
from main.api.Tickable import Tickable
from main.Field import Field

class FieldManager(Eventable, Tickable):

    def __init__(self, board, priority):
        Eventable.__init__(self)
        Tickable.__init__(self, priority)
        self.__board = board
        self.__fields = []
        self.__selected = None
        self.__actions = []

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
                action['source'].pos = action['dest']
        pass

    def tick(self):
        self.cleanDead()
        self.parseActions();

    def reset(self):
        self.selected = None
        for field in self.fields:
            field.unit.resetActions()

    def click(self, pos):
        field = self.getFieldAtPos(pos)
        if(field != None and field.unit.owner == self.board.currentPlayer):
            self.selected = field
        elif self.selected != None:
            destination = pos
            if destination in Field.getOperationRadius(self.selected):
                destinationField = self.getFieldAtPos(destination)
                if destinationField == None:
                    self.addAction(dict(source=self.selected, action="move", dest=pos))
                else:
                    self.addAction(dict(source=self.selected, action="attack", dest=destinationField))



    def addField(self, field):
        self.__fields.append(field)

    def addAction(self, field):
        self.__actions.append(field)

    def getFieldAtPos(self, pos):
        for field in self.fields:
            if field.pos == pos:
                return field
        return None




