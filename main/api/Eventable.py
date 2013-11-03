class Eventable(object):
    
    def __init__(self):
        self.__eventManager = None
    
    @property 
    def eventManager(self):
        return self.__eventManager
    
    def setEventManager(self, eventManager):
        self.__eventManager = eventManager
        
    def afterEventManagerSet(self):
        pass