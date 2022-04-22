'''
Breadth-First Search Class. It implements BFS algorithm.

Interface of this class:
    * initialize the class
    * make one step
    * 

'''

from Archive.backend import enqueue
from square import Square
from queue import Queue
from collections import deque
from myQueue import myQueue


class BFS:

    def enqueue(self): #, board, curr_node, q):
        """
        This function adds new neighbours to the queue
        :args:
        :return:
        """
        r = self.curr_node.r
        c = self.curr_node.c
        q = self.q
        board = self.board
        curr_node = self.curr_node
        
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
        
        self.curr_node.r = r
        self.curr_node.c = c
        self.q = q
        self.board = board

        return self.q


    def __init__(self, board):
        
        self.board = board
        self.beg_node = Square.start_node
        self.end_node = Square.target_node
        self.beg_node.width = 0
        self.end_node.width = 0
        self.curr_node = self.beg_node
        #mark root as visited
        self.beg_node.visited = 1

        #initialize Queue
        #q = Queue()
        self.q = myQueue()
        #enqueue neighbours
        self.q = self.enqueue()

        
    def is_solved(self):
        return self.end_node.visited == 1

    def make_one_step(self):
        
        #node = dequeue
        self.curr_node = self.q.get()
        #visit node
        self.q = self.enqueue()

        self.curr_node.visited = 1
        if self.curr_node is not self.beg_node and self.curr_node is not self.end_node:
            self.curr_node.color = "blue"
            self.curr_node.width = 0
        self.prev_node = self.curr_node     