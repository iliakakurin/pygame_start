import pygame as pg
from random import choice

#class Player():
#    size = 30
 #   speed_y = 0
  #  speed = 0
   # phase = 0
    #def __init__(self,x_pos,y_pos):
#   self.x = x_pos
#  self.y = y_pos

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, surf):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            bottomleft=(x,y))
        self.size = 30
        self.speed_y = 0
        self.phase = 0

    def update(self, g, FPS, H):
        if self.phase > 0:
            self.phase -= 1
            self.speed_y += g / FPS
            self.rect.y += 30 * self.speed_y / FPS
        if self.phase == 0:
            self.speed_y = 0
            self.rect.y = H // 2 - 91

class Cactus(pg.sprite.Sprite):

    score = 0

    def __init__(self, x, y, surf_list):
        pg.sprite.Sprite.__init__(self)
        self.image = surf_list[0]
        #self.image = choice(surf_list)
        self.rect = self.image.get_rect(
            bottomleft=(x, y))
        self.mask = pg.mask.from_surface(self.image)
        self.mask.invert()

        #self.mask.to_surface(self.image)

        self.size_x = 20
        self.size_y = 20
        self.speed_x = -4

    def update(self, g, FPS, H):
        if self.rect.x > 0:
            self.rect.x += self.speed_x
        else:
            self.kill()
            Cactus.score += 1






#class Cactus():
#    size_x = 20
#    size_y = 20
#    speed_x = -2
#    def __init__(self, x_pos, y_pos, width, height):
#        self.x = x_pos
#        self.y = y_pos
#        self.w = width
#        self.h = height
