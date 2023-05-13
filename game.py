import pygame
from player import Player
from constants import CHUNKSIZE
from confvar import renderDistance, showGrass
chunks = []
for x in range(1):
	for y in range(1):
		chunks.append([x,y])
def game():
	player = Player((8, 8))
	pressedKeys = {
		"up": False,
		"down": False,
		"left": False,
		"right": False,
	}
	playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
	loadedChunks = []
	for x in range(playerChunkPos[0]-renderDistance//2, playerChunkPos[0]+renderDistance//2):
		for y in range(playerChunkPos[1]-renderDistance//2, playerChunkPos[1]+renderDistance//2):
			if not [x,y] in chunks:
				chunks.append([x,y])
			loadedChunks.append([x,y])
	cameraOffset = [0,0]
	while 1:
		mousePos = pygame.mouse.get_pos()
		clock.tick(fps)
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
			player.up()
			# cameraOffset[1] += 3
		if pressedKeys["down"]:
			player.y += player.speed
			# cameraOffset[1] -= 3
		if pressedKeys["left"]:
			player.left()
		if pressedKeys["right"]:
			player.x += player.speed
		player.render(screen)

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_w:
					pressedKeys["up"] = True
				elif event.key == K_s:
					pressedKeys["down"] = True
				elif event.key == K_a:
					pressedKeys["left"] = True
				elif event.key == K_d:
					pressedKeys["right"] = True
				elif event.key == K_ESCAPE:
					mainMenu()
			elif event.type == KEYUP:
				if event.key == K_w:
					pressedKeys["up"] = False
				elif event.key == K_s:
					pressedKeys["down"] = False
				elif event.key == K_a:
					pressedKeys["left"] = False
				elif event.key == K_d:
					pressedKeys["right"] = False
			elif event.type == MOUSEBUTTONDOWN:
				pass
			if event.type == QUIT:
				gameExit()

		screen.blit(cursor, mousePos)
		pygame.display.update()