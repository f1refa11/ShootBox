import pygame
from pygame.locals import QUIT
from button import Button
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from confvar import fpsLimit
def graphicsSettings():
	from main import cursor,logo,screen,clock
	from settingsMenu import settingsMenu
	backButton = Button((20,20), "Back", callback=settingsMenu)
	title = cacheFont("Graphics Settings",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()