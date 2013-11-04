from main.Constants import SQUARE_SIZE

class Drawable():
    __priority = 0
    def __init__(self, game, priority=None):
        if(priority != None):
            self.__priority = priority
        self.__game = game

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

    def blitTranslated(self, image, x, y=None):
        if(x == None and y == None):
            return
        if isinstance(x, int) :
            blitPos = [x * SQUARE_SIZE, y * SQUARE_SIZE]
        else:
            blitPos = [x[0] * SQUARE_SIZE, x[1] * SQUARE_SIZE]
        self.screen.blit(image, blitPos)

