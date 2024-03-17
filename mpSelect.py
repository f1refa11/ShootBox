import pygame
from pygame.locals import QUIT
from funcs import quit
from text import newText
from widgets.button import Button
from widgets.menulist import MenuList
from confmgr import fpsLimit
from screenmgr import screen
from gettext import translation, gettext as _

a = translation("shootbox", "./assets/lang", ['ru'], fallback=True)
def mpSelect():
	from main import cursor,clock
	from mainMenu import mainMenu
	backButton = Button((20,20), "Back", callback=mainMenu)
	menulist = MenuList((0,140), {
		_("Join Server"): lambda x:x,
		_("Host Server"): None
	})
	title = newText(_("Multiplayer"),size=32)
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
				quit()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()