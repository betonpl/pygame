import pygame
from main.impl.Board import Board
from main.impl.BoardDrawer import BoardDrawer
from main.impl.GameDrawer import GameDrawer
from main.impl.EventManager import EventManager
from main.impl.UnitDrawer import UnitDrawer
from main.Constants import SQUARE_SIZE
from main.impl.ControlDrawer import ControlDrawer
from main.impl.Control import Control

class Game(object):
    def __init__(self):
        self.__fpsClock = pygame.time.Clock()
        self.__size = size = 21, 11
        self.__screen = None
        self.__eventManager = eventManager = EventManager(self)

        self.__board = board = Board(size[0], size[1] - 1, priority=1)
        self.__control = control = Control(board)

        self.registerEventListeners(board, control)
        self.__drawers = self.registerDrawers(BoardDrawer(self, 10), GameDrawer(self, 9), UnitDrawer(self, 21), ControlDrawer(self, 19))
        self.__tickers = self.registerTickers(board, eventManager, board.fieldManager, board.battleManager)

    def registerEventListeners(self, *listeners):
        for listener in listeners:
            listener.eventManager = self.eventManager

    def registerDrawers(self, *drawers):
        self.checkPriorities(drawers)
        return drawers

    def registerTickers(self, *tickers):
        self.checkPriorities(tickers)
        return tickers

    @property
    def eventManager(self):
        return self.__eventManager

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def size(self):
        return self.__size

    @property
    def board(self):
        return self.__board

    def initPyGame(self):
        pygame.init()
        pixelSize = self.size[0] * SQUARE_SIZE, self.size[1] * SQUARE_SIZE
        self.screen = pygame.display.set_mode(pixelSize, pygame.DOUBLEBUF)

    def loop(self):
        self.initPyGame()
        while self.__eventManager.tick():
            self.__tickersLoop()
            self.__drawersLoop()
            self.__fpsClock.tick(60)
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
            if element.priority > 0 and priorities.has_key(element.priority):
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
