from main.api.Drawable import Drawable
import pygame.font
from main.game.config.Constants import SQUARE_SIZE
from main.game.config.ImgRes import ImgRes
from main.api.Field import Field

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
        self.blitTranslated(imageResources.getCursor(), self.board.currentHover)


        if self.game.board.selected != None:
            self.drawSelected(imageResources)

        myfont = pygame.font.SysFont("monospace", 64)
        label = myfont.render('Active player: {0}'.format(self.board.currentPlayer.name), 1, (255, 255, 255))
        self.blitTranslated(label, 0, 10)

    def drawSelected(self, imageResources):
        selected = self.board.selected
        self.blitTranslated(imageResources.getTarget(), selected.x, selected.y)

        for pos in Field.getRange(selected, selected.unit.stats.moveRange):
            if(self.board.isInside(pos)):
                self.blitTranslated(imageResources.getRange("green"), pos)

        for pos in Field.getRange(selected, selected.unit.stats.attackRange):
            if(self.board.isInside(pos)):
                self.blitTranslated(imageResources.getRange("red"), pos)
