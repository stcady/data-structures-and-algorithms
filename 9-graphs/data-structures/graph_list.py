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
            
            
# Time-Complexity: O(V+E) in adjacency list format
# Time-Complexity: O(V^2) in adjacency matrix format

def dfs_stack(gph, source, target):
    count = gph.count
    visited = [False] * count
    stk = []
    stk.append(source)
    visited[source] = True
    while len(stk) != 0:
        curr = stk.pop()
        print(curr, end=' ')
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                stk.append(destination)
                visited[destination] = True
    return visited[target]
    
def dfs_recurse(gph, source, target):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, source, visited)
    return visited[target]
from collections import deque

def dfs_util(gph, index, visited):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            dfs_util(gph, destination, visited)
            
def bfs(gph, source, target):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    print("BFS : ", end=' ')
    que = deque([])
    que.append(source)
    while len(que) != 0:
        curr = que.popleft()
        print(curr, end=' ')
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append(destination)
                visited[destination] = True
    return visited[target]