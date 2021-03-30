class Stack:

    class Node:

        def __init__(self,data):
            self.data = data
            self.pointer = None

    def __init__(self):
        self.start = None
    
    def push(self,data):
        new = Stack.Node(data)
        new.pointer = self.start 
        self.start = new
    
    def pop(self):
        if self.start != None:
            popped = self.start.data
            self.start = self.start.pointer
            return popped
        return None
    
    def peek(self):
        if self.start != None:
            return self.start.data
        return None
    
    ##get_vals is a bool indicating whether to return the contents as a list
    def empty(self,get_vals):
        if get_vals:
            contents = []
            while self.start != None:
                contents.append(self.pop())
            return contents
        else:
            self.start = None
            return None

def show():
    stack = Stack()
    items = list(range(0,21))
    for i in items:
        stack.push(i)
    print(stack.peek())
    print(stack.empty(True))
    
show()
