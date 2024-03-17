import pygame
import os
import path
# preload font sizes
fonts = []
for x in range(1, 100):
	fonts.append(pygame.font.Font(os.path.join(path.assets, "font.ttf"), x))
	
#prerender text to return as Surface
def newText(text, color = (255, 255, 255), size=24, antialiasing=True, wraplength=0, align=pygame.FONT_LEFT, bold=False, italic=False) -> pygame.Surface:
	fonts[size].align = align
	fonts[size].bold = bold
	fonts[size].italic = italic

	from i18n import loc
	try:
		return fonts[size].render(loc[text], antialiasing, color, wraplength=wraplength)
	except:
		return fonts[size].render(text, antialiasing, color, wraplength=wraplength)