# TODO: make all pygame window managment here(size update function, fullscreen etc.)
import pygame
from confmgr import GPUAcceleration, isFullscreen, useVSync

width = 1024
height = 576

flags = pygame.RESIZABLE

def init():
    global screen
    screen = pygame.display.set_mode((width, height), flags)
    pygame.display.set_caption("ShootBox")
    # pygame.mouse.set_visible(False)

def sizeReload(new: tuple[int, int], checkFlags=True): 
    global width, height, screen, flags
    # flags generation
    if checkFlags:
        flags = pygame.RESIZABLE
        if isFullscreen: 
            flags |= pygame.FULLSCREEN
            if GPUAcceleration: flags |= pygame.HWSURFACE
    screen = pygame.display.set_mode(new, flags, vsync=int(useVSync))

def switchFullscreen():
    global screen
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
