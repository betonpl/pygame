from Field import Field
class CharacterUnit:
    
    def __init__(self, pos, stats, hp, image):
        self.__actions = 2
        self.__position = Field(pos.x,pos.y)
        self.__statAttack = stats[0]
        self.__statRange = stats[1]
        self.__statDefense = stats[2]
        self.__statSpeed = stats[3]
        self.__healthPoints = hp
        self.__image = image
        
    def refresh(self):
        self.__actions = 2 
        
    def getPosition(self):
        return self.__position;

    def move(self):
        if( not self.canDoSth() ):
            return
        self.__actions -= 1
        
    def attack(self, target):
        if( not self.canDoSth()):
            return
        target.defence( self.__statAttack )
        self.__actions -= 1
        
    def defence(self, value):
        dmg = value - self.__statDefense
        if( dmg > 0 ):
            self.__healthPoints -= dmg
            if( self.__healthPoints < 1 ):
                self.die()

    def die(self):
        return None
    
    def canDoSth(self):
        if( self.__actions > 0 ):
            return True
        return False
    
    def __drawers(self):
        return self.__image
