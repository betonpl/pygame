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
        self.__currentPlayer = None
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
    def players(self):
        return self.__players

    @property
    def currentHover(self):
        return self.__currentHover

    @property
    def currentPlayer(self):
        return self.__currentPlayer

    @currentPlayer.setter
    def currentPlayer(self, value):
        if len(self.players) > 0 and value in self.players:
            self.__currentPlayer = value

    def addPlayer(self, player):
        self.__players.append(player)

    def addField(self, field):
        self.__fields.append(field)

    def afterEventManagerSet(self):
        self.eventManager.register(None, self, EventManager.HOVERABLE)
        self.eventManager.register(None, self, EventManager.CLICKABLE)

    def click(self, pos):
        pass

    def tick(self):
        if self.currentPlayer == None:
            self.currentPlayer = self.__players[0]

    def hover(self, pos):
        self.__currentHover = pos if self.isInside(pos) else None

    def isInside(self, pos):
        return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height
