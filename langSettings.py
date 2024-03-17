import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from funcs import quit
from text import newText
from widgets.button import Button
from widgets.menulist import MenuList
from confmgr import fpsLimit
from constants import LANGS
def langSettings():
	from main import cursor,clock
	from screenmgr import screen
	from settingsMenu import settingsMenu
	import confmgr
	import i18n
	backButton = Button((20,20), "Back", callback=settingsMenu)
	title = newText("Language Settings",size=32)
	warning = newText("Please note that not all translations are complete; the reason is that nearly all translations are supported by community. The percentage shows how much of the language is translated.", size=15, wraplength=screen.get_width())
	langsSurfs = {}
	langsRects = {}
	localLang = confmgr.lang
	for idx,langKey in enumerate(LANGS.keys()):
		if confmgr.lang != langKey:
			tmpText = newText(LANGS[langKey], (177, 177, 177), 20)
			langsSurfs[langKey] = tmpText
		else:
			tmpText = newText(LANGS[langKey], size=20)
			langsSurfs[langKey] = tmpText
			localLang = langKey
		langsRects[langKey] = pygame.Rect(20, 180+idx*28, tmpText.get_width(), tmpText.get_height())
	while 1:
		clock.tick(fpsLimit)
		screen.fill((28, 21, 53))
		screen.blit(title, (20,92))
		screen.blit(warning, (20,130))
		for langItem in langsSurfs.keys():
			screen.blit(langsSurfs[langItem], langsRects[langItem])
		backButton.render(screen)
		for event in pygame.event.get():
			backButton.eventHold(event)
			if event.type == QUIT:
				quit()
			elif event.type == MOUSEBUTTONDOWN:
				for lng in langsRects.keys():
					if langsRects[lng].collidepoint(pygame.mouse.get_pos()):
						langsSurfs[localLang] = newText(LANGS[localLang], (177, 177, 177), 20)
						langsSurfs[lng] = newText(LANGS[lng], size=20)
						localLang = lng
						confmgr.config["lang"] = confmgr.lang = lng
						i18n.reload()
						langSettings()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()