import pygame
from pygame.locals import *

from constantes import *
from classes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre,cote_fenetre))
fond = pygame.image.load(image_fond).convert()
hero = pygame.image.load(image_hero)
pygame.display.set_icon(hero)

pygame.display.set_caption(titre_fenetre)
level =Level("maze")
level.generer()
level.afficher(fenetre)
pygame.display.flip()

mg = Perso("images/MacGyver.png","images/MacGyver.png","images/MacGyver.png","images/MacGyver.png",level)
continuer = 1
while continuer:
		
	for event in pygame.event.get():

		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer=0
		elif event.type == KEYDOWN:

			if event.key == K_RIGHT:
				
				mg.deplacer("droite")
			elif event.key == K_LEFT:
				
				mg.deplacer('gauche')
			elif event.key == K_UP:
				
				mg.deplacer('haut')
			elif event.key == K_DOWN:
				
				mg.deplacer('bas') 
	fenetre.blit(fond, (0,0))
	level.afficher(fenetre)
	fenetre.blit(mg.direction, (mg.x, mg.y)) 
	pygame.display.flip()		

	#déplacements de macgyver
	
	# if posMacgyver = posGardien="a" et que gathered = 3:
	# 	print("Gagné")		

	# elif posMacgyver = posGardien ="a"et que gathered < 3:
	# 	print("perdu")
	# continuer = 0




