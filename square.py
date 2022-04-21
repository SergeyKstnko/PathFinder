'''
This module represents a square and attributes of the board

'''

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
    # Switch to determine what is the next user's step while picking beginning
    #and end node or choosing an algorithm to run
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
    
