# Notifications Module
from funcs import loadPathTexture
from fontmgr import cacheFont, renderFont, fonts
from paths import uiTexturesPath
import pygame
from pygame import MOUSEBUTTONDOWN
from screenmgr import screen
notifyUnread = False
notifyIconSelected = False
panelOpened = True
notifications = {
    "unread": [],
    "read": [],
    "new": []
}
panelSurface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
scrollSurf = pygame.Surface((320, screen.get_height()-80), pygame.SRCALPHA)
panelItemsSurf = newItemsSurf = pygame.Surface((320,0), pygame.SRCALPHA)
panelItemsRect = newItemsSurf.get_rect()
scrollRect = scrollSurf.get_rect(y=72,x=screen.get_width()-328)

close = loadPathTexture(uiTexturesPath, "close.png")
closeOpacity = 100
close.set_alpha(closeOpacity)
closeRect = pygame.Rect(screen.get_width()-44, 12, 32, 32)

scrollGradient = loadPathTexture(uiTexturesPath, "notifyGradient.png", size=(320, 16))

# icon
notifyIcon = loadPathTexture(uiTexturesPath, "notifyIcon.png") # default
notifyIconS = loadPathTexture(uiTexturesPath, "notifyIconS.png") # selected
notifyIconU = loadPathTexture(uiTexturesPath, "notifyIconU.png") # unread
notifyIconUS = loadPathTexture(uiTexturesPath, "notifyIconUS.png") # selected-unread
notifyIconRect = pygame.Rect(screen.get_width()-44, 12, 32, 32)

# notification
notify = [
    ["TL", "T", "TR"],
    ["L" , "C", "R"],
    ["BL", "B", "BR"]
]
notify = [[loadPathTexture(uiTexturesPath, "notify%s.png"%i2).convert_alpha() for i2 in i1] for i1 in notify]

class Notification:
    def __init__(self, title: str, desc, items=[], width=288, placement="new"):
        global panelOpened
        self.placement = placement
        # appear animation depending on config
        from confmgr import uiAnimations
        self.opacity = 0 if uiAnimations else 255

        self.width = width

        # text render
        self.title = cacheFont(title, size=14, wraplength=self.width, bold=True)
        self.desc = fonts[13].render(desc, True, (255, 255, 255), wraplength=self.width)
        self.itemsHeight = 0
        for item in items: self.itemsHeight += cacheFont(item[0], (127, 124, 196), 13).get_height()+8
        self.itemsSurf = pygame.Surface((self.width, self.itemsHeight), pygame.SRCALPHA)
        self.itemsHeight = 0
        # self.itemsRects = []
        fonts[13].underline = True
        for item in items:
            tmpSurf = cacheFont(item[0], (142, 138, 227), 13, wraplength=self.width)
            renderFont(tmpSurf, (0,self.itemsHeight), self.itemsSurf)
            # self.itemsRects.append((pygame.Rect()))
            self.itemsHeight += tmpSurf.get_height()+4
        fonts[13].underline = False
        self.height = self.title.get_height()+8+self.desc.get_height()+self.itemsHeight
        self.rect = pygame.Rect(0, 0, self.width+16, self.height+16)
        tmpHeight = 0
        if placement == "new":
            for item in notifications[placement]:
                tmpHeight += item.height+36
            self.rect.topright = (screen.get_width()-24, 56+tmpHeight)
        elif placement == "unread" and panelOpened:
            for item in notifications[placement]:
                tmpHeight += item.height+36
            self.rect.topright = (304, tmpHeight)
        elif placement == "read":
            for item in notifications[placement]:
                tmpHeight += item.height
            self.rect.topright = (screen.get_width()-24, 56)
        elif type(placement) == tuple:
            self.rect.topright = placement
        self.bgSurf = pygame.Surface((self.width+32, self.height+32), pygame.SRCALPHA)
        notify[0][1] = pygame.transform.scale(notify[0][1], (self.width, 16))
        notify[2][1] = pygame.transform.scale(notify[2][1], (self.width, 16))
        notify[1][2] = pygame.transform.scale(notify[1][2], (16, self.height))
        notify[1][0] = pygame.transform.scale(notify[1][0], (16, self.height))
        notify[1][1] = pygame.transform.scale(notify[1][1], (self.width, self.height))
        for y in range(len(notify)):
            for x in range(len(notify[y])):
                x2 = (self.width+16 if x == 2 else x*16)
                y2 = (self.height+16 if y == 2 else y*16)
                self.bgSurf.blit(notify[y][x], (x2,y2))
    def render(self, surf: pygame.Surface = screen):
        surf.blit(self.bgSurf, (self.rect.x, self.rect.y))
        renderFont(self.title, (self.rect.x+16, self.rect.y+16), surf)
        renderFont(self.desc, (self.rect.x+16, self.rect.y+self.title.get_height()+24), surf)
        surf.blit(self.itemsSurf, (self.rect.x+16, self.rect.y+self.height-self.itemsHeight+24))
        # pygame.draw.rect(surf, (255, 0, 0), (self.rect.x, self.rect.y, self.rect.w+16, self.rect.h+16), 1)
    def eventHold(self, event):
        if event.type == MOUSEBUTTONDOWN:
            pass
# functions

def renderMain(place: pygame.Surface = screen):
    # icon
    if notifyIconRect.collidepoint(pygame.mouse.get_pos()):
        notifyIconSelected = True
    else:
        notifyIconSelected = False
    if notifyUnread:
        if notifyIconSelected:
            place.blit(notifyIconUS, notifyIconRect)
        else:
            place.blit(notifyIconU, notifyIconRect)
    else:
        if notifyIconSelected:
            place.blit(notifyIconS, notifyIconRect)
        else:
            place.blit(notifyIcon, notifyIconRect)
    # new notifications
    for notify in notifications["new"]:
        notify.render()
    # panel render
    if panelOpened:
        renderPanel(place)

def renderPanel(place: pygame.Surface):
    global closeOpacity,scrollRect
    panelSurface.fill((0,0,0,100))
    scrollSurf.fill((0,0,0,0))
    panelSurface.fill((28, 21, 53), (screen.get_width()-336, 0, 336, screen.get_height()))
    renderFont(cacheFont("Notifications", size=18, wraplength=336, align=pygame.FONT_CENTER), (screen.get_width()-336, 0), panelSurface)
    for notify in notifications["unread"]:
        notify.render(panelItemsSurf)

    scrollSurf.blit(panelItemsSurf, panelItemsRect)
    panelSurface.blit(scrollSurf, scrollRect)
    pygame.draw.rect(scrollSurf, (255, 255, 0), panelItemsRect, 4)
    # pygame.draw.rect(panelSurface, (255, 0, 0), scrollRect, 1)
    pygame.draw.rect(panelSurface, (155, 155, 155), (screen.get_width()-6, 72, 4, (screen.get_height()-80)*((screen.get_height()-80)/panelItemsRect.h)), border_radius=1000)
    place.blit(panelSurface, (0, 0))

    place.blit(close, closeRect)
    if closeRect.collidepoint(pygame.mouse.get_pos()):
        if closeOpacity < 255:
            closeOpacity += 8
    else:
        if closeOpacity > 100:
            closeOpacity -= 8
    close.set_alpha(closeOpacity)

def eventHold(event):
    global panelOpened
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            if closeRect.collidepoint(pygame.mouse.get_pos()) and panelOpened:
                panelOpened = False
            elif notifyIconRect.collidepoint(pygame.mouse.get_pos()) and not panelOpened:
                panelOpened = True
        # print(panelItemsRect.h)
        if panelItemsRect.h > screen.get_height()-80:
            if event.button == 5:
                panelItemsRect.y -= 25
                tmp = scrollRect.h-panelItemsRect.h
                panelItemsRect.y = tmp if not tmp < panelItemsRect.y else panelItemsRect.y
            if event.button == 4:
                panelItemsRect.y += 25
                panelItemsRect.y = 0 if panelItemsRect.y > 0 else panelItemsRect.y

def newNotify(title, desc, items: list = []):
    global scrollRect,panelItemsSurf
    if panelOpened:
        tmpnotify = Notification(title, desc, items, placement="unread")
        panelItemsRect.h += tmpnotify.rect.h+20
        panelItemsSurf = pygame.Surface((320,panelItemsRect.h), pygame.SRCALPHA)
        notifications["unread"].append(tmpnotify)
    else:
        tmpnotify = Notification(title, desc, items)
        notifications["new"].append(tmpnotify)
    