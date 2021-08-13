import sys
from pygame.constants import K_1, K_SPACE
import pygame
import backend as be

clock = pygame.time.Clock()

# Version we recommend you use
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((be.Square.WINDOW_WIDTH, be.Square.WINDOW_HEIGHT))
# Set title
pygame.display.set_caption("My Algorithm Visualizer")

game_running = True

#j is a column and k is a row
board = [[be.Square(j,k) for k in range(be.Square.c)] for j in range(be.Square.r)]


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
        if (be.Square.switch == 0 or be.Square.switch == 1) and event.type == pygame.MOUSEBUTTONDOWN:
            xpos = event.pos[0] // be.Square.p
            ypos = (event.pos[1] - be.Square.y_line) // be.Square.p
            #print("(%d,%d)" % (xpos,ypos))
            if be.Square.switch == 0:
                be.Square.start_node = board[ypos][xpos]
                be.Square.start_node.width = 0
                be.Square.switch = 1
                be.Square.prompt = "Choose destination"
            elif be.Square.switch == 1:
                be.Square.target_node = board[ypos][xpos]
                be.Square.target_node.width = 0
                be.Square.switch = 3 
                be.Square.prompt = "Press SPACE bar to start Dijkstra Algorithm"
        elif be.Square.switch == 3 and event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                be.dijkstra(board, be.Square.start_node, be.Square.target_node, game_window)
    
    pygame.draw.line(game_window, (0,0,0,0), (0,be.Square.y_line), (be.Square.WINDOW_WIDTH,be.Square.y_line), width=3)
    
    #(pos_left, pos_right, width, height)
    #sm_rect = pygame.Rect(50, 100, 10, 10)
    #pygame.draw.rect(game_window, "blue", sm_rect, 1)

    for y in range(0,be.Square.r):
        for x in range(0,be.Square.c):
            sm_rect = pygame.Rect(be.Square.p*x, be.Square.y_line+be.Square.p*y, be.Square.p, be.Square.p)
            pygame.draw.rect(game_window, board[y][x].color, sm_rect, board[y][x].width)
            if board[y][x].visited == 1:
                pygame.draw.rect(game_window, "black", sm_rect, width = 1)
    
    txt_surface = font.render(be.Square.prompt, True, pygame.Color('black'))
    game_window.blit(txt_surface, (25, 25)) 

    clock.tick(14)
    #pygame.display.update()
    pygame.display.flip()
    

pygame.quit()
sys.exit()
