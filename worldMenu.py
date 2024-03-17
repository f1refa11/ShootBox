import pygame
from pygame.locals import QUIT
from funcs import quit
from text import newText
from widgets.button import Button
from widgets.scrollable import Scrollable
from confmgr import fpsLimit
import glob
import os
from funcs import openJSON
# TODO: add support for drag-n-dropping world folders to import
def singleplayerSelect():
	from main import cursor,clock
	from screenmgr import screen
	from mainMenu import mainMenu

	# from game import game
	backButton = Button((10,10), "Back", callback=mainMenu)
	worldsList = glob.glob("worlds/*/")
	if not os.path.isdir('worlds'):
		os.mkdir('worlds')
		worldsList = glob.glob("worlds/*/")
	validWorlds = []
	for world in worldsList:
		try:
			worldMeta = openJSON(world+"meta.json")
			validWorlds.append(worldMeta)
		except FileNotFoundError:
			pass
	# generating small surfaces
	worldSurfaces = [] # (title surface, description surf)
	worldsSurfHeight = 0
	for vWorld in validWorlds:
		tempTitle = newText(vWorld["title"], size=24, wraplength=round((screen.get_width()-8)*0.55))
		worldSurfaces.append((tempTitle,worldsSurfHeight))
		worldsSurfHeight += tempTitle.get_height() +8
	# TODO: make scrolling + make it smooth af
	worldsSurf = pygame.Surface(((screen.get_width()-8)*0.55, worldsSurfHeight), pygame.SRCALPHA)
	for worldPart in worldSurfaces:
		worldsSurf.blit(worldPart[0], (0, worldPart[1]))
		
	testRect = pygame.Rect(0,100,100,64)

	if len(validWorlds) > 1:
		scrollableWorldList = Scrollable((4,134), worldsSurf, 400)
	noWorlds = newText("No worlds found!")
	title = newText("Singleplayer",size=28)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		screen.blit(title, (20,92))
		backButton.render(screen)
		if len(validWorlds) < 1:
			screen.blit(noWorlds, (20, 140))

		if len(validWorlds) > 1:
			scrollableWorldList.render(screen)
		
		pygame.draw.rect(scrollableWorldList.sourceSurf, (255, 0, 0), testRect, 2)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if len(validWorlds) > 1:
				scrollableWorldList.eventHold(event)
			if event.type == QUIT:
				quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if pygame.Rect((testRect.x + scrollableWorldList.pos[0], testRect.y + scrollableWorldList.pos[1]), (testRect.size)).collidepoint(pygame.mouse.get_pos()):
					print("пенис")
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()