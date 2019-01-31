import pygame
import sys
from UserString import MutableString

pygame.init()
manx = 0
many = 0
manPos = ' '	
DISPLAYSURF = pygame.display.set_mode((600,480 ), 0, 32)
pygame.display.set_caption('IoT-Sokoban')
WHITE = (255, 255, 255)

imgWall = pygame.image.load('iot_wall.png') 
imgBox = pygame.image.load('box.png')
imgDot = pygame.image.load('dot.png') 

imgManF= pygame.image.load('iot_manF.png') 
imgManB= pygame.image.load('iot_manB.png') 
imgManL= pygame.image.load('iot_manL.png') 
imgManR= pygame.image.load('iot_manR.png') 
imgMan= imgManF 


iot_stage =[
	[MutableString("##########"),
	MutableString("##  #  @##"),
	MutableString("###   ## #"),
	MutableString("#   B    #"),
	MutableString("##   # B #"),
	MutableString("#  ###  ##"),
	MutableString("#   .#  .#"),
	MutableString("##########")],
	
	[MutableString("##########"),
	MutableString("#    # @ #"),
	MutableString("###    ###"),
	MutableString("#   B   .#"),
	MutableString("###    ###"),
	MutableString("#    #   #"),
	MutableString("#  # B  .#"),
	MutableString("##########")]
	]

iot_map2= iot_stage[0]
iot_map = iot_stage[0]
manOn = False
while True:
	
		

	DISPLAYSURF.fill(WHITE)
	for ix in range(10):
		for iy in range(8):
			if '#' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgWall, (ix*60 , iy*60))
				
			elif '.' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgDot, (ix*60 , iy*60))
			elif 'B' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgBox, (ix*60 , iy*60))

			elif '@' == iot_map[iy][ix]:
#				if manOn == False:
					DISPLAYSURF.blit(imgMan, (ix*60 , iy*60))
					manx = ix
					many = iy
#					manOn = True
#				else:
#					iot_map[iy][ix] = ' '
#	for ix in range(10):
#		for iy in range(8):
#			if iot_map2[iy][ix] != iot_map[iy][ix] and '@' != iot_map[iy][ix]:
#				iot_map[iy][ix] = iot_map2[iy][ix]		
			
				
					
					

#	manOn = False
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			TempX = manx
			TempY = many
			if event.key == pygame.K_DOWN:
				imgMan = imgManF
				many = many + 1
			elif event.key == pygame.K_UP:
				imgMan = imgManB
				many = many - 1
			elif event.key == pygame.K_LEFT:
				imgMan = imgManL
				manx = manx -1
			elif event.key == pygame.K_RIGHT:
				imgMan = imgManR
				manx = manx +1
			else:
				continue
			if ' '== iot_map[many][manx] or '.' == iot_map[many][manx]:
				iot_map[many][manx] = '@'
				iot_map[TempY][TempX] = ' '
			else:
				manx= TempX
				many= TempY
		elif event.type == pygame.quit:
			pygame.quit()
			sys.exit()


