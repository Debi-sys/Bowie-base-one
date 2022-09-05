import pygame
import sys
import os
from pygame.locals import *
import screeninfo
import math
from PIL import Image

class Goomba(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = (pygame.image.load('Assets/Visuals/Sprites/theman.png'), Image.open('Assets/Visuals/Sprites/theman.png').size())
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screendata = screeninfo.get_monitors()
    screendata = screendata[0]
    dimensions = (screendata.width, screendata.height)
    gamewindow = pygame.display.set_mode(dimensions)

    # copy pasted code for reverse engineering:

    bg = pygame.image.load(os.path.join("./", "Assets/Visuals/Backgrounds/example_bg.jpg"))

    pygame.mouse.set_visible(0)

    pygame.display.set_caption('Space Age Game')


    # fix indentation

    pygame.display.flip()

    theman = Goomba((20, 30))

    while True:

        clock.tick(60)

        gamewindow.blit(bg, (100, 10))

        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()


        pygame.display.update()

main()