import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confmgr import fpsLimit
def multiplayerSelect():
	from main import cursor,logo,screen,clock
	from playSelect import playSelect
	backButton = Button((20,20), "Back", callback=playSelect)
	join = Button((20,140), "Join Server", 240)
	host = Button((20,210), "Host Server", 240)
	title = cacheFont("Singleplayer",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		join.render(screen)
		host.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()