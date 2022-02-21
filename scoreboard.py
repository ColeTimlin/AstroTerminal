from turtle import right
import pygame

class Scoreboard:
  left_player_score = 0
  right_player_score = 0
  WINNING_SCORE = 5
  
  def __init__(self, screen, p_won_func): 
    self.screen = screen
    self.main_p_won = p_won_func
    self.font = pygame.font.SysFont('chalkduster.ttf', 24)

  def write_score(self):
    img = self.font.render("P1: " + str(self.left_player_score) + " vs P2: " + str(self.right_player_score), True, (255,255,255))
    self.screen.blit(img, (self.screen.get_width()/2 - 50, self.screen.get_height() * .1))
  
  def player_won(self, leftPlayer = True):
    self.main_p_won(leftPlayer)

  def playerScored(self, leftPlayer = True):
    if(leftPlayer == False):
      self.left_player_score += 1
      print(f"New score is P1:{self.left_player_score} P2: {self.right_player_score}")
    else:
      self.right_player_score += 1
      print(f"New score is P1:{self.left_player_score} P2: {self.right_player_score}")
    self.write_score()

    if(self.left_player_score == 3):
      self.leftPlayer = True
      self.player_won(leftPlayer)
      pygame.display.quit()
      pygame.quit()
      pygame.init = False
    elif(self.right_player_score == 3):
      self.leftPlayer = False
      self.player_won(leftPlayer)
      pygame.display.quit()
      pygame.quit()
      pygame.init = False