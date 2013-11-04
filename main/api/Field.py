from math import copysign, floor
import math

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

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def unit(self):
        return self._unit

    @property
    def pos(self):
        return self.x, self.y

    def moveTo(self, value):
        if(isinstance(value, tuple)):
            self.x = int(value[0])
            self.y = int(value[1])

        if(isinstance(value, Field)):
            self.x = int(value.x)
            self.y = int(value.y)
        self.unit.countActionPoints()

    def distanceFrom(self, field):
        return self.distanceBetween(self, field)

    @staticmethod
    def distanceBetween(field1, field2):
        distanceOnXAxe = copysign(field1.x - field2.x, 1)
        distanceOnYAxe = copysign(field1.y - field2.y, 1)
        return math.floor(math.sqrt (distanceOnXAxe ** 2 + distanceOnYAxe ** 2))

    def __str__(self):
        return "x: " + str(self.x) + "\ty: " + str(self.y)

    @staticmethod
    def pxLocationToField(pos):
        return Field(floor(pos[0] / 64), floor(pos[1] / 64))

    @staticmethod
    def getRange(selected, rangeValue):
        selectedPos = (int(selected.pos[0]), int(selected.pos[1]))
        for x in range(selectedPos[0] - rangeValue, selectedPos[0] + rangeValue + 1):
            for y in range(selectedPos[1] - rangeValue, selectedPos[1] + rangeValue + 1):
                if Field.distanceBetween(selected, Field(x, y, None)) <= rangeValue:
                    yield (x, y)

