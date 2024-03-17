import pygame
from player import Player
from constants import CHUNKSIZE
from confmgr import renderDistance, showGrass, fpsLimit, enableRPC
from main import clock,cursor
import screenmgr
from screenmgr import screen
from funcs import loadPathTexture,gameExit
from path import blocksPath,uiTexturesPath
from text import renderFont, cacheFont
def game():
	from mainMenu import mainMenu
	player = Player((0,0))
	# loading resources

	# enviroment
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
	chunks = {(0,0):[]}
	#configuring player
	pressedKeys = {
		"up": False,
		"down": False,
		"left": False,
		"right": False,
	}
	#generating other chunks which are in renderDistance
	playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
	loadedChunks = {}
	for x in range(playerChunkPos[0]-renderDistance//2, playerChunkPos[0]+renderDistance//2):
		for y in range(playerChunkPos[1]-renderDistance//2, playerChunkPos[1]+renderDistance//2):
			if (x,y) not in chunks.keys():
				chunks[(x,y)] = []
			loadedChunks[(x,y)] = []
	cameraOffset = [(screenmgr.width//2-32-player.x),(screenmgr.height//2-32-player.y)]

	mouseActionState = 0
	actionDelay = 8
	mouseTimeCount = actionDelay

	blockCollisions = []
	# TODO: load and unload blockCollisions' rects so collidelist doesn't take long to check

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
			# TODO: remove unnessessary chunks instead of fully clearing loadedChunks
			loadedChunks.clear()
			for x in range(playerChunkPos[0]-renderDistance//2, playerChunkPos[0]+renderDistance//2):
				for y in range(playerChunkPos[1]-renderDistance//2, playerChunkPos[1]+renderDistance//2):
					if (x,y) not in chunks:
						chunks[(x,y)] = []
					loadedChunks[(x,y)] = chunks[(x,y)].copy()

		for chunk in loadedChunks:
			chunkRect = pygame.Rect(chunk[0]*64*CHUNKSIZE+cameraOffset[0], chunk[1]*64*CHUNKSIZE+cameraOffset[1], 64*CHUNKSIZE, 64*CHUNKSIZE)
			chunkSurface = pygame.Surface((64*CHUNKSIZE, 64*CHUNKSIZE))
			if showGrass:
				for x in range(CHUNKSIZE):
					for y in range(CHUNKSIZE):
						chunkSurface.blit(grass, (x*64, y*64))
			else:
				chunkSurface.fill((57, 194, 114)) # because we don't need to fill if we have showGrass

			for block in loadedChunks[chunk]:
				chunkSurface.blit(brickWall, (block["pos"][0]*64, block["pos"][1]*64))

			# block select outline
			if chunkRect.collidepoint(mousePos[0], mousePos[1]):
				pygame.draw.rect(chunkSurface, (255, 255, 255), ((mousePos[0]-chunkRect.x)//64*64, (mousePos[1]-chunkRect.y)//64*64,64,64),2)

			# debug chunk pos show(debug purposes)
			renderFont(cacheFont("(%s,%s)"%(chunk[0],chunk[1])),(10,10),chunkSurface)

			screen.blit(chunkSurface, chunkRect)
			pygame.draw.rect(screen, (255, 0, 0), chunkRect, 1)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key in [pygame.K_w, pygame.K_UP]:
					pressedKeys["up"] = True
				elif event.key in [pygame.K_s, pygame.K_DOWN]:
					pressedKeys["down"] = True
				elif event.key in [pygame.K_a, pygame.K_LEFT]:
					pressedKeys["left"] = True
				elif event.key in [pygame.K_d, pygame.K_RIGHT]:
					pressedKeys["right"] = True
				elif event.key == pygame.K_ESCAPE:
					mainMenu()
				elif event.key == pygame.K_LSHIFT:
					actionDelay = 0
				elif event.key == pygame.K_LALT:
					player.speed = 10
				elif event.key == pygame.K_LCTRL:
					player.speed = 5
			elif event.type == pygame.KEYUP:
				if event.key in [pygame.K_w, pygame.K_UP]:
					pressedKeys["up"] = False
				elif event.key in [pygame.K_s, pygame.K_DOWN]:
					pressedKeys["down"] = False
				elif event.key in [pygame.K_a, pygame.K_LEFT]:
					pressedKeys["left"] = False
				elif event.key in [pygame.K_d, pygame.K_RIGHT]:
					pressedKeys["right"] = False
				elif event.key == pygame.K_LSHIFT:
					actionDelay = 8
				elif event.key == pygame.K_LALT:
					player.speed = 3
				elif event.key == pygame.K_LCTRL:
					player.speed = 3
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
				elif event.button == 1:
					mouseActionState = 1 # break
				elif event.button == 3:
					mouseActionState = 2 # place
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button in [1,3]:
					mouseActionState = 0 # reset
					mouseTimeCount = actionDelay
			elif event.type == pygame.WINDOWSIZECHANGED:
				screenmgr.width, screenmgr.height = event.x,event.y
				hotbarX, hotbarY = screenmgr.width//2-136, screenmgr.height-50
				player.rendX, player.rendY = screenmgr.width//2-32, screenmgr.height//2-32
				cameraOffset = [(screenmgr.width//2-32-player.x),(screenmgr.height//2-32-player.y)]
			if event.type == pygame.QUIT:
				gameExit()
		player.render(screen)

		if pressedKeys["up"]:
			player.y -= player.speed
			cameraOffset[1] += player.speed
			player.rect.y = player.y+8
			if player.rect.collidelist(blockCollisions) != -1:
				player.y += player.speed
				cameraOffset[1] -= player.speed
				player.rect.y = player.y+8
		if pressedKeys["down"]:
			player.y += player.speed
			cameraOffset[1] -= player.speed
			player.rect.y = player.y+8
			if player.rect.collidelist(blockCollisions) != -1:
				player.y -= player.speed
				cameraOffset[1] += player.speed
				player.rect.y = player.y+8
		if pressedKeys["left"]:
			player.x -= player.speed
			cameraOffset[0] += player.speed
			player.rect.x = player.x+8
			if player.rect.collidelist(blockCollisions) != -1:
				player.x += player.speed
				cameraOffset[0] -= player.speed
				player.rect.x = player.x+8
		if pressedKeys["right"]:
			player.x += player.speed
			cameraOffset[0] -= player.speed
			player.rect.x = player.x+8
			if player.rect.collidelist(blockCollisions) != -1:
				player.x -= player.speed
				cameraOffset[0] += player.speed
				player.rect.x = player.x+8

		if mouseActionState != 0: # one algorithm for 2 actions
			if mouseTimeCount < actionDelay:
				mouseTimeCount += 1
			else:
				mouseTimeCount = 0
				# calculate mouse position relative to game surface
				mx,my = pygame.mouse.get_pos()
				# print(destX, destY, player.x, player.y)
				blockX, blockY = (mx-(screenmgr.width//2-32)+player.x)//64, (my-(screenmgr.height//2-32)+player.y)//64
				chunkX, chunkY = blockX//CHUNKSIZE, blockY//CHUNKSIZE
				resX, resY = blockX, blockY
				resX = abs(resX)//8
				resX *= 8
				resX = abs(blockX) - resX
				if blockX < 0 and resX != 0:
					resX = 8 - resX

				resY = abs(resY)//8
				resY *= 8
				resY = abs(blockY) - resY
				if blockY < 0 and resY != 0:
					resY = 8 - resY
				if mouseActionState == 1: # break
					try:
						chunks[(chunkX, chunkY)].remove({"pos":(resX,resY),"block":"lol"})
						loadedChunks[(chunkX, chunkY)].remove({"pos":(resX,resY),"block":"lol"})
						blockCollisions.remove(pygame.Rect(blockX*64, blockY*64, 64, 64))
					except:
						pass
				elif mouseActionState == 2: # place
					try:
						if {"pos":(resX,resY),"block":"lol"} not in chunks[(chunkX, chunkY)]:
							tempRect = pygame.Rect(blockX*64, blockY*64, 64, 64)
							if not player.rect.colliderect(tempRect):
									blockCollisions.append(tempRect)
									chunks[(chunkX, chunkY)].append({"pos":(resX,resY),"block":"lol"})
									loadedChunks[(chunkX, chunkY)].append({"pos":(resX,resY),"block":"lol"})
					except:
						pass

		# pygame.draw.rect(screen, (255, 0, 0), (player.rendX+8, player.rendY+8, 48, 48), 1)

		# for x in blockCollisions:
		# 	pygame.draw.rect(screen, (255, 255, 0), x, 3)

		screen.blit(hotbarSurf, (hotbarX, hotbarY))

		screen.blit(cursor, mousePos)
		pygame.display.update()