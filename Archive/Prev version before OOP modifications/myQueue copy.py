class myQueue:
    'This class implements Queue in Python3'   

    class Node:
        def __init__(self, node=None):
            self.node = node
            self.next = None
        
        def change_next(self, node):
            self.next = node
        
        def get_content(self):
            return self.node
    

    def __init__(self):
        self.length = 0 
        self.beg = None
        self.end = None


    def put(self, node):
        self.next_node = self.Node(node)
        if self.length == 0:
            self.beg = self.next_node
            self.end = self.beg
            self.length += 1
        elif self.length > 0:
            self.end.change_next(self.next_node)
            self.end = self.next_node
            self.length += 1
        else:
            print("ERROR in Queue. Length is somehow less than 0.")

    def get(self):
        if self.length == 0:
            print("Queue is empty and there is nothing to pop.")
        elif self.length > 0:
            return_content = self.beg.get_content()
            self.beg = self.beg.next
            self.length -= 1
            if self.length == 0:
                self.end = None
            return return_content
        else:
            print("ERROR in Queue. Length is somehow less than 0.")

    def empty(self):
        return not self.length

