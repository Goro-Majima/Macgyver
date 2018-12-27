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
		hero = pygame.image.load(image_hero).convert()
		badguy = pygame.image.load(image_badguy).convert_alpha()

		num_ligne = 0
		for ligne in self.structure:
			num_case=0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':
					fenetre.blit(mur,(x,y))
				elif sprite == 'd':
					fenetre.blit(hero,(x,y))
				elif sprite == 'a':
					fenetre.blit(badguy,(x,y))
				num_case +=1
			num_ligne+=1

class Perso:
	def __init__(self):
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

		self.level = Level

	