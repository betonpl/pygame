from main.api.Drawable import Drawable
from main.ImgRes import ImgRes
from main.unit.Warrior import Warrior

class UnitDrawer(Drawable):

    def __init__(self, game, priority=0):
        Drawable.__init__(self, game, priority)


    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()

        # # MZI ## potrzebna pozycja
        for field in self.game.board.fields:
            self.drawUnit(imageResources, field.content, field.pos)

    def drawUnit(self, imageResources, unit, pos):
        ownerName = unit.owner.name
        self.blitTranslated(imageResources.getPlayerBorder(ownerName, float(unit.hp) / unit.stats.hp), pos)
        self.blitTranslated(imageResources.getUnitIcon(ownerName, unit.image), pos)
        self.blitTranslated(imageResources.getActionDot(0, 1 if unit.actions > 0 else 0), pos)
        self.blitTranslated(imageResources.getActionDot(1, 1 if unit.actions > 1 else 0), pos)
