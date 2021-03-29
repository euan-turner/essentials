from dataclasses import dataclass
from typing import Any

##Leaf Nodes have data:str and freq:int -> occurrences of data in a string
##Root Nodes have data:None and freq:int -> total freq of subtree
@dataclass
class Node():
    left: Any
    right: Any
    freq: int
    data: Any
    bin_id : str = ''

class Linked_List():
    class LL_Node():
        def __init__(self,node):
            self.node = node
            self.freq = node.freq
            self.pointer = None
    def __init__(self):
        self.start = None
        self.size = 0
        

    def put(self,node):
        try:
            new = Linked_List.LL_Node(node)
            current = self.start
            if current == None:
                self.start = new
            elif new.freq < current.freq:
                new.pointer = current
                self.start = new
            else:
                while current != None and new.freq >= current.freq:
                    previous = current
                    current = current.pointer
                new.pointer = previous.pointer
                previous.pointer = new
            self.size += 1
            return True
        except:
            return False

    def get(self):
        if self.size > 0:
            root = self.start
            self.start = root.pointer
            self.size -= 1
            return root
        return None

class Huffman_Tree():

    def __init__(self):
        self.root = None
        self.string = None

    def build(self,string):
        try:
            ##Create dictionary of character frequencies
            freqs = {}
            for char in string:
                if freqs.get(char) == None:
                    freqs[char] = 1
                else:
                    freqs[char] +=1
            ##Use priority queue to order characters by frequency
            ll = Linked_List()
            for (char,freq) in freqs.items():
                leaf = Node(None,None,freq,char)
                ll.put(leaf)
            
            ##Take letters/nodes in pairs, create a root node, and put root node back with combined frequency
            while ll.size > 1:
                left = ll.get()
                right = ll.get()
                root = Node(left.node,right.node,left.freq+right.freq,None)
                ll.put(root)
            self.root = ll.get().node
            self.string = string
            base_bin = ''
            self.update_bin(self.root,base_bin)
            return True
        except:
            return False

    ##Pre-Order Traversal: call with root = self.root and val = '' 
    def update_bin(self,root,val):
        if root != None:
            if root.data != None: ## Node contains a character
                root.bin_id = val
                self.string = self.string.replace(root.data,root.bin_id)
            if root.left != None:
                newval = val + '0'
                self.update_bin(root.left,newval)
            if root.right != None:
                newval = val + '1'
                self.update_bin(root.right,newval)

    ##Return a string with the binary compression
    def get_comp(self):
        return self.string
    
    ##Returns (int x, int y) pair - x is the denary integer. y is the number of leading 0s in the binary
    def get_comp_as_int(self):
        leading_zeros = 0
        i = 0
        while self.string[i] == '0':
            leading_zeros += 1
            i+=1
        return (int(self.string,2),leading_zeros)
            

            
        
        
tree = Huffman_Tree()
tree.build('abracadabra')

print(tree.get_comp())
print(tree.get_comp_as_int())






     


    

