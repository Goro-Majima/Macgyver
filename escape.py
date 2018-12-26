import pygame
from pygame.locals import *

from constantes import *

pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

#Titre
pygame.display.set_caption(titre_fenetre)




continuer = 1

while continuer:

	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()
	
	for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer = 0