import pygame
from pygame import QUIT
from funcs import gameExit
from fontmgr import cacheFont
from widgets.button import Button
from confmgr import fpsLimit, enableRPC
from constants import VER
def mainMenu():
	from main import cursor,logo,screen,clock
	from settingsMenu import settingsMenu
	from playSelect import playSelect
	from about import about
	import modules.notifications as notifications
	logo.set_alpha(0)
	
	#defining buttons
	playBtn = Button((12, logo.get_height()+24), "Play", 240, callback=playSelect)
	settingsBtn = Button((12, playBtn.rect.bottom+4), "Settings", 240, callback=settingsMenu)
	aboutBtn = Button((12, settingsBtn.rect.bottom+4), "About", 240, callback=about)
	exitBtn = Button((12, aboutBtn.rect.bottom+4), "Exit", 240, callback=gameExit)
	# caching version title
	ver = cacheFont(VER, size=18)
	verRect = ver.get_rect()
	verRect.bottomright = screen.get_rect().bottomright

	# updating discord rpc if enabled
	if enableRPC:
		from main import RPC,rpcState
		if rpcState != "menu":
			RPC.update(
				state="Простаивает",
				details="В главном меню",
				buttons= [{"label": "GitHub Repo", "url": "https://github.com/f1refa11/ShootBox"},]
			)
			rpcState = "menu"
	
	notifications.newNotify("bruhs? bruh bruhich is now verybruh! come bruh it!", "bruh bruh bruruuuuh bruhrbubub burfububr bruhuhuhuh. bruh bruh, brubruburburb.")
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))

		screen.blit(logo, (12, 12))

		#logo appear animation
		if logo.get_alpha() < 255:
			logo.set_alpha(logo.get_alpha()+5)

		for event in pygame.event.get():
			playBtn.eventHold(event)
			settingsBtn.eventHold(event)
			aboutBtn.eventHold(event)
			exitBtn.eventHold(event)
			notifications.eventHold(event)
			if event.type == QUIT:
				gameExit()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				notifications.newNotify("bruhs? bruh bruhich is now verybruh! come bruh it!", "bruh bruh bruruuuuh bruhrbubub burfububr bruhuhuhuh. bruh bruh, brubruburburb.")
		playBtn.render(screen)
		settingsBtn.render(screen)
		aboutBtn.render(screen)
		exitBtn.render(screen)
		screen.blit(ver, verRect)
		notifications.renderMain()

		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()