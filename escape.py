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
COUNTER = MYFONT.render("Items: 0", 1, (255, 25, 0))

#Create the maze and randomly display items over it.
level = Level()
level.create()
items = Items()
MG = Stargate(level)
level.cast(WINDOW)
items.shuffle(level)
pygame.display.flip()

#Define variables
SYRINGE_COUNT = 0
ETHER_COUNT = 0
TUBE_COUNT = 0
TOTAL = 0

#Generate win/loss message.
screen = Tk()

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
    level.cast(WINDOW)
    WINDOW.blit(MG.direction, (MG.x_axis, MG.y_axis))
    WINDOW.blit(COUNTER, (120, 0))
    items.showobjects(WINDOW, SYRINGE_COUNT, TUBE_COUNT, ETHER_COUNT)
    pygame.display.flip()


    if level.structure[MG.case_y][MG.case_x] == 'a' and TOTAL != 3:
	    #Need to create text bubble
        KEEPPLAYING = 0
        label_field = Label(screen, text="  The guard caught you ! GAME OVER.  ")
        label_field.pack()
        screen.mainloop()
    elif level.structure[MG.case_y][MG.case_x] == 'a' and TOTAL == 3:
        KEEPPLAYING = 0
        label_field = Label(screen, text="  You put the guard down. nice escape, \
        Congratulations you just beat the game !!  ")
        label_field.pack()
        screen.mainloop()
    if MG.case_y == items.rysyr and MG.case_x == items.rxsyr and SYRINGE_COUNT == 0:
        SYRINGE_COUNT += 1
        TOTAL += 1

        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 25, 0))
    if MG.case_y == items.rytube and MG.case_x == items.rxtube and TUBE_COUNT == 0:
        TUBE_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 55, 0))
    if MG.case_y == items.ryether and MG.case_x == items.rxether and ETHER_COUNT == 0:
        ETHER_COUNT = 1
        TOTAL += 1
        COUNTER = MYFONT.render("Items: "+ str(TOTAL), 1, (255, 25, 0))
