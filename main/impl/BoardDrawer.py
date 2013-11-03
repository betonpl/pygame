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
                self.screen.blit(imageResources.getBorder(), [x * SQUARE_SIZE, y * SQUARE_SIZE])

        self.blitTranslated(imageResources.getActive(), self.board.currentHover)
