from main.api.Tickable import Tickable
from main.api.Eventable import Eventable
import math
from main.game.manager.FieldManager import FieldManager
from main.game.manager.BattleManager import BattleManager, Battle
from main.game.config.BoardConfigure import BoardConfigure
from main.game.manager.EventManager import EventManager

class Board(Tickable, Eventable):

    def  __init__ (self, width, height, priority):
        Tickable.__init__(self, priority)
        Eventable.__init__(self)
        self.__size = dict(width=width, height=height)
        self.__players = self.__currentPlayer = self.__currentHover = self.__fieldManager = None
        self.__fieldManager = FieldManager(self, self.priority + 1)
        self.__battleManager = BattleManager(self.priority + 2)
        self.__newGame()

    def __newGame(self):
        self.__players = []
        self.__currentPlayer = None
        self.__currentHover = None
        self.fieldManager.resetManager()
        BoardConfigure(self)
    @property
    def width(self):
        return self.__size['width']

    @property
    def height(self):
        return self.__size['height']

    @property
    def fields(self):
        return self.__fieldManager.fields

    @property
    def players(self):
        return self.__players

    @property
    def currentHover(self):
        return self.__currentHover

    @property
    def currentPlayer(self):
        return self.__currentPlayer

    @property
    def selected(self):
        return self.__fieldManager.selected

    @property
    def fieldManager(self):
        return self.__fieldManager

    @property
    def battleManager(self):
        return self.__battleManager

    @currentPlayer.setter
    def currentPlayer(self, value):
        if len(self.players) > 0 and value in self.players:
            self.__currentPlayer = value

    def addPlayer(self, player):
        self.__players.append(player)

    def addField(self, field):
        self.__fieldManager.addField(field)

    def afterEventManagerSet(self):
        self.eventManager.register(None, self, EventManager.HOVERABLE)
        self.eventManager.register(None, self.__fieldManager, EventManager.CLICKABLE)

    def isAllExhausted(self):
        if len(self.fields) == 0:
            return False
        for field in self.fields:
            if field.unit.owner == self.currentPlayer and not field.unit.isExhausted():
                return False
        return True

    def tick(self):
        if self.currentPlayer == None:
            self.currentPlayer = self.__players[0]
        if self.isAllExhausted():
            self.nextRound()
        for action in self.fieldManager.actions:
            if(action['action'] == 'attack'):
                self.battleManager.addBattle(Battle(action['source'].unit, action['dest'].unit))
                self.fieldManager.actions.remove(action)

    def hover(self, pos):
        self.__currentHover = pos if self.isInside(pos) else None

    def nextRound(self):
        currentPlayerIndex = self.players.index(self.currentPlayer)
        nextPlayerIndex = int(math.fmod(currentPlayerIndex + 1, len(self.players)))
        self.currentPlayer = self.players[nextPlayerIndex]
        self.fieldManager.reset()

    def isInside(self, pos):
        return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height
