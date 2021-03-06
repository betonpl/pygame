from main.api.Drawable import Drawable
from main.game.config.Constants import SQUARE_SIZE
from main.game.config.ImgRes import ImgRes
class GameDrawer(Drawable):

    def __init__(self, game, priority=None):
        Drawable.__init__(self, game, priority=priority)



    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()

        for x in range(0, self.game.size[0]):
            for y in range(0, self.game.size[1]):
                self.screen.blit(imageResources.getBackground(), [x * SQUARE_SIZE, y * SQUARE_SIZE])

