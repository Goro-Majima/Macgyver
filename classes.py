'''Classes for the creation of the maze, moving hero and items'''
import random
import pygame
from pygame.locals import *
from constants import *
class Level:
    """ Init the level structure."""
    def __init__(self):
        self.structure = 0
    def create(self):
        """Run through the file maze and append each letter to its line into a list """
        with open("maze", "r") as fichier:
            level_structure = []
            for line in fichier:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_structure.append(level_line)
            self.structure = level_structure

    def cast(self, window):
        """ Initialize the labyrinth according to the structure list. """
        wall = pygame.image.load(image_wall).convert()
        badguy = pygame.image.load(image_badguy).convert_alpha()
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x_axis = num_case * sprite_size
                y_axis = num_line * sprite_size
                if sprite == 'm':
                    window.blit(wall, (x_axis, y_axis))
                elif sprite == 'a':
                    window.blit(badguy, (x_axis, y_axis))
                num_case += 1
            num_line += 1

class Stargate:
    """Init the Hero and set to his starting position. """
    def __init__(self, level):

        self.macgyver = pygame.image.load("images/MacGyver.png").convert_alpha()

        self.case_x = 0
        self.case_y = 0
        self.x_axis = 0
        self.y_axis = 0
        self.direction = self.macgyver
        self.level = level
    def moveto(self, direction):
        """ Creation of his move and boundaries """
        if direction == "right":
            #Avoid right boundary
            if self.case_x < (numberofsprite - 1):
                if self.level.structure[self.case_y][self.case_x+1] != "m":
                    #Avoid right boundary
                    self.case_x += 1
                    self.x_axis = self.case_x * sprite_size

        #Moving left
        if direction == 'left':
            #Avoid left boundary
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x_axis = self.case_x * sprite_size

        #Moving up
        if direction == 'up':
            #Y  inversed
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y_axis = self.case_y * sprite_size

        #Moving down
        if direction == 'down':
            if self.case_y < (numberofsprite - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y_axis = self.case_y * sprite_size
class Items:
    """ Init items randomly on the floor map."""
    def __init__(self):
        self.rxsyr = random.randint(0, numberofsprite-1)
        self.rysyr = random.randint(0, numberofsprite-1)
        self.rxtube = random.randint(0, numberofsprite-1)
        self.rytube = random.randint(0, numberofsprite-1)
        self.rxether = random.randint(0, numberofsprite-1)
        self.ryether = random.randint(0, numberofsprite-1)
               #init coordinates
        self.x_syringe = 0
        self.y_syringe = 0
        self.x_tube = 0
        self.y_tube = 0
        self.x_ether = 0
        self.y_ether = 0
    def shuffle(self, level):
        """ run through the list and set items out of wall and guard """
        self.level = level
        #syringe coordinate
        while self.level.structure[self.rysyr][self.rxsyr] != "0":
            self.rxsyr = random.randint(0, numberofsprite-1)
            self.rysyr = random.randint(0, numberofsprite-1)

        self.x_syringe = self.rxsyr * sprite_size
        self.y_syringe = self.rysyr * sprite_size

        #tube coordinate
        while self.level.structure[self.rytube][self.rxtube] != "0":
            self.rxtube = random.randint(0, numberofsprite-1)
            self.rytube = random.randint(0, numberofsprite-1)

        self.x_tube = self.rxtube * sprite_size
        self.y_tube = self.rytube * sprite_size

        #ether coordinate
        while self.level.structure[self.ryether][self.rxether] != "0":
            self.rxether = random.randint(0, numberofsprite-1)
            self.ryether = random.randint(0, numberofsprite-1)
        self.x_ether = self.rxether * sprite_size
        self.y_ether = self.ryether * sprite_size

        return self.rxsyr, self.rxtube, self.rxether, self.rysyr, self.rytube, self.ryether

    def showobjects(self, window, SYRINGE_COUNT, TUBE_COUNT, ETHER_COUNT):
        """"
        During the first loop, show the three items with the count =0, then each item
        hit by mg will add 1 to their respective count, which clear the object for the next loop.

        """

        self.SYRINGE_COUNT = SYRINGE_COUNT
        self.TUBE_COUNT = TUBE_COUNT
        self.ETHER_COUNT = ETHER_COUNT
        syringe = pygame.image.load(image_syringe).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()
        ether = pygame.image.load(image_ether).convert_alpha()
        if self.SYRINGE_COUNT == 0:
            window.blit(syringe, (self.x_syringe, self.y_syringe))
        if TUBE_COUNT == 0:
            window.blit(tube, (self.x_tube, self.y_tube))
        if ETHER_COUNT == 0:
            window.blit(ether, (self.x_ether, self.y_ether))
