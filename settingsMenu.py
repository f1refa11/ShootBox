import pygame
from pygame import QUIT
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confvar import fpsLimit
def settingsMenu():
	from main import cursor,logo,screen,clock
	from mainMenu import mainMenu
	from graphicsSettings import graphicsSettings
	from soundSettings import soundSettings
	from langSettings import langSettings
	backButton = Button((20,20), "Back", callback=mainMenu)
	graphicsButton = Button((20,140), "Graphics", 240, callback=graphicsSettings)
	soundButton = Button((20,210), "Sound", 240, callback=soundSettings)
	langButton = Button((20,280), "Language", 240, callback=langSettings)
	title = cacheFont("Settings",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		renderFont(title, (20,92), screen)
		backButton.render(screen)
		graphicsButton.render(screen)
		soundButton.render(screen)
		langButton.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()