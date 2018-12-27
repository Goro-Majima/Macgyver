import pygame
from pygame.locals import *

from constantes import *
from classes import *
pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre,cote_fenetre))

hero = pygame.image.load(image_hero)
pygame.display.set_icon(hero)

pygame.display.set_caption(titre_fenetre)

continuer = 1
while continuer:
	
	level =Level("maze")
	level.generer()
	level.afficher(fenetre)

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer=0
		


	#afficher fenetre avec tout dedans
	#déplacements de macgyver
	
	# if posMacgyver = posGardien="a" et que gathered = 3:
	# 	print("Gagné")

	# elif posMacgyver = posGardien ="a"et que gathered < 3:
	# 	print("perdu")
	# continuer = 0




