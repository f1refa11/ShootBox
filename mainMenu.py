import pygame
from pygame import QUIT
from funcs import gameExit
from widgets.button import Button
from confvar import fpsLimit, enableRPC
from sys import exit
def mainMenu():
	from main import cursor,logo,screen,clock,RPC,rpcState
	from settingsMenu import settingsMenu
	from playSelect import playSelect
	logo.set_alpha(0)
	
	#defining buttons
	playBtn = Button((12, logo.get_height()+24), "Play", 240, callback=playSelect)
	settingsBtn = Button((12, playBtn.rect.bottom+4), "Settings", 240, callback=settingsMenu)
	aboutBtn = Button((12, settingsBtn.rect.bottom+4), "About", 240)
	exitBtn = Button((12, aboutBtn.rect.bottom+4), "Exit", 240, callback=exit)

	if enableRPC:
		if rpcState != "menu":
			RPC.update(
				state="Простаивает",
				details="В главном меню",
				buttons= [{"label": "GitHub Repo", "url": "https://github.com/f1refa11/ShootBox"},]
			)
			rpcState = "menu"
	
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
			# aboutBtn.eventHold(event)
			exitBtn.eventHold(event)
			if event.type == QUIT:
				gameExit()
		
		playBtn.render(screen)
		settingsBtn.render(screen)
		aboutBtn.render(screen)
		exitBtn.render(screen)
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()