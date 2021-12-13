# Time-Complexity: O(E)
# Space-Complexity: O(E+V)

class Graph(object):
    def __init__(self, cnt):
        self.count = cnt
        self.adj = [[] for _ in range(cnt)]
        
    def add_directed_edge(self, source, destination, cost=1):
        edge = (destination, cost)
        self.adj[source].append(edge)
    
    def add_undirected_edge(self, source, destination, cost=1):
        self.add_directed_edge(source, destination, cost)
        self.add_directed_edge(destination, source, cost)
        
    def print_graph(self):
        for i in range(self.count):
            print("Vertex ", i, " is connected to : ", end=' ')
            for edge in self.adj[i]:
                print("(", edge[0], edge[1], ")", end=' ')
            print("")
            
graph = Graph(4)
graph.add_undirected_edge(0, 1)
graph.add_undirected_edge(0, 2)
graph.add_undirected_edge(1, 2)
graph.add_undirected_edge(2, 3)
graph.print_graph()