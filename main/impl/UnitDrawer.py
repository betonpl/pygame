from main.api.Drawable import Drawable
from main.ImgRes import ImgRes
from main.unit.Warrior import Warrior

class UnitDrawer(Drawable):

    def __init__(self, game, priority=0):
        Drawable.__init__(self, game, priority)

        # # MZI ## trzeba miec jakas jednostke
        # # MZI ## to jest czysto teoretyczny model
        self._unit = Warrior("orange")

    @property
    def unit(self):
        return self._unit

    def draw(self):
        Drawable.draw(self)
        imageResources = ImgRes.getInstance()

        # # MZI ## potrzebna pozycja
        pos = [0, 0]

        # # MZI ## ramka
        self.screen.blit(imageResources.getPlayerBorder(self._unit.owner), pos)

        # # MZI ## ikonka
        self.screen.blit(imageResources.getUnitIcon(self._unit.image), pos)

        # # MZI ## akcje
        self.screen.blit(imageResources.getActionDot(1, "g" if self._unit.actions > 0 else "gray"), pos)
        self.screen.blit(imageResources.getActionDot(2, "g" if self._unit.actions > 1 else "gray"), pos)
