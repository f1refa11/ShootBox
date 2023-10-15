import pygame
from pygame.locals import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from widgets.textArea import TextArea
from confmgr import fpsLimit
def worldCreate():
	from main import cursor,logo,screen,clock
	from singleplayerSelect import singleplayerSelect
	from game import game
	backButton = Button((20,20), "Back", callback=singleplayerSelect)
	worldName = TextArea((20,140), text="New world", placeholder="World name")
	title = cacheFont("Create new World", size=32)
	createButton = Button((20, 220), "Create", autoresizeOffset=32, callback=game)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		worldName.render(screen)
		createButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			worldName.eventHold(event)
			createButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()