import math, random


class SudokuGenerator:

  def __init__(self, row_length, removed_cells):  # initialize sudoku board
    self.row_length = row_length
    self.removed_cells = removed_cells
    self.board = [[0 for _ in range(self.row_length)]
                  for _ in range(self.row_length)]
    self.box_length = int(math.sqrt(row_length))

  def get_board(self):
    return self.board  #returns board

  def print_board(self):
    for row in self.board:
      print(row)  #prints each row in board

  def valid_in_row(self, row, num):
    for i in self.board[
        row]:  #checks each number in a row and compares it to desired number
      if num == i:
        return False
    return True

  def valid_in_col(self, col, num):
    for i in range(
        self.row_length
    ):  #checks each number in a collumn and compares it to desired number
      if num == self.board[i][col]:
        return False
    return True

  def valid_in_box(
    self, row_start, col_start, num
  ):  #checks each value in a 3x3 box and compares it to the desired number
    while row_start % 3 != 0:
      row_start -= 1
    while col_start % 3 != 0:
      col_start -= 1
    for i in range(row_start, row_start + 3):
      for j in range(col_start, col_start + 3):
        if num == self.board[i][j]:
          return False
    return True

  def is_valid(
    self, row, col, num
  ):  #goes through the row, col, and box checking if the desired number is able to be placed
    if self.valid_in_row(row, num) is True:
      if self.valid_in_col(col, num) is True:
        if self.valid_in_box(row, col, num) is True:
          return True
    return False

  def fill_box(self, row_start,
               col_start):  #fills a 3x3 box with randomly generated numbers
    for i in range(row_start, row_start + 3):
      for j in range(col_start, col_start + 3):
        while True:
          number = random.randint(1, 9)
          if self.is_valid(row_start, col_start, number) is True:
            self.board[i][j] = number
            break
          else:
            continue

  def fill_diagonal(
      self):  #fills the boxes on the diagonal line of the main square
    self.fill_box(0, 0)
    self.fill_box(3, 3)
    self.fill_box(6, 6)

  def fill_remaining(self, row, col):  #fills remaining box squares
    if (col >= self.row_length and row < self.row_length - 1):
      row += 1
      col = 0
    if row >= self.row_length and col >= self.row_length:
      return True
    if row < self.box_length:
      if col < self.box_length:
        col = self.box_length
    elif row < self.row_length - self.box_length:
      if col == int(row // self.box_length * self.box_length):
        col += self.box_length
    else:
      if col == self.row_length - self.box_length:
        row += 1
        col = 0
        if row >= self.row_length:
          return True

    for num in range(1, self.row_length + 1):
      if self.is_valid(row, col, num):
        self.board[row][col] = num
        if self.fill_remaining(row, col + 1):
          return True
        self.board[row][col] = 0
    return False

  def fill_values(self):
    self.fill_diagonal()
    self.fill_remaining(0, self.box_length)

  def remove_cells(self):
    for num in range(
        self.removed_cells
    ):  #randomly chooses the correct amount of squares to remove, changes depending on difficulty
      while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if self.board[row][col] != 0:
          self.board[row][col] = 0
          break
        else:
          continue


def generate_sudoku(size, removed):  #creates the sudoku puzzle
  sudoku = SudokuGenerator(size, removed)
  sudoku.fill_values()
  board = sudoku.get_board()
  sudoku.remove_cells()
  board = sudoku.get_board()
  return board
