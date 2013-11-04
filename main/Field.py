from math import copysign, floor

class Field:

    def __init__(self, x, y, unit):
        self._x = x
        self._y = y
        self._unit = unit

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def unit(self):
        return self._unit

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        if(type(value, tuple)):
            self._x = value[0]
            self._y = value[1]

        if(type(value, Field)):
            self._x = value.x
            self._y = value.y


    def distanceFrom(self, field):
        return self.distanceBetween(self, field)

    @staticmethod
    def distanceBetween(field1, field2):
        distanceOnXAxe = copysign(field1.x - field2.x, 1)
        distanceOnYAxe = copysign(field1.y - field2.y, 1)
        return distanceOnXAxe if distanceOnXAxe > distanceOnYAxe else distanceOnYAxe

    def getPixelPosition(self):
        return [self._x * 64, self._y * 64]

    def __str__(self):
        return "x: " + str(self._x) + "\ty: " + str(self._y)

    @staticmethod
    def pxLocationToField(pos):
        return Field(floor(pos[0] / 64), floor(pos[1] / 64))

    @staticmethod
    def getOperationRadius(selected):
        unitRadius = selected.unit.stats.radius
        for x in xrange(selected.x - unitRadius, selected.x + unitRadius + 1):
            for y in xrange(selected.y - unitRadius, selected.y + unitRadius + 1):
                if Field.distanceBetween(selected, Field(x, y, None)):
                    yield (x, y)
