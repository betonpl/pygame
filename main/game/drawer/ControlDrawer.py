from main.api.Drawable import Drawable
from main.game.manager.Control import Control
from main.game.config.ImgRes import ImgRes

class ControlDrawer(Drawable):

    def __init__(self, game, priority=19):
        Drawable.__init__(self, game, priority)

    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()

        self.blitTranslated(imageResources.getButtonBorder(), Control.position)
        self.blitTranslated(imageResources.getSkipIcon(), Control.position)

