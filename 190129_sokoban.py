import pygame
import sys
from UserString import MutableString
import time
pygame.init()
manx = 0
many = 0

iot_caption = 'IoT-Sokoban'
pygame.display.set_caption(iot_caption)
DISPLAYSURF = pygame.display.set_mode((600,480 ), 0, 32)
WHITE = (255, 255, 255)

imgWall = pygame.image.load('iot_wall.png') 

imgBox = pygame.image.load('box.png') 
imgDot = pygame.image.load('dot.png') 

imgClear = pygame.image.load('stclear.png') 

imgManF= pygame.image.load('iot_manF.png') 
imgManB= pygame.image.load('iot_manB.png') 
imgManL= pygame.image.load('iot_manL.png') 
imgManR= pygame.image.load('iot_manR.png') 
imgMan= imgManF 


iot_stage =[
	[MutableString("##########"),
	MutableString("##  #  @##"),
	MutableString("###   ## #"),
	MutableString("#  B.    #"),
	MutableString("##   # B #"),
	MutableString("# B###  ##"),
	MutableString("#   .#  .#"),
	MutableString("##########")],

	[MutableString("##########"),
	MutableString("#    # @ #"),
	MutableString("###    ###"),
	MutableString("#.  BB  .#"),
	MutableString("###    ###"),
	MutableString("#.  B#   #"),
	MutableString("#  #     #"),
	MutableString("##########")]
	]
	
stage_num=0

iot_caption = "IoT-Sokoban [STAGE: %d]" % (stage_num+1) 
pygame.display.set_caption(iot_caption)

iot_map = []
for iStage in range(8):
	iot_map.append(iot_stage[stage_num][iStage][:])
	continue
while True:

	
		

	DISPLAYSURF.fill(WHITE)
	stage_end = True
	for ix in range(10):
		for iy in range(8):
			if '#' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgWall, (ix*60 , iy*60))
				
			elif 'B' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgBox, (ix*60 , iy*60))
				if '.' !=iot_stage[stage_num][iy][ix]:
					stage_end = False
			elif '.' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgDot, (ix*60 , iy*60))
				
			elif '@' == iot_map[iy][ix]:
					DISPLAYSURF.blit(imgMan, (ix*60 , iy*60))
					manx = ix
					many = iy
	
	pygame.display.update()
	if True == stage_end:
		DISPLAYSURF.blit(imgClear, (120 , 0))
			
		pygame.display.update()
		keyinput = False
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					keyinput = True
					break
			if True == keyinput:
				break
			time.sleep(0.1)
			continue
		stage_num = stage_num+ 1

		iot_map = []
		for iStage in range(8):
			iot_map.append(iot_stage[stage_num][iStage][:])

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			TempX = manx
			TempY = many
			if event.key == pygame.K_DOWN:
				imgMan = imgManF
				many =many + 1
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
#			if ' '== iot_map[many][manx] or '.' == iot_map[many][manx]:
			if '#' != iot_map[many][manx]:
				if 'B' == iot_map[many][manx]:
					if ' ' == iot_map[2*many-TempY][2*manx-TempX] or '.' == iot_map[2*many-TempY][2*manx-TempX]:
						iot_map[2*many-TempY][2*manx-TempX] = 'B'
					else:
						manx= TempX
						many= TempY
				if '.' == iot_stage[stage_num][TempY][TempX]:
					iot_map[TempY][TempX]='.'
				else:
					iot_map[TempY][TempX]=' '

				iot_map[many][manx] = '@'
			
			else:
				manx= TempX
				many= TempY
		elif event.type == pygame.quit:
			pygame.quit()
			sys.exit()



