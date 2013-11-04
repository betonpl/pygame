from main.api.Drawable import Drawable
from main.ImgRes import ImgRes
from main.Constants import SQUARE_SIZE
import pygame.font

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
            self.blitTranslated(imageResources.getTarget(), self.board.selected.pos)
            
        myfont = pygame.font.SysFont("monospace", 64) 
        label = myfont.render('Active player: {0}'.format(self.board.currentPlayer.name), 1, (255,255,255)) 
        self.blitTranslated(label, 0, 10)
