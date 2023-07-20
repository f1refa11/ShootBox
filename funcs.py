import orjson,os,pygame
from sys import exit as appExit
from paths import *
def openJSON(filename):
	return orjson.loads(open(filename, "r", encoding="utf-8").read())

def saveJSON(var, filename):
	open(filename, "w", encoding="utf-8").write(orjson.dumps(var))

def loadPathTexture(path, name, antialias=True, size=None):
	if size == None:
		return pygame.image.load(os.path.join(path, name)).convert_alpha()
	else:
		if antialias:
			return pygame.transform.smoothscale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()
		else:
			return pygame.transform.scale(pygame.image.load(os.path.join(path, name)), size).convert_alpha()

def gameExit():
	pygame.quit()
	appExit()