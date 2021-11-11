def function2():
    print("function2 line 1")

def function1():
    print("function1 line 1")
    function2()
    print("function1 line 2")

def main():
    print("main line 1")
    function1()
    print("main line 2")

if __name__ == "__main__":
    main()