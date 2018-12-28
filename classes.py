import pygame
from pygame.locals import *
from constants import *

class Level:
	def __init__(self,fichier):
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
	def youcanplay(self,window):

		wall = pygame.image.load(image_wall).convert()
		#start = pygame.image.load(image_hero).convert_alpha()
		badguy = pygame.image.load(image_badguy).convert_alpha()

		num_line = 0
		for line in self.structure:
			num_case=0
			for sprite in line:
				x = num_case * sprite_size
				y = num_line * sprite_size
				if sprite == 'm':
					window.blit(wall,(x,y))
				#elif sprite == 'd':
					#fenetre.blit(start,(x,y))
				elif sprite == 'a':
					window.blit(badguy,(x,y))
				num_case +=1
			num_line+=1

class Stargate:
	def __init__(self,right,level):
		self.right = pygame.image.load(right).convert_alpha()

		self.case_x = 0
		self.case_y = 0
		self.x = 0 
		self.y = 0
		
		self.direction = self.right
		self.level= level
	def moveto(self,direction):
		if direction == "right":
			#Avoid right boundarie
			if self.case_x < (numberofsprite - 1):
				if self.level.structure[self.case_y][self.case_x+1] != "m":
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
			

