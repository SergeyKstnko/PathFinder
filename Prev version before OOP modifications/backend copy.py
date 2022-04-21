'''
This code is the backened that implements Dijkstra and BFS Algorithms

'''

import pygame
from pygame.display import update
from queue import Queue
from collections import deque
import cProfile
import pstats
clock = pygame.time.Clock()


class Square:
    #BOARD CONSTANTS
    WINDOW_WIDTH = 990
    WINDOW_HEIGHT = 760
    #How many columns will the board have
    c = 66
    #How many rows will the board have
    r = 45
    #Width of a small square
    p = 15
    #height where horizontal line begins. The one that separates upper white
    #space and the board
    y_line = 75

    #BOARD VARIABLES
    prompt = "Choose starting point"
    start_node = None
    target_node = None
    #what does this switch do?
    switch = 0

    def __init__(self,r,c):
        #row and column coorodinates of a current square
        self.r = r
        self.c = c
        #If node was Visited or Queued. 0 for not visited/queued, 1 for visited/queued
        self.visited = 0
        #shortest distance from Start Node
        #if you start from this node then distance is 0, previous vertex is nothing
        #-1 is infinity
        self.shortest_dist = -1
        #Row and Column coordinates of a previous node
        self.prev_node = None
        self.prev_r = -1
        self.prev_c = -1
        #weight of this node
        self.weight = 1

        ##GUI attributes
        self.color = "black"
        #???
        self.width = 1
    


def pick_shortest(not_visited):
    """
    Function picks unvisited node with shortest distance
    :args:      
    "return:    node from the list with the shortest path to the start node
    """
    #print(not_visited[0].get_coord())
    shortest = not_visited[0]
    ind = 0
    for i in range(1,len(not_visited)):
        if not_visited[i].shortest_dist < shortest.shortest_dist and not_visited[i].shortest_dist >= 0:
            ind = i

    #remove and return shortest from not_visited
    return not_visited.pop(ind)


def add_to_notvisited(board, curr_node, not_visited):
    """
    This function adds new neighbours to not_visited list
    :args:
    :return:
    """
    r = curr_node.r
    c = curr_node.c
    
    if r-1 >= 0 and r-1 < len(board):
        if board[r-1][c] not in not_visited:
            not_visited.append(board[r-1][c])
    if r+1 >=0 and r+1 < len(board):
        if board[r+1][c] not in not_visited:
            not_visited.append(board[r+1][c])
    if c-1 >=0 and c-1 < len(board[0]):
        if board[r][c-1] not in not_visited:
            not_visited.append(board[r][c-1]) 
    if c+1 >= 0 and c+1 < len(board[0]):
        if board[r][c+1] not in not_visited:
            not_visited.append(board[r][c+1])


def update_screen(board, game_window):
    
    #Game content
    #Color of window background
    game_window.fill((255,255,255))

    pygame.draw.line(game_window, (0,0,0,0), (0,Square.y_line), (Square.WINDOW_WIDTH,Square.y_line), width=3)

    for y in range(0,Square.r):
        for x in range(0,Square.c):
            #(pos_left, pos_right, width, height)
            sm_rect = pygame.Rect(Square.p*x, Square.y_line+Square.p*y, Square.p, Square.p)
            pygame.draw.rect(game_window, board[y][x].color, sm_rect, board[y][x].width)
            if board[y][x].visited == 1:
                pygame.draw.rect(game_window, "black", sm_rect, width = 1)

    #clock.tick(300)
    #pygame.display.update()
    pygame.display.flip()

def color_shortest_path(curr_node, beg_node,board, game_window):
    """
    This functions goes back from the end_node and changes color for the
    shortest path to yellow
    This function will be recursive
    """
    #base case
    if curr_node is beg_node:
        return
    #print("%d, %d" % curr_node.r, print(curr_node.c))
    curr_node.color = "yellow"
    update_screen(board, game_window)
    color_shortest_path(curr_node.prev_node, beg_node, board, game_window)


def wrap(curr_node, beg_node, board, game_window):
    color_shortest_path(curr_node.prev_node, beg_node, board, game_window)


def dijkstra(board, beg_node, end_node, game_window):
    print("Djakstra")
    profile = cProfile.Profile()
    profile.enable()

    """
    This function implements Dijkstra algorithm
    :args:      
    :return:    
    """
    beg_node.width = 0
    end_node.width = 0

    not_visited = []
    #visited is implemented with 1 or 0 inside Square class
    beg_node.shortest_dist = 0
    curr_node = beg_node
    
    found = False
    #while haven't reached target node/(not all are visited)
    while not found:

        #go over all its the neighbours
        r = curr_node.r
        c = curr_node.c
        #if unvisited -> place all neighbours in the unvisited list
            #if new shortest distance smaller than the current one then update it
            #update previous vertex for each neighbour
        if r-1 >= 0 and r-1 < len(board):
            if board[r-1][c] not in not_visited and board[r-1][c].visited == 0:
                not_visited.append(board[r-1][c])

                new = curr_node.shortest_dist + board[r-1][c].weight
                if new < board[r-1][c].shortest_dist or board[r-1][c].shortest_dist < 0:
                    board[r-1][c].shortest_dist = new
                    board[r-1][c].prev_node = curr_node
                    #board[r-1][c].prev_r = curr_node.r
                    #board[r-1][c].prev_c = curr_node.c
        if r+1 >=0 and r+1 < len(board):
            if board[r+1][c] not in not_visited and board[r+1][c].visited == 0:
                not_visited.append(board[r+1][c])

                new = curr_node.shortest_dist + board[r+1][c].weight
                if new < board[r+1][c].shortest_dist or board[r+1][c].shortest_dist < 0:
                    board[r+1][c].shortest_dist = new
                    board[r+1][c].prev_node = curr_node
                    #board[r+1][c].prev_r = curr_node.r
                    #board[r+1][c].prev_c = curr_node.c
        if c-1 >=0 and c-1 < len(board[0]):
            if board[r][c-1] not in not_visited and board[r][c-1].visited == 0:
                not_visited.append(board[r][c-1])

                new = curr_node.shortest_dist + board[r][c-1].weight
                if new < board[r][c-1].shortest_dist or board[r][c-1].shortest_dist < 0:
                    board[r][c-1].shortest_dist = new
                    board[r][c-1].prev_node = curr_node
                    #board[r][c-1].prev_r = curr_node.r
                    #board[r][c-1].prev_c = curr_node.c
        if c+1 >= 0 and c+1 < len(board[0]):
            if board[r][c+1] not in not_visited and board[r][c+1].visited == 0:
                not_visited.append(board[r][c+1])

                new = curr_node.shortest_dist + board[r][c+1].weight
                if new < board[r][c+1].shortest_dist or board[r][c+1].shortest_dist < 0:
                    board[r][c+1].shortest_dist = new
                    board[r][c+1].prev_node = curr_node
                    #board[r][c+1].prev_r = curr_node.r
                    #board[r][c+1].prev_c = curr_node.c
        
        #mark current node as visited
        curr_node.visited = 1
        if curr_node is not beg_node and curr_node is not end_node:
            curr_node.color = "blue"
            curr_node.width = 0
        #pick node from unvisited list with shortes distance
        if len(not_visited):
            curr_node = pick_shortest(not_visited)


        #If end node visited
        if end_node.visited == 1:
            #print("END %d", end_node.shortest_dist)
            found = True

        #found = True

        update_screen(board, game_window)
    wrap(end_node, beg_node, board, game_window)

    profile.disable()
    ps = pstats.Stats(profile)
    #ps.sort_stats('calls','percall')
    ps.print_stats()






#BFS IMPLEMENTATION STARTS HERE

#import pdb

from myQueue import myQueue

def enqueue(board, curr_node, q):
    """
    This function adds new neighbours to the queue
    :args:
    :return:
    """
    r = curr_node.r
    c = curr_node.c
    
    if r-1 >= 0 and r-1 < len(board):
        if not board[r-1][c].visited:
            q.put(board[r-1][c])
            #q.append(board[r-1][c])
            board[r-1][c].prev_r = curr_node.r
            board[r-1][c].prev_c = curr_node.c
            board[r-1][c].prev_node = curr_node
            #board[r-1][c].visited = 1
    if r+1 >=0 and r+1 < len(board):
        if not board[r+1][c].visited:
            q.put(board[r+1][c])
            #q.append(board[r+1][c])
            board[r+1][c].prev_r = curr_node.r
            board[r+1][c].prev_c = curr_node.c
            board[r+1][c].prev_node = curr_node
            #board[r+1][c].visited = 1
    if c-1 >=0 and c-1 < len(board[0]):
        if not board[r][c-1].visited:
            q.put(board[r][c-1]) 
            #q.append(board[r][c-1])
            board[r][c-1].prev_r = curr_node.r
            board[r][c-1].prev_c = curr_node.c
            board[r][c-1].prev_node = curr_node
            #board[r][c-1].visisted = 1
    if c+1 >= 0 and c+1 < len(board[0]):
        if not board[r][c+1].visited:
            q.put(board[r][c+1])
            #q.append(board[r][c+1])
            board[r][c+1].prev_r = curr_node.r
            board[r][c+1].prev_c = curr_node.c
            board[r][c+1].prev_node = curr_node
            #board[r][c+1].visisted = 1
    return q



def bfs(board, beg_node, end_node, game_window):
    print("BFS")
    profile = cProfile.Profile()
    profile.enable()


    #initialize Queue
    #q = Queue()
    q = myQueue()
    #mark root as visited
    beg_node.visited = 1
    #enqueue neighbours
    q = enqueue(board, beg_node, q)
    
    found = False
    
    #while queue is not empty and target node was not found
    while (not q.empty()) and (not found):
        #node = dequeue
        curr_node = q.get()
        #visit node
        q = enqueue(board, curr_node, q)
        curr_node.visited = 1
        if curr_node is not beg_node and curr_node is not end_node:
            curr_node.color = "blue"
            curr_node.width = 0
        prev_node = curr_node

        if end_node.visited == 1:
            print("Here YO")
            found = True        

        update_screen(board, game_window)

    #if found:
    print("Found")
    wrap(end_node, beg_node, board, game_window)
    
    profile.disable()
    ps = pstats.Stats(profile)
    #ps.sort_stats('calls','percall')
    ps.print_stats()
