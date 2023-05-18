import pygame
from pygame import MOUSEBUTTONDOWN
from paths import uiTexturesPath
from funcs import loadPathTexture
from fontmgr import cacheFont,renderFont
textAreaLeft = loadPathTexture(uiTexturesPath, "textAreaCorner.png", True, (16, 64))
textAreaLeftActive = loadPathTexture(uiTexturesPath, "textAreaCornerActive.png", True, (16, 64))
textAreaRight = pygame.transform.flip(textAreaLeft, True, False)
textAreaRightActive = pygame.transform.flip(textAreaLeftActive, True, False)
textAreaBody = loadPathTexture(uiTexturesPath, "textAreaBody.png", True, (16, 64))
textAreaBodyActive = loadPathTexture(uiTexturesPath, "textAreaBodyActive.png", True, (16, 64))
class TextArea:
	def __init__(self, pos, width=240, maxLen=128, text="", placeholder="", color=(0,0,0)):
		# passing arguments to variables
		self.pos = pos
		self.width = width
		self.maxLen = maxLen
		self.text = text
		self.placeholder = placeholder
		self.color = color

		# setting default variables
		self.active = False

		# prerendering default text
		self.textRender = cacheFont(self.text, self.color)
		self.placeholderText = cacheFont(self.placeholder, (179, 179, 179))
		
		# calculating main widget rects
		self.rect = pygame.Rect(pos, (self.width, 64))
		self.cornerLeftRect = pygame.Rect(pos, (16, 64))
		self.bodyRect = pygame.Rect((pos[0]+16, pos[1]), (self.width-32, 64))
		self.cornerRightRect = pygame.Rect((pos[0]+(self.width-16), pos[1]), (16, 64))
		
		# generating text surface
		self.textSurface = pygame.Surface((self.rect.w-16,self.rect.h-16), pygame.SRCALPHA, 32)
		self.textSurfaceRect = pygame.Rect(self.rect.x+8,self.rect.y+8,self.rect.w-16,self.rect.h-16)

		# generating body texture
		self.bodyTexture = pygame.transform.scale(textAreaBody, (self.width-32, 64))
		self.bodyTextureActive = pygame.transform.scale(textAreaBodyActive, (self.width-32, 64))

		# creating other rects
		self.textRect = self.textRender.get_rect(x=0)
		self.textRect.y = (self.textSurfaceRect.h-self.textRect.h)*0.5
		if self.textRect.w > self.textSurfaceRect.w:
			self.textRect.right = self.textSurfaceRect.right-8

		self.textCursor = pygame.Rect((self.textSurfaceRect.x+self.textRect.right+2, self.textSurfaceRect.y), (2, self.textSurfaceRect.bottom-self.textSurfaceRect.y))

		# backspace variables
		self.bckSpaceEnabled = False
		self.bckSpaceCountdown = False
		self.bckSpaceDelay = 10
		self.bckSpaceTime = 4
		self.bckSpaceCurrent = 0
		self.bckSpaceDelayCurrent = 0
	def updateText(self):
		# updating texts and its rects(used when self.text is changed)
		self.textRender = cacheFont(self.text, self.color)
		self.placeholderText = cacheFont(self.placeholder, (179, 179, 179))
		self.textRect = self.textRender.get_rect(x=0)
		self.textRect.y = (self.textSurfaceRect.h-self.textRect.h)*0.5
		if self.textRect.w > self.textSurfaceRect.w:
			self.textRect.right = self.textSurfaceRect.w
		self.textCursor = pygame.Rect((self.textSurfaceRect.x+self.textRect.right+2, self.textSurfaceRect.y), (2, self.textSurfaceRect.bottom-self.textSurfaceRect.y))
	def eventHold(self, event):
		# if clicked on TextArea
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				self.active = True
			else:
				self.active = False
		# if KEYDOWN and backspace
		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
					self.updateText()
					self.bckSpaceCountdown = True
		# backspace reset when KEYUP
		if event.type == pygame.KEYUP:
			self.bckSpaceCountdown = False
			self.bckSpaceCurrent = 0
			self.bckSpaceDelayCurrent = 0
			self.bckSpaceEnabled = False
		# text input event
		if event.type == pygame.TEXTINPUT:
			if self.active:
				if len(self.text) <= self.maxLen:
					self.text += event.text
					self.updateText()
	def render(self, screen: pygame.Surface):
		#backspace thing
		if self.bckSpaceCountdown:
			if self.bckSpaceDelayCurrent < self.bckSpaceDelay:
				self.bckSpaceDelayCurrent += 1
			else:
				self.bckSpaceEnabled = True
				self.bckSpaceCountdown = False
		if self.bckSpaceEnabled:
			if self.bckSpaceCurrent < self.bckSpaceTime:
				self.bckSpaceCurrent += 1
			else:
				self.text = self.text[:-1]
				self.updateText()
				self.bckSpaceCurrent = 0
		# rendering textures
		if self.active:
			screen.blit(textAreaLeftActive, self.cornerLeftRect)
			screen.blit(self.bodyTextureActive, self.bodyRect)
			screen.blit(textAreaRightActive, self.cornerRightRect)
		else:
			screen.blit(textAreaLeft, self.cornerLeftRect)
			screen.blit(self.bodyTexture, self.bodyRect)
			screen.blit(textAreaRight, self.cornerRightRect)
		self.textSurface.fill((255,255,255,0))
		# rendering placeholder
		if len(self.text) == 0:
			renderFont(self.placeholderText, self.textRect, self.textSurface)
			pass
		# rendering text
		self.textSurface.blit(self.textRender, self.textRect)
		pygame.draw.rect(screen, (0, 0, 0), self.textCursor)
		screen.blit(self.textSurface, self.textSurfaceRect)
