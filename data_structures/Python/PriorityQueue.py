class PriorityQueue:

    class Node:
        def __init__(self, data, priority):
            self.data = data
            self.priority = priority
            self.pointer = None

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def enqueue(self, data, priority):
        ##Check for queue overflow
        try:
            new_node = PriorityQueue.Node(data, priority)
            if self.back == None:
                self.front = new_node
                self.back = new_node
            elif new_node.priority < self.front.priority:
                new_node.pointer = self.front
                self.front = new_node
            else:
                curr = self.front
                nextn = self.front.pointer
                while nextn and nextn.priority <= new_node.priority:
                    curr = nextn
                    nextn = curr.pointer

                curr.pointer = new_node
                new_node.pointer = nextn
                ##print(curr.data, new_node.data, nextn.data)
                if nextn == None:
                    self.back = new_node
            self.size += 1
            return True
        except:
            return False

    def dequeue(self):
        ##Check for queue underflow
        if self.front != None:
            popped = self.front.data
            self.front = self.front.pointer

            if self.front == None:
                self.back = None
            self.size -= 1
            return popped
        else:
            return None


def show():
    items = [("Florida", 3), ("Georgia", 2), ("Delaware", 1), ("Alabama", 3), ("California", 2), ("New York", 1)]
    q = PriorityQueue()
    for i in items:
        q.enqueue(i[0],i[1])

    item = ''
    while item != None:
        print(item)
        item = q.dequeue()

show()