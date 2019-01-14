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

#Display live gathered item, monospace writing style, 40 is the size
MYFONT = pygame.font.SysFont("monospace", 40)
COUNTER = MYFONT.render("ITEM: 0", 1, (255, 255, 255))

#END message
MYFONT2 = pygame.font.SysFont("monospace", 20)
WIN = MYFONT.render("YOU WIN", 1, (255, 255, 255))
LOSS = MYFONT.render("YOU LOST", 1, (255, 255, 255))
CONTINUE = MYFONT2.render("PRESS ENTER TO RESTART OR ECHAP TO QUIT", 1, (255, 255, 255))

#First window with instructions of the game
MENUSCREEN = 1
END = 0

while MENUSCREEN:
    KEEPPLAYING = 0
    MENU = pygame.image.load(screen_menu)
    WINDOW.blit(MENU, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            MENUSCREEN = 0
            KEEPPLAYING = 0
        elif event.type == KEYDOWN and event.key == K_RETURN:
            KEEPPLAYING = 1
            MENUSCREEN = 0

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

        while KEEPPLAYING:
        #LOOP running automatically, game display
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

            if LEVEL.structure[MG.case_y][MG.case_x] == 'a':
                KEEPPLAYING = 0
                END = 1
    while END:
    #Enter a new loop and showing the maze with only wall, Macgyver does not show anymore
        WINDOW.blit(FLOOR, (0, 0))
        LEVEL.build(WINDOW)
        if TOTAL == 3:
            WINDOW.blit(WIN, (200, 240))
        elif TOTAL != 3:
            WINDOW.blit(LOSS, (200, 240))
        WINDOW.blit(CONTINUE, (40, 280))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                END = 0
            elif event.type == KEYDOWN and event.key == K_RETURN:
                MENUSCREEN = 1
                END = 0
