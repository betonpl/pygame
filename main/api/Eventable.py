class Eventable(object):

    def __init__(self):
        self.__eventManager = None

    @property
    def eventManager(self):
        return self.__eventManager

    @eventManager.setter
    def eventManager(self, eventManager):
        self.__eventManager = eventManager
        self.afterEventManagerSet()

    def afterEventManagerSet(self):
        pass
