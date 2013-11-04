from main.api.Eventable import Eventable

class FieldManager(Eventable):

    def __init__(self, board):
        Eventable.__init__(self)
        self.__fields = []

    @property
    def fields(self):
        return self.__fields

