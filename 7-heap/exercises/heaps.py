import heapq
import math

# kth_smallest finds the kth smallest element in the arrray
def kth_smallest(arr, k):
    size = len(arr)
    heapq.heapify(arr)
    i = 0
    value = 0
    while i < size and i < k:
        value = heapq.heappop(arr)
        i += 1
    return value

# is_min_heap checks if the array represents a min binary heap
def is_min_heap(arr):
    size = len(arr)
    parent = 0
    for parent in range(size//2 + 1):
        left_child = parent*2 + 1
        right_child = parent*2 + 2
        if ((left_child < size) and (arr[parent] > arr[left_child])) or ((right_child < size) and (arr[parent] > arr[right_child])) :
            return False
    return True

# is_maxc_heap checks if the array represents a max binary heap
def is_max_heap(arr):
    size = len(arr)
    parent = 0
    for parent in range(size//2 + 1):
        left_child = parent*2 + 1
        right_child = parent*2 + 2
        if ((left_child < size) and (arr[parent] < arr[left_child])) or ((right_child < size) and (arr[parent] < arr[right_child])) :
            return False
    return True

def chota_bhim(cups):
    time = 60
    size = len(cups)
    cups.sort(reverse=True)
    value = 0
    while time > 0:
        value += cups[0]
        cups[0] = math.ceil(cups[0]/2.0)
        i = 0
        # Insert into proper location.
        while i < size-1 :
            if(cups[i] > cups[i+1]):
                break
            temp = cups[i]
            cups[i] = cups[i+1]
            cups[i+1] = temp
            i += 1
        time -= 1
    print(value)

def join_rope(ropes):
    heapq.heapify(ropes)
    total = 0
    value = 0
    while len(ropes) > 1:
        value = heapq.heappop(ropes)
        value += heapq.heappop(ropes)
        heapq.heappush(ropes, value)
        total += value
    print(total)

def kth_largest_stream(k):
    hp = []
    size = 0
    while 1:
        data = eval(input("Enter data: ")) 
        size = len(hp)
        if size < k - 1:
            hp.append(data)
        else:
            if size == k - 1:
                hp.append(data)
                heapq.heapify(hp)
            elif hp[0] < data :
                heapq.heappush(hp, data)
                heapq.heappop(hp)
            print(hp)
            print("Kth larges element is :: ", hp[0])
        size += 1