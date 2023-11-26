import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from funcs import gameExit,loadPathTexture
from paths import uiTexturesPath
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confmgr import fpsLimit
def about():
	from main import cursor,clock
	from screenmgr import screen
	from mainMenu import mainMenu
	import webbrowser
	backButton = Button((20,20), "Back", callback=mainMenu)
	title = cacheFont("About", size=32)
	github = loadPathTexture(uiTexturesPath, "github.png", size=(64,64))
	ghOpacity = 100
	ghRect = pygame.Rect(20, 130, 64, 64)
	github.set_alpha(ghOpacity)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))
		renderFont(title, (20, 92), screen)
		backButton.render(screen)

		if ghRect.collidepoint(pygame.mouse.get_pos()):
			if ghOpacity < 255:
				ghOpacity += 8
				github.set_alpha(ghOpacity)
		else:
			if ghOpacity > 100:
				ghOpacity -= 8
				github.set_alpha(ghOpacity)
		screen.blit(github, ghRect)

		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
			elif event.type == MOUSEBUTTONDOWN:
				if ghRect.collidepoint(pygame.mouse.get_pos()):
					webbrowser.open_new_tab("https://github.com/f1refa11/ShootBox")
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()