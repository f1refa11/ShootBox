import pygame
from text import newText
import screenmgr
class MenuList:
    def __init__(self, pos, list: dict[str, callable]):
        # PADDING: X - 15; Y - 9
        self.pos = pos # starting pos
        self.content = list
        
        self.width = 0 # max width without padding(8 on each sides)
        height = 0 # temp var
        textSurfs = [] # (Surface, height, callback)
        for itemKey in list.keys():
            itemText = newText(itemKey, wraplength=screenmgr.width//2)
            textSurfs.append((itemText, height, list[itemKey]))
            self.width = max(self.width, itemText.get_width())
            height += itemText.get_height()+18
        
        self.rect = pygame.Rect((0,0), (self.width+30, height))
        self.hover = False
        self.rectHover = False # if mouse in entire menulist
        self.surf = pygame.Surface((self.width+30,height), pygame.SRCALPHA)
        self.selSurf = pygame.Surface((self.width+30,height), pygame.SRCALPHA)
        self.selAlpha = 0
        self.selSurf.set_alpha(0)
        self.selRect = pygame.Rect(0,0,self.width+30,textSurfs[1][1])
        
        self.itemRects = [] # (Rect, callback)
        for textItem in textSurfs:
            self.surf.blit(textItem[0], (15, textItem[1]+9))
            self.itemRects.append((pygame.Rect(0, textItem[1], self.width+30, textItem[0].get_height()+18), textItem[2]))

        # animation vars
        self.endY = None
        self.yDown = None
    def eventHold(self, event):
        # TODO: combine eventHold and render functions???
        mx,my = pygame.mouse.get_pos()
        mx -= self.pos[0]
        my -= self.pos[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            # TODO: use pygame.Rect.collidedict
            for item in self.itemRects:
                if item[0].collidepoint(mx,my):
                    item[1]()
        elif event.type == pygame.MOUSEMOTION:
            self.hover = False
            if self.rect.collidepoint(mx,my):
                for item in self.itemRects:
                    if item[0].collidepoint(mx,my):
                        self.hover = True
                        self.selRect.height = item[0].height # TODO: made animation for height
                        if self.rectHover:
                            if self.yDown is None:
                                if item[0].y-self.selRect.y > 0:
                                    self.yDown = True
                                else:
                                    self.yDown = False
                            self.endY = item[0].y
                        else:
                            self.selRect.y = item[0].y
                self.rectHover = True
            else:
                self.rectHover = False
    def render(self, surf: pygame.Surface):
        self.selSurf.fill((0,0,0,0))
        self.selSurf.fill((255, 255, 255), self.selRect)
        # pygame.draw.rect(self.selSurf, (255, 255, 255), self.selRect)
        if self.hover:
            if self.selAlpha < 50:
                self.selAlpha += 6
            else:
                self.selAlpha = 50
        else:
            if self.selAlpha > 0:
                self.selAlpha -= 6
            else:
                self.selAlpha = 0
        
        if self.endY is not None:
            if self.yDown:
                if self.endY > self.selRect.y:
                    self.selRect.y += 10
                else:
                    self.selRect.y = self.endY
                    self.endY = None
                    self.yDown = None
            else:
                if self.endY < self.selRect.y:
                    self.selRect.y -= 10
                else:
                    self.selRect.y = self.endY
                    self.endY = None
                    self.yDown = None
            

        self.selSurf.set_alpha(self.selAlpha)
        surf.blit(self.selSurf, self.pos)
        surf.blit(self.surf, self.pos)