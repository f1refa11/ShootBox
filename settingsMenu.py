import pygame
from pygame import QUIT
import funcs
from text import newText
from widgets.button import Button
from widgets.menulist import MenuList
from confmgr import fpsLimit
from gettext import translation, gettext as _

# TODO: make settings in one page with cool sidebar with icons(basically like VSCode)

a = translation("shootbox", "./assets/lang", ['ru'], fallback=True)
def settingsMenu():
	from main import cursor, clock
	from screenmgr import screen
	from mainMenu import mainMenu
	from graphicsSettings import graphicsSettings
	from soundSettings import soundSettings
	from langSettings import langSettings
	from modulesMenu import modulesMenu
	backButton = Button((20,20), "Back", callback=mainMenu)
	menulist = MenuList((0,140), {
		_("Graphics"): graphicsSettings,
		_("Sound"): soundSettings,
		_("Language"): langSettings
	})
	modulesButton = Button((20,350), "Modules", 240, callback=modulesMenu)
	title = newText("Settings",size=32)
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		screen.blit(title, (20,92))
		backButton.render(screen)
		menulist.render(screen)

		for event in pygame.event.get():
			backButton.eventHold(event)
			menulist.eventHold(event)
			if event.type == QUIT:
				funcs.quit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()