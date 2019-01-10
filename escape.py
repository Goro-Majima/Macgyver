"""
Macgyver escape game is the first video game in pygame for my project 3
The goal is to move Macgyver over the maze in order to collect items and put the guard down.

Python scripts
Files: escape.py, constants.py, classes.py, maze + images

"""
import pygame
from pygame.locals import *
from constants import *
from classes import *

#pygame modules need to be initialized
pygame.init()

#Initialize game with title and logo.
WINDOW = pygame.display.set_mode((win_size, win_size))
FLOOR = pygame.image.load(image_floor).convert()
HERO = pygame.image.load(image_hero)
pygame.display.set_icon(HERO)
pygame.display.set_caption(window_title)

#First window with instructions of the game
PLAYING = 1
KEEPPLAYING = 1
while PLAYING:
    MENU = pygame.image.load(screen_menu)
    WINDOW.blit(MENU, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            PLAYING = 0
            KEEPPLAYING = 0
        elif event.type == KEYDOWN and event.key == K_RETURN:
            KEEPPLAYING = 1
            PLAYING = 0

#Display live gathered item, monospace writing style, 40 is the size
MYFONT = pygame.font.SysFont("monospace", 40)
COUNTER = MYFONT.render("ITEM: 0", 1, (255, 255, 255))

#END message
MYFONT2 = pygame.font.SysFont("monospace", 40)
WIN = MYFONT2.render("YOU WIN", 1, (255, 255, 255))
LOSS = MYFONT2.render("YOU LOST", 1, (255, 255, 255))
#Create the maze and randomly display items over it.
LEVEL = Level()
LEVEL.create()
ITEM = Items()
MG = Stargate(LEVEL)
#Here because we need to randomly spread once and not at each loop
ITEM.shuffle(LEVEL)

#Define variables
SYRINGE_COUNT = 0
ETHER_COUNT = 0
TUBE_COUNT = 0
TOTAL = 0

# #Generate win/loss label message.
# SCREEN = Tk()

while KEEPPLAYING:
#LOOP running automatically, auto display
    pygame.display.flip()

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            KEEPPLAYING = 0
        elif event.type == KEYDOWN:

            if event.key == K_RIGHT:
                MG.moveto("right")
            elif event.key == K_LEFT:
                MG.moveto('left')
            elif event.key == K_UP:
                MG.moveto('up')
            elif event.key == K_DOWN:
                MG.moveto('down')
    WINDOW.blit(FLOOR, (0, 0))
    LEVEL.build(WINDOW)
    WINDOW.blit(MG.direction, (MG.x_axis, MG.y_axis))
    WINDOW.blit(COUNTER, (120, 0))
    ITEM.showobjects(WINDOW, SYRINGE_COUNT, TUBE_COUNT, ETHER_COUNT)
    pygame.display.flip()


    if LEVEL.structure[MG.case_y][MG.case_x] == 'a' and TOTAL != 3:
	    #Need to create text bubble
        WINDOW.blit(LOSS, (200, 240))
        pygame.display.flip()
        # FIELD = Label(SCREEN, text="  The guard caught you ! GAME OVER.  ")
        # FIELD.pack()
        # SCREEN.mainloop()
    elif LEVEL.structure[MG.case_y][MG.case_x] == 'a' and TOTAL == 3:
        # FIELD = Label(SCREEN, text="  You put the guard down. Nice escape,\
        # congratulations, you just beat the game !!  ")
        # FIELD.pack()
        # SCREEN.mainloop()
        WINDOW.blit(WIN, (200, 240))
        pygame.display.flip()
    if MG.case_y == ITEM.rysyr and MG.case_x == ITEM.rxsyr and SYRINGE_COUNT == 0:
        SYRINGE_COUNT += 1
        TOTAL += 1

        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 255, 255))
    if MG.case_y == ITEM.rytube and MG.case_x == ITEM.rxtube and TUBE_COUNT == 0:
        TUBE_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 255, 255))
    if MG.case_y == ITEM.ryether and MG.case_x == ITEM.rxether and ETHER_COUNT == 0:
        ETHER_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 255, 255))
