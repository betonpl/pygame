
class Drawable():
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

    @property
    def screen(self):
        return self.game.screen

    def draw(self):
        pass

