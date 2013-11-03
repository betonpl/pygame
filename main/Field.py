from math import copysign, floor

class Field:

    def __init__(self, x, y, content):
        self._x = x
        self._y = y
        self._content = content

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def content(self):
        return self._content

    @property
    def pos(self):
        return self.x, self.y

    def distanceFrom(self, field):
        distanceOnXAxe = copysign(self.x - field.x, 1)
        distanceOnYAxe = copysign(self.y - field.y, 1)
        return distanceOnXAxe if distanceOnXAxe > distanceOnYAxe else distanceOnYAxe

    def getPixelPosition(self):
        return [self._x * 64, self._y * 64]

    def __str__(self):
        return "x: " + str(self._x) + "\ty: " + str(self._y)

    @staticmethod
    def pxLocationToField(pos):
        return Field(floor(pos[0] / 64), floor(pos[1] / 64))
