import pygame
from funcs import loadPathTexture
from path import playerPath
import math
from confmgr import showDirectionArrow
import screenmgr
playerIdle = loadPathTexture(playerPath, "idle.png", True, (64, 64))
if showDirectionArrow != 0: playerDirection = loadPathTexture(playerPath, "direction.png", True, (64,64)).convert_alpha()
class Player:
	def __init__(self, pos) -> None:
		# TODO: remove this unneccessary stupid self.x self.y and use this fucking pygame.Rect
		self.x, self.y = pos
		self.speed = 3
		self.rect = pygame.Rect(self.x+8, self.y+8, 48, 48)

		self.rendX, self.rendY = screenmgr.width//2-32, screenmgr.height//2-32

		self.arrowCount = 0
		self.arrowOpacity = 255

		self.inventory = []
		self.health = 100
	def collisionCheck():
		pass
	def up(self):
		self.y -= self.speed
	def down(self):
		pass
	def left(self):
		self.x -= self.speed
	def right(self):
		pass
	def render(self, surface: pygame.Surface):
		self.rect.x, self.rect.y = self.x+8, self.y+8
		mx,my = pygame.mouse.get_pos()
		dx,dy = mx-self.rendX-32, my-self.rendY-32
		angle = -math.degrees(math.atan2(dy,dx))-90
		tempTexture = pygame.transform.rotozoom(playerIdle, angle, 1).convert_alpha()
		if showDirectionArrow != 0: tempTextureDirection = pygame.transform.rotozoom(playerDirection, angle, 1).convert_alpha()
		if showDirectionArrow == 1:
			tempTextureDirection.set_alpha(self.arrowOpacity)
			if self.arrowCount < 9:
				if self.arrowCount % 2 == 0:
					if self.arrowOpacity > 0:
						self.arrowOpacity -= 10
					else:
						self.arrowOpacity = 0
						self.arrowCount += 1
				else:
					if self.arrowOpacity < 255:
						self.arrowOpacity += 10
					else:
						self.arrowOpacity = 255
						self.arrowCount += 1
		self.renderRect = tempTexture.get_rect(centerx=self.rendX+32,centery=self.rendY+32)

		#rendering to screen
		surface.blit(tempTexture, self.renderRect)
		if showDirectionArrow != 0: surface.blit(tempTextureDirection, self.renderRect)