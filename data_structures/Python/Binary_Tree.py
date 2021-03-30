from Queue import Queue

class Binary_Tree:
    ##Inner class for each node, all values defined in add method
    class Node:
        def __init__(self,dat):
            self.data = dat
            self.left = None
            self.right = None
            self.bin_id = '' ##0 is a branch left, 1 is a branch right
    
    def __init__(self):
        self.root = None

    def add_node(self,data):
        
        new_node = Binary_Tree.Node(data)
        current_node = self.root

        ##Binary tree is empty
        if current_node == None:
            self.root = new_node

        else:
            while current_node != None:
                
                previous = current_node
                if current_node.data > new_node.data:
                    current_node = current_node.left
                    new_node.bin_id += '0'

                elif current_node.data < new_node.data:
                    current_node = current_node.right
                    new_node.bin_id += '1'

            if new_node.data < previous.data:
                previous.left = new_node
            elif new_node.data > previous.data:
                previous.right = new_node
                

    def delete_node(self,data):
        current_node = self.root
        while current_node != None and current_node.data != data:
            previous = current_node
            if data < current_node.data:
                current_node = current_node.left
            
            elif data > current_node.data:
                current_node = current_node.right
        ##Node to delete does not exist
        if current_node == None:
            return False
        
        ##Node exists and has no children
        if current_node.left == None and current_node.right == None:
            ##Case for deleting root
            if current_node == self.root:
                self.root = None
            elif previous.data > current_node.data:
                previous.left = None
            else:
                previous.right = None
        
        ##Node exists and has one child - left
        elif current_node.right == None:
            ##Case for deleting root
            if current_node == self.root:
                self.root = current_node.left
            elif previous.data > current_node.data:
                previous.left = current_node.left
            else:
                previous.right = current_node.left
        
        ##Node exists and has one child - Right
        elif current_node.left == None:
            ##Case for deleting root
            if current_node == self.root:
                self.root = current_node.right
            elif previous.data > current_node.data:
                previous.left = current_node.right
            else:
                previous.right = current_node.right

        ##Node exists and has two children
        else:
            right_node = current_node.right
            ##Right node has  a left subtree
            if right_node.left != None:
                ##Find smallest leaf node in right_node.left subtree
                smallest = right_node
                while smallest.left != None:
                    previous = smallest
                    smallest = smallest.left
                current_node.data = smallest.data
                previous.left = None
            ##Right node has no left subtree - it is the least value
            else:
                current_node.data = right_node.data
                current_node.right = right_node.right
        return True

    ##Call with root as a paramater
    def binary_search(self,current_node,value):
        if current_node == None or current_node.data == value:
            return current_node
        elif value < current_node.data:
            return self.binary_search(current_node.left,value)
        elif value > current_node.data:
            return self.binary_search(current_node.right,value)
        
    ##Call with root as parameter - modifies data_output in place
    ##Node Left Right
    def pre_order(self,current_node, data_output):
        if current_node != None:
            data_output.append([current_node.data,current_node.bin_id])
        
        if current_node.left != None:
            self.pre_order(current_node.left, data_output)
        if current_node.right != None:
            self.pre_order(current_node.right, data_output)

    ##Call with root as parameter - modifies data_output in place
    ##Left Node Right
    def in_order(self,current_node, data_output):
        if current_node != None:

            if current_node.left != None:
                self.in_order(current_node.left, data_output)

            data_output.append([current_node.data,current_node.bin_id])

            if current_node.right != None:
                self.in_order(current_node.right, data_output)

    ##Call with root as parameter - modifies data_output in place
    ##Left Right Node
    def post_order(self,current_node, data_output):
        if current_node != None:

            if current_node.left != None:
                self.post_order(current_node.left, data_output)
            if current_node.right != None:
                self.post_order(current_node.right, data_output)
            
            data_output.append([current_node.data,current_node.bin_id])
    

    def breadth_first(self):
        current_node = self.root
        q = Queue()
        data_output = []
        while current_node != None:
            ##data_output.append([current_node.data,current_node.bin_id])
            data_output.append(current_node.data)
            if current_node.left != None:
                q.enqueue(current_node.left)
            if current_node.right != None:
                q.enqueue(current_node.right)
            
            
            current_node = q.dequeue()
        return data_output

    ##Call with current_node as the root
    def reverse(self,current_node):
        if current_node == None:
            return None
        current_node.left, current_node.right = current_node.right, current_node.left
        new_id = ''
        for b in current_node.bin_id:
            new_id += '0' if b == '1' else '1'
        current_node.bin_id = new_id
        self.reverse(current_node.left)
        self.reverse(current_node.right)
    
    ##Call with self.root as node
    def get_height(self,node):
        if node != None:
            return 1 + max(self.get_height(node.left),self.get_height(node.right))
        else:
            return -1

    ##Get to the top-down view of the binary tree - i.e. the top node at each horizontal width
    def get_top_view(self):
        n_i_v = {}
        hd = 0
        height = 0
        n_i_v[0] = [height,self.root]
        height+=1
        ##To the left
        self.buildView(self.root.left,n_i_v,hd-1,height)
        ##To the right
        self.buildView(self.root.right,n_i_v,hd+1,height)
        nodes = [value[1].data for (key,value) in sorted(n_i_v.items())]
        return sorted(nodes)

    ##Recursive function for get_top_view()
    def buildView(self,node,n_i_v,hd,height):
        if node == None:
            return 
        try:
            test = n_i_v[hd]
            if test[0] > height:
                n_i_v[hd] = [height,node]
        except:
            n_i_v[hd] = [height,node]
        height+=1
        ##To the left
        self.buildView(node.left,n_i_v,hd-1,height)
        ##To the right
        self.buildView(node.right,n_i_v,hd+1,height)




def show():
    tree = Binary_Tree()
    vals = [25, 39, 46, 20, 3, 23, 35, 32, 8, 16, 12, 33, 36, 31, 49, 41, 2, 4, 6, 9, 17, 34, 24, 13, 0, 42, 37, 40, 44, 30]
    for val in vals:
        tree.add_node(val)
    '''
    ##print("\nRoot: ", tree.root.data)

    pre_out = []
    ##tree.pre_order(tree.root, pre_out)
    ##print("\nPre-Order:", [i[0] for i in pre_out])

    in_out = []
    tree.in_order(tree.root, in_out)
    print("\nIn-Order:",[i[0] for i in in_out])
    tree.delete_node(23)
    in_out = []
    tree.in_order(tree.root, in_out)
    print("\nIn-Order:",[i[0] for i in in_out])


    post_out = []
    tree.post_order(tree.root, post_out)
    print("\nPost-Order:",[i[0] for i in post_out])
    '''
    breadth_out = tree.breadth_first()
    print("\nBreadth-First:",breadth_out)
    '''
    height = tree.get_height(tree.root)
    print(height)

    six_node = tree.binary_search(tree.root,6)
    print("\nBinary Search:",six_node.data,six_node.bin_id)

    tree.reverse(tree.root)
    print("\nReversed Breadth-First:",tree.breadth_first())
    top_view = tree.get_top_view()
    print(top_view)
    '''
show()
