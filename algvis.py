import pygame
import sys

from pygame.constants import K_1
import backend as be

clock = pygame.time.Clock()
WINDOW_WIDTH = 990
WINDOW_HEIGHT = 755


# Version we recommend you use
pygame.init()
# If we want to check the result we can assign the return value
# to a variable and then print it
#init_result = pygame.init()
#print(init_result)

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set title
pygame.display.set_caption("My Algorithm Visualizer")

game_running = True

#y
r = 45
#x
c = 66
#With of a small square
p = 15


#j is a column and k is a row
board = [[be.Square(j,k) for k in range(c)] for j in range(r)]

#What is the square to start?
#What is the square to end?
start_node = board[25][25]
target_node = board[10][20]


while game_running:
    #Game content
    #Color of window background
    game_window.fill((255,255,255))
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_1:
                be.dijkstra(board, start_node, target_node, game_window)

    #height where line begins
    y_line = 75
    pygame.draw.line(game_window, (0,0,0,0), (0,y_line), (WINDOW_WIDTH,y_line), width=3)
    
    #(pos_left, pos_right, width, height)
    #sm_rect = pygame.Rect(50, 100, 10, 10)
    #pygame.draw.rect(game_window, "blue", sm_rect, 1)

    for y in range(0,r):
        for x in range(0,c):
            sm_rect = pygame.Rect(p*x, y_line+p*y, p, p)
            pygame.draw.rect(game_window, board[y][x].color, sm_rect, board[y][x].width)
            if board[y][x].visited == 1:
                pygame.draw.rect(game_window, "black", sm_rect, width = 1)

    clock.tick(14)
    #pygame.display.update()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
