class Linked_List:
 
    class Node:
        def __init__(self,dat):
            self.data = dat
            self.pointer = None
    
    def __init__(self):
        self.start_pointer = None
    
    def add_node(self,dat):
        ##Check for overflow
        try:
            new_node = Linked_List.Node(dat)
            current_node = self.start_pointer
            ##Check if list is empty
            if current_node == None:
                self.start_pointer = new_node
            ##New node should be placed before first node, becomes first node
            elif new_node.data < current_node.data:
                new_node.pointer = current_node
                self.start_pointer = new_node
            ##New node should be placed somewhere in the list
            else:
                while current_node != None and new_node.data > current_node.data:
                    previous = current_node
                    current_node = current_node.pointer
                new_node.pointer = previous.pointer
                previous.pointer = new_node
                    
            return True
        except:
            return False

    def delete_node(self,val):
        ##Check if linked list is empty
        if self.start_pointer == None:
            return False
        ##Removing first item from list
        elif self.start_pointer.data == val:
            self.start_pointer = self.start_pointer.pointer
        else:
            current_node = self.start_pointer
            while current_node.data != val:
                previous = current_node
                current_node = current_node.pointer
                if current_node == None:
                    return False
            previous.pointer = current_node.pointer
            return True

    
    def traverse(self):
        current_node = self.start_pointer
        ##Check if list is empty:
        if current_node == None:
            return False
        else:
            output = []
            while current_node != None:
                output.append(current_node.data) 
                current_node = current_node.pointer
            return output
        
    def reverse(self):
        current_node = self.start_pointer
        next_node = current_node.pointer
        while next_node != None:
            next_next_node = next_node.pointer

            ##Specific case for first node
            if current_node == self.start_pointer:
                current_node.pointer = None
            
            next_node.pointer = current_node

            current_node = next_node
            next_node = next_next_node

        self.start_pointer = current_node

def show():
    items = [5,3,7,1,6,3]
    ll = Linked_List()
    for i in items:
        ll.add_node(i)
    ll.delete_node(9)
    output = ll.traverse()
    print("Traverse:", output)
    ll.reverse()
    output2 = ll.traverse()
    print("Reverse:", output2)

show()
