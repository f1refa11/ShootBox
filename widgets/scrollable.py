# TODO: basically a surface with scrolling features; you specify the position, the view size, the surface, and it's ready!
import pygame
class Scrollable:
    def __init__(self, pos: tuple[int, int], surface: pygame.Surface, height, scrollLeft = True):
        self.sourceSurf = surface
        self.viewSurface = pygame.Surface((surface.get_width(),height), pygame.SRCALPHA)
        self.scrollHeight = 0
        self.scrollVelocity = 0 # for future smooth scroll

        # scrollbar
        self.bodyRect = pygame.Rect(pos[0], pos[1], 8, height)
        self.thumbRect = pygame.FRect(pos[0], pos[1], 8, height**2//self.sourceSurf.get_height())

        self.pos = pos
        self.rect = pygame.Rect(self.pos, (self.viewSurface.get_width(), self.viewSurface.get_height()))
        self.grabbed = False
    def eventHold(self, event):
        rx,ry = pygame.mouse.get_rel()
        mx,my = pygame.mouse.get_pos()
        if self.sourceSurf.get_height() <= self.viewSurface.get_height():
            return
        # mouse scroll
        if event.type == pygame.MOUSEBUTTONDOWN and event.button in [4,5] and self.rect.collidepoint((mx,my)):
            if event.button == 4:
                if self.scrollHeight+25 <= 0:
                    self.scrollHeight += 25
                else:
                    self.scrollHeight = 0
            elif event.button == 5:
                if self.scrollHeight-self.viewSurface.get_height()-25 >= -self.sourceSurf.get_height():
                    self.scrollHeight -= 25
                else:
                    self.scrollHeight = -self.sourceSurf.get_height()+self.viewSurface.get_height()
            self.thumbRect.y = abs(self.scrollHeight)/self.sourceSurf.get_height()*self.bodyRect.h+self.pos[1]

        # thumb
        elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            # when dragging the thumb
            if self.thumbRect.collidepoint((mx,my)):
                self.thumbRect.y += ry
            elif self.bodyRect.collidepoint((mx,my)):
                self.thumbRect.y = my-(self.thumbRect.h//2)
            elif self.grabbed:
                self.thumbRect.y += ry
            self.scrollHeight = -(self.sourceSurf.get_height()/self.viewSurface.get_height()*(self.thumbRect.y-self.pos[1]))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bodyRect.collidepoint((mx,my)) and not self.thumbRect.collidepoint((mx,my)):
            # when we click outside thumb rect but inside scrollbar
            self.thumbRect.y = my-(self.thumbRect.h//2)
            self.scrollHeight = -(self.sourceSurf.get_height()/self.viewSurface.get_height()*(self.thumbRect.y-self.pos[1]))
        elif event.type == pygame.MOUSEBUTTONUP:
            self.grabbed = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.bodyRect.collidepoint((mx,my)):
            self.grabbed = True

        if self.thumbRect.y < self.bodyRect.y:
            self.thumbRect.y = self.bodyRect.y
            self.scrollHeight = -(self.sourceSurf.get_height()/self.viewSurface.get_height()*(self.thumbRect.y-self.pos[1]))
        elif self.thumbRect.bottom > self.bodyRect.bottom:
            self.thumbRect.bottom = self.bodyRect.bottom
            self.scrollHeight = -(self.sourceSurf.get_height()/self.viewSurface.get_height()*(self.thumbRect.y-self.pos[1]))
    def updateScrollbar(self):
        # this will be called when we add something in the source surf
        pass
    def render(self, surf: pygame.Surface):
        self.viewSurface.fill((0,0,0,0))
        self.viewSurface.blit(self.sourceSurf, (0, self.scrollHeight))
        surf.blit(self.viewSurface, (self.pos[0]+8, self.pos[1]))

        if not self.sourceSurf.get_height() <= self.viewSurface.get_height():
            pygame.draw.rect(surf, (255, 255, 255), self.bodyRect)
            pygame.draw.rect(surf, (0, 255, 0), self.thumbRect)