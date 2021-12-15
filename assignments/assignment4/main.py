from graph import Graph

def main():
    nodes = ["San Francisco", "Seattle", "Phoenix", "Atlanta", "New York", "Cleveland", "Detroit", "San Diego", "Miami"]
    gph = Graph(nodes)
    gph.add_undirected_edge("San Francisco", "Seattle", 2)
    gph.add_undirected_edge("San Francisco", "San Diego", 2)
    gph.add_undirected_edge("San Francisco", "Phoenix", 3)
    gph.add_undirected_edge("San Diego", "Phoenix", 1)
    gph.add_undirected_edge("Phoenix", "Atlanta", 4)
    gph.add_undirected_edge("Phoenix", "Miami", 5)
    gph.add_undirected_edge("Seattle", "Cleveland", 4)
    gph.add_undirected_edge("Seattle", "Phoenix", 3)
    gph.add_undirected_edge("Seattle", "Detroit", 3)
    gph.add_undirected_edge("Detroit", "New York", 1)
    gph.add_undirected_edge("Cleveland", "New York", 2)
    gph.add_undirected_edge("Miami", "New York", 1)
    gph.add_undirected_edge("Atlanta", "Miami", 1)
    gph.add_undirected_edge("Detroit", "Cleveland", 1)

    print("________________________________________________________________")
    previous_nodes, shortest_path = gph.dijkstra_algorithm("San Francisco")
    print("________________________________________________________________")
    print(previous_nodes)
    print(shortest_path)
    print("________________________________________________________________")
    gph.print_dijkstra_result(previous_nodes, shortest_path, "San Francisco", "New York")
    print("________________________________________________________________")

    
    #gph.print_dijkstra_result(previous_nodes, shortest_path, "San Francisco", "Atlanta")

    #previous_nodes, shortest_path = gph.dijkstra_algorithm("Detroit")
    #gph.print_dijkstra_result(previous_nodes, shortest_path, "Detroit", "San Diego")

if __name__ == "__main__":
    main()
