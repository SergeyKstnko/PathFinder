'''
This code is the backened that implements Dijkstra Algorithm

'''

class Square:

    def __init__(self,r,c):
        #row and column coorodinates of a current square
        self.r = r
        self.c = c
        #0 for not visited, 1 for visited
        self.visited = 0
        #shortest distance from Start Node
        #if you start from this node then distance is 0, previous vertex is nothing
        #-1 is infinity
        self.shortest_dist = -1
        #Row and Column coordinates of a previous node
        self.prev_r = r
        self.prev_c = c
        #weight of this node
        self.weight = 1
    
    def get_coord(self):
        return (self.r,self.c)



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



def dijkstra(board, beg_node, end_node):
    """
    This function implements Dijkstra algorithm
    :args:      
    :return:    
    """
    not_visited = []
    #visited is implemented with 1 or 0 inside Square class
    beg_node.shortest_dist = 0
    curr_node = beg_node

    #add_to_notvisited(board,beg_node,not_visited)
    
    found = False
    #while haven't reached target node/(not all are visited)
    while not found:

        #print(curr_node.get_coord())


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
                    board[r-1][c].prev_r = curr_node.r
                    board[r-1][c].prev_c = curr_node.c
        if r+1 >=0 and r+1 < len(board):
            if board[r+1][c] not in not_visited and board[r+1][c].visited == 0:
                not_visited.append(board[r+1][c])

                new = curr_node.shortest_dist + board[r+1][c].weight
                if new < board[r+1][c].shortest_dist or board[r+1][c].shortest_dist < 0:
                    board[r+1][c].shortest_dist = new
                    board[r+1][c].prev_r = curr_node.r
                    board[r+1][c].prev_c = curr_node.c
        if c-1 >=0 and c-1 < len(board[0]):
            if board[r][c-1] not in not_visited and board[r][c-1].visited == 0:
                not_visited.append(board[r][c-1])

                new = curr_node.shortest_dist + board[r][c-1].weight
                if new < board[r][c-1].shortest_dist or board[r][c-1].shortest_dist < 0:
                    board[r][c-1].shortest_dist = new
                    board[r][c-1].prev_r = curr_node.r
                    board[r][c-1].prev_c = curr_node.c
        if c+1 >= 0 and c+1 < len(board[0]):
            if board[r][c+1] not in not_visited and board[r][c+1].visited == 0:
                not_visited.append(board[r][c+1])

                new = curr_node.shortest_dist + board[r][c+1].weight
                if new < board[r][c+1].shortest_dist or board[r][c+1].shortest_dist < 0:
                    board[r][c+1].shortest_dist = new
                    board[r][c+1].prev_r = curr_node.r
                    board[r][c+1].prev_c = curr_node.c
        
        #mark current node as visited
        curr_node.visited = 1
        #pick node from unvisited list with shortes distance
        if len(not_visited):
            curr_node = pick_shortest(not_visited)


        #If end node visited
        if end_node.visited == 1:
            #print("END %d", end_node.shortest_dist)
            found = True

        #found = True
    

n = 10

board = [[Square(r,c) for c in range(n)] for r in range(n)]

#What is the square to start?
#What is the square to end?
start_node = board[0][0]
target_node = board[99][99]


dijkstra(board,start_node, target_node)
print(target_node.shortest_dist)

'''
#testing pick shortest
#nodes around (2,20)
board[1][20].shortest_dist = 2
board[2][19].shortest_dist = 20
board[3][20].shortest_dist = 10
board[2][21].shortest_dist = 9
not_visited = [board[1][20],board[2][19],board[3][20],board[2][21]]
print(pick_shortest(not_visited).get_coord(), "\n")
for i in not_visited:
    print(i.get_coord())
'''



'''
#testing add_to_unvisited
#not_visited = []
curr = board[90][0]

add_to_unvisited(board, curr, not_visited)
for el in not_visited:
    print(el.get_coord())

'''