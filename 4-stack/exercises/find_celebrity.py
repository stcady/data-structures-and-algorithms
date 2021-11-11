
def is_known(relation, a, b):
    if relation[a][b] == 1:
        return True
    else:
         False

def find_celebrity(relation, count):
    stk = []
    first, second = 0, 0
    for i in range(count):
        stk.append(i)
    first = stk.pop()
    while len(stk):
        second = stk.pop()
        if is_known(relation, first, second):
            first = second
    for i in range(count):
        if first != i and is_known(relation, first, i):
            return -1
        if first != i and is_known(relation, i, first) == False:
            return -1
    return first

def find_celebrity2(relation, count):
    stk = []
    first, second = 0, 0
    for i in range(count):
        if is_known(relation, first, i):
            stk.append(i)
    first = stk.pop()
    while len(stk):
        second = stk.pop()
        if is_known(relation, first, second):
            first = second
    for i in range(count):
        if first != i and is_known(relation, first, i):
            return -1
        if first != i and is_known(relation, i, first) == False:
            return -1
    return first
