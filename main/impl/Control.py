from main.api.Eventable import Eventable
from main.impl.EventManager import EventManager

class Control(Eventable):
    
    position = (20,10)
    
    def  __init__ (self):
        Eventable.__init__(self)
        
    def afterEventManagerSet(self):
        self.eventManager.register(self.position, self, EventManager.CLICKABLE)
        
    def click(self,pos):
        print 'jestem w {0}!'.format(self.__class__)
        
    