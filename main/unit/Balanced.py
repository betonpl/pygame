from main.api.Unit import Unit
from main.api.Stats import Stats

class Balanced(Unit):
    
    def __init__(self, owner, actions=Unit.ACTIONS):
        Unit.__init__(self, Stats(5, 2, 1, 5, 10), "3", owner, actions=actions)
        self.name = "Unnamed Balanced"
    