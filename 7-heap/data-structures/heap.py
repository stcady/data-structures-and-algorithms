class Heap(object):

    # Heap class constructor for creating a new priority queue
    def __init__(self, is_min, array=None):
        if array == None:
            self.arr = [] 
        else:
            self.arr = array
        self.size = len(array)
        self.is_min_heap = is_min
        i = self.size // 2
        while i >= 0:
            self.percolate_down(i)
            i -= 1
    
    # comp compares two values and returns comparison result    
    def comp(self, first, second):
        if self.is_min_heap == True:
            return (first - second) > 0 # Min Heap
        else:
            return (first - second) < 0 # Max Heap
    
    # add adds a new value to the priority queue via proclate up
    def add(self, value):
        self.size += 1
        self.arr[self.size] = value
        self.percolate_up(self.size)
    
    # remove removes top value from the priority queue via proclate down
    def remove(self):
        if self.size == 0:
            raise RuntimeError("EmptyHeap")
        value = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.percolate_down(0)
        self.size -= 1
        return value
    
    # print_heap prints the contents of the priority queue
    def print_heap(self):
        print(self.arr)
    
    # is_empty checks if the priority queue is empty
    def is_empty(self):
        return self.size == 0
    
    # peek returns the first element of the priority queue
    def peek(self):
        if self.size == 0:
            raise RuntimeError("EmptyHeap")
        return self.arr[1]
    
    # percolate_down restores heap order when a parent node is not following heap property with its children
    def percolate_down(self, parent):   
        left_child = 2 * parent +  1
        right_child = left_child + 1
        child = -1
        if left_child < self.size:
            child = left_child
        if right_child < self.size and self.comp(self.arr[left_child], self.arr[right_child]):
            child = right_child

        if child != -1 and self.comp(self.arr[parent], self.arr[child]):
            temp = self.arr[parent]
            self.arr[parent] = self.arr[child]
            self.arr[child] = temp
            self.percolate_down(child)
            
    # percolate_up restores heap order when a child node is not following heap property with its parent
    def percolate_up(self, child):
        parent = (child - 1)// 2
        if parent < 0:
            return

        if self.comp(self.arr[parent], (self.arr[child])):
            temp = self.arr[child]
            self.arr[child] = self.arr[parent]
            self.arr[parent] = temp
            self.percolate_up(parent)

def heap_sort(array):
    hp = Heap(False, array)
    i = 0
    size = len(array)
    while i < size:
        array[size - i -1] = hp.remove()
        i += 1   
    return array  
            
def main():
    a = [1, 9, 6, 7, 8, 0, 2, 4, 5, 3]
    hp = Heap(True, a)
    hp.print_heap()
    print(hp.remove())
    hp.print_heap()
    print(a)
    b = heap_sort(a)
    print(b)
    
if __name__ == "__main__":
    main()