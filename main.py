# -*- coding: utf-8 -*-
CHUNKSIZE = 8
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

def gameExit():
	pygame.exit()
	exit()

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
blocksPath = os.path.join(texturesPath, "blocks")
playerPath = os.path.join(texturesPath, "player")

#loading all assets
#ui assets
cursor = loadPathTexture(uiTexturesPath, "cursor.png", True, (64, 64))
buttonCornerLeft = loadPathTexture(uiTexturesPath, "buttonCorner.png", True, (16, 64))
buttonCornerLeftActive = loadPathTexture(uiTexturesPath, "buttonCornerActive.png", True, (16, 64))
buttonCornerRight = pygame.transform.flip(buttonCornerLeft, True, False)
buttonCornerRightActive = pygame.transform.flip(buttonCornerLeftActive, True, False)
buttonBody = loadPathTexture(uiTexturesPath, "buttonBody.png", True, (16, 64))
buttonBodyActive = loadPathTexture(uiTexturesPath, "buttonBodyActive.png", True, (16, 64))

#ground assets
grass = loadPathTexture(blocksPath, "grass.png", True, (64, 64))
sand = loadPathTexture(blocksPath, "sand.png", True, (64, 64))

#player assets
playerIdle = loadPathTexture(playerPath, "idle.png", True, (64, 64))

#loading fonts
fonts = []
for x in range(1, 100):
	fonts.append(pygame.font.Font(os.path.join(resourcesPath, "font.ttf"), x))

#defining fonts functions
#prerender text to return as Surface
def cacheFont(text, color = (255, 255, 255), size=24, antialiasing=True) -> pygame.Surface:
	return fonts[size].render(text, antialiasing, color)

#render prerendered text(see cacheFont) to surface(default: screen)
def renderFont(render, pos, surface: pygame.Surface = screen):
	surface.blit(render, pos)

#defining classes
#UI classes
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
	def render(self, screen: pygame.Surface = screen):
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
		renderFont(self.text, self.textRect)
	def eventHold(self, event):
		#running callback if mouse clicked on button
		if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
			self.callback()

#player class
class Player:
	def __init__(self, pos) -> None:
		self.x, self.y = pos
		self.speed = 3
	def render(self, surface: pygame.Surface):
		surface.blit(playerIdle, (self.x, self.y))

#stopping loading screen after setting things up
loadingScreen = False

def mainMenu():
	logo.set_alpha(0)
	
	#defining buttons
	playBtn = Button((12, logo.get_height()+24), "Play", 240, callback=game)
	settingsBtn = Button((12, playBtn.rect.bottom+4), "Settings", 240)
	aboutBtn = Button((12, settingsBtn.rect.bottom+4), "About", 240)
	exitBtn = Button((12, aboutBtn.rect.bottom+4), "Exit", 240, callback=exit)
	while 1:
		clock.tick(60)
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
		
		playBtn.render()
		settingsBtn.render()
		aboutBtn.render()
		exitBtn.render()
		
		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()

chunks = []
for x in range(512):
	for y in range(512):
		chunks.append([x,y])

def game():
	player = Player((8, 8))
	pressedKeys = {
		"up": False,
		"down": False,
		"left": False,
		"right": False,
	}
	playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
	loadedChunks = []
	for x in range(1):
		for y in range(1):
			x1 = playerChunkPos[0]+x
			y1 = playerChunkPos[1]+y
			if [x1,y1] in chunks:
				loadedChunks.append([x1,y1])
	print(loadedChunks)
	while 1:
		clock.tick(60)
		screen.fill((51, 153, 218))

		if playerChunkPos != (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE)):
			playerChunkPos = (player.x//(64*CHUNKSIZE), player.y//(64*CHUNKSIZE))
			loadedChunks.clear()
			for x in range(1):
				for y in range(1):
					x1 = playerChunkPos[0]+x
					y1 = playerChunkPos[1]+y
					if [x1,y1] in chunks:
						loadedChunks.append([x1,y1])
			print(loadedChunks)

		for chunk in loadedChunks:
			chunkRect = pygame.Rect(chunk[0]*64*CHUNKSIZE, chunk[1]*64*CHUNKSIZE, 64*CHUNKSIZE, 64*CHUNKSIZE)
			chunkSurface = pygame.Surface((64*CHUNKSIZE, 64*CHUNKSIZE))
			chunkSurface.fill((57, 194, 114))
			screen.blit(chunkSurface, chunkRect)

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_w:
					pressedKeys["up"] = True
				elif event.key == K_s:
					pressedKeys["down"] = True
				elif event.key == K_a:
					pressedKeys["left"] = True
				elif event.key == K_d:
					pressedKeys["right"] = True
				elif event.key == K_ESCAPE:
					mainMenu()
			elif event.type == KEYUP:
				if event.key == K_w:
					pressedKeys["up"] = False
				elif event.key == K_s:
					pressedKeys["down"] = False
				elif event.key == K_a:
					pressedKeys["left"] = False
				elif event.key == K_d:
					pressedKeys["right"] = False
			if event.type == QUIT:
				gameExit()

		if pressedKeys["up"]:
			player.y -= player.speed
		if pressedKeys["down"]:
			player.y += player.speed
		if pressedKeys["left"]:
			player.x -= player.speed
		if pressedKeys["right"]:
			player.x += player.speed
		player.render(screen)

		screen.blit(cursor, pygame.mouse.get_pos())
		pygame.display.update()
	
mainMenu()