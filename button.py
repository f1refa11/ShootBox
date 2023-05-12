import pygame,os,sys
from pygame import MOUSEBUTTONDOWN
from paths import *

def loadPathTexture(path, name, antialias=True, size=None):
	if size == None:
		return pygame.image.load(os.path.join(path, name)).convert_alpha()
	else:
		if antialias:
			return pygame.transform.smoothscale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()
		else:
			return pygame.transform.scale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()

fonts = []
for x in range(1, 100):
	fonts.append(pygame.font.Font(os.path.join(resourcesPath, "font.ttf"), x))

def cacheFont(text, color = (255, 255, 255), size=24, antialiasing=True) -> pygame.Surface:
	return fonts[size].render(text, antialiasing, color)

#render prerendered text(see cacheFont) to surface(default: screen)
def renderFont(render, pos, surface: pygame.Surface):
	surface.blit(render, pos)

buttonCornerLeft = loadPathTexture(uiTexturesPath, "buttonCorner.png", True, (16, 64))
buttonCornerLeftActive = loadPathTexture(uiTexturesPath, "buttonCornerActive.png", True, (16, 64))
buttonCornerRight = pygame.transform.flip(buttonCornerLeft, True, False)
buttonCornerRightActive = pygame.transform.flip(buttonCornerLeftActive, True, False)
buttonBody = loadPathTexture(uiTexturesPath, "buttonBody.png", True, (16, 64))
buttonBodyActive = loadPathTexture(uiTexturesPath, "buttonBodyActive.png", True, (16, 64))
class Button:
	def __init__(self, pos, text, width=None, autoresizeOffset=8, callback=None):
		#saving arguments as variables
		self.pos = pos
		if width != None: self.width = width
		self.text = text
		self.active = False
		self.callback = callback

		#prerendering text
		self.text = cacheFont(text)

		#defining width if None
		if self.width == None: self.width = self.text.get_width()+autoresizeOffset

		#defining button rects
		self.rect = pygame.Rect(pos, (self.width, 64))
		self.cornerLeftRect = pygame.Rect(pos, (16, 64))
		self.bodyRect = pygame.Rect((pos[0]+16, pos[1]), (self.width-32, 64))
		self.cornerRightRect = pygame.Rect((pos[0]+(self.width-16), pos[1]), (16, 64))

		#scaling body texture
		self.bodyTexture = pygame.transform.scale(buttonBody, (self.width-32, 64))
		self.bodyTextureActive = pygame.transform.scale(buttonBodyActive, (self.width-32, 64))

		self.textRect = pygame.Rect((pos[0]+self.rect.w//2-self.text.get_width()//2, pos[1]+(self.rect.h//2-self.text.get_height()//2)), (self.text.get_width(), self.text.get_height()))
	def render(self, screen: pygame.Surface):
		#checking if button is hovered by mouse
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			self.active = True
		else:
			self.active = False
		
		#rendering button depending on state
		if self.active:
			screen.blit(buttonCornerLeftActive, self.cornerLeftRect)
			screen.blit(self.bodyTextureActive, self.bodyRect)
			screen.blit(buttonCornerRightActive, self.cornerRightRect)
		else:
			screen.blit(buttonCornerLeft, self.cornerLeftRect)
			screen.blit(self.bodyTexture, self.bodyRect)
			screen.blit(buttonCornerRight, self.cornerRightRect)
		#rendering text
		renderFont(self.text, self.textRect, screen)
	def eventHold(self, event):
		#running callback if mouse clicked on button
		if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
			self.callback()