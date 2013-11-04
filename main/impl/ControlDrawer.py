from main.api.Drawable import Drawable
from main.ImgRes import ImgRes
from main.impl.Control import Control

class ControlDrawer(Drawable):

    def __init__(self, game, priority=19):
        Drawable.__init__(self, game, priority)

    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()
        
        self.blitTranslated(imageResources.getButtonBorder(),Control.position)
        self.blitTranslated(imageResources.getSkipIcon(),Control.position)
        
