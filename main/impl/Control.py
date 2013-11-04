from main.api.Eventable import Eventable
from main.impl.EventManager import EventManager

class Control(Eventable):

    position = (10, 10)

    def  __init__ (self, board):
        Eventable.__init__(self)
        self.__board = board

    def afterEventManagerSet(self):
        self.eventManager.register(self.position, self, EventManager.CLICKABLE)

    def click(self, pos):
        self.__board.nextRound()

