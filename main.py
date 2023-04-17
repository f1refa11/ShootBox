# -*- coding: utf-8 -*-
#importing other libraries
import os,json,threading
from sys import exit

#removing Pygame welcome notice
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#importing pygame and its extensions
import pygame
from pygame.locals import *

# defining functions
def openJSON(filename):
	return json.load(open(filename, "r", encoding="utf-8"))

def saveJSON(var, filename):
	json.dump(var, open(filename, "w", encoding="utf-8"))

def loadPathTexture(path, name, antialias=True, size=None):
	if size == None:
		return pygame.image.load(os.path.join(path, name)).convert_alpha()
	else:
		if antialias:
			return pygame.transform.smoothscale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()
		else:
			return pygame.transform.scale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()

#loading config file
config = openJSON("config.json")

# initializing pygame
pygame.init()

#init screen
screen = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("ShootBox")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

#configuring essential paths
rootPath = os.path.dirname(__file__)
resourcesPath = os.path.join(rootPath, "resources")
texturesPath = os.path.join(resourcesPath, "textures")
uiTexturesPath = os.path.join(texturesPath, "ui")

#loading logo
logo = loadPathTexture(uiTexturesPath, "logo.png")

#setting essential for startup variables
loadingScreenSize = (screen.get_width(), screen.get_height())
loadingRect_base = pygame.Rect(loadingScreenSize[0]//2-200, loadingScreenSize[1]-88, 400, 24)
loadingRect = pygame.Rect(loadingRect_base.x+4, loadingRect_base.y+4, 0, 16)
loadingLogoRect = logo.get_rect()
loadingLogoRect.x = loadingScreenSize[0]//2-224
loadingLogoRect.y = loadingRect_base.y - 112
loadingScreen = True

#defining loading screen
def renderLoadScreen():
	global loadingRect
	while loadingScreen:
		screen.fill((11, 9, 24))
		clock.tick(30)
		pygame.draw.rect(screen, (255, 255, 255), loadingRect_base, 2)
		pygame.draw.rect(screen, (255, 255, 255), loadingRect)
		pygame.display.update()

#setting up and starting loading screen thread
loadingDisplayThread = threading.Thread(target=renderLoadScreen)
loadingDisplayThread.setDaemon(True)
loadingDisplayThread.start()

#loading all paths


#loading all assets
cursor = loadPathTexture(uiTexturesPath, "cursor.png", True, (64, 64))
buttonCornerLeft = loadPathTexture(uiTexturesPath, "buttonCorner.png", True, (16, 64))
buttonCornerLeftActive = loadPathTexture(uiTexturesPath, "buttonCornerActive.png", True, (16, 64))
buttonCornerRight = pygame.transform.flip(buttonCornerLeft, True, False)
buttonCornerRightActive = pygame.transform.flip(buttonCornerLeftActive, True, False)
buttonBody = loadPathTexture(uiTexturesPath, "buttonBody.png", True, (16, 64))
buttonBodyActive = loadPathTexture(uiTexturesPath, "buttonBodyActive.png", True, (16, 64))

#loading fonts
fonts = []
for x in range(1, 100):
	fonts.append(pygame.font.Font(os.path.join(resourcesPath, "font.ttf"), x))

#defining fonts functions
#prerender text to return as Surface
def cacheFont(text: str, color = (255, 255, 255), size=24, antialiasing=True):
	return fonts[size].render(text, antialiasing, color)

#render prerendered text(see cacheFont) to surface(default screen)
def renderFont(render, pos, surface: pygame.Surface = screen):
	surface.blit(render, pos)

#defining classes
#UI classes
class Button:
	def __init__(self, pos, width, text):
		#saving arguments as variables
		self.pos = pos
		self.width = width
		self.text = text
		self.active = False

		#defining button rects
		self.rect = pygame.Rect(pos, (self.width, 64))
		self.cornerLeftRect = pygame.Rect(pos, (16, 64))
		self.bodyRect = pygame.Rect((pos[0]+16, pos[1]), (self.width-32, 64))
		self.cornerRightRect = pygame.Rect((pos[0]+(self.width-16), pos[1]), (16, 64))

		#scaling body texture
		self.bodyTexture = pygame.transform.scale(buttonBody, (width-32, 64))
		self.bodyTextureActive = pygame.transform.scale(buttonBodyActive, (width-32, 64))
	def render(self, screen):
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

#stopping loading screen after setting things up
loadingScreen = False

def mainMenu():
	testButton = Button((16, 16), 256, "bober")
	while 1:
		clock.tick(60)
		screen.fill((28, 21, 53))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
		testButton.render(screen)
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()
	
mainMenu()