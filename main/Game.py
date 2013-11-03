import pygame
from main.impl.Board import Board
from main.impl.BoardDrawer import BoardDrawer
from main.impl.GameDrawer import GameDrawer
from main.impl.EventManager import EventManager
from main.impl.UnitDrawer import UnitDrawer
from main.Constants import SQUARE_SIZE
from main.impl.UnitManager import UnitManager


class Game(object):
    def __init__(self):
        pygame.init()

        self.fpsClock = pygame.time.Clock()
        self.__drawers = self.__tickers = None
        self.__size = size = 21, 11
        pixelSize = size[0] * SQUARE_SIZE , size[1] * SQUARE_SIZE
        self.__screen = pygame.display.set_mode(pixelSize, pygame.DOUBLEBUF)
        pygame.mouse.set_visible(1)
        self.__eventManager = None
        self.__board = board = Board(21, 10)
        self.__unitManager = unitManager = UnitManager(board, 11)
        eventManager = self.registerEventManager(EventManager(self), self.__board)
        self.registerDrawers(BoardDrawer(self, 10), GameDrawer(self, 9), UnitDrawer(self, 21))
        self.registerTickers(board, unitManager, eventManager)

    def registerEventManager(self, eventManager, *eventables):
        self.__eventManager = eventManager
        for eventable in eventables:
            eventable.setEventManager(eventManager)
            eventable.afterEventManagerSet()
        return self.__eventManager

    def registerDrawers(self, *drawers):
        self.checkPriorities(drawers)
        self.__drawers = drawers

    def registerTickers(self, *tickers):
        self.checkPriorities(tickers)
        self.__tickers = tickers

    @property
    def screen(self):
        return self.__screen

    @property
    def size(self):
        return self.__size
    @property
    def board(self):
        return self.__board

    def loop(self):
        while self.__eventManager.tick():
            self.__tickersLoop()
            self.__drawersLoop()
            self.fpsClock.tick(60)
        self.game_exit()

    def __tickersLoop(self):
        for ticker in self.priorityGenerator(self.__tickers):
            ticker.tick()

    def __drawersLoop(self):
        for drawer in self.priorityGenerator(self.__drawers):
            drawer.draw()
        pygame.display.flip()

    @staticmethod
    def priorityGenerator(inputList):
        inputList = list(inputList)
        currentPriority = 0

        while(len(inputList) > 0):
            for element in inputList:
                if element.priority < 0:
                    inputList.remove(element)
                    continue
                elif element.priority == currentPriority:
                    inputList.remove(element)
                    yield element
            currentPriority += 1

    @staticmethod
    def checkPriorities(inputList):
        priorities = {}
        for element in inputList:
            if  priorities.has_key(element.priority):
                raise Exception("Priorities cannot be the same in {0} and {1} due to deadlock at generator"
                                .format(str(element), str(priorities.get(element.priority))))
            priorities[element.priority] = element
        return True

    @staticmethod
    def game_exit():
        exit()
if __name__ == '__main__':
    game = Game()
    game.loop()
