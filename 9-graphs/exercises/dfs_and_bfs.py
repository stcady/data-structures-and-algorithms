
from typing import Counter


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