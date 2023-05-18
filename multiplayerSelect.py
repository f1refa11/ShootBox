import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from button import Button
def multiplayerSelect():
	from main import cursor,logo,screen,clock
	from playSelect import playSelect
	backButton = Button((20,20), "Back", callback=playSelect)
	createButton = Button((20,140), "Create World", 240)
	loadButton = Button((20,210), "Load World", 240)
	title = cacheFont("Singleplayer",size=32)
	while 1:
		clock.tick(75)
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