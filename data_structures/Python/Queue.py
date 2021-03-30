class Queue:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.pointer = None
    
    def __init__(self):
        self.front_pointer = None
        self.back_pointer = None
        self.size = 0

    def enqueue(self,data):
        ##Check for queue overflow
        try:
            new_node = Queue.Node(data)
            ##Check if queue is empty
            if self.back_pointer == None:
                self.front_pointer = new_node
            else:
                self.back_pointer.pointer = new_node

            self.back_pointer = new_node
            self.size += 1
            return True

        except:
            return False

    def dequeue(self):
        ##Check for queue underflow
        if self.front_pointer != None:
            popped = self.front_pointer.data
            self.front_pointer = self.front_pointer.pointer
            
            ##Check if last item was popped
            if self.front_pointer == None:
                self.back_pointer = None
            self.size -= 1
            return popped

        else:
            return None
        
    def peek(self):
        ##Check for queue underflow
        if self.front_pointer != None:
            return self.front_pointer.data
        else:
            return None
        
    def empty(self):
        self.front_pointer = self.back_pointer = None



def show():
    items = ["Florida","Georgia","Delaware","Alabama","California"]
    q = Queue()
    for i in items:
        q.enqueue(i)
        print(q.size)

    item = ''
    while item != None:
        print(item)
        item = q.dequeue()
        
    
##show()
