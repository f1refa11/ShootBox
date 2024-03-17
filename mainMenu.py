import pygame
import funcs
from text import newText
from confmgr import fpsLimit, enableRPC
from constants import VER
from widgets.menulist import MenuList
from gettext import translation, gettext as _

a = translation("shootbox", "./assets/lang", ['ru'], fallback=True)
def mainMenu():
	from main import cursor,logo,clock
	from screenmgr import screen
	from settingsMenu import settingsMenu
	from worldMenu import singleplayerSelect
	from mpSelect import mpSelect
	from about import about
	import modules.notifications as notifications
	logo.set_alpha(0)
	
	#defining buttons
	startPos = (0, logo.get_height()+24)
	ver = newText(VER, size=18)
	verRect = ver.get_rect()
	verRect.bottomright = screen.get_rect().bottomright

	# updating discord rpc if enabled
	if enableRPC:
		from main import RPC,rpcState
		if rpcState != "menu":
			RPC.update(
				state=_("Idle"),
				details=_("In the main menu"),
				buttons= [{"label": "GitHub Repo", "url": "https://github.com/f1refa11/ShootBox"},]
			)
			rpcState = "menu"
	
	menulist = MenuList(startPos, {
		_("Singleplayer"): singleplayerSelect,
		_("Multiplayer"): mpSelect,
		_("Settings"): settingsMenu,
		_("About"): about,
		_("Exit"): funcs.quit
	})
	
	notifications.newNotify("bruhs? bruh bruhich is now verybruh! come bruh it!", "bruh bruh bruruuuuh bruhrbubub burfububr bruhuhuhuh. bruh bruh, brubruburburb.")
	while 1:
		# TODO: put tick algorithm into function
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		screen.blit(logo, (12, 12))

		#logo appear animation
		if logo.get_alpha() < 255:
			logo.set_alpha(logo.get_alpha()+5)
		
		menulist.render(screen)

		screen.blit(ver, verRect)
		notifications.renderMain()

		for event in pygame.event.get():
			notifications.eventHold(event)
			menulist.eventHold(event)
			if event.type == pygame.QUIT:
				funcs.quit()
			# elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				# notifications.newNotify("bruhs? bruh bruhich is now verybruh! come bruh it!", "bruh bruh bruruuuuh bruhrbubub burfububr bruhuhuhuh. bruh bruh, brubruburburb.")

		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()