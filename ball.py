import pygame
import random
import numpy 
from pygame.display import mode_ok

MAX_SPEED = (1000,500)
MIN_SPEED = (50,5)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))


class Ball:
    velocity = (0,0)
    size = 10
    color = (255, 255, 255)

    def __init__(self, screen):
        self.screen = screen
        self.pos = (screen.get_width()/2,screen.get_width()/2)
        rDir = -1 if random.randint(1,2) == 1 else 1
        self.velocity = (random.randint(50, 200) * rDir,random.randint(-120,120))

    def update(self, dT):
        
        
        
        self.pos = (self.pos[0] + (self.velocity[0] * dT),
                    self.pos[1] + (self.velocity[1] * dT))
        #if(self.pos[0] < 1): 
        #    self.flip_x(random.randint(-100, 100))
        #    self.pos = (self.pos[0] + 5, self.pos[1])
        #elif self.pos[0] + self.size > self.screen.get_width():
        #    self.flip_x(random.randint(-100, 100))
        #    self.pos = (self.pos[0] - 5, self.pos[1])

        if(self.pos[1] < 1):
            self.flip_y(random.randint(-10, 10))
            self.pos = (self.pos[0], self.pos[1] + 5)
        elif self.pos[1] + self.size > self.screen.get_height():
            self.flip_y(random.randint(-10, 10))
            self.pos = (self.pos[0], self.pos[1] - 5)

    def flip_x(self, change = 0):
        x,y = self.velocity
        newDir = -numpy.sign(x)      
        newX = abs(x) + change
        newX = clamp(abs(newX), MIN_SPEED[0], MAX_SPEED[0])

        self.velocity = (newX * newDir, self.velocity[1])


    def flip_y(self, change = 0):
        x,y = self.velocity
        newDir = -numpy.sign(y)
        newY = abs(y) + change
        newY = clamp(abs(newY), MIN_SPEED[1], MAX_SPEED[1])
        self.velocity = (self.velocity[0], newY * newDir)


    def collision_check(self, rect_pos, extents):
        le1 = self.pos[0]
        re1 = self.pos[0] + self.size
        le2 = rect_pos[0]
        re2 = rect_pos[0] + extents[0]
        te1 = self.pos[1]
        be1 = self.pos[1] + self.size
        te2 = rect_pos[1]
        be2 = rect_pos[1] + extents[1]
        if re1 >= le2 and le1 <= re2 and te1 <= be2 and be1 >= te2: return True
        return False
    def draw(self):
        pygame.draw.rect(self.screen, self.color ,pygame.Rect(self.pos, (self.size, self.size)))
