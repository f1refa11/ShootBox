import pygame
from funcs import loadPathTexture
from paths import *
playerIdle = loadPathTexture(playerPath, "idle.png", True, (64, 64))
class Player:
	def __init__(self, pos) -> None:
		self.x, self.y = pos
		self.speed = 3
		self.rect = pygame.Rect(self.x, self.y, 64, 64)
	def collisionCheck():
		# if self.rect
		pass
	def up(self):
		# if not self.rect.top < 3:
		self.y -= self.speed
	def down(self):
		pass
	def left(self):
		# if not self.rect.left < 3:
		self.x -= self.speed
	def right(self):
		pass
	def render(self, surface: pygame.Surface):
		#updating changed(possibly) variables
		self.rect = pygame.Rect(self.x, self.y, 64, 64)

		#rendering to screen
		surface.blit(playerIdle, (self.x, self.y))
		pygame.draw.rect(surface, (255, 0, 0), self.rect, 1)