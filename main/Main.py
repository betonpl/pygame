import pygame, sys
from CharacterUnit import CharacterUnit
from Board import Board
from Field import Field
from pygame.tests.test_utils import xrange_
from main.ImgRes import ImgRes
 

def drawUnits(units):
    for u in units:
        screen.blit(u.__drawers(), u.getPosition().getPixelPosition())
        
pygame.init()
# 157.158.38.222:3480 http 3422 ssh python python123 varwwwhtml

size = width, height = 1280 + 64, 640 + 64
screen = pygame.display.set_mode(size)

pygame.mouse.set_pos([1, 1])
pygame.mouse.set_visible(1)
imgResources = ImgRes.getInstance()
background = imgResources.getBackground()
board = imgResources.getBorder()
mouse = imgResources.getActive()
buttonBorder = imgResources.getButtonBorder()
menu1 = imgResources.getMenuIcon(1)
menu2 = imgResources.getMenuIcon(2)
menu3 = imgResources.getMenuIcon(3)

player1Units = []
player1Units.insert(0, CharacterUnit(Field(2, 0), [4, 1, 2, 3], 10, imgResources.getUnitIcon('blue', 1)))
player1Units.insert(1, CharacterUnit(Field(1, 1), [2, 1, 4, 2], 10, imgResources.getUnitIcon('blue', 2)))
player1Units.insert(2, CharacterUnit(Field(0, 2), [3, 1, 3, 4], 10, imgResources.getUnitIcon('blue', 3)))

player2Units = []
player2Units.insert(0, CharacterUnit(Field(18, 9), [4, 1, 2, 3], 10, imgResources.getUnitIcon('orange', 1)))
player2Units.insert(1, CharacterUnit(Field(19, 8), [2, 1, 4, 2], 10, imgResources.getUnitIcon('orange', 2)))
player2Units.insert(2, CharacterUnit(Field(20, 7), [3, 1, 3, 4], 10, imgResources.getUnitIcon('orange', 3)))
clock = pygame.time.Clock()
accPx, accPy = 0, 0
state = 1

while state > 0:
    clock.tick_busy_loop(40)
    for x in xrange(0, 21):
        for y in range(0, 11):
            screen.blit(background, [x * 64, y * 64])
    for x in range(0, 21):
        for y in range(0, 10):
            screen.blit(board, [x * 64, y * 64])
            
    screen.blit(menu1, [576 , 640])
    screen.blit(menu2, [640 , 640])
    screen.blit(menu3, [704 , 640])
    screen.blit(buttonBorder, [576 , 640])
    screen.blit(buttonBorder, [640 , 640])
    screen.blit(buttonBorder, [704 , 640])
    
    drawUnits(player1Units)
    drawUnits(player2Units)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit   
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            state = 0
        if event.type == pygame.MOUSEMOTION: 
            px, py = pygame.mouse.get_pos()
            accPx, accPy = px / 64, py / 64
    screen.blit(mouse, [accPx * 64, accPy * 64])
    pygame.display.set_caption("Fps:" + str(clock.get_fps()))
    pygame.display.flip()
    
