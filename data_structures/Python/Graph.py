import Queue
graph = {
    'Root':'A',
    'A':['B','C','D'],
    'B':['A','E'],
    'C':['A','D'],
    'D':['A','C','F'],
    'E':['B','G'],
    'F':['D'],
    'G':['E'],
}
##Equivalent adjacency matrix
adj_matrix = [[0,1,1,1,0,0,0],
              [1,0,0,0,1,0,0],
              [1,0,0,1,0,0,0],
              [1,0,1,0,0,1,0],
              [0,1,0,0,0,0,1],
              [0,0,0,1,0,0,0],
              [0,0,0,0,1,0,0]]
data = ['A','B','C','D','E','F','G']

def breadth_first(graph,root):
    visited = []
    q = Queue.Queue()
    current_node = root
    while current_node != None:

        for node in graph[current_node]:
            if node not in visited:
                q.enqueue(node)
        if current_node not in visited:
            visited.append(current_node)
        current_node = q.dequeue()
    return visited

##Initiate call with current_node as the root
def depth_first(graph,current_node,visited):
    visited.append(current_node)
    for node in graph[current_node]:
        if node not in visited:
            depth_first(graph,node,visited)

##Work on making OOP implementation using nodes and pointers - similar to Binary_Tree
class Graph:

    class Node:
        def __init__(self):
            self.data = None
            self.pointers = []

    class Pointer:
        src = None
        dest = None
        weight = None

    def __init__(self):
        self.root = None 

    ##Convert adjacency matrix into graph of nodes and pointers
    ##data is 1xn    matrix is nxn
    def create_graph(self,matrix,data):
        ##Take first row and data value as root
        for n in range(len(data)):
            node = Graph.Node()
            node.data = data[n]
            data[n] = node
        ##Data is now a list of nodes
        ##Add pointers
        for src in range(len(matrix)):
            for dest in range(len(matrix[src])):
                if matrix[src][dest] != 0:
                    pointer = Graph.Pointer()
                    pointer.weight = matrix[src][dest]
                    pointer.src = data[src]
                    pointer.dest = data[dest]
                    ##print(pointer.weight,pointer.src.data,pointer.dest.data)
                    ##print(pointer.weight,data[src].data,data[dest].data)
                    data[src].pointers.append(pointer)
                    
        
        
        self.root = data[0]
    
    ##Breadth-First search
    def bfs(self):
        visited = []
        q = Queue.Queue()
        current_node = self.root
        while current_node != None:
            for p in current_node.pointers:
                if p.dest.data not in visited:
                    q.enqueue(p.dest)
            if current_node.data not in visited:
                visited.append(current_node.data)
            current_node = q.dequeue()
        return visited
    
    ##Depth-First search
    ##Initiate call with current_node as root
    def dfs(self,visited,current_node):
        ##print("\n",current_node.data)
        visited.append(current_node.data)
        ##print(visited)
        for test in current_node.pointers:
            ##print(test.dest.data, end = ",")
            pass
        for p in current_node.pointers:
            if p.dest.data not in visited:
                ##print("\n",p.src.data, "->", p.dest.data, "Current =", current_node.data)
                self.dfs(visited,p.dest)


def show(adj_matrix,data):
    bfs_visited = breadth_first(graph,graph['Root'])
    print("Adj-List Breadth-First:",bfs_visited)

    dfs_visited = []
    depth_first(graph,graph['Root'],dfs_visited)
    print("Adj-List Depth-First:",dfs_visited)

    Graph_Nodes = Graph()
    
    Graph_Nodes.create_graph(adj_matrix,data)
    print("OOP Breadth-First:",Graph_Nodes.bfs())
    
    v = []
    Graph_Nodes.dfs(v,Graph_Nodes.root)
    print("OOP Depth-First:",v)
show(adj_matrix, data)
