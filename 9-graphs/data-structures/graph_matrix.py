# Time-Complexity: O(1)
# Space-Complexity: O(n^2)

class Graph(object):
    
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[0 for _ in range(cnt)] for _ in range(cnt)]
        
    def add_direct_edge(self, source, destination, cost=1):
        self.adj[source][destination] = cost
    
    def add_undirected_edge(self, source, destination, cost=1):
        self.add_direct_edge(source, destination, cost)
        self.add_direct_edge(destination, source, cost)
        
    def print_graph(self):
        for i in range(self.count):
            print("Vertex ", i, " is connected to : ", end=' ')
            for j in range(self.count):
                if self.adj[i][j] != 0:
                    print(j, end=' ')
            print("")
                
graph = Graph(4)
graph.add_undirected_edge(0, 1)
graph.add_undirected_edge(0, 2)
graph.add_undirected_edge(1, 2)
graph.add_undirected_edge(2, 3)
graph.print_graph()