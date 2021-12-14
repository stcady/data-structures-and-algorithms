import sys
from collections import defaultdict
import heapq as heap

# Graph initializes the graph class
class Graph(object):

    # Graph class constructor that initializes the set of nodes and adds it to the adjacency table
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {}
        for node in nodes:
            self.adj[node] = {}

    # add_directed_edge adds a directed edge with a specified weight between the source and destination
    def add_directed_edge(self, source, destination, weight):
        self.adj[source][destination] = weight
    
    # add_directed_edge adds a undirected edge with a specified weight between the source and destination
    def add_undirected_edge(self, source, destination, weight):
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    # add_node adds a new node/vertex to the graph data structure
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self.adj[node] = {}
        else:
            raise Exception("NodeExists")
    
    # weight returns the weight of the specified edge
    def weight(self, source, destination):
        return self.adj[source][destination]

    def dijkstra_algorithm(self, start_node):
        visited = set()
        previous = {}
        pq = []
        node_weights = defaultdict(lambda: float('inf'))
        node_weights[start_node] = 0
        heap.heappush(pq, (0, start_node))
        while len(pq) != 0:
            # go greedily by always extending the shorter cost nodes first
            (_, node) = heap.heappop(pq)
            visited.add(node)
            for destination, weight in self.adj[node].items():
                new_weight = node_weights[node] + weight
                if node_weights[destination] > new_weight and destination not in visited:
                    previous[destination] = node
                    node_weights[destination] = new_weight
                    heap.heappush(pq, (new_weight, destination))
        return previous, node_weights

    def print_dijkstra_result(self, previous, shortest_path, start_node, end_node):
        path = []
        node = end_node
        while node != start_node:
            path.append(node)
            node = previous[node]
            print(path)
        # Add start node
        path.append(start_node)
        print(path)
        print("Shortest path: {}.".format(shortest_path[end_node]))
        print(" -> ".join(reversed(path)))