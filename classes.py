import pygame
import random
from pygame.locals import *
from constants import *

class Level:
	def __init__(self):
		self.structure =0



	def create(self):
		with open("maze","r") as fichier:
			level_structure =[]
			for line in fichier:
				level_line =[]
				for sprite in line:
					if sprite != '\n':
						level_line.append(sprite)
				level_structure.append(level_line)
			self.structure = level_structure
	
	def cast(self,window):
		wall = pygame.image.load(image_wall).convert()
		badguy = pygame.image.load(image_badguy).convert_alpha()

		num_line = 0
		for line in self.structure:
			num_case=0
			for sprite in line:
				x = num_case * sprite_size
				y = num_line * sprite_size
				if sprite == 'm':
					window.blit(wall,(x,y))
				elif sprite == 'a':
					window.blit(badguy,(x,y))
				num_case +=1
			num_line+=1

class Stargate:
	def __init__(self,level):		

		syringe = pygame.image.load(image_syringe).convert_alpha()
		tube = pygame.image.load(image_tube).convert_alpha()
		ether = pygame.image.load(image_ether).convert_alpha()

		self.start = pygame.image.load("images/MacGyver.png").convert_alpha()

		self.case_x = 0
		self.case_y = 0
		self.x = 0 
		self.y = 0
		
		self.direction = self.start
		self.level= level
		#init coordinates
		self.p1= 0
		self.p2 =0
		self.p3= 0
		self.p4 =0
		self.p5= 0
		self.p6 =0

		
	def moveto(self,direction):
		if direction == "right":
			#Avoid right boundary
			if self.case_x < (numberofsprite - 1):
				if self.level.structure[self.case_y][self.case_x+1] != "m":
					#Avoid right boundary
					self.case_x +=1
					self.x = self.case_x * sprite_size			
					
		#Moving left
		if direction == 'left':
			#Avoid left boundary
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * sprite_size	
					
		
		#Moving up
		if direction == 'up':
			#Y  inversed 
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * sprite_size
					
		#Moving down
		if direction == 'down':
			if self.case_y < (numberofsprite - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * sprite_size
									
	def shuffle(self):
		
		#syringe coordinate
		self.x0 = random.randint(0, numberofsprite-1)
		self.y0 = random.randint(0, numberofsprite-1)
			
		while self.level.structure[self.y0][self.x0] != "0":			
			self.x0 = random.randint(0, numberofsprite-1)
			self.y0 = random.randint(0, numberofsprite-1)	
		
		self.p1 = self.x0 * sprite_size
		self.p2 = self.y0 * sprite_size	
					
		#tube coordinate
		self.x1 = random.randint(0, numberofsprite-1)
		self.y1 = random.randint(0, numberofsprite-1) 		
		while self.level.structure[self.y1][self.x1] != "0":			
			self.x1 = random.randint(0, numberofsprite-1)
			self.y1 = random.randint(0, numberofsprite-1)	
		
		self.p3 = self.x1 * sprite_size
		self.p4 = self.y1 * sprite_size

		#tube coordinate
		self.x2 = random.randint(0, numberofsprite-1)
		self.y2 = random.randint(0, numberofsprite-1) 
		while self.level.structure[self.y2][self.x2] != "0":			
			self.x2 = random.randint(0, numberofsprite-1)
			self.y2 = random.randint(0, numberofsprite-1)	
		
		self.p5 = self.x2 * sprite_size
		self.p6 = self.y2 * sprite_size
		
		return self.x0,self.x1,self.x2,self.y0,self.y1,self.y2

	def showobjects(self,window,syringecount,tubecount,ethercount):
		#During the first loop, show the three items with the count =0, then each item 
		#hit by mg will add 1 to their respective count, which clear the object for the next loop.
		self.syringecount = syringecount
		self.tubecount =tubecount
		self.ethercount = ethercount
		syringe = pygame.image.load(image_syringe).convert_alpha()
		tube = pygame.image.load(image_tube).convert_alpha()
		ether = pygame.image.load(image_ether).convert_alpha()
		if self.syringecount ==0:
			window.blit(syringe,(self.p1,self.p2))
		if tubecount == 0:
			window.blit(tube,(self.p3,self.p4))
		if ethercount == 0:
			window.blit(ether,(self.p5,self.p6))


	




		

		
