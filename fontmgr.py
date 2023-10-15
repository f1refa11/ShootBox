import pygame,os
from paths import resourcesPath
# preload font sizes
fonts = []
for x in range(1, 100):
	fonts.append(pygame.font.Font(os.path.join(resourcesPath, "font.ttf"), x))
	
#prerender text to return as Surface
def cacheFont(text, color = (255, 255, 255), size=24, antialiasing=True, wraplength=0, align=pygame.FONT_LEFT, bold=False, italic=False) -> pygame.Surface:
	fonts[size].align = align
	fonts[size].bold = bold
	fonts[size].italic = italic

	from local import loc
	try:
		return fonts[size].render(loc[text], antialiasing, color, wraplength=wraplength)
	except:
		return fonts[size].render(text, antialiasing, color, wraplength=wraplength)

#render prerendered text(see cacheFont) to surface(default: screen)
def renderFont(render, pos, surface: pygame.Surface):
	surface.blit(render, pos)