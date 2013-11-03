from main.api.Drawer import Drawer
from main.ImgRes import ImgRes

class BoardDrawer(Drawer):

    def __init__(self, game, priority=0):
        Drawer.__init__(self, game, priority)
        self._board = game.board

    @property
    def board(self):
        return self._board

    def draw(self):
        Drawer.draw(self)
        imageResources = ImgRes.getInstance()
        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                self.screen().blit(imageResources.getBackground(), [x * Drawer.SQUARE_SIZE, y * Drawer.SQUARE_SIZE])
        for x in range(0, self.board.width):
            for y in range(0, self.board.height):
                self.screen().blit(imageResources.getBorder(), [x * Drawer.SQUARE_SIZE, y * Drawer.SQUARE_SIZE])

        self.blitTranslated(imageResources.getActive(), self.board.currentHover)

    def blitTranslated(self, image, x, y=None):
        if(x == None and y == None):
            return
        if len(x) == 2:
            blitPos = [x[0] * Drawer.SQUARE_SIZE, x[1] * Drawer.SQUARE_SIZE]
        else:
            blitPos = [x * Drawer.SQUARE_SIZE, y * Drawer.SQUARE_SIZE]
        self.screen().blit(image, blitPos)


