from sudoku_generator import *
import pygame
from constants import *
from cell import Cell


class Board:

    def __init__(self, width, height, screen, difficulty): # initialize board
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
      
        self.selected = None # set up selected cell
        self.sudoku = SudokuGenerator(9, difficulty) # generate sudoku board
        self.sudoku.board = generate_sudoku(9, difficulty) # populate sudoku board
        self.board = [
            [Cell(self.sudoku.get_board()[j][i], j, i, self.screen) for i in range(height)]
            for j in range(width)
        ] # transform sudoku board into cell objects

        # Buttons
        button_font = pygame.font.Font(None, BASE_FONT)

        # RESET
        reset_text = button_font.render("RESET", False, BUTTON_TEXT)
        self.reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        self.reset_surf.fill(BUTTON_COLOR)
        self.reset_surf.blit(reset_text, (10, 10))
        self.reset_rect = None

        # RESTART
        restart_text = button_font.render("RESTART", False, BUTTON_TEXT)
        self.restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        self.restart_surf.fill(BUTTON_COLOR)
        self.restart_surf.blit(restart_text, (10, 10))
        self.restart_rect = None

        # EXIT
        exit_text = button_font.render("EXIT", False, BUTTON_TEXT)
        self.exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        self.exit_surf.fill(BUTTON_COLOR)
        self.exit_surf.blit(exit_text, (10, 10))
        self.exit_rect = None

    def draw(self):

        self.screen.fill(BG_COLOR)

        # Box Lines
        for i in range(3, 10, 3):
            pygame.draw.line(self.screen, BASE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), BOX_LINE)
            pygame.draw.line(self.screen, BASE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, WIDTH), BOX_LINE)

        # Grid Lines
        for i in range(0,9):
            pygame.draw.line(self.screen, BASE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), GRID_LINE)
            pygame.draw.line(self.screen, BASE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, WIDTH), GRID_LINE)

        # Cells
        for i in self.board:
            for j in i:
                j.draw()

        # Selection
        if self.selected and 0 <= self.selected.row < 9 and 0 <= self.selected.col < 9:
            y_corner = self.selected.row * SQUARE_SIZE
            x_corner = self.selected.col * SQUARE_SIZE
            pygame.draw.line(
                self.screen, SELECT_COLOR, (x_corner, y_corner),
                (x_corner + SQUARE_SIZE, y_corner), GRID_LINE
            )
            pygame.draw.line(
                self.screen, SELECT_COLOR, (x_corner, y_corner),
                (x_corner, y_corner + SQUARE_SIZE), GRID_LINE
            )
            pygame.draw.line(
                self.screen, SELECT_COLOR, (x_corner, y_corner + SQUARE_SIZE),
                (x_corner + SQUARE_SIZE, y_corner + SQUARE_SIZE), GRID_LINE
            )
            pygame.draw.line(
                self.screen, SELECT_COLOR, (x_corner + SQUARE_SIZE, y_corner),
                (x_corner + SQUARE_SIZE, y_corner + SQUARE_SIZE), GRID_LINE
            )

        self.reset_rect = self.reset_surf.get_rect(
            center=(WIDTH // 9 * 1.5, WIDTH + (HEIGHT - WIDTH) // 2)
        )

        self.restart_rect = self.restart_surf.get_rect(
            center=(WIDTH // 9 * 4.5, WIDTH + (HEIGHT - WIDTH) // 2)
        )

        self.exit_rect = self.exit_surf.get_rect(
            center=(WIDTH // 9 * 7.5, WIDTH + (HEIGHT - WIDTH) // 2)
        )

    def select(self, row, col): # sets the selected value to the cell object at the provided board coordinates
        self.selected = self.board[row][col]

    def click(self, x, y): # convert screen coordinates to grid coordinates
        if x < WIDTH and y < WIDTH:
            return y // SQUARE_SIZE, x // SQUARE_SIZE

    def clear(self):
        self.selected.set_sketched_value(0) # clears sketched value
        self.selected.set_cell_value(self.sudoku.get_board()[self.selected.row][self.selected.col]) # selected cell reset to original

    def sketch(self, value): # place the value in the sketch slot
        if self.selected.value == 0:
          self.selected.set_sketched_value(value)

    def place_number(self, value): # place the value in the number slot
        self.selected.set_cell_value(value)

    def reset_to_original(self): # reset the board to the original
        self.board = [
            [Cell(self.sudoku.get_board()[j][i], j, i, self.screen) for i in range(self.height)]
            for j in range(self.width)
        ]

    def is_full(self): # checks if the board is full
        for i in self.board:
            for j in i:
                if j.value == 0:
                    return False
        return True

    def update_board(self): # changes sudoku board into current board
        self.sudoku.board = [[i.value for i in j] for j in self.board]

    def find_empty(self): # finds the first empty slot
        for i, j in enumerate(self.board):
            for k, l in enumerate(j):
                if l.value == 0:
                    return i, k
        return None

    def check_board(self): # checks if the board is valid
        self.update_board()
        for row_index, row in enumerate(self.sudoku.get_board()):
            for col_index, col in enumerate(row):
                temp = col
                row[col_index] = 0
                if not self.sudoku.is_valid(row_index, col_index, temp):
                    return False
                row[col_index] = int(temp)
        return True
      