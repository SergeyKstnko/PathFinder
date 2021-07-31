import pygame
import sys
#import backend as be

WINDOW_WIDTH = 990
WINDOW_HEIGHT = 900
#dimensions of the board
n_x = 66
n_y = 10


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


while game_running:
    #Game content
    print("Hello")
    #Color of window background
    game_window.fill((255,255,255))
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    #height where line begins
    y_line = 75
    pygame.draw.line(game_window, (0,0,0,0), (0,y_line), (WINDOW_WIDTH,y_line), width=3)
    
    #(pos_left, pos_right, width, height)
    #sm_rect = pygame.Rect(50, 100, 10, 10)
    #pygame.draw.rect(game_window, "blue", sm_rect, 1)

    p = 15
    for y in range(0,45):
        for x in range(0,n_x-1):
            sm_rect = pygame.Rect(p*x,y_line+p*y, p, p)
            pygame.draw.rect(game_window, "blue", sm_rect, width=1)
    
    #sm_rect = pygame.Rect(p*1,p*1, p, p)
    #pygame.draw.rect(game_window, "blue", sm_rect, width=1)

    pygame.display.update()

pygame.quit()
sys.exit()
