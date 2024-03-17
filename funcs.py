import orjson
import os
import pygame
from sys import exit as appExit
def openJSON(filename):
	return orjson.loads(open(filename, "r", encoding="utf-8").read())

def saveJSON(var, filename):
	with open(filename, "w", encoding="utf-8") as a:
		a.write(orjson.dumps(var))

def loadPathTexture(path, name, antialias=True, size=None) -> pygame.Surface:
	if size is None:
		return pygame.image.load(os.path.join(path, name)).convert_alpha()
	else:
		if antialias:
			return pygame.transform.smoothscale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()
		else:
			return pygame.transform.scale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()

def quit():
	pygame.quit()
	appExit()