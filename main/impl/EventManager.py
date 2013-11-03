from math import floor
import pygame
from pygame.locals import QUIT, K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEMOTION
from main.Constants import SQUARE_SIZE
from main.api.Tickable import Tickable

class EventManager(Tickable):
    HOVERABLE = 1
    CLICKABLE = 2
    __BROADCAST = -1.0, -1.0

    class __EventListener():
        def __init__(self, key, delegate):
            self.key = key
            self.delegate = delegate

    def __init__(self, game):
        Tickable.__init__(self, game, -1)
        self.__game = game
        self.listeners = {}
        self.listeners[EventManager.CLICKABLE] = []
        self.listeners[EventManager.HOVERABLE] = []

    def registerAtEventIfAble(self, pos, manager, flags, eventType):
        if eventType & flags:
            pos = pos if pos != None else EventManager.__BROADCAST
            self.listeners[eventType].append(EventManager.__EventListener(pos, manager))
    """
    @param pos: position
    @param manager: object with method click / hover
    @param flags: flags where should be use an manager at pos 
    """
    def register(self, pos, manager, flags=CLICKABLE):
        self.registerAtEventIfAble(pos, manager, flags, eventType=EventManager.CLICKABLE)
        self.registerAtEventIfAble(pos, manager, flags, eventType=EventManager.HOVERABLE)

    def __getListeners(self, event):
        return self.listeners[event]

    def unregister(self, pos):
        pos = pos if pos != None else EventManager.__BROADCAST
        for eventType, listeners in self.listeners:
            for listener in listeners:
                if self.__isBroadcastOrRegisteredService(pos, listener.key):
                    self.listeners[eventType].remove(listener)

    def __checkClicks(self, p):
        pos = self.__translateToPos(p)
        for listener in self.__getListeners(EventManager.CLICKABLE):
            if self.__isBroadcastOrRegisteredService(pos, listener.key):
                listener.delegate.click(pos)

    def __checkHovers(self, p):
        pos = self.__translateToPos(p)
        for listener in self.__getListeners(EventManager.HOVERABLE):
            if self.__isBroadcastOrRegisteredService(pos, listener.key):
                listener.delegate.hover(pos)

    def tick(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return False
            if event.type == MOUSEBUTTONDOWN :
                self.__checkClicks(pygame.mouse.get_pos())
            if event.type == MOUSEMOTION :
                self.__checkHovers(pygame.mouse.get_pos())
        return True

    @property
    def game(self):
        return self.__game

    @staticmethod
    def __translateToPos(p):
        return floor(p[0] / SQUARE_SIZE), floor(p[1] / SQUARE_SIZE)

    @staticmethod
    def __isBroadcastOrRegisteredService(pos, key):
        return key == pos or key == EventManager.__BROADCAST
