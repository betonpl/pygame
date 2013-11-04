import pygame
from math import ceil

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

    def getPlayerBorder(self, color, precent):
        # return self.getImage( "unit/hit_points_" + color + "_" + str(precent) )
        if precent >= 0 and precent <= 1 :
            return self.getImage('unit/hit_points_{0}_{1}'.format(color, int(ceil((float(precent)) * 10) * 10)))
        print 'precent in ImgRes.getPlayerBorder(color,border) must be value from 0 to 1. Now is {0}'.format(precent)

    def getCursor(self):
        return self.getImage('interface/cursor')

    def getCrosshair(self):
        return self.getImage('interface/crosshair')

    def getRange(self, color):
        return self.getImage('board/{0}'.format(color))

    def getUnitIcon(self, color, icon):
        return self.getImage('unit/{0}_{1}'.format(color, icon))

    def getSkipIcon(self):
        return self.getImage('interface/button_skip')

    def getBackground(self):
        return self.getImage('board/bg')

    def getBorder(self):
        return self.getImage('board/border')

    def getButtonBorder(self):
        return self.getImage('interface/button_border')

    def getTarget(self):
        return self.getImage('interface/target')

    def getActionDot(self, dotId, status):
        return self.getImage('unit/action_{0}_{1}'.format(dotId, status))
