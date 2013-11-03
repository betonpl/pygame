
class Stats(object):
    
    def __init__(self, attack=0, defence=0, radius=0, speed=0, hp=0):   
        self._attack = attack
        self._defence = defence
        self._radius = radius
        self._speed = speed
        self._hp = hp

    @property
    def attack(self):
        return self._attack
    
    @property
    def defence(self):
        return self._defence
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def speed(self):
        return self._speed  
    
    @property
    def hp(self):
        return self._hp
    
    
      
