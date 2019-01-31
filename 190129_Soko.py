import pygame
import sys


pygame.init()

	
DISPLAYSURF = pygame.display.set_mode((600,480 ), 0, 32)
pygame.display.set_caption('IoT-Sokoban')
WHITE = (255, 255, 255)

imgWall = pygame.image.load('iot_wall.png') 

imgMan= pygame.image.load('iot_man.png') 

iot_map = [
	"##########",
	"##  #  @##",
	"###   ## #",
	"#        #",
	"##   #   #",
	"#  ###  ##",
	"#    #   #",
	"##########"]
manx = 0
many = 0
for ix in range(10):
	for iy in range(8):
		if '@' == iot_map[iy][ix]:
			DISPLAYSURF.blit(imgMan, (ix*60 , iy*60))
			manx = ix
			many = iy
while True:
	
	DISPLAYSURF.fill(WHITE)
	for ix in range(10):
		for iy in range(8):
			if '#' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgWall, (ix*60 , iy*60))
		
	DISPLAYSURF.blit(imgMan, (manx*60 , many*60))
	pygame.display.update()
	

	for event in pygame.event.get():
		if event.type == pygame.quit:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				many = many + 1 
				if '#' == iot_map[many][manx]:
					many = many - 1
			elif event.key == pygame.K_UP:
				many = many - 1
				if '#' == iot_map[many][manx]:
					many = many + 1
			elif event.key == pygame.K_RIGHT:
				manx = manx + 1
				if '#' == iot_map[many][manx]:
					manx = manx - 1
			elif event.key == pygame.K_LEFT:
				manx = manx - 1
				if '#' == iot_map[many][manx]:
					manx = manx + 1

