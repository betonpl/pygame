import pygame

class ImgRes:
    
    instance = None
    
    def __init__(self):
        self.path = "res/img/"
        self.resources = {}
    
    @staticmethod
    def getInstance():
        if ImgRes.instance == None:
            ImgRes.instance = ImgRes()
        return ImgRes.instance
    
    def getImage(self, img):
        if img in self.resources:
            return self.resources[img]
        else:
            self.resources[img] = self.loadImage(img)
            return self.getImage(img)
    
    def loadImage(self, img):
        return pygame.image.load(self.path + img + ".png").convert_alpha()
    
    def getPlayerBorder(self, color):
        return self.getImage(color + "0")
    
    def getActive(self):
        return self.getImage("active")
    
    def getCrosshair(self):
        return self.getImage("crosshair")
    
    def getRange(self, color):
        return self.getImage(color)
    
    def getUnitIcon(self, color, iconId):
        return self.getImage(color + str(iconId))
    
    def getMenuIcon(self, iconId):
        return self.getImage("menu" + str(iconId))
    
    def getBackground(self):
        return self.getImage("bg")
    
    def getBorder(self):
        return self.getImage("border")
    
    def getButtonBorder(self):
        return self.getImage("button_border")
    
    def getActionDot(self,id,color):
        return self.getImage("action"+str(id)+color)
