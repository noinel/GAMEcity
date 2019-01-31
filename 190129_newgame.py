import pygame
import sys


pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300 ), 0, 32)
pygame.display.set_caption('NewGame')
WHITE = (255, 100, 0)

catImg = pygame.image.load('cat.png') #125 , 79

catx = 100
caty = 100 

while True:

	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(catImg, (catx, caty))
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.quit:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			 if event.key == pygame.K_DOWN:
				 caty = caty + 10
				 if caty > 221:
					caty = 221
			 elif event.key == pygame.K_UP:
				 caty = caty - 10
				 if caty < 0:
					 caty = 0
			 elif event.key == pygame.K_RIGHT:
				 catx = catx + 10
				 if catx > 275:
					 catx = 275
			 elif event.key == pygame.K_LEFT:
				 catx = catx - 10
				 if catx < 0:
					 catx = 0
