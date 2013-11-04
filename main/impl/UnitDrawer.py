from main.api.Drawable import Drawable
from main.ImgRes import ImgRes

class UnitDrawer(Drawable):

    def __init__(self, game, priority=0):
        Drawable.__init__(self, game, priority)


    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()

        # # MZI ## potrzebna pozycja
        for field in self.game.board.fields:
            if field.content.isAlive():
                self.drawUnit(imageResources, field.content, field.pos)

    def drawUnit(self, imageResources, unit, pos):
        ownerName = unit.owner.name
        self.blitTranslated(imageResources.getPlayerBorder(ownerName, float(unit.hp) / unit.stats.hp), pos)
        self.blitTranslated(imageResources.getUnitIcon(ownerName, unit.image), pos)
        if self.game.board.currentPlayer == unit.owner:
            self.blitTranslated(imageResources.getActionDot(0, 1 if unit.actions > 0 else 0), pos)
            self.blitTranslated(imageResources.getActionDot(1, 1 if unit.actions > 1 else 0), pos),
        if self.game.board.selected != None:
            self.blitTranslated(imageResources.getCursor(), self.game.board.selected.pos)
