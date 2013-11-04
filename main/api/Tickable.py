
class Tickable():
    __priority = 0

    def __init__(self, priority=None):
        if(priority != None):
            self.__priority = priority

    @property
    def priority(self):
        return self.__priority

    def tick(self):
        pass

