import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from funcs import gameExit
from fontmgr import cacheFont,renderFont
from widgets.button import Button
from confmgr import fpsLimit
from constants import LANGS
def langSettings():
	from main import cursor,screen,clock
	from settingsMenu import settingsMenu
	import confmgr
	import local
	backButton = Button((20,20), "Back", callback=settingsMenu)
	title = cacheFont("Language Settings",size=32)
	warning = cacheFont("Please note that not all translations are complete; the reason is that nearly all translations are supported by community. The percentage shows how much of the language is translated.", size=15, wraplength=screen.get_width())
	langsSurfs = {}
	langsRects = {}
	localLang = confmgr.lang
	for idx,langKey in enumerate(LANGS.keys()):
		if confmgr.lang != langKey:
			tmpText = cacheFont(LANGS[langKey], (177, 177, 177), 20)
			langsSurfs[langKey] = tmpText
		else:
			tmpText = cacheFont(LANGS[langKey], size=20)
			langsSurfs[langKey] = tmpText
			localLang = langKey
		langsRects[langKey] = pygame.Rect(20, 180+idx*28, tmpText.get_width(), tmpText.get_height())
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))
		renderFont(title, (20,92), screen)
		renderFont(warning, (20,130), screen)
		for langItem in langsSurfs.keys():
			renderFont(langsSurfs[langItem], langsRects[langItem], screen)
			pygame.draw.rect(screen, (255, 0, 0), langsRects[langItem], 1)
		backButton.render(screen)
		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				gameExit()
			elif event.type == MOUSEBUTTONDOWN:
				for lng in langsRects.keys():
					if langsRects[lng].collidepoint(pygame.mouse.get_pos()):
						langsSurfs[localLang] = cacheFont(LANGS[localLang], (177, 177, 177), 20)
						langsSurfs[lng] = cacheFont(LANGS[lng], size=20)
						localLang = lng
						confmgr.config["lang"] = lng
						confmgr.lang = confmgr.config["lang"]
						local.reload()
						langSettings()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()