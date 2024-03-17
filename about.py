import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from funcs import quit,loadPathTexture
import path
from text import newText
from widgets.button import Button
from widgets.scrollable import Scrollable
from confmgr import fpsLimit
from constants import CONTRIB_DESIGN, CONTRIB_CODE, CONTRIB_TEST
def about():
	from main import cursor,clock
	from screenmgr import screen
	from mainMenu import mainMenu
	import webbrowser
	text = []
	height = 0

	temp = newText("Design:",size=26)
	text.append((temp, 0, height))
	height += temp.get_height()
	for x in CONTRIB_DESIGN:
		temp = newText(x, italic=True, size=22)
		text.append((temp, 8, height))
		height += temp.get_height()

	height += 8

	temp = newText("Coding:",size=26)
	text.append((temp, 0, height))
	height += temp.get_height()
	for x in CONTRIB_CODE:
		temp = newText(x, italic=True, size=22)
		text.append((temp, 8, height))
		height += temp.get_height()

	height += 8
	
	temp = newText("Testing:",size=26)
	text.append((temp, 0, height))
	height += temp.get_height()
	for x in CONTRIB_TEST:
		temp = newText(x, italic=True, size=22)
		text.append((temp, 8, height))
		height += temp.get_height()
	a = pygame.Surface((screen.get_width(),height), pygame.SRCALPHA)

	for t in text:
		a.blit(t[0], (t[1],t[2]))

	scroll = Scrollable((20,200), a, 350)

	backButton = Button((20,20), "Back", callback=mainMenu)
	title = newText("About", size=32)
	github = loadPathTexture(path.ui, "github.png", size=(64,64))
	ghOpacity = 100
	ghRect = pygame.Rect(20, 130, 64, 64)
	github.set_alpha(ghOpacity)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))
		screen.blit(title, (20, 92))
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

		scroll.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			scroll.eventHold(event)
			if event.type == QUIT:
				quit()
			elif event.type == MOUSEBUTTONDOWN:
				if ghRect.collidepoint(pygame.mouse.get_pos()):
					webbrowser.open_new_tab("https://github.com/f1refa11/ShootBox")
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()