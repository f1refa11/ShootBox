import pygame
from pygame import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confmgr import fpsLimit
def settingsMenu():
	from main import cursor, clock
	from screenmgr import screen
	from mainMenu import mainMenu
	from graphicsSettings import graphicsSettings
	from soundSettings import soundSettings
	from langSettings import langSettings
	from modulesMenu import modulesMenu
	backButton = Button((20,20), "Back", callback=mainMenu)
	graphicsButton = Button((20,140), "Graphics", 240, callback=graphicsSettings)
	soundButton = Button((20,210), "Sound", 240, callback=soundSettings)
	langButton = Button((20,280), "Language", 240, callback=langSettings)
	modulesButton = Button((20,350), "Modules", 240, callback=modulesMenu)
	title = cacheFont("Settings",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		graphicsButton.render(screen)
		soundButton.render(screen)
		langButton.render(screen)
		modulesButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			graphicsButton.eventHold(event)
			soundButton.eventHold(event)
			langButton.eventHold(event)
			modulesButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()