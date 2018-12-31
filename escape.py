import pygame

from pygame.locals import *

from constants import *
from classes import *

window = pygame.display.set_mode((win_size,win_size))
floor = pygame.image.load(image_floor).convert()
hero = pygame.image.load(image_hero)

# ether = pygame.image.load(image_ether).convert_alpha()
# tube = pygame.image.load(image_tube).convert_alpha()
pygame.display.set_icon(hero)
pygame.display.set_caption(window_title)


level =Level()
level.create()
mg = Stargate(level)
level.cast(window)
mg.shuffle()

pygame.display.flip()

keepplaying = 1
while keepplaying:
#LOOP running automatically, auto display	
	# pygame.time.Clock().tick(30)
	for event in pygame.event.get():

		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			keepplaying=0
		elif event.type == KEYDOWN:

			if event.key == K_RIGHT:				
				mg.moveto("right")
			elif event.key == K_LEFT:				
				mg.moveto('left')
			elif event.key == K_UP:				
				mg.moveto('up')
			elif event.key == K_DOWN:				
				mg.moveto('down') 
	
	window.blit(floor, (0,0))
	level.cast(window)
	window.blit(mg.direction, (mg.x, mg.y)) 
	mg.showobjects(window)
	pygame.display.flip()	


	if level.structure[mg.case_y][mg.case_x] == 'a':
		#Need to create text bubble
		keepplaying =0
	if mg.case_y == mg.y0 and mg.case_x == mg.x0:
		mg.delete(window)
	if mg.case_y == mg.y1 and mg.case_x == mg.x1:
		print("ok ether")
	if mg.case_y == mg.y2 and mg.case_x == mg.x2:
		print("ok tube")	

	#TROUVER UN MOYEN DE RECUPER LES VARIABLES P1 P2 P3 ETC
	
	# if posMacgyver = posGardien="a" et que gathered = 3:
	# 	print("Gagné")		

	# elif posMacgyver = posGardien ="a"et que gathered < 3:
	# 	print("perdu")
	# continuer = 0




