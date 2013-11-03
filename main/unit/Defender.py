from main.api.Unit import Unit
from main.api.Stats import Stats

class Defender(Unit):
    
    def __init__(self, owner, actions=Unit.ACTIONS):
        Unit.__init__(self, Stats(4, 3, 1, 4, 15), "2", owner, actions=actions)
        self.name = "Unnamed Defender"

    
