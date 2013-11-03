import pygame
from main.Board import Board
from main.impl.BoardDrawer import BoardDrawer
from main.impl.GameDrawer import GameDrawer
from main.impl.EventManager import EventManager

class Game(object):

    def __init__(self):
        pygame.init()

        # # MZI ## FPSy sa dobre
        self.fpsClock = pygame.time.Clock()
        self.__drawers = self.__tickers = None
        size = 1280 + 64, 640 + 64
        self.__screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
        pygame.mouse.set_visible(1)
        self.__eventManager = None
        self.__board = Board(21, 10, self)
        self.registerEventManager(EventManager(self), self.__board)
        self.registerDrawers(BoardDrawer(self, 10), GameDrawer(self, 20))
        self.registerTickers(self.__board)

    def registerEventManager(self, eventManager, *eventables):
        self.__eventManager = eventManager
        for eventable in eventables:
            eventable.setEventManager(eventManager)
            eventable.afterEventManagerSet()

    def registerDrawers(self, *drawers):
        self.__drawers = drawers

    def registerTickers(self, *tickers):
        self.__tickers = tickers

    def screen(self):
        return self.__screen

    @property
    def board(self):
        return self.__board

    @staticmethod
    def game_exit():
        exit()

    def __tick(self):
        pass

    def loop(self):
        while self.__eventManager.tick():
            self.__tick()
            self.draw()
            self.fpsClock.tick(60)
        self.game_exit()

    def draw(self):
        drawers = list(self.__drawers[:])
        currentPriority = 0
        while(len(drawers) > 0):
            for drawer in drawers:
                if drawer.priority < 0:
                    drawers.remove(drawer)
                elif drawer.priority == currentPriority :
                    drawer.draw()
                    drawers.remove(drawer)
            currentPriority += 1
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.loop()
