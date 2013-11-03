from main.api.Drawer import Drawer
from main.ImgRes import ImgRes
from main.unit.Warrior import Warrior

class UnitDrawer(Drawer):
    
    def __init__(self, game, priority=0):
        Drawer.__init__(self, game, priority)
        
        ## MZI ## trzeba miec jakas jednostke
        ## MZI ## to jest czysto teoretyczny model
        self._unit = game.unit
    
    @property
    def unit(self):
        return self._unit
    
    def draw(self):
        Drawer.draw(self)
        imageResources = ImgRes.getInstance()
        
        ## MZI ## potrzebna pozycja
        pos = [0,0]
        
        u = Warrior("orange")
        
        self.screen().blit(imageResources.getPlayerBorder(self._unit.owner()), pos)
        self.screen().blit(imageResources.getUnitIcon(self._unit.image()))
        
        for x in range(0, 21):
            for y in range(0, 11):
                self.screen().blit(imageResources.getBackground(), [x * Drawer.SQUARE_SIZE, y * Drawer.SQUARE_SIZE])
        for x in range(0, 21):
            for y in range(0, 10):
                self.screen().blit(imageResources.getBorder(), [x * Drawer.SQUARE_SIZE, y * Drawer.SQUARE_SIZE])
        
        self.blitTranslated(imageResources.getActive(), self.board.currentHover)
