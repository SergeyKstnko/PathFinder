#import pdb
import sys
from pygame.constants import K_1, K_SPACE
import pygame
import backend as be
from square import Square
from dijkstra import Dijkstra



clock = pygame.time.Clock()

# Version we recommend you use
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((Square.WINDOW_WIDTH, Square.WINDOW_HEIGHT))
# Set title
pygame.display.set_caption("My Algorithm Visualizer")

game_running = True

#j is a column and k is a row
board = [[Square(j,k) for k in range(Square.c)] for j in range(Square.r)]

board[10][10].weight = 10
board[11][10].weight = 10
board[12][10].weight = 10
board[13][10].weight = 10
board[14][10].weight = 10
board[15][10].weight = 10
board[16][10].weight = 10



def update_screen():    
 
    for y in range(0,Square.r):
        for x in range(0,Square.c):
            #(pos_left, pos_right, width, height)
            sm_rect = pygame.Rect(Square.p*x, Square.y_line+Square.p*y, Square.p, Square.p)
            pygame.draw.rect(game_window, board[y][x].color, sm_rect, board[y][x].width)
            if board[y][x].visited == 1:
                pygame.draw.rect(game_window, "black", sm_rect, width = 1)

    pygame.display.flip()


while game_running:
    #Game content
    #Color of window background
    game_window.fill((255,255,255))
    font = pygame.font.Font(None, 32)
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False
        
        if Square.switch in [0,1] and event.type == pygame.MOUSEBUTTONDOWN:
            xpos = event.pos[0] // Square.p
            ypos = (event.pos[1] - Square.y_line) // Square.p

            if Square.switch == 0:
                Square.start_node = board[ypos][xpos]
                Square.start_node.width = 0
                Square.switch = 1
                Square.prompt = "Choose destination"
            elif Square.switch == 1:
                Square.target_node = board[ypos][xpos]
                Square.target_node.width = 0
                Square.switch = 3 
                Square.prompt = "Press SPACE bar to start Dijkstra Algorithm"
        elif Square.switch == 3 and event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:

                alg = Dijkstra(board)
                #while solution is not found
                while not alg.is_solved():
                    #move one step further
                    alg.make_one_step()
                    update_screen()
                    clock.tick(40)
                
                while not alg.is_shortest_path_colored():
                    alg.color_path_one_step()
                    update_screen()
                    clock.tick(40)
    

    pygame.draw.line(game_window, (0,0,0,0), (0,Square.y_line), (Square.WINDOW_WIDTH,Square.y_line), width=3)


    for y in range(0,Square.r):
        for x in range(0,Square.c):
            #(pos_left, pos_right, width, height)
            sm_rect = pygame.Rect(Square.p*x, Square.y_line+Square.p*y, Square.p, Square.p)
            pygame.draw.rect(game_window, board[y][x].color, sm_rect, board[y][x].width)
            if board[y][x].visited == 1:
                pygame.draw.rect(game_window, "black", sm_rect, width = 1)
    
    txt_surface = font.render(Square.prompt, True, pygame.Color('black'))
    game_window.blit(txt_surface, (25, 25)) 

    pygame.display.flip()
    

pygame.quit()
sys.exit()
