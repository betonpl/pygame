from main.impl.EventManager import EventManager
from main.api.Tickable import Tickable
from main.api.Eventable import Eventable
from main.impl.BoardConfigure import BoardConfigure

class Board(Tickable, Eventable):

    def  __init__ (self, width, height, priority=1):
        Tickable.__init__(self, priority)
        Eventable.__init__(self)
        self.__size = dict(width=width, height=height)
        self.__fields = []
        self.__players = []
        self.__currentHover = None
        self.__currentRound = 0
        BoardConfigure(self)

    @property
    def width(self):
        return self.__size['width']

    @property
    def height(self):
        return self.__size['height']

    @property
    def fields(self):
        return self.__fields

    @property
    def currentHover(self):
        return self.__currentHover

    def addPlayer(self, player):
        self.__players.append(player)

    def addField(self, field):
        self.__fields.append(field)

    def afterEventManagerSet(self):
        self.eventManager.register(None, self, EventManager.HOVERABLE)
        self.eventManager.register(None, self, EventManager.CLICKABLE)

    def click(self, pos):
        pass

    def hover(self, pos):
        pos = pos[0] if pos[0] <= self.width - 1 else self.width - 1, pos[1] if pos[1] <= self.height - 1 else self.height - 1
        self.__currentHover = pos

