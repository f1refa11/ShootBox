import pygame
from pygame import QUIT
from funcs import *
from button import Button
from game import game
logo = loadPathTexture(uiTexturesPath, "logo.png")
def mainMenu(screen: pygame.Surface, clock: pygame.time.Clock):
	logo.set_alpha(0)
	
	#defining buttons
	playBtn = Button((12, logo.get_height()+24), "Play", 240, callback=game)
	settingsBtn = Button((12, playBtn.rect.bottom+4), "Settings", 240)
	aboutBtn = Button((12, settingsBtn.rect.bottom+4), "About", 240)
	exitBtn = Button((12, aboutBtn.rect.bottom+4), "Exit", 240, callback=exit)
	while 1:
		clock.tick(75)
		screen.fill((28, 21, 53))

		screen.blit(logo, (12, 12))

		#logo appear animation
		if logo.get_alpha() < 255:
			logo.set_alpha(logo.get_alpha()+5)

		for event in pygame.event.get():
			playBtn.eventHold(event)
			# settingsBtn.eventHold(event)
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