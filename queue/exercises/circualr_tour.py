# Find if there is a circular tour possible to visit all the petrol pumps

from collections import deque

def circular_tour(arr, n):
    que = deque([])
    next_pump = 0
    count = 0
    petrol = 0
    while len(que) != n:
        while petrol >= 0 and len(que) != n:
            que.append(next_pump)
            petrol += (arr[next_pump][0] - arr[next_pump][1])
            next_pump = (next_pump + 1) % n
        while petrol < 0 and len(que) > 0:
            prev_pump = que.popleft()
            petrol -= (arr[prev_pump][0] - arr[prev_pump][1])
        count += 1
        if count == n:
            return -1
    if petrol >= 0:
        return que.popleft()
    else:
        return -1

def main():
    tour = [[8, 6], [1, 4], [7, 6]]
    print(circular_tour(tour, 3))

if __name__ == "__main__":
    main()
