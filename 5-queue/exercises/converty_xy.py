from collections import deque

def converty_xy(src, dst):
    que = deque([])
    visited = {}
    while len(que) != 0:
        node = que.popleft()
        visited[node[0]] = 1
        value = node[0]
        steps = node[1]
        if value == dst:
            return steps
        if value < dst and (value * 2) not in visited:
            que.append((value * 2, steps + 1))
        if value > 0 and (value - 1) not in visited:
            que.append((value - 1, steps + 1))
    return -1

def main():
    for i in range(20):
        print("3 to ", i, " : ", converty_xy(3, i))

if __name__ == "__main__":
    main()
