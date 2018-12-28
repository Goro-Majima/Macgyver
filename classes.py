import pygame
from pygame.locals import *
from constantes import *

class Level:
	def __init__(self,fichier):
		self.structure =0



	def generer(self):
		with open("maze","r") as fichier:
			structure_niveau =[]
			for ligne in fichier:
				ligne_niveau =[]
				for sprite in ligne:
					if sprite != '\n':
						ligne_niveau.append(sprite)
				structure_niveau.append(ligne_niveau)
			self.structure = structure_niveau

	def afficher(self,fenetre):

		mur = pygame.image.load(image_mur).convert()
		#start = pygame.image.load(image_hero).convert_alpha()
		badguy = pygame.image.load(image_badguy).convert_alpha()

		num_ligne = 0
		for ligne in self.structure:
			num_case=0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':
					fenetre.blit(mur,(x,y))
				#elif sprite == 'd':
					#fenetre.blit(start,(x,y))
				elif sprite == 'a':
					fenetre.blit(badguy,(x,y))
				num_case +=1
			num_ligne+=1

class Perso:
	def __init__(self,droite,gauche,haut,bas,level):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = 0 
		self.y = 0
		
		self.direction = self.droite
		self.level= level
	def deplacer(self,direction):
		if direction == "droite":
			if self.case_x < (nombre_sprite - 1):
				if self.level.structure[self.case_y][self.case_x+1] != "m":
					self.case_x +=1
					self.x = self.case_x * taille_sprite
			self.direction = self.droite
			
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas