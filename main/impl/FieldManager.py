from main.api.Eventable import Eventable

class FieldManager(Eventable):

    def __init__(self, board):
        Eventable.__init__(self)
        self.__fields = []

    @property
    def fields(self):
        return self.__fields

    def addField(self, field):
        self.__fields.append(field)

    def getFieldAtPos(self, pos):
        for field in self.fields:
            if field.pos == pos:
                return field
        return None
