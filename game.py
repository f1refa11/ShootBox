import pygame
from player import Player
from constants import CHUNKSIZE
from confmgr import renderDistance, showGrass, fpsLimit, enableRPC
from main import clock,cursor
import screenmgr
from screenmgr import screen
from funcs import loadPathTexture,gameExit
from paths import blocksPath,uiTexturesPath
from fontmgr import renderFont, cacheFont
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
				elif event.button == 3:
					# calculate mouse position relative to game surface
					mx,my = pygame.mouse.get_pos()
					destX, destY = (mx-(screenmgr.width//2-32)+player.x)//64, (my-(screenmgr.height//2-32)+player.y)//64
					chunkX, chunkY = destX//CHUNKSIZE, destY//CHUNKSIZE
					resX, resY = destX, destY
					resX = abs(resX)//8
					resX *= 8
					resX = abs(destX) - resX
					if destX < 0 and resX != 0:
						resX = 8 - resX
					
					resY = abs(resY)//8
					resY *= 8
					resY = abs(destY) - resY
					if destY < 0 and resY != 0:
						resY = 8 - resY

					if {"pos":(resX,resY),"block":"lol"} not in chunks[(chunkX, chunkY)]:
						chunks[(chunkX, chunkY)].append({"pos":(resX,resY),"block":"lol"})
						loadedChunks[(chunkX, chunkY)].append({"pos":(resX,resY),"block":"lol"})
				elif event.button == 1:
					# calculate mouse position relative to game surface
					mx,my = pygame.mouse.get_pos()
					destX, destY = (mx-(screenmgr.width//2-32)+player.x)//64, (my-(screenmgr.height//2-32)+player.y)//64
					chunkX, chunkY = destX//CHUNKSIZE, destY//CHUNKSIZE
					resX, resY = destX, destY
					resX = abs(resX)//8
					resX *= 8
					resX = abs(destX) - resX
					if destX < 0 and resX != 0:
						resX = 8 - resX
					
					resY = abs(resY)//8
					resY *= 8
					resY = abs(destY) - resY
					if destY < 0 and resY != 0:
						resY = 8 - resY

					try:
						chunks[(chunkX, chunkY)].remove({"pos":(resX,resY),"block":"lol"})
						loadedChunks[(chunkX, chunkY)].remove({"pos":(resX,resY),"block":"lol"})
					except:
						pass

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