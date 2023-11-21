from constants import *
import pygame


class Cell:

  def __init__(self, value, row, col, screen):  # initialize cell
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen

    self.sketched_value = 0  # prepare sketched value

  def set_cell_value(self, value): #sets the cells value
    self.value = value

  def set_sketched_value(self, value): #sets the users sketched value
    self.sketched_value = value

  def draw(self): #draws the number in the cell
    font = pygame.font.Font(None, BASE_FONT)

    if 0 <= self.value < 10:  # generate the cell value if number is correct
      num_surf = font.render(str(self.value), 0, BASE_COLOR)
      num_rect = num_surf.get_rect(
        center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2,
                SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
      self.screen.blit(num_surf, num_rect)
      if self.value == 0:  # empty cell slot if 0
        self.screen.fill(BG_COLOR, num_rect)

    if 0 <= self.sketched_value < 10:  # generate sketched value if number is correct
      sketch_surf = font.render(str(self.sketched_value), 0, SKETCH_COLOR)
      sketch_rect = sketch_surf.get_rect(
        center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 4,
                SQUARE_SIZE * self.row + SQUARE_SIZE // 4))
      self.screen.blit(sketch_surf, sketch_rect)
      if self.sketched_value == 0:  # empty sketch slot if 0
        self.screen.fill(BG_COLOR, sketch_rect)
