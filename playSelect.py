import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from button import Button
def playSelect():
	from main import cursor,logo,screen,clock
	from mainMenu import mainMenu
	from singleplayerSelect import singleplayerSelect
	from multiplayerSelect import multiplayerSelect
	backButton = Button((20,20), "Back", callback=mainMenu)
	singleplayerButton = Button((20,140), "Singleplayer", 240, callback=singleplayerSelect)
	multiplayerButton = Button((20,210), "Multiplayer", 240, callback=multiplayerSelect)
	title = cacheFont("Settings",size=32)
	while 1:
		clock.tick(75)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		singleplayerButton.render(screen)
		multiplayerButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			singleplayerButton.eventHold(event)
			multiplayerButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()