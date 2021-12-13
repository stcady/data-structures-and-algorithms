
from typing import Counter
from collections import deque
from graph_list import Graph


def topological_sort(gph):
    stk = []
    count = gph.count
    visited = [False] * count
    for i in range(count):
        if visited[i] == False:
            topological_sort_dfs(gph, i, visited, stk)
    print("Topological Sort :: ", end=' ')
    while len(stk) != 0:
        print(stk.pop(), end=' ')
        
def topological_sort_dfs(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            topological_sort_dfs(gph, destination, visited, stk)
    stk.append(index)
    
def path_exists(gph, source, destination):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, source, visited)
    return visited[destination]
    
def dfs_util(gph, index, visited):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            dfs_util(gph, destination, visited)
            
def count_all_paths_dfs(gph, visited, source, dest):
    if source == dest:
        return 1
    count = 0
    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            count += count_all_paths_dfs(gph, visited, edge[0], dest)
    visited[source] = 0
    return count

def print_all_paths_dfs(gph, visited, source, dest, path):
    path.append(source)
    if source == dest:
        print(path)
        return
    visited[source] = 1
    for edge in gph.adj[source]:
        if visited[edge[0]] == 0:
            print_all_paths_dfs(gph, visited, edge[0], dest, path)
    visited[source] = 0
    path.pop()
    
def root_vertex(gph):
    count = gph.count
    visited = [False] * count
    retVal = -1
    for i in range(count):
        if visited[i] == False:
            dfs_util(gph, i, visited)
            retVal = i
    print("Root vertex is :: ", retVal)
    
def transitive_closure_util(gph, source ,index, tc):
    if tc[source][index] == 1:
        return
    tc[source][index] = 1
    for edge in gph.adj[index]:
            transitive_closure_util(gph, source, edge[0], tc)

def transitive_closure(gph):
    count = gph.count
    tc = [[0 for _ in range(count)] for _ in range(count)]
    for source in range(count):
        transitive_closure_util(gph, source, source, tc)
    for row in tc:
        print(row)
    return tc

def bfs_distance(gph, source, dest):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        depth = node[1]
        for edge in gph.adj[curr]:
            if edge[0] == dest:
                return depth+1
            if visited[edge[0]] == False:
                que.append((edge[0], depth+1))
                visited[edge[0]] = True
    return -1

def bfs_level_node(gph, source):
    count = gph.count
    visited = [False] * count
    visited[source] = True
    que = deque([])
    que.append((source, 0))
    print("\nNode  - Level")
    while len(que) != 0:
        node = que.popleft()
        curr = node[0]
        depth = node[1]
        print(curr ," - ", depth)
        for edge in gph.adj[curr]:
            destination = edge[0]
            if visited[destination] == False:
                que.append((destination, depth+1))
                visited[destination] = True
                
def is_cycle_present_undirected_dfs(graph, index, parentIndex, visited):
    visited[index] = True
    for node in graph.adj[index]:
        dest = node[0]
        if visited[dest] == False:
            if is_cycle_present_undirected_dfs(graph, dest, index, visited) :
                return True
        elif parentIndex != dest :
            return True
    return False

def is_cycle_present_dfs(graph, index, visited, marked):
    visited[index] = True
    marked[index] = True
    for node in graph.adj[index]:
        dest = node[0]
        if marked[dest] == True:
            return True
        if visited[dest] == False:
            if is_cycle_present_dfs(graph, dest, visited, marked) :
                return True
    marked[index] = False
    return False

def transpose_graph(gph):
    count = gph.count
    g = Graph(count)
    for i in range(count):
        for edge in gph.adj[i]:
            destination = edge[0]
            g.add_direct_edge(destination, i)
    return g
    
def is_connected_undirected(gph):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

def is_strongly_connected(gph):
    count = gph.count
    visited = [False] * count
    dfs_util(gph, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    graph_reversed = transpose_graph(gph)
    visited = [False] * count
    dfs_util(graph_reversed, 0, visited)
    for i in range(count):
        if visited[i] == False:
            return False
    return True

def dfs_util2(gph, index, visited, stk):
    visited[index] = True
    for edge in gph.adj[index]:
        destination = edge[0]
        if visited[destination] == False:
            dfs_util2(gph, destination, visited, stk)
    stk.append(index)

def strongly_connected_component(gph):
    count = gph.count
    visited = [False] * count
    stk = []
    for i in range(count):
        if visited[i] == False:
            dfs_util2(gph, i, visited, stk)
    
    graph_reversed = transpose_graph(gph)
    visited = [False] * count
    while len(stk) != 0:
        index = stk.pop()
        if visited[index] == False:
            stk2 = []
            dfs_util2(graph_reversed, index, visited, stk2)
            print(stk2)
            
def primsMST(gph):
    previous = [-1] * gph.count
    dist = [sys.maxsize] * gph.count
    visited = [False] * gph.count
    source = 0
    dist[source] = 0
    previous[source] = -1
    pq = PriorityQueue()
    for i in range(gph.count):
        pq.add(sys.maxsize, i)
    pq.update_key(0, source)
    
    while pq.size() != 0:
        val = pq.pop()
        source = val[1]
        visited[source] = True

        for edge in gph.adj[source]:
            destination = edge[0]
            cost = edge[1]
            if cost < dist[destination] and visited[destination] == False:
                dist[destination] = cost
                previous[destination] = source
                pq.update_key(cost, destination)
    
    total_cost = 0

    for i in range(gph.count):
        if dist[i] == sys.maxsize:
            print("node id" , i , "prev" , previous[i] , "distance : Unreachable")
        else:
            print("node id" , i , "prev" , previous[i] , "distance :" , dist[i])
            total_cost += dist[i]

    print("Total MST cost: ", str(total_cost))
    
