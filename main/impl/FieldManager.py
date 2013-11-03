from main.api.Tickable import Tickable

class FieldManager(Tickable):

    def __init__(self, board, priority):
        Tickable.__init__(self, priority)


