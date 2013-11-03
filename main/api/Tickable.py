
class Tickable():
    __priority = 0
    
    def __init__(self, game, priority=None):
        if(priority != None):
            self.__priority = priority
        self.__game = game
        print str(self.__class__) + " priority is " + str(priority)

    @property 
    def priority(self):
        return self.__priority
    
    @property 
    def game(self):
        return self.__game

    def tick(self):
        pass
    
