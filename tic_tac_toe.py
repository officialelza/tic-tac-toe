import pygame

pygame.init()
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TIC-TAC-TOE')

#Variable definitions
run = True
player = 1
clicked = False
winner = 1
pos = []
board = []
game_over = False
p = 0 

#Colours & font
Screen_colour = (173,231,237)
red = (94,20,20)
yellow = (227, 225, 68)
green_Font = (15, 56, 8)
white_font = (160, 209, 152)
font = pygame.font.Font('sauce.otf',15)

# play again rectangle
again_rect = pygame.Rect(60,245,170,30)

def draw_grid():
    line_colour = (15,45,85)
    for i in range(1,3):
        pygame.draw.line(screen, line_colour, (0, i * 100), (SCREEN_WIDTH,i * 100), width=10)
        pygame.draw.line(screen, line_colour, (i * 100, 0), (i * 100, SCREEN_HEIGHT), width=10)

# creation of list
for i in range(3):
    row = [0] * 3
    board.append(row)


def draw_XO():
    x_pos = 0
    for i in board:
        y_pos = 0
        for j in i:
            if j == 1:
                pygame.draw.line(screen, yellow, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), 10)
                pygame.draw.line(screen, yellow, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), 10)
            if j == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50),40,10)
            y_pos +=1
        x_pos +=1

def checks_winner():
    global winner, game_over
    # Check rows
    for row in board:
        if sum(row) == 3:
            winner = 1
            game_over = True
        elif sum(row) == -3:
            winner = 2
            game_over = True

    # Check columns
    for col in range(3):
        col_sum = board[0][col] + board[1][col] + board[2][col]
        if col_sum == 3:
            winner = 1
            game_over = True
        elif col_sum == -3:
            winner = 2
            game_over = True

    # Check diagonals
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        winner = 1
        game_over = True
    elif board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        winner = 2
        game_over = True


   
def draw_winner(winner):
    # Winner Text Display
    text = "Player " + str(winner) + " WINS!"
    y = font.render(text, True , white_font)
    imp = pygame.image.load(r"cat.gif")
    new_size = (300,300)
    resized_image = pygame.transform.scale(imp, new_size)
    center = screen.get_rect()

    # Image Display
    screen.blit(resized_image, resized_image.get_rect(center = screen.get_rect().center))
    pygame.draw.rect(screen, green_Font, (60,190,165,40))
    screen.blit(y, (80,193))

    # Play Again Display
    again_text = "Play Again?"
    again = font.render(again_text, True , white_font)
    pygame.draw.rect(screen, green_Font, again_rect)
    screen.blit(again, (97,243))
    
def reset_game():
    global board, player, game_over, clicked, winner
    board = [[0] * 3 for _ in range(3)]
    player = 1
    winner = 0
    game_over = False
    clicked = False

def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

def main():
    global run, player, game_over, clicked, winner, pos, board, p
    while run:
        screen.fill(Screen_colour)
        draw_grid() 
        draw_XO()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if game_over == 0:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    pos_x = pos[0]
                    pos_y = pos[1]
                    row = pos_x //100
                    col = pos_y //100
                    print(row, col)
                    if board[row][col] == 0:
                        board[row][col] = player
                        player*= -1
                    
                        checks_winner()
                        p = is_board_full()

        if game_over == 1:
            draw_winner(winner)
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    reset_game()

        if p == 1:
                print("Filled Board")

                    
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()