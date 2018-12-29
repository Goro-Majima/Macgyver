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
		self.start = pygame.image.load("images/MacGyver.png").convert_alpha()

		self.case_x = 0
		self.case_y = 0
		self.x = 0 
		self.y = 0
		
		self.direction = self.start
		self.level= level

		self.p1= 0
		self.p2 =0
	def moveto(self,direction):
		if direction == "right":
			#Avoid right boundary
			if self.case_x < (numberofsprite - 1):
				if self.level.structure[self.case_y][self.case_x+1] != "m":
					#Avoid right boundary
					self.case_x +=1
					self.x = self.case_x * sprite_size			
					print(self.level.structure[self.case_y][self.case_x])	
					print(self.case_y,self.case_x)
					print(self.x)
		#Moving left
		if direction == 'left':
			#Avoid left boundary
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * sprite_size	
					print(self.level.structure[self.case_y][self.case_x])	
					print(self.case_y,self.case_x)
					print(self.x)	
		
		#Moving up
		if direction == 'up':
			#Y  inversed 
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * sprite_size
					print(self.level.structure[self.case_y][self.case_x])	
					print(self.case_y,self.case_x)
					print(self.y)
		#Moving down
		if direction == 'down':
			if self.case_y < (numberofsprite - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * sprite_size
					print(self.level.structure[self.case_y][self.case_x])	
					print(self.case_y,self.case_x)
					print(self.y)
	def shuffle(self):
		
		
		# object2 = pygame.image.load("images/ether.png").convert_alpha()
		# object3 = pygame.image.load("images/tube_plastique.png").convert_alpha()	
		xo = random.randint(0,numberofsprite-1 )
		yo = random.randint(0,numberofsprite-1 )
		while self.level.structure[xo][yo] == "m" or self.level.structure[xo][yo] == "a" :
			xo = random.randint(0,numberofsprite-1 )
			yo = random.randint(0,numberofsprite-1)		 		
			print(xo,yo)
				
		self.p1 = xo * sprite_size
		self.p2 = yo * sprite_size 
		print(xo,yo)
		print(self.level.structure[xo][yo])
		print(self.p1,self.p2)	
		#pas bon car ça multiplie dans les murs qui sont plus "m"
	
	def showobjects(self,window):
		syringe = pygame.image.load(image_syringe).convert_alpha()
		window.blit(syringe,(self.p1,self.p2))
