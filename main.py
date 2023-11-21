import pygame, sys
from constants import *
from board import Board


def main():
    playing = False
    board = None
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    end_screen = False
    while True: #game loop
        screen.fill(BG_COLOR) #Creating start screen
        screen.blit(easy_surface, easy_rectangle)
        screen.blit(medium_surface, medium_rectangle)
        screen.blit(hard_surface, hard_rectangle)
        screen.blit(title_surface, title_rectangle)
        screen.blit(subtitle_surface, subtitle_rectangle)
        for event in pygame.event.get(): #checking for actions, proceeds to main game once a button is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    board = Board(9, 9, screen, 30)
                    Board.draw(board)
                    playing = True
                elif medium_rectangle.collidepoint(event.pos):
                    board = Board(9, 9, screen, 40)
                    Board.draw(board)
                    playing = True
                elif hard_rectangle.collidepoint(event.pos):
                    board = Board(9, 9, screen, 50)
                    Board.draw(board)
                    playing = True
        pygame.display.update()
        while playing: #main board loop
            screen.blit(reset_surface, reset_rectangle) #generates the menu options
            screen.blit(restart_surface, restart_rectangle)
            screen.blit(exit_surface, exit_rectangle)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # checks for interactions with the board, or buttons
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    location = Board.click(board, x, y)
                    try: #Attempts to get the location of the mouse click, convert it to a location, and select the cell at that location. If location is out of bounds, one of the buttons were clicked instead
                        Board.select(board, location[0], location[1])
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        selectrow, selectcol = location[0], location[1]
                    except:
                        if exit_rectangle.collidepoint(event.pos): # check exit button
                            pygame.quit()
                            sys.exit()
                        elif restart_rectangle.collidepoint(event.pos): # check restart button
                            board = None
                            playing = False
                        elif reset_rectangle.collidepoint(event.pos): # check reset button
                            board.reset_to_original()
                            board.draw()
                            screen.blit(reset_surface, reset_rectangle)
                            screen.blit(restart_surface, restart_rectangle)
                            screen.blit(exit_surface, exit_rectangle)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: # fills the selected square based on what button was pressed
                        Board.sketch(board, 1)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_2: # button 2
                        Board.sketch(board, 2)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_3: # button 3
                        Board.sketch(board, 3)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_4: # button 4
                        Board.sketch(board, 4)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_5:
                        Board.sketch(board, 5) # button 5
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_6: # button 6
                        Board.sketch(board, 6)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_7: # button 7
                        Board.sketch(board, 7)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_8: # button 8
                        Board.sketch(board, 8)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_9: # button 9
                        Board.sketch(board, 9)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                    elif event.key == pygame.K_BACKSPACE: # clears the selected cell
                        Board.clear(board)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        # selects a different square based on the posititon of the current square
                        # modulus is used to allow the user to select a square on the opposite
                        #side of the board using arrow keys
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        Board.select(board, (selectrow + 1) % 9, selectcol % 9) # moves selection down one cell
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        selectrow = selectrow + 1
                    elif event.key == pygame.K_w or event.key == pygame.K_UP: # moves selection up one cell
                        Board.select(board, (selectrow + 8) % 9, selectcol % 9)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        selectrow = selectrow + 8
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT: # moves selection left one cell
                        Board.select(board, selectrow % 9, (selectcol + 8) % 9)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        selectcol = selectcol + 8
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: # moves selection right one cell
                        Board.select(board, selectrow % 9, (selectcol + 1) % 9)
                        Board.draw(board)
                        screen.blit(reset_surface, reset_rectangle)
                        screen.blit(restart_surface, restart_rectangle)
                        screen.blit(exit_surface, exit_rectangle)
                        selectcol = selectcol + 1
                    elif event.key == pygame.K_KP_ENTER or event.key == 13: # fills in the cell number, clears the selected number
                        if 0 < int(board.selected.sketched_value) < 10:
                            value = board.selected.sketched_value
                            Board.clear(board)
                            Board.place_number(board, value)
                            board.draw()
                            screen.blit(reset_surface, reset_rectangle)
                            screen.blit(restart_surface, restart_rectangle)
                            screen.blit(exit_surface, exit_rectangle)
                            pygame.display.update()
                            if Board.is_full(board): # checks if the board is full
                                end_screen = True
                                playing = False
            pygame.display.update()
        while end_screen: #game over screen
            if board.check_board(): # if won, display text
                screen.fill(BG_COLOR)
                screen.blit(game_won_surface, game_won_rect)
                screen.blit(restart_surface, restart_rectangle)
            else: # if lost, display text
                screen.fill(BG_COLOR)
                screen.blit(game_over_surface, game_over_rect)
                screen.blit(restart_surface, restart_rectangle)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # check restart button
                    if restart_rectangle.collidepoint(event.pos):
                        board = None
                        end_screen = False
                        playing = False
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sudoku")
    selectrow, selectcol = 0, 0
    #Initializing the text used for the menus
    title_font = pygame.font.Font(None, TITLE_FONT)
    text_font = pygame.font.Font(None, BASE_FONT)
    title_surface = title_font.render("Sudoku", 0, BASE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2,
                                                     HEIGHT // 3))
    subtitle_surface = text_font.render("Select Game Mode: ", 0, BASE_COLOR)
    subtitle_rectangle = subtitle_surface.get_rect(center=(WIDTH // 2,
                                                           HEIGHT // 2 - BASE_FONT))
    easy_text = text_font.render("EASY", 0, BUTTON_TEXT)
    medium_text = text_font.render("MEDIUM", 0, BUTTON_TEXT)
    hard_text = text_font.render("HARD", 0, BUTTON_TEXT)

    # initialize buttons
    easy_surface = pygame.Surface(
      (easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface(
      (medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface(
      (hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # difficulty buttons location
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2 - 117, HEIGHT // 2))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2 + 120, HEIGHT // 2))
    reset_text = text_font.render("RESET", 0, BUTTON_TEXT)

    # reset button
    reset_surface = pygame.Surface(
      (reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 145,
                                                     HEIGHT // 2 + 315))
    # restart button
    restart_text = text_font.render("RESTART", 0, BUTTON_TEXT)

    restart_surface = pygame.Surface(
      (restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2,
                                                         HEIGHT // 2 + 315))
    # exit button
    exit_text = text_font.render("EXIT", 0, BUTTON_TEXT)

    exit_surface = pygame.Surface(
      (exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 130,
                                                   HEIGHT // 2 + 315))
    #Game end text
    game_won_surface = title_font.render("Game Won!", 0, BUTTON_TEXT)
    game_won_rect = game_won_surface.get_rect(center=(WIDTH // 2,
                                                      HEIGHT // 2 - 200))
    game_over_surface = title_font.render("Game Over :(", 0, BUTTON_TEXT)
    game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2,
                                                        HEIGHT // 2 - 200))
    main()
