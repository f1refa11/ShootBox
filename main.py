# -*- coding: utf-8 -*-
#importing libraries
import os
import threading

#removing Pygame welcome notice
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

#importing pygame and its extensions
import pygame
from pygame.locals import *

#importing functions
from funcs import loadPathTexture

# initializing pygame
pygame.font.init()

#init screen
import screenmgr
screenmgr.init()
clock = pygame.time.Clock()

#configuring essential paths
from paths import uiTexturesPath

#loading main textures
logo = loadPathTexture(uiTexturesPath, "logo.png")
cursor = loadPathTexture(uiTexturesPath, "cursor.png", True, (64, 64))

#connecting to discord rpc
from confmgr import enableRPC
import confmgr
def startRPC():
	from pypresence import Presence, DiscordNotFound
	client_id = "1129418228989436005"
	RPC = Presence(client_id)
	try:
		RPC.connect()
		rpcState = None
	except:
		confmgr.enableRPC = False
if enableRPC:
	rpcthread = threading.Thread(target=startRPC,daemon=False)
	rpcthread.start()
#stopping loading screen after setting things up
loadingScreen = False

if __name__ == '__main__':
	from mainMenu import mainMenu
	mainMenu()