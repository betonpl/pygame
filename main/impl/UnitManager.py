from main.api.Tickable import Tickable

class UnitManager(Tickable):

    def __init__(self, board, priority):
        Tickable.__init__(self, priority)
