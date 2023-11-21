import pygame, sys
from constants import *
from sudoku_generator import *
from board import Board


def main():

    playing = False
    board = None
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    end_screen = False
    end_text = ""

    while True:
    # Game Event Loop

        screen.fill(BG_COLOR)
        
        # Display title
        screen.blit(title_surf, title_rect)

        # Display difficulty buttons
        screen.blit(easy_surf, easy_rect)
        screen.blit(med_surf, med_rect)
        screen.blit(hard_surf, hard_rect)

        # Display group number
        screen.blit(group_surf, group_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Detect difficulty chosen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    playing = True
                    board = Board(9, 9, screen, 30)
                    board.draw()
                elif med_rect.collidepoint(event.pos):
                    playing = True
                    board = Board(9, 9, screen, 40)
                    board.draw()
                elif hard_rect.collidepoint(event.pos):
                    playing = True
                    board = Board(9, 9, screen, 50)
                    board.draw()

        pygame.display.update()

        # Playing Event Loop
        while playing:
            for event in pygame.event.get():
                # Quit functionality
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Selection functionality
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if board.reset_rect.collidepoint(event.pos):
                        board.reset_to_original()
                    elif board.restart_rect.collidepoint(event.pos):
                        board = None
                        playing = False
                    elif board.exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                    elif not event.pos[1] > WIDTH:
                        row, col = board.click(event.pos[0], event.pos[1])
                        board.select(row, col)
                if event.type == pygame.KEYDOWN:
                    if board.selected:
                        # Sketch functionality
                        if event.unicode in [str(i) for i in range(1, 10)]:
                            board.sketch(int(event.unicode))
                        # Submit answer functionality
                        elif event.key == pygame.K_RETURN and board.selected.value == 0:
                            board.place_number(board.selected.sketched_value)
                            board.selected.set_sketched_value(0)
                            board.draw()
                            screen.blit(board.reset_surf, board.reset_rect)
                            screen.blit(board.restart_surf, board.restart_rect)
                            screen.blit(board.exit_surf, board.exit_rect)
                            pygame.display.update()
                            pygame.time.delay(400)
                            if board.is_full():
                                if board.check_board():
                                    end_text = "Game Won!"
                                else:
                                    end_text = "Game Over"
                                end_screen = True
                                playing = False
                    # Selection arrow keys functionality
                    if event.key == pygame.K_UP and board.selected.row > 0:
                        board.select(board.selected.row - 1, board.selected.col)
                    elif event.key == pygame.K_DOWN and board.selected.row < 8:
                        board.select(board.selected.row + 1, board.selected.col)
                    elif event.key == pygame.K_LEFT and board.selected.col > 0:
                        board.select(board.selected.row, board.selected.col - 1)
                    elif event.key == pygame.K_RIGHT and board.selected.col < 8:
                        board.select(board.selected.row, board.selected.col + 1)
                    # Clear functionality
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                
                # If playing, draw the board and buttons
                if playing:
                    board.draw()
                    screen.blit(board.reset_surf, board.reset_rect)
                    screen.blit(board.restart_surf, board.restart_rect)
                    screen.blit(board.exit_surf, board.exit_rect)

            pygame.display.update()

        if end_screen:
            # END TEXT
            screen.fill(BG_COLOR)
            end_surf = title_font.render(end_text, False, BASE_COLOR)
            end_rect = end_surf.get_rect(
                center=(WIDTH // 2, HEIGHT // 3)
            )
            screen.blit(end_surf, end_rect)
            screen.blit(end_res_surf, end_res_rect)

            pygame.display.update()

            while end_screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # If player clicks restart button, return to main menu
                        if end_res_rect.collidepoint(event.pos):
                            end_screen = False
                            break


if __name__ == '__main__':
    # Initialization
    pygame.init()
    pygame.display.set_caption("Sudoku")

    # Define fonts
    title_font = pygame.font.Font(None, TITLE_FONT)
    text_font = pygame.font.Font(None, BASE_FONT)

    # TITLE
    title_surf = title_font.render("Sudoku", False, BASE_COLOR)
    title_rect = title_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 3)
    )

    # EASY
    easy_text = text_font.render("EASY", False, BUTTON_TEXT)
    easy_surf = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surf.fill(BUTTON_COLOR)
    easy_surf.blit(easy_text, (10, 10))
    easy_rect = easy_surf.get_rect(
        center=(WIDTH // 9 * 1.5, HEIGHT // 2)
    )

    # MEDIUM
    med_text = text_font.render("MEDIUM", False, BUTTON_TEXT)
    med_surf = pygame.Surface((med_text.get_size()[0] + 20, med_text.get_size()[1] + 20))
    med_surf.fill(BUTTON_COLOR)
    med_surf.blit(med_text, (10, 10))
    med_rect = med_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    # HARD
    hard_text = text_font.render("HARD", False, BUTTON_TEXT)
    hard_surf = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surf.fill(BUTTON_COLOR)
    hard_surf.blit(hard_text, (10, 10))
    hard_rect = hard_surf.get_rect(
        center=(WIDTH // 9 * 7.5, HEIGHT // 2)
    )

    # END RESTART
    end_res_text = text_font.render("RESTART", False, BUTTON_TEXT)
    end_res_surf = pygame.Surface((end_res_text.get_size()[0] + 20, end_res_text.get_size()[1] + 20))
    end_res_surf.fill(BUTTON_COLOR)
    end_res_surf.blit(end_res_text, (10, 10))
    end_res_rect = end_res_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2)
    )

    # GROUP NUMBER
    group_surf = text_font.render("Sudoku Project Group 149", False, BASE_COLOR)
    group_rect = group_surf.get_rect(
        center=(WIDTH // 2, HEIGHT - group_surf.get_size()[1])
    )

    main()