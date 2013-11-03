from main.api.Unit import Unit
from main.api.Stats import Stats

class Warrior(Unit):

    def __init__(self, owner, actions=Unit.ACTIONS):
        Unit.__init__(self, Stats(6, 1, 2, 3, 12), "1", owner, actions=actions)
        self.name = "Unnamed Warrior"
