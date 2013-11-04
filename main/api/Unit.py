class Unit(object):
    ACTIONS = 2
       
    def __init__(self, stats, image, owner, actions=ACTIONS):
        self._stats = stats
        self._image = image
        self._actions = actions
        self._hp = stats.hp
        self._owner = owner
        self._name = ""
        self.__maxActions = actions 
            
    @property
    def stats(self):
        return self._stats
    
    @property
    def image(self):
        return self._image

    @property 
    def hp(self):
        return self._hp
    
    @property 
    def actions(self):
        return self._actions
    
    @property
    def owner(self):
        return self._owner
                    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
            
    def hit(self, by):
        self._hp = self._hp - by if by < self._hp else 0

    def isAlive(self):
        return self.hp > 0
    
    def isDead(self):
        return not self.isAlive()
    
    def isExhausted(self):
        return self.actions < 1
        
    def countActionPoints(self):
        self._actions -= 1
    
    def resetActions(self):
        self._actions = self.__maxActions
