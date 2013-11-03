from main.impl.EventManager import EventManager
from main.api.Tickable import Tickable
from main.api.Eventable import Eventable

class Board(Tickable, Eventable):

    def  __init__ (self, width, height, game):
        Tickable.__init__(self, game, -1)
        Eventable.__init__(self)
        self._width = width
        self._height = height
        self.__fields = []
        self.__currentHover = None

    def addField(self, field):
        self.__fields.append(field)

    def deleteField(self, pos):
        for field in self.__fields:
            if field.pos == pos:
                self.__fields.remove(field)

    def getField(self, pos):
        for field in self.__fields:
            if field.pos == pos:
                return field
        return None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def fields(self):
        return self.__fields

    @property
    def currentHover(self):
        return self.__currentHover

    def afterEventManagerSet(self):
        self.eventManager.register(None, self, EventManager.HOVERABLE)
        self.eventManager.register(None, self, EventManager.CLICKABLE)

    def click(self, pos):
        print "Click in Board at " + str(pos)

    def hover(self, pos):
        print "Hovering in Board at " + str(pos)
        pos = pos[0] if pos[0] <= self._width - 2 else self._width - 2 , pos[1] if pos[1] <= self._height - 2 else self._height - 2
        self.__currentHover = pos

