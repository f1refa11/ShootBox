import pygame
from player import Player
from constants import CHUNKSIZE
from confmgr import renderDistance, showGrass, fpsLimit, enableRPC
from main import clock,cursor
import screenmgr
from screenmgr import screen
from funcs import *
from paths import blocksPath
def game():
	from mainMenu import mainMenu
	#loading resources
	#textures
	grass = loadPathTexture(blocksPath, "grass.png", True, (64, 64))
	sand = loadPathTexture(blocksPath, "sand.png", True, (64, 64))

	brickWall = loadPathTexture(blocksPath, "bricks.png", True, (64, 64))

	# gui

	# hotbar
	hotbarIndex = 2
	hotbar = loadPathTexture(uiTexturesPath, "hotbar.png", True, (48, 48))
	hotbarOutline = loadPathTexture(uiTexturesPath, "hotbar-outline.png", True, (48,48))
	hotbarSurf = pygame.Surface((272, 48), pygame.SRCALPHA)
	for x in range(5):
		if x == hotbarIndex:
			hotbarSurf.blit(hotbarOutline, (x*56, 0))
		else:
			hotbarSurf.blit(hotbar, (x*56, 0))
	hotbarX, hotbarY = screenmgr.width//2-136, screenmgr.height-50

	#generating first chunk
	chunks = []
	for x in range(1):
		for y in range(1):
			chunks.append([x,y])
	#configuring player
	player = Player((8, 8))
	pressedKeys = {
		"up": False,
		"down": False,
		"left": False,
		"right": False,
	}
	#generating other chunks which are in renderDistance
	playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
	loadedChunks = []
	for x in range(playerChunkPos[0]-renderDistance//2, playerChunkPos[0]+renderDistance//2):
		for y in range(playerChunkPos[1]-renderDistance//2, playerChunkPos[1]+renderDistance//2):
			if not [x,y] in chunks:
				chunks.append([x,y])
			loadedChunks.append([x,y])
	cameraOffset = [0,0]

	#discord rpc
	if enableRPC:
		from main import RPC,rpcState
		if rpcState != "game":
			RPC.update(
				state="Играет",
				details="Одиночная игра",
				buttons= [{"label": "GitHub Repo", "url": "https://github.com/f1refa11/ShootBox"},]
			)
			rpcState = "game"
	while 1:
		mousePos = pygame.mouse.get_pos()
		clock.tick(fpsLimit)
		screen.fill((51, 153, 218))

		if playerChunkPos != (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE)):
			playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
			loadedChunks.clear()
			for x in range(playerChunkPos[0]-renderDistance//2, playerChunkPos[0]+renderDistance//2):
				for y in range(playerChunkPos[1]-renderDistance//2, playerChunkPos[1]+renderDistance//2):
					if [x,y] in chunks:
						loadedChunks.append([x,y])
					else:
						chunks.append([x,y])
						loadedChunks.append([x,y])

		for chunk in loadedChunks:
			chunkRect = pygame.Rect(chunk[0]*64*CHUNKSIZE+cameraOffset[0], chunk[1]*64*CHUNKSIZE+cameraOffset[1], 64*CHUNKSIZE, 64*CHUNKSIZE)
			chunkSurface = pygame.Surface((64*CHUNKSIZE, 64*CHUNKSIZE))
			chunkSurface.fill((57, 194, 114))
			if showGrass:
				for x in range(CHUNKSIZE):
					for y in range(CHUNKSIZE):
						chunkSurface.blit(grass, (x*64, y*64))
			if chunkRect.collidepoint(mousePos[0], mousePos[1]):
				pygame.draw.rect(chunkSurface, (255, 255, 255), ((mousePos[0]-chunkRect.x)//64*64, (mousePos[1]-chunkRect.y)//64*64,64,64),2)
			screen.blit(chunkSurface, chunkRect)
			pygame.draw.rect(screen, (255, 0, 0), chunkRect, 1)

		if pressedKeys["up"]:
			player.y -= player.speed
			cameraOffset[1] += player.speed
		if pressedKeys["down"]:
			player.y += player.speed
			cameraOffset[1] -= player.speed
		if pressedKeys["left"]:
			player.x -= player.speed
			cameraOffset[0] += player.speed
		if pressedKeys["right"]:
			player.x += player.speed
			cameraOffset[0] -= player.speed
		player.render(screen)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					pressedKeys["up"] = True
				elif event.key == pygame.K_s:
					pressedKeys["down"] = True
				elif event.key == pygame.K_a:
					pressedKeys["left"] = True
				elif event.key == pygame.K_d:
					pressedKeys["right"] = True
				elif event.key == pygame.K_ESCAPE:
					mainMenu()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_w:
					pressedKeys["up"] = False
				elif event.key == pygame.K_s:
					pressedKeys["down"] = False
				elif event.key == pygame.K_a:
					pressedKeys["left"] = False
				elif event.key == pygame.K_d:
					pressedKeys["right"] = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button in [4,5]:
					if event.button == 5:
						if hotbarIndex > 0:
							hotbarIndex -= 1
						else:
							hotbarIndex = 4
					elif event.button == 4:
						if hotbarIndex < 4:
							hotbarIndex += 1
						else:
							hotbarIndex = 0
					hotbarSurf.fill((0,0,0,0))
					for x in range(5):
						if x == hotbarIndex:
							hotbarSurf.blit(hotbarOutline, (x*56, 0))
						else:
							hotbarSurf.blit(hotbar, (x*56, 0))
					
			elif event.type == pygame.WINDOWSIZECHANGED:
				screenmgr.width, screenmgr.height = event.x,event.y
				hotbarX, hotbarY = screenmgr.width//2-136, screenmgr.height-50
				player.rendX, player.rendY = screenmgr.width//2-32, screenmgr.height//2-32
				cameraOffset = [(screenmgr.width//2-32-player.x),(screenmgr.height//2-32-player.y)]
			if event.type == pygame.QUIT:
				gameExit()

		screen.blit(hotbarSurf, (hotbarX, hotbarY))

		screen.blit(cursor, mousePos)
		pygame.display.update()