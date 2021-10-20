# Time Complexity

# O(n)
def fun1(n):
    m = 0
    i = 0
    while i < n:
        m += 1
        i += 1
    return n

# O(n^2)
def fun2(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            i += 1
        i += 1
    return m

# O(n^2)
def fun3(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < i:
            m += 1
            j += 1
        i += 1
    return m

# O(log(n))
def fun4(n):
    m = 0
    i = 1
    while i < n:
        m += 1
        i = i * 2
    return m

def fun5(n):
    m = 0
    i = n
    while i > 0:
        m += 1
        i = i // 2
    return m

def main():
    fun1(100)
    fun2(100)
    fun3(100)

if __name__ == "__main__":
    main()