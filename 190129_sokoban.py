import pygame
import sys
from UserString import MutableString
import time
pygame.init()
DISPLAYSURF = None
	
manx = 0
many = 0
iot_count = 0
pixelx = 60
pixely = 60
tilex = 10
tiley = 8
displayx = tilex * pixelx
displayy = tiley * pixely
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
	MutableString("#   #  @##"),
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
	MutableString("##########")],

	[MutableString("##########"),
	MutableString("#      @ #"),
	MutableString("#####    #"),
	MutableString("#.  BB  .#"),
	MutableString("#     ####"),
	MutableString("#.  B    #"),
	MutableString("#        #"),
	MutableString("##########")]
	]
	
iot_map = []

stage_num=0

def IotSetCaption(caption):
		
	pygame.display.set_caption(caption)

def IotLoadMap():
	global iot_map

	for iStage in range(tiley):
		iot_map.append(iot_stage[stage_num][iStage][:])

def IotDraw():

	global manx
	global many
	global stage_end

	DISPLAYSURF.fill(WHITE)
	stage_end = True

	for ix in range(tilex):
		for iy in range(tiley):
			if   '#' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgWall, (ix*pixelx , iy*pixely))
			
			elif 'B' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgBox, (ix*pixelx , iy*pixely))
				if '.' !=iot_stage[stage_num][iy][ix]:
					stage_end = False
			elif '.' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgDot, (ix*pixelx , iy*pixely))
			
			elif '@' == iot_map[iy][ix]:
				DISPLAYSURF.blit(imgMan, (ix*pixelx , iy*pixely))
				manx = ix
				many = iy

def IotInit():
	global DISPLAYSURF

	DISPLAYSURF = pygame.display.set_mode((displayx,displayy ), 0, 32)
	IotLoadMap()
	pygame.display.update()



#================================================================================================
IotInit()
while True:

	
	IotSetCaption("IoT-Sokoban [STAGE: %d][count: %d]"% (stage_num+1, iot_count))
		
	
	IotDraw()

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
		for iStage in range(tiley):
			iot_map.append(iot_stage[stage_num][iStage][:])
		iot_count = 0
		IotSetCaption("IoT-Sokoban [STAGE: %d][count: %d]"% (stage_num+1, iot_count))
		continue

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
			elif event.key == pygame.K_r:
				iot_map = []
				for iStage in range(tiley):
					iot_map.append(iot_stage[stage_num][iStage][:])
				iot_count = 0
				IotSetCaption("IoT-Sokoban [STAGE: %d][count: %d]"% (stage_num+1, iot_count))
				break	
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
#						iot_count = iot_count -1
						continue
				if '.' == iot_stage[stage_num][TempY][TempX]:
					iot_map[TempY][TempX]='.'
				else:
					iot_map[TempY][TempX]=' '

				iot_map[many][manx] = '@'
				iot_count= iot_count+1	
				IotSetCaption("IoT-Sokoban [STAGE: %d][count: %d]"% (stage_num+1, iot_count))
			else:
				manx= TempX
				many= TempY
		elif event.type == pygame.quit:
			pygame.quit()
			sys.exit()



