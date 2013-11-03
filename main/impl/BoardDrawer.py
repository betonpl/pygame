from main.api.Drawable import Drawable
from main.ImgRes import ImgRes
from main.Constants import SQUARE_SIZE

class BoardDrawer(Drawable):

    def __init__(self, game, priority=0):
        Drawable.__init__(self, game, priority)
        self._board = game.board

    @property
    def board(self):
        return self._board

    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()
        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                self.screen().blit(imageResources.getBackground(), [x * SQUARE_SIZE, y * SQUARE_SIZE])
        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                self.screen().blit(imageResources.getBorder(), [x * SQUARE_SIZE, y * SQUARE_SIZE])

        self.blitTranslated(imageResources.getActive(), self.board.currentHover)

    def blitTranslated(self, image, x, y=None):
        if(x == None and y == None):
            return
        if len(x) == 2:
            blitPos = [x[0] * SQUARE_SIZE, x[1] * SQUARE_SIZE]
        else:
            blitPos = [x * SQUARE_SIZE, y * SQUARE_SIZE]
        self.screen().blit(image, blitPos)


