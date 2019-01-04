"""1st video game in pygame for my project 3"""
from tkinter import *
import pygame
from pygame.locals import *
from constants import *
from classes import *
pygame.init()

#Initialize interface with title and logo.
WINDOW = pygame.display.set_mode((win_size, win_size))
FLOOR = pygame.image.load(image_floor).convert()
HERO = pygame.image.load(image_hero)
pygame.display.set_icon(HERO)
pygame.display.set_caption(window_title)

#Display live gathered item
MYFONT = pygame.font.SysFont("monospace", 40)
COUNTER = MYFONT.render("ITEM: 0", 1, (255, 25, 0))

#Create the maze and randomly display items over it.
LEVEL = Level()
LEVEL.create()
ITEM = Items()
MG = Stargate(LEVEL)
LEVEL.cast(WINDOW)
ITEM.shuffle(LEVEL)
pygame.display.flip()

#Define variables
SYRINGE_COUNT = 0
ETHER_COUNT = 0
TUBE_COUNT = 0
TOTAL = 0

#Generate win/loss message.
SCREEN = Tk()

KEEPPLAYING = 1
while KEEPPLAYING:
#LOOP running automatically, auto display
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
    LEVEL.cast(WINDOW)
    WINDOW.blit(MG.direction, (MG.x_axis, MG.y_axis))
    WINDOW.blit(COUNTER, (120, 0))
    ITEM.showobjects(WINDOW, SYRINGE_COUNT, TUBE_COUNT, ETHER_COUNT)
    pygame.display.flip()


    if LEVEL.structure[MG.case_y][MG.case_x] == 'a' and TOTAL != 3:
	    #Need to create text bubble
        KEEPPLAYING = 0
        FIELD = Label(SCREEN, text="  The guard caught you ! GAME OVER.  ")
        FIELD.pack()
        SCREEN.mainloop()
    elif LEVEL.structure[MG.case_y][MG.case_x] == 'a' and TOTAL == 3:
        KEEPPLAYING = 0
        FIELD = Label(SCREEN, text="  You put the guard down. nice escape, \
        Congratulations you just beat the game !!  ")
        FIELD.pack()
        SCREEN.mainloop()
    if MG.case_y == ITEM.rysyr and MG.case_x == ITEM.rxsyr and SYRINGE_COUNT == 0:
        SYRINGE_COUNT += 1
        TOTAL += 1

        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 25, 0))
    if MG.case_y == ITEM.rytube and MG.case_x == ITEM.rxtube and TUBE_COUNT == 0:
        TUBE_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 55, 0))
    if MG.case_y == ITEM.ryether and MG.case_x == ITEM.rxether and ETHER_COUNT == 0:
        ETHER_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 25, 0))
