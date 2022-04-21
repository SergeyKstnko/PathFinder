'''
Dijkstra class. It implements Dijkstra algorithm.

This class has:
    * function that returns if solution is found
    * function that moves solution one step forward
    * function that solves all the board immidiatelly (meaning it has the board)

    #pass the board at the time this class is initialized
    #then just call functions

'''

from square import Square


class Dijkstra:
    def __init__(self, board):
        
        self.board = board

        self.beg_node = Square.start_node
        self.end_node = Square.target_node
        self.beg_node.width = 0
        self.end_node.width = 0

        self.not_visited = []
        
        self.beg_node.shortest_dist = 0
        self.curr_node = self.beg_node




    def pick_shortest(self, not_visited):
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

    def add_to_notvisited(self, board, curr_node, not_visited):
        pass
    
    def is_shortest_path_colored(self):
        return self.curr_node is self.beg_node
    
    def color_path_one_step(self):
        """
        This functions goes back from the end_node and changes color for the
        shortest path to yellow
        This function will be recursive
        """
        #base case
        #if curr_node is beg_node:
        #    return
        #print("%d, %d" % curr_node.r, print(curr_node.c))
        self.curr_node.color = "yellow"
        #update_screen(board)
        self.curr_node = self.curr_node.prev_node
        #color_shortest_path(curr_node.prev_node, beg_node, board, game_window)

    def wrap(self, curr_node, beg_node, board, game_window):
        self.color_shortest_path(curr_node.prev_node, beg_node, board, game_window)

    def get_board(self):
        return self.board

    #if end node is solved then return 1
    def is_solved(self):
        return self.end_node.visited


    def make_one_step(self):
       
        r = self.curr_node.r
        c = self.curr_node.c
        board = self.board
        not_visited = self.not_visited
        #current shortest
        curr_node = self.curr_node
        
        #go over all its the neighbours
        #if unvisited -> place all neighbours in the unvisited list
            #if new shortest distance smaller than the current one then update it
            #update previous vertex for each neighbour

        #UPDATE for later me: r-1 < len(board) would it be always satisfied since we sabtract 1 from
        #already valid r???????
        if r-1 >= 0 and r-1 < len(board):
            if board[r-1][c] not in not_visited and board[r-1][c].visited == 0:
                not_visited.append(board[r-1][c])
                new = curr_node.shortest_dist + board[r-1][c].weight

                if new < board[r-1][c].shortest_dist or board[r-1][c].shortest_dist < 0:
                    board[r-1][c].shortest_dist = new
                    board[r-1][c].prev_node = curr_node

        if r+1 >=0 and r+1 < len(board):
            if board[r+1][c] not in not_visited and board[r+1][c].visited == 0:
                not_visited.append(board[r+1][c])

                new = curr_node.shortest_dist + board[r+1][c].weight
                if new < board[r+1][c].shortest_dist or board[r+1][c].shortest_dist < 0:
                    board[r+1][c].shortest_dist = new
                    board[r+1][c].prev_node = curr_node


        if c-1 >=0 and c-1 < len(board[0]):
            if board[r][c-1] not in not_visited and board[r][c-1].visited == 0:
                not_visited.append(board[r][c-1])

                new = curr_node.shortest_dist + board[r][c-1].weight
                if new < board[r][c-1].shortest_dist or board[r][c-1].shortest_dist < 0:
                    board[r][c-1].shortest_dist = new
                    board[r][c-1].prev_node = curr_node

        if c+1 >= 0 and c+1 < len(board[0]):
            if board[r][c+1] not in not_visited and board[r][c+1].visited == 0:
                not_visited.append(board[r][c+1])

                new = curr_node.shortest_dist + board[r][c+1].weight
                if new < board[r][c+1].shortest_dist or board[r][c+1].shortest_dist < 0:
                    board[r][c+1].shortest_dist = new
                    board[r][c+1].prev_node = curr_node

        
        #mark current node as visited
        curr_node.visited = 1
        if curr_node is not self.beg_node and curr_node is not self.end_node:
            curr_node.color = "blue"
            curr_node.width = 0
        #pick node from unvisited list with shortes distance
        if len(not_visited):
            curr_node = self.pick_shortest(not_visited)

        if self.is_solved():
            curr_node == self.end_node.prev_node

        self.curr_node.r = r
        self.curr_node.c = c
        self.board = board
        self.not_visited = not_visited
        self.curr_node = curr_node

        return self.board
