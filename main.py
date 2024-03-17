# -*- coding: utf-8 -*-
#importing libraries

import threading
import pygame
import screenmgr
from funcs import loadPathTexture
import confmgr
import path

pygame.font.init()

#init screen
screenmgr.init()
clock = pygame.time.Clock()

#loading main textures
logo = loadPathTexture(path.ui, "logo.png")
cursor = loadPathTexture(path.ui, "cursor.png", True, (32, 32))

#connecting to discord rpc
def startRPC():
	from pypresence import Presence
	client_id = "1129418228989436005"
	RPC = Presence(client_id)
	try:
		RPC.connect()
	except Exception as e:
		print(e)
		confmgr.enableRPC = False

if confmgr.enableRPC:
	rpcthread = threading.Thread(target=startRPC,daemon=True)
	rpcthread.start()

if __name__ == '__main__':
	from mainMenu import mainMenu
	mainMenu()