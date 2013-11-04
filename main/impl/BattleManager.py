from main.api.Tickable import Tickable

class Battle():
    def __init__(self, attacker, defender):
        self.__attacker = attacker
        self.__defender = defender
        calculatedDamage = self.calcDamage(attacker, defender)
        self.__damage = calculatedDamage if calculatedDamage > 0 else 0
    
    @property
    def damage(self):
        return self.__damage

    @property
    def attacker(self):
        return self.__attacker    

    @property
    def defender(self):
        return self.__defender    
    
    @staticmethod
    def calcDamage(attacker, defender):
        return attacker.stats.attack - defender.stats.defence

class BattleManager(Tickable):

    def __init__(self, priority):
        Tickable.__init__(self, priority)
        self.__battles = []
        
    def tick(self):
        for battle in self.__battles:
            self.__resolveBattle(battle)
            self.__battles.remove(battle)
    
    def addBattle(self, battle):
        self.__battles.append(battle) 
            
    def __resolveBattle(self, battle):
        battle.defender.hit(battle.damage)
        battle.attacker.countActionPoints()
    
