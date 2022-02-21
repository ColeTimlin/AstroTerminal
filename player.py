import pygame
#from main import *
SPEED = 450

class Player:
  pos = (0,0)
  size = (10,60)
  


  #Extendable Functions
  def player_hit_ball(self):
    pass



  def __init__(self, screen, color, xStart):
    self.screen = screen
    self.color = color
    self.pos = (xStart, screen.get_height() / 2)

  def move(self, direction, dT):
    if(direction == "up" and self.pos[1] > 0):
      self.pos = (self.pos[0], self.pos[1] - (SPEED * dT))
    elif direction == "down" and self.pos[1] + self.size[1] < self.screen.get_height():
      self.pos = (self.pos[0], self.pos[1] + SPEED * dT)

  def draw(self):
    pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos, self.size))