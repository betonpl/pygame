from main.impl.EventManager import EventManager
from main.api.Tickable import Tickable
from main.api.Eventable import Eventable

class Board(Tickable, Eventable):
    PLAYERS = ["blue", "orange"]

    def  __init__ (self, width, height):
        Tickable.__init__(self, 10)
        Eventable.__init__(self)
        self.__width = width
        self.__height = height
        self.__fields = []
        self.__currentHover = None
        self.__currentRound = 0

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

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
        pos = pos[0] if pos[0] <= self.__width - 1 else self.__width - 1, pos[1] if pos[1] <= self.__height - 1 else self.__height - 1
        self.__currentHover = pos

