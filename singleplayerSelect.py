import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confmgr import fpsLimit
def singleplayerSelect():
	from main import cursor,logo,clock
	from screenmgr import screen
	from playSelect import playSelect
	from worldLoad import worldLoad
	from worldCreate import worldCreate
	# from game import game
	backButton = Button((20,20), "Back", callback=playSelect)
	createButton = Button((20,140), "Create World", 240, callback=worldCreate)
	loadButton = Button((20,210), "Load World", 240, callback=worldLoad)
	title = cacheFont("Singleplayer",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		createButton.render(screen)
		loadButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			createButton.eventHold(event)
			loadButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()