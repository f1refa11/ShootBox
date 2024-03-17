import pygame
from pygame.locals import QUIT
from funcs import quit
from text import newText
from widgets.button import Button
from confmgr import fpsLimit
def soundSettings():
	from main import cursor,clock
	from screenmgr import screen
	from settingsMenu import settingsMenu
	backButton = Button((20,20), "Back", callback=settingsMenu)
	title = newText("Sound Settings",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		screen.blit(title, (20,92))
		backButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				quit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()