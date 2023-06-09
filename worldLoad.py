import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from button import Button
from confvar import fpsLimit
def worldLoad():
	from main import cursor,logo,screen,clock
	from singleplayerSelect import singleplayerSelect
	backButton = Button((20,20), "Back", callback=singleplayerSelect)
	title = cacheFont("Load existing World", size=32)
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