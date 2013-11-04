
class Stats(object):
    
    def __init__(self, attack=0, defence=0, attackRange=0, moveRange=0, hp=0):   
        self._attack = attack
        self._defence = defence
        self._attackRange = attackRange
        self._moveRange = moveRange
        self._hp = hp

    @property
    def attack(self):
        return self._attack
    
    @property
    def defence(self):
        return self._defence
    
    @property
    def attackRange(self):
        return self._attackRange
    
    @property
    def moveRange(self):
        return self._moveRange  
    
    @property
    def hp(self):
        return self._hp
    
    
      
